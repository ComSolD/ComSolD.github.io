from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('task', views.task, name='task'),
    path('create', views.create, name='create'),
]