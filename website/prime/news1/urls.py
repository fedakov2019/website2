from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='news1_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail')
]