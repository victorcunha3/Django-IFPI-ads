from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, status
from .serializer import TarefaSerializer, UserSerializer
from .models import Tarefas
from django.http import Http404

class HelloVV(APIView):
    def get(self, request):
        return Response({'cav': 'msg'})

class ListCreateTarefa(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        #serializer = TarefaSerializer(Tarefas.objects.all(), many=True)
        tarefa = Tarefas.objects.filter(usuario=request.user)
        serializer = TarefaSerializer(tarefa, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['usuario'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DetailUpdateDeleteTarefa(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_tarefa(self, pk):
        try:
            return Tarefas.objects.get(pk=pk)
        except Tarefas.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        tarefa = self.get_tarefa(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        tarefa = self.get_tarefa(pk)
        self.check_object_permissions(request, tarefa)  # Verifica as permissões
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        tarefa = self.get_tarefa(pk)
        self.check_object_permissions(request, tarefa)  # Verifica as permissões
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def check_object_permissions(self, request, obj):
        #Verifica se o usuário autenticado é o proprietário da tarefa.
        if obj.usuario != request.user:
            self.permission_denied(request, message='Você não tem permissão para realizar esta ação.')



class UserSignup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)