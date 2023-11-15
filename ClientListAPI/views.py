from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import ClientSerializer
from clientapp.models import Client as ClientModel

# Create your views here.

@api_view(['GET', 'POST'])
def clients(request):

    if request.method == 'GET':
        client_list = ClientModel.objects.all()
        serialized_list = ClientSerializer(client_list, many=True)
        # return Response('list of the clients', status=status.HTTP_200_OK)
        return Response(serialized_list.data)
    
    if request.method == 'POST':
        serialized_item = ClientSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        data = serialized_item.validated_data
        print(data)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def client(request, pk):
    # client_one = ClientModel.objects.get(pk=pk)
    client_one = get_object_or_404(ClientModel, pk=pk)
    serialized_item = ClientSerializer(client_one)
    # return Response('list of the clients', status=status.HTTP_200_OK)
    return Response(serialized_item.data)


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


class ClientListView(generics.ListCreateAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer

class SingleClientView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer