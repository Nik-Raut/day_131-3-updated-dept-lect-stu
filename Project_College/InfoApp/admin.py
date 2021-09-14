

from django.contrib import admin
from .models import *

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','dept_name']

admin.site.register(Department,DepartmentAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','Stu_name','Roll_No','Marks','dept_name']


admin.site.register(Student, StudentAdmin)


class LecturerAdmin(admin.ModelAdmin):
    list_display = ['id','Lecturer_name','Lecturer_subject']


admin.site.register(Lecturer, LecturerAdmin)



