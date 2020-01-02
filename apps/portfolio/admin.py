from django.contrib import admin
from .models import Technology, Project, Image, Page

admin.site.register(Page)
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Technology)
