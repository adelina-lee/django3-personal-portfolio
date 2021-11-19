from django.contrib import admin

from .models import Project  # get Project from models.py

admin.site.register(Project)  # to display Project model in the admin page

# Register your models here.
