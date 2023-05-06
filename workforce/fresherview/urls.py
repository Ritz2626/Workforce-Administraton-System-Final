from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView
from employee_information.views import fresher_dashboard
urlpatterns = [
     path('fresher_dashboard/<int:pid>',views.fresher_dashboard,name='fresher_dashboard'),
     path('fresher_home',views.fresher_home,name='fresher_home'),
     path('quiz',views.quiz,name='quiz'),
     path('study',views.study,name='study'),
]