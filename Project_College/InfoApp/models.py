from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    dept_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name


class Student(models.Model):

    Roll_No=models.IntegerField()
    Stu_name=models.CharField(max_length=50)
    Marks=models.IntegerField()

    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.Stu_name




class Lecturer(models.Model):

    Lecturer_name = models.CharField(max_length=30)
    Lecturer_subject=models.CharField(max_length=30)

    dept_name = models.ManyToManyField(Department)

    '''
    def multiple_dept_of_lectuer(self):
        return ",".join([str(x) for x in self.department.all()])
        
    '''

    def __str__(self):
        return self.Lecturer_name





