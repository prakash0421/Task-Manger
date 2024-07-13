from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task,Register
from .form import Registerform,Taskform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .dd import get_coordinates
def my_task(request):
    task=Task.objects.filter(assigned_to=request.user)
    return render(request,'my_task.html',{'tasks':task})
    

def home(request):
    return render(request,'home.html')


def register(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            address = form.cleaned_data.get('address')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            coordinates = get_coordinates(address)

            if coordinates is None:
                form.add_error('address', 'Invalid address')
            else:
                user.latitude = coordinates[0]
                user.longitude = coordinates[1]
                user.save()

                # Authenticate and log the user in
                
                user = authenticate( username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    print('success')
                    return redirect('home')  # Redirect to a success page
                else:
                    form.add_error(None, 'Authentication failed')

    else:
        form = Registerform()

    return render(request, 'register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # or any other page
        else:
            # Invalid form, you can add an error message or handle it as needed
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout(request):
    auth_logout(request)
    return redirect('home')
@login_required(login_url='/login/')
# views.py


def add_task(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():  # Check if the form data is valid
            # Retrieve cleaned data from the form
            task_name = form.cleaned_data['task_name']
            due_date = form.cleaned_data['due_date']
            assigned_by = form.cleaned_data['assigned_by']
            status = form.cleaned_data['status']
            assigned_to = form.cleaned_data['assigned_to']

            # Create a new Task object
            Task.objects.create(
                task_name=task_name,
                due_date=due_date,
                assigned_by=assigned_by,
                assigned_to=assigned_to,
                status=status
            )
            return redirect('home')  # Redirect to 'home' URL after successful task creation
    else:
        form = Taskform()
    
    return render(request, 'add_task.html', {'form': form})

def view_all_task(request):
    task=Task.objects.all()
    return render(request,'view_all_task.html',{'tasks':task})
def edit(request, pk):
    task = get_object_or_404(Task, id=pk)  # Retrieve single Task instance or return 404 if not found

    if request.method == "POST":
        status = request.POST.get('status')
        task.status = status
        task.save()  # Save the updated status to the task object
        return redirect('home')  # Redirect to 'home' URL after updating

    return render(request, 'edit.html', {'tasks': task})
def my_profie(request):
    detail=Register.objects.get(username=request.user)
    return render(request,'profie.html',{'detail':detail})
def delete_account(request,pk):
    delete=Register.objects.filter(id=pk)
    delete.delete()
    return redirect('home')
def delete(request,pk):
    delete=Task.objects.filter(id=pk)
    delete.delete()
    return redirect('view_all_task')
# Create your views here.
