from django.shortcuts import render
from django.http import HttpResponse, JsonResponse  # creates HTTP responses and JSON responses
from django.views.decorators.csrf import csrf_exempt  # exempt view from CSRF verification
from rest_framework.parsers import JSONParser  # Used to parse incoming jSON requests
from snippets.models import Snippet # Model
from snippets.serializers import SnippetSerializer  # serializer class used to convert model instances to JSON and vice versa

# Create API endpoints
# List and create snippets

@csrf_exempt   # used to disable csrf protection
def snippet_list(request):
    # list all code snippets or create a new snippet

    if request.method == 'GET':
        snippets = Snippet.objects.all()     # retrieve all snippet objects/ instances from the database
        serializer = SnippetSerializer(snippets, many=True)   # takes the list of instances, converts each instance into a dictionary
        # The many=True argument indicates that the serializer is dealing with multiple instances
        return JsonResponse(serializer.data, safe=False)  # Here the serializer data containes list of dictionaries, this data is then passed
        # to 'JSONResponse' to convert it into a json response that can bereturned
    
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    @csrf_exempt
    def snipper_detail(request, pk):

        # Retrieve, update or delete a code snippet_list
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return HttpResponse(status=400)
        
        if request.method == 'GET':
            serializer = SnippetSerializer(snippet)
            return HttpResponse(status=400)
        
        elif request.method == "PUT":
            data = JSONParser.parse(request)  # parses it into a Python dictionary or list, {} or []
            serializer = SnippetSerializer(snippet, data=data)  # data is the updated data parsed from the request
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status = 400)
        
        elif request.method == 'DELETE':
            snippet.delete()
            return HttpResponse(status=204)  # no content response , successful deletion



# Tutorial 2

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET','POST'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)