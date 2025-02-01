from django.urls import path
from .views import TodoUpdateDelete, TodoGET, SignUpGET, SignUpUpdateDelete

urlpatterns = [
    # Todo API
    path('todo/', TodoGET.as_view(), name='todo-list'),
    path('todo/<int:pk>/', TodoUpdateDelete.as_view(), name='todo-detail'),
    
    # SignUp API
    path('signup/', SignUpGET.as_view(), name='signup-list'),
    path('signup/<int:pk>/', SignUpUpdateDelete.as_view(), name='signup-detail'),
]