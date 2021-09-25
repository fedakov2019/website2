from django.shortcuts import render, redirect
from .models import Articles
from django.db import connection
from collections import namedtuple
from .form import ArticlesForm
from django.views.generic import DetailView
import datetime

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'new1/detail_view.html'
    context_object_name = 'article'

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
def create(request):
    error=''
    if request.method == 'POST':
        form =ArticlesForm(request.POST)
        if form.is_valid():

            return redirect('home')
        else:
            error='Форма была неверной'

    nefs = ArticlesForm()
    data = {'form': nefs,
            'error': error}
    return render(request, "new1/create.html", data)

def index(request):
    with connection.cursor() as cursor:
        RET = (datetime.date(2021,1,1), datetime.date(2021,8,31))
        cursor.execute("SELECT * FROM Probn2(%s,%s)", RET )
        row = namedtuplefetchall(cursor)
    new = Articles.objects.all()
    cursor.close
    return render(request, "new1/new1_home.html", {'news':new,'row':row})
# Create your views here.
