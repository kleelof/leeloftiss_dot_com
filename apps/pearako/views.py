from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegistrationForm
from .models import Projects
from .utils import _get_project_by_id, _get_project_by_slug


def index(request):
    template = 'index'
    projects = Projects.objects.filter(show_on_home=True)

    if request.path == '/jewels/':
        template ='jewels'
        projects = Projects.objects.filter(show_on_jewels=True)

    if request.path == '/bootcamp/':
        template = 'bootcamp'
        projects = Projects.objects.filter(show_on_bootcamp=True)

    if request.path == '/all_projects/':
        template = 'all_projects'
        projects = Projects.objects.all()

    return render(request, f'pearako/{template}.html', {'projects': projects})


def login(request):
    if not request.POST:
        return render(request, 'pearako/login.html')

    if request.POST['username'] and request.POST['password']:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            auth_login(request, user)
            return redirect('index')

    messages.error(request, 'Invalid Credentials')
    return redirect('login')


def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('index')


def register(request):
    if not request.POST:
        return render(request, 'pearako/register.html')

    form = RegistrationForm(request.POST)
    if not form.is_valid():
        return render(request, 'pearako/register.html', {'form': form})

    form.save()
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password=password)
    auth_login(request, user)
    return redirect('index')


def view_project(request, project_id):
    project = _get_project_by_id(project_id)
    if not project:
        messages.error(request, 'Invalid Project')
        return redirect('index')
    return render(request, 'pearako/view_project.html', {'project': project})


def demo_project(request, project_slug):
    project = _get_project_by_slug(project_slug)
    if not project:
        messages.error(request, 'Invalid Project')
        return redirect('index')
    return render(request, f'pearako/demo_projects/{project.slug}.html', {'project': project})



