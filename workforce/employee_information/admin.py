from django.contrib import admin
from employee_information.models import Department, Position, Employees,Project,notification,Task,Attendance
from leadview.models import files1
from employeeview.models import Leave
# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'date', 'status')
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employees)
admin.site.register(Project)
admin.site.register(notification)
admin.site.register(Task)
admin.site.register(files1)
admin.site.register(Leave)
admin.site.register(Attendance,AttendanceAdmin)