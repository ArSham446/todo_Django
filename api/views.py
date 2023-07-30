from rest_framework import generics
from .models import todo
from .serializer import todoSerializer

class todoList(generics.ListCreateAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer

class todoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer
