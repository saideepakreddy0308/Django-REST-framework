from django.urls import include, path
from rest_framework import routers  # Its for url routing for viewsets

from django_tutorial import views

router = routers.DefaultRouter()  # automatically generates URL patterns for the viewsets
router.register(r'users',views.UserViewSet)   # users is url prefix
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),  # includes all urls of both viewsets
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),  # includes authentication URLs, provided by DRF
    path('snippet', include('snippet.urls'))]
    # namespace , here it helps in differentiating between different sets of URLs
