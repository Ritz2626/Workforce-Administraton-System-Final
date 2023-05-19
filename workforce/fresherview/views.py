from django.shortcuts import render

# Create your views here.
from employee_information.views import fresher_dashboard
from employee_information.models import Department,Employees,Attendance,notification
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
    if request.method=='POST':
     query1=request.POST['startdate']
     query2=request.POST['enddate']
     pid=request.user
     n=Employees.objects.filter(code=pid)
     f=Employees.objects.filter(code=pid).values
     p=Employees.objects.get(code=pid).pk
     attend=Attendance.objects.filter(date__range=[query1,query2],employee_id=p).order_by('-date')
     print(attend)
     
     context={
        'attend':attend,
        'n':n

     }
     return render(request,'fresher_view/check_attendance.html',context)
    else:
     context={}
     return render(request,'fresher_view/check_attendance.html',context)

def notices_fresher(request):
    context={
        'notices':notification.objects.order_by('-time')
    }
    return render(request,'fresher_view/notices.html',context)