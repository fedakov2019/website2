from django.forms import formset_factory
from django.shortcuts import render,redirect
from .form1 import spisok1
from .form import UserForm
from django.db import connection
from .pipr import report
import numpy as np
import datetime
from collections import namedtuple
import pandas as pd
def recup_wos(request):
    return render(request, "news/news_home.html")
def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
def othet(request):
    error = ''

    nefs = UserForm()
    rn1 = 'Сформировать отчет Да/Нет?'


    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            date2 = {'rd': rn1,
                      'error': error,
                 'form': form                 }
            date1= form.cleaned_data['date1'].strftime('%d.%m.%Y')
            date2 = form.cleaned_data['date2'].strftime('%d.%m.%Y')
            return redirect("othet11", date1, date2)
        else:
             error='ошибка ввода'

    date2 = {'rd': rn1,
                'error': error,
                'form': nefs,

                }
    return render(request, "news/othet1.html", date2)
def othet1(request, date1, date2):

    ret = (datetime.datetime.strptime(date1,'%d.%m.%Y').date(),datetime.datetime.strptime(date2,'%d.%m.%Y').date())
    with connection.cursor() as cursor:

        cursor.execute("SELECT  [dat] ,[ksg] FROM [test1].[dbo].[spisok] where dat between "+
                       "%s and %s", ret)
        row = namedtuplefetchall(cursor)
        spisok=()
        for el in row:
           spisok += (el[1],str(el[1])+' '+el[0].strftime('%d.%m.%Y')),
        form1=spisok1(spisok)
        form2=formset_factory(form1)
        form3=form2()
        error=''
        if request.method == 'POST':
            form = form2(request.POST)
            if form.is_valid():
                dat = form.cleaned_data[0].get('Countries')
                as1=''
                for el in dat:
                    if as1=='':
                        as1=el
                    else:
                        as1+=','+el

                date2 = {'d1': date1,
                         'd2': date2,
                         'error': error,
                         'form': as1}


                return render(request, "news/othet111.html", date2)
            else:
                error = 'ошибка ввода'
        date2 = {'d1': date1,

                 'd2': date2,
                  'rew':form3,
                 'error':error
                 }

    return render(request, "news/othet11.html", date2)