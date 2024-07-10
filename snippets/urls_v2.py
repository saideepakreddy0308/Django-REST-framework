from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_v2

urlpatterns = [
    path('snippets/',views_v2.SnippetList.as_view()),
    path('snippets/<int:pk>/', views_v2.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)