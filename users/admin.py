from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    # Add form = 
    model = CustomUser
    list_dispaly = ["username","email","is_staff"]
    
admin.site.register(CustomUser,CustomUserAdmin)