from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.everyblogs, name='everyblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

] 
