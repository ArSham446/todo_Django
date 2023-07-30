

from django.urls import path
from .views import todoList, todoUpdateDelete


urlpatterns = [
    path('', todoList.as_view()),
    path('api/todo/', todoList.as_view()),
    path('api/todo/<int:pk>/', todoUpdateDelete.as_view())
]
