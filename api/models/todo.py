# api/models/todo.py
from django.db import models
from .signup import SignUp

class ToDoList(models.Model):
    user = models.ForeignKey(SignUp, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True,max_length=50)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
