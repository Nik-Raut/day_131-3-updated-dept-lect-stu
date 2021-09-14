from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),

    #addview
    path('addStudent/',addStudent,name='addStudent'),
    path('addLecturer/',addLecturer,name='addLecturer'),
    path('addDepartment/',addDepartment,name='addDepartment'),

    #showlist
    path('studentsList/',studentsList,name='studentsList'),
    path('lecturersList/',lecturersList,name='lecturersList'),
    path('deparmentsList/', deparmentsList, name='deparmentsList'),

    path('dept_stu/<int:id>', dept_stu, name='dept_stu'),
    path('dept_lect/<int:id>', dept_lect, name='dept_lect'),


    #update
    path('updateStudent/<int:id>', updateStudent, name='updateStudent'),
    path('updateLecturer/<int:id>', updateLecturer, name='updateLecturer'),
    path('updateDepartment/<int:id>', updateDepartment, name='updateDepartment'),

    #deleteview
    path('deleteStudent/<int:id>', deleteStudent, name='deleteStudent'),
    path('deleteLecturer/<int:id>', deleteLecturer, name='deleteLecturer'),
    path('deleteDepartment/<int:id>', deleteDepartment, name='deleteDepartment'),

    #search
    path('search/',search, name='search'),





]