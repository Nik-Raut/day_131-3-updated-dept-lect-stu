from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


def home(request):
    template_name='InfoApp/home.html'
    context={}
    return render(request,template_name,context)

#create view

@login_required(login_url='login')
def addStudent(request):
    form=StudntForm()
    if request.method=='POST':
        form=StudntForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentsList')
    template_name='InfoApp/addStudent.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='login')
def addLecturer(request):
    form = LecturerForm()
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lecturersList')
    template_name = 'InfoApp/addLecturer.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login')
def addDepartment(request):

    form = DepartmentForm()
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deparmentsList')
    template_name = 'InfoApp/addDepartment.html'
    context = {'form': form}
    return render(request, template_name, context)

#show all views

def studentsList(request):
    all_students=Student.objects.all()
    context = {'all_students': all_students}
    template_name = 'InfoApp/listStudent.html'
    return render(request, template_name, context)

def lecturersList(request):
    all_lecturers=Lecturer.objects.all()
    context = {'all_lecturers': all_lecturers}
    template_name = 'InfoApp/listLecturer.html'
    return render(request, template_name, context)


def deparmentsList(request):
    all_departments=Department.objects.all()
    context = {'all_departments': all_departments}
    template_name = 'InfoApp/listDepartment.html'
    return render(request, template_name, context)

@login_required(login_url='login')
def dept_stu(request, id):
    department = Department.objects.get(id=id)
    all_students = Student.objects.filter(dept_name=department)
    template_name = 'InfoApp/departmentStudents.html'
    context = {'all_students': all_students}
    return render(request, template_name, context)

@login_required(login_url='login')
def dept_lect(request, id):
    department = Department.objects.get(id=id)
    all_lecturers = Lecturer.objects.filter(dept_name=department)
    template_name = 'InfoApp/departmentLecturer.html'
    context = {'all_lecturers': all_lecturers}
    return render(request, template_name, context)


#updateview

@login_required(login_url='login')
def updateStudent(request,id):
    student = Student.objects.get(id=id)
    form=StudntForm(instance=student)

    if request.method=='POST':
        form=StudntForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('studentsList')
    template_name = 'InfoApp/addStudent.html'
    context={'form':form}
    return render(request, template_name, context)

@login_required(login_url='login')
def updateLecturer(request,id):
    lecturer = Lecturer.objects.get(id=id)
    form=LecturerForm(instance=lecturer)

    if request.method=='POST':
        form=LecturerForm(request.POST,instance=lecturer)
        if form.is_valid():
            form.save()
            redirect('lecturersList')
    template_name = 'InfoApp/addLecturer.html'
    context={'form':form}
    return render(request, template_name, context)

@login_required(login_url='login')
def updateDepartment(request, id):
    dept = Department.objects.get(id=id)
    form = DepartmentForm(instance=dept)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=dept)
        if form.is_valid():
            form.save()
            return redirect('deparmentsList')
    template_name = 'InfoApp/addDepartment.html'
    context = {'form': form}
    return render(request, template_name, context)

#deleteview

@login_required(login_url='login')
def deleteStudent(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('studentsList')


@login_required(login_url='login')
def deleteLecturer(request,id):
    lect=Lecturer.objects.get(id=id)
    lect.delete()
    return redirect('lecturersList')

@login_required(login_url='login')
def deleteDepartment(request, id):
    dept = Department.objects.get(id=id)
    '''
    data = Lecturer.objects.filter(dept_name=dept)
 
    for i in data:
        for j in i.dept_name.all():
            if len(i.dept_name.all()) == 1 and j == dept:
                i.delete()
    '''
    dept.delete()
    return redirect('deparmentsList')



@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        searched_name = request.POST.get('searchName')

        searched_stu = Student.objects.filter(Stu_name__icontains=searched_name)

        searched_lect = Lecturer.objects.filter(Lecturer_name__icontains=searched_name)

        context = {'searched_stu': searched_stu, 'searched_lect': searched_lect}
        return render(request, 'InfoApp/searchResult.html', context)
    template_name = 'InfoApp/searchData.html'
    context = {}
    return render(request, template_name, context)