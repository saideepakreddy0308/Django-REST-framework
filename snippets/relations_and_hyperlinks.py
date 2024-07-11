# fully-qualified urls: Its a complete web address that includes the domain name and the protocol
# so that users can access the resurces directly from that response

# StaticHTMLRenderer: Renders the response of pre-formatted HTML
# Hyperlinking: Using urls to represent relationships between resources, rather than using primary keys

# Instead of returning {'user_id':1}, we return  {"user": "http://127/0.0.0.1:8000/users/1/"}

# reverse: Here its a function to generata full url views
# root endpoint: a central URL, that lists all available endpoints
# @api_view: Decorator to create a simple API view


# Learning Course
# Views and URL patterns

# Class based views: More modular and resuable
# Function based views: Simpler and StraightForward

from rest_framework import generics
from  snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# SnipperList is class-based view that handles listing all snippets and creating new snippets
class SnipperList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# Function based view for the API root
from rest_framework import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'users': reverse('user-list', request=request, format=format)
            'snippets': reverse('snipper-list', request=request, format=format)
        }
    )

# Here the view returns a response with links to the user list and snippet list.

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('', views.api_root)
    path('snippets/', views.SnipperList.as_view(),name='snipper-list'),
    path('snippets/<int:pk>',views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    # path(users)
    # path(users/<int:pk>)
]

urlpattern = format_suffix_patterns(urlpatterns)


# Serializers and Hyperlinks

from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet--highlight', format=format)

    class Meta:
        Model = Snippet
        fields = ['url','id', 'highlight', 'owner', 'title', 'code','linenos']


from django.contrib.auth.models import User

# User Serializer using Hyperlinked Model Serailizer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail,read_only'=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']


# More on class meta
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()


    class Meta:
        db_table = 'book_table'
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        unique_together = ['title','author']  # here it means, no two fields should have the combination of title and author, it must be unique from each other.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','author','published_date']
        read_only_fields = ['id']
        extra_kwargs = {
            'author': {'required':True},
        }
# Meta class is a crucial part of django models  and serializers, allowing to configure various aspects in their behavior.
# In models, it configures database-related options, and other model serializers, it defines how the model fields,
# should be serialized and deserialized, making it easier to control the API output and input.

