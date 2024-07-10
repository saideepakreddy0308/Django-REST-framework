from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets


from django_tutorial. serializers import GroupSerializer, UserSerializer

# Defined userviewset, inherited from ModelViewSet and modelviewset it provides
# default implementations for CRUD operations
class UserViewSet(viewsets. ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer   # used for serializing and deserializing user objects
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets. ModelViewSet):
    
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
