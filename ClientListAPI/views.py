from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.

@api_view(['GET', 'POST'])
def clients(request):
    return Response('list of the clients', status=status.HTTP_200_OK)


class ClientList(APIView):
    
    def get(self, request):
        author = request.GET.get('author')
        if(author):
            return Response({"message": "list of the books by " + author}, status.HTTP_200_OK)
        return Response({"message": "list of the clients"}, status.HTTP_200_OK)
    

    def post(self, request):
        return Response({"title": request.data.get("title")}, status.HTTP_201_CREATED)
    

class Client(APIView):
    
    def get(self, request, pk):
        return Response({"message": "single client with id " + str(pk)}, status.HTTP_200_OK)
    
    def put(self, request, pk):
        return Response({"title": request.data.get("title")}, status.HTTP_200_OK)