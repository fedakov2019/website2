from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.recup_wos, name='news_home'),
    path('othet1/', views.othet, name='othet1'),
    path('othet1/<date1>/<date2>/', views.othet1, name='othet11'),



]
