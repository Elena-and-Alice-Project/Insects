from django.shortcuts import render
from animals.models import AnimalCategory, Animal

# Create your views here.

# функции - обработчики запросов = контроллеры = вьюхи

def index(request):
    context = {
        'title': 'Инсектопедия',
        'username': 'Alice'
    }
    return render(request, 'animals/index.html')

def animals(request):
    context = {
        'title': 'Каталог насекомых',
        'animals': Animal.objects.all(),
        'category': AnimalCategory.objects.all()
    }
    return render(request, 'animals/animals.html', context)

def search(request):
    context = {
        'title': 'Поиск в картотеке',
        'username': 'Alice'
    }
    return render(request, 'animals/search.html', context)

def simulator(request):
    context = {
        'title': 'Симулятор',
        'username': 'Alice'
    }
    return render(request, 'animals/simulator.html', context)

def login(request):
    context = {
        'title': 'Страница входа',
        'username': 'Alice'
    }
    return render(request, 'animals/login.html', context)