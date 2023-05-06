from django.db import models
from django.utils.timezone import now
from employee_information.models import Department
# Create your models here.
class Quiz(models.Model):
    name=models.CharField(max_length=255)
    link_quiz=models.CharField(max_length=255)
    duration=models.IntegerField(help_text="Enter the duration in minutes")
    date=models.DateTimeField(default=now)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    link_answer=models.CharField(max_length=500)


    def __str__(self):
        return self.name
    
class video(models.Model):
    name=models.TextField()
    link=models.TextField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
