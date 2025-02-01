from django.contrib import admin
from .models.signup import SignUp
from .models.todo import ToDoList

@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_completed', 'created_at', 'updated_at')
