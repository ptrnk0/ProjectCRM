from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
# from rest_framework import authentication, permissions
from .serializers import ClientSerializer
from clientapp.models import Client as ClientModel

# Create your views here.

class ClientList(APIView):

    def get(self, request):
        all_clients = ClientModel.objects.all()
        serialized_data = ClientSerializer(all_clients, many=True)
        return Response(serialized_data.data, status.HTTP_200_OK)
    
    def post(self, request):
        deserialized_data = ClientSerializer(data=request.data)
        if deserialized_data.is_valid():
            client = deserialized_data.save()
            client.save()
        return Response(deserialized_data.data, status.HTTP_201_CREATED)


class Client(APIView):

    def get(self, request, pk):
        client = get_object_or_404(ClientModel, pk=pk)
        serialized_data = ClientSerializer(client)
        return Response(serialized_data.data, status.HTTP_200_OK)

    def put(self, request, pk):
        client = get_object_or_404(ClientModel, pk=pk)
        deserialized_data = ClientSerializer(client, data=request.data)
        if deserialized_data.is_valid():
            client_model = deserialized_data.save()
            client_model.save()
        return Response(deserialized_data.data, status.HTTP_200_OK)
    
    def patch(self, request, pk):
        client = ClientModel.objects.get(id=pk)
        deserialized_data = ClientSerializer(client, data=request.data, partial=True)
        if deserialized_data.is_valid():
            client_model = deserialized_data.save()
            client_model.save()
        return Response(deserialized_data.data, status.HTTP_200_OK)
    
    def delete(self, request, pk):
        client = ClientModel.objects.get(id=pk)
        name = f"{client.first_name} {client.last_name}"
        client.delete()
        return Response({"message": f"client {name} deleted"}, status.HTTP_200_OK)


# class ClientListView(generics.ListCreateAPIView):
#     queryset = ClientModel.objects.all()
#     serializer_class = ClientSerializer

# class DeleteClientView(generics.DestroyAPIView):
#     queryset = ClientModel.objects.all()
#     serializer_class = ClientSerializer