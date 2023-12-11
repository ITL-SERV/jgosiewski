from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models    

class UserAdmin(UserAdmin):
    fieldsets = (
                (None, {
            "fields": (
                "username", "first_name", "last_name", "email", 
                "password", "groups", "user_permissions", "is_staff", 
                "is_active", "is_superuser", "last_login", "date_joined", "phone", "type_user"  
                )
        }),
    )  

admin.site.register(models.User, UserAdmin)

admin.site.register(models.TypeUser)