from django.contrib import admin
from django.urls import path, re_path, register_converter
from . import views
from . import converters 
from main.views import registration




urlpatterns = [
    path('', views.index, name='home'), #main
    path('about/', views.about, name='about'), 
    path('user/registration/', registration),
    path('user/login/', views.login_us, name='login'),
    path('chet/plus/', views.plus),
    path('chet/plus/ez/', views.plus_ez, name='1+'),
    path('chet/plus/no/', views.plus_no, name='2+'),
    path('chet/plus/har/', views.plus_har, name='3+'),
    path('chet/minus/', views.minus),
    path('chet/minus/ez/', views.minus_ez, name='1-'),
    path('chet/minus/no/', views.minus_no, name='2-'),
    path('chet/minus/har/', views.minus_har, name='3-'),
    path('chet/mult/', views.mult),
    path('chet/mult/ez/', views.mult_ez, name='1*'),
    path('chet/mult/no/', views.mult_no, name='2*'),
    path('chet/mult/har/', views.mult_har, name='2*'),
    path('chet/divis/', views.divis),
    path('chet/divis/ez/', views.divis_ez, name='1/'),
   #path('chet/divis/no/', views.divis_no, name='2/'),
    #path('chet/divis/har/', views.divis_har, name='3/'),
   # path('fix/<int:pk>', match_problem_fix, name="fix")   
]
