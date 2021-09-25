from django.shortcuts import render


# Create your views here.


def index(request):
    date = {'title': 'Главная страница',
            'Array_auto': ['audi', 'bmw', 'skoda']}
    return render(request, 'main/index.html', date)


def index2(request):
    return render(request, 'main/about.html')
