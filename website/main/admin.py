from django.contrib import admin
from django.contrib import admin
from .models import Transaction, Project  # Import the models here


# Register your models here.

admin.site.register(Transaction)
admin.site.register(Project)
