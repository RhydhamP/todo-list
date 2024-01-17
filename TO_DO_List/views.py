from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import *

# username:rhydham password:rhy@1111
# Create your views here.
def index(request):
    return render(request, 'newTaskCreation.html')

def createNewTask(request):
    task_list = task.objects.all()
   
    if request.method=="POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title in task_list:
            messages.error(request, 'Title Already taken')
            return redirect(createNewTask)
        elif title and description:
            newTask = task.objects.create(
                title=title,
                description=description
            )
            newTask.save()
            return redirect(createNewTask)
        else:
            return redirect(createNewTask)


    return render(request, 'newTaskCreation.html', {'task_list':task_list})

def edit(request, id):
    title = task.objects.get(id=id)
    description = task.objects.get(id=id)

    title.delete()

    return render(request, 'edit.html', {'title': title})

def delete(request, id):
    title = task.objects.get(id=id)
    title.delete()

    return redirect(createNewTask)

def start(request, id):
    title = task.objects.get(id=id)

    title.start = True
    title.save()

    return redirect(createNewTask)

def complete(request, id):
    title = task.objects.get(id=id)

    if title.start:
        title.complete = True
    title.save()

    return redirect(createNewTask)

def login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
       
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
         
        
        user = authenticate(username=username, password=password)
         
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            User.objects.filter(username)
            return redirect('index')
     
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
         
        user = User.objects.filter(username=username)
         
        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/register/')
         
        user = User.objects.create_user(
            username=username,
            email=email
        )
         
        user.set_password(password)
        user.save()
         
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')
    
    return render(request, 'register.html')

def logout(request):
    return render(request, 'index.html')