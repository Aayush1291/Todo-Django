from .models.todo import ToDoList
from .serializers import ToDoListSerializer
from .models.signup import SignUp
from .serializers import SignUpSerializer
from rest_framework import generics

class SignUpGET(generics.ListCreateAPIView):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer


class SignUpUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer

class TodoGET(generics.ListCreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer


class TodoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
