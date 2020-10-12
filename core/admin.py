from django.contrib import admin
from .models import pet 
# Register your models here.

@admin.register 
class PetAdmin(admin.ModelAdmin.)
    list_display = ['id','city']