from django.urls import path

from .views import index, login, logout, register, view_project, demo_project, view_image, view_projects_page, view_by_technology

t=1
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('jewels/', index, name='jewel_projects'),
    path('bootcamp/', index, name='bootcamp_projects'),
    path('all_projects/', index, name='all_projects'),
    path('view_project/<int:project_id>', view_project, name='view_project'),
    path('demo_project/<str:project_slug>', demo_project, name='demo_project'),
    path('view_image/<int:image_id>', view_image, name='view_image'),
    path('view_projects_page/<int:page_id>', view_projects_page, name='view_projects_page'),
    path('view_by_technology/<int:technology_id>', view_by_technology, name='view_by_technology'),
]