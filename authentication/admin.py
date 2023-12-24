from django.contrib import admin
from .models import User

#from django.contrib.auth.admin import UserAdmin

# Customize Admin
class UserAdmin(admin.ModelAdmin):
    
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email', 'is_staff')
    list_per_page = 25
    

# Register your models here.
admin.site.register(User, UserAdmin)