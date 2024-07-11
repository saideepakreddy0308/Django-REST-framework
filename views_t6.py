# viewsets same thing as view classes, expect that they provide operations such as retrieve,  update rather than get or put

from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Using Routers
router = DefaultRouter()
router.register(r'users' ,views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),

]



# Code with Custom Action

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenicatedOrReadOnly, IsOwnerOrReadOnly]


    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])

    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Using Routers
router = DefaultRouter()
router.register(r'users' ,views.UserViewSet, basename='user')
router.register(r'snippets', views.SnipperViewSet, basename='snippet')

urlpatterns = [
    path('', include(router.urls)),

]


# VIewsets better to maintain a clean and consistent codebase, as API grows