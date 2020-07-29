from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    count = Task.objects.all().count()
    return render(request, "main/index.html", {'title': 'Главная страница сайта', 'count': count})

def task(request):
    tasks = Task.objects.order_by('-id')
    return render(request, "main/task.html", {'title': 'Список заданий', 'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
        else:
            error = 'Форма была неверной'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "main/create.html", context)