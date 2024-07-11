from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet
from permissions import IsOwnerOrReadOnly

class UserSerialzer(serializers.ModelSerialzer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset = Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id','username','snippets']

# views.py
    def perform_create(self,serializer):
        serializer.save(owner = self.request.user)
    # Here this create method of our serializer will now be passed an additional 'owner' field, along with the validated data from the request

    # This to be reflected , lets update the snipperserializer
    owner = serializers.ReadOnlyField(source='owner.username')
    # add owner to list of fields in the inner Meta Class



# Adding persmissions to views
from rest_framework import permissions

# now, to both views
permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly ]

