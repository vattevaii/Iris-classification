# from django.conf.urls import url,include
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.rend,name="main"),
    path('input/', views.inp, name='input'),
    path('input-succ/', views.success, name='input_success'),
    path('list/',views.list_of_iris.as_view(), name='list'),
]