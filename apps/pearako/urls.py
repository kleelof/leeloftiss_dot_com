from django.urls import path
from django.views.generic import TemplateView

from .views import index, login, logout, register, view_project

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('jewels/', index, name='jewel_projects'),
    path('bootcamp/', index, name='bootcamp_projects'),
    path('all_projects/', index, name='all_projects'),
    path('view_project/<int:project_id>', view_project, name='view_project'),
]