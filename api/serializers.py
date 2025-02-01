# api/serializers.py
from rest_framework import serializers
from .models.todo import ToDoList
from .models.signup import SignUp

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = '__all__'

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'
