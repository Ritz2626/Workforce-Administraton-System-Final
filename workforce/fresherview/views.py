from django.shortcuts import render

# Create your views here.
from employee_information.views import fresher_dashboard
from employee_information.models import Department,Employees
from .models import Quiz,video

def quiz(request):
    pid=request.user
    dept=Employees.objects.get(code=pid).department_id
    quizzes=Quiz.objects.all()
    context={
        'dept':dept,
        'quiz':quizzes
    }
    return render(request,'fresher_view/quiz.html',context)

def fresher_home(request):
    pid=request.user
    fresher=(Employees.objects.filter(code=pid).values)
    dept=Employees.objects.get(code=pid).department_id
    pos=Employees.objects.get(code=pid).position_id
    proj=Employees.objects.get(code=pid).project_id
    context={
        'fresher':fresher,
        'dept':dept,
       'pos':pos,
       'proj':proj,
    }
    return render(request,'fresher_view/home_fresher.html',context)

def study(request):
    videos=video.objects.all()
    context={
        'videos':videos,
    }
    return render(request,'fresher_view/study_material.html',context)

def fresher_attendance(request):
    return render(request,'fresher_view/check_attendance.html')
