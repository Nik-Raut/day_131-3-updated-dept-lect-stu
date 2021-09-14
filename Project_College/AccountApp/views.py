
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def registraionview(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='AccountApp/registration.html'
    context={'form':form}
    return render(request,template_name,context)


def loginview(request):
    if request.method=='POST':
        U=request.POST.get('un')
        P=request.POST.get('ps')

        user=authenticate(username=U,password=P)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')

    template_name='AccountApp/login.html'
    context={}
    return render(request,template_name,context)


def logoutview(request):
    logout(request)
    return redirect('login')