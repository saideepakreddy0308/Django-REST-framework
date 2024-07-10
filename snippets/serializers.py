from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """

        # Here, uses the create method of the snippet model manager to create a new Snippet Instance
        # the validated data syntax unpacks the dictionary into keyword arguments
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """

        # Here, iterated through the validated_data and updates the corresponding fields
        # of the 'Snippet' instance

        # Uses 'get' method to retrieve each fields value from 'validated_data',
        # falling back to the current value of the instance if the field is not provided.
        # saves the updated instance and returns it

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        # instance.language = validated_data.get('language', instance.language)
        # instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
    

    # python manage.py shell
    # serialzing and deserialzing
# snippet = Snippet(code='foo = 'bar'\n')
# snippet.save()
# serializer = SnippetSerializer(snippet)
# serializer.data

# Translated the model instance into python native datatypes
# content = JsonRenderer().render(serializer.data)
# content

# Then deseralization

# MODEL SERIALIZERS
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id','title','code','linenos']

# in python mange.py shell
# from serializers import SnippetSerializer
# serializer = SnippetSerializer()
# print(repr(serializer))