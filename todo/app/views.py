from django.shortcuts import render
from .serializers import TodoSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Todo
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def todo_api(request,id=None):
    if request.method=='GET':
        if id is not None:
            todo=Todo.objects.get(id=id)
            serializer=TodoSerializer(todo)
            return Response(serializer.data)
    
        todo=Todo.objects.all()
        serializer=TodoSerializer(todo,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return JsonResponse({'msg':'Todo not created....'})
        
    if request.method=='PUT':
        if id is not None:
            todo=Todo.objects.get(id=id)
            serializer=TodoSerializer(instance=todo,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            

    if request.method=='DELETE':
        if id is not None:
            todo=Todo.objects.get(id=id)
            todo.delete()
            return Response({'msg':'Todo Deleted....'})

