from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView
from employee_information.views import team_details
from .views import file_upload
urlpatterns = [
     path('home_lead', views.home_lead, name="home-lead"),
     path('team_details',views.team_details,name="team_details"),
     path('file-upload',views.file_upload,name="file-upload"),
     path('delete/<int:id>',views.delete,name='delete'),
     path('study_material',views.study_material,name='study_material'),
     path('delete_material/<int:id>',views.delete_material,name='delete_material'),
     path('notices_lead',views.notices_lead,name='notices_lead'),
     path('team_attendance',views.team_attendance,name='team_attendance'),
     path('quiz_upload',views.quiz_upload,name='quiz_upload'),
     path('delete_quiz/<int:id>',views.delete_quiz,name='delete_quiz'),

]