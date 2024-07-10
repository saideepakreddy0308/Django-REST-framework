# imports from built in django's authentication system
# User model it respresents a user account, and includes fields like username, password, email, groups
# Group model represents a group of users, which can be used for assigning permissions
from django.contrib.auth.models import Group, User

# serializers in DRF are used to convert complex datatypes such as querysets and model instances into native python datatypes
#  that can be easily rendered into JSON, XML or other content types
from rest_framework import serializers


# HyperlinkedModelSerializer , subclass of Model serializer, that used hyperlinks for relationships ratherthan primary keys
class UserSerializer(serializers.HyperlinkedModelSerializer):

    # Meta, its a nested class used to specify metadata
    class Meta:
        model = User
        # url: hyper link to detail view of user
        # groups: the user belong to, this is typically many to many relationship
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



# Hyperlinks: that point to specific resources
# Metadata: information about the serializer class itself