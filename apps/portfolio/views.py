from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegistrationForm
from .models import Project, Image, Page, Technology
import random


def index(request):
    page = Page.objects.filter(is_home=True).first()
    if not page:
        page = Page.objects.all().first()

    return render(request, 'portfolio/projects_page_base.html', {
        'projects': Project.objects.filter(page=page) if page else None,
        'page': page
    })


def login(request):
    if not request.POST:
        return render(request, 'portfolio/login.html')

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
        return render(request, 'portfolio/register.html')

    form = RegistrationForm(request.POST)
    if not form.is_valid():
        return render(request, 'portfolio/register.html', {'form': form})

    form.save()
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password=password)
    auth_login(request, user)
    return redirect('index')


def view_project(request, project_id):
    project = Project.objects.filter(id=project_id).first()
    if not project:
        messages.error(request, 'Invalid Project')
        return redirect('index')
    related_projects = Project.objects.filter(technologies__in=project.technologies.all()).exclude(id=project.id).distinct()
    return render(request, 'portfolio/view_project.html', {
        'project': project,
        'related_projects': related_projects
    })


def demo_project(request, project_slug):
    project = Project.objects.filter(slug=project_slug).first()
    if not project:
        messages.error(request, 'Invalid Project')
        return redirect('index')
    return render(request, f'portfolio/demo_projects/{project.slug}.html', {'project': project})


def view_image(request, image_id):
    image = Image.objects.get(pk = image_id)
    return render(request, 'portfolio/display_image.html', {'image': image})


def view_projects_page(request, page_id):
    page = Page.objects.filter(id=page_id).first()
    projects = Project.objects.filter(page=page) if page else None
    if projects:
        projects = [project for project in projects]
        random.shuffle(projects)
    return render(request, 'portfolio/projects_page_base.html', {
        'projects': projects,
        'page': page
    })


def view_by_technology(request, technology_id):
    technology = Technology.objects.filter(id=technology_id).first()
    if not technology:
        pass
    projects = Project.objects.filter(technologies=technology)
    if projects:
        projects = [project for project in projects]
        random.shuffle(projects)
    return render(request, 'portfolio/projects_page_base.html', {
        'technology': technology,
        'projects': projects
    } )

