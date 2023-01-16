from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
# admin.site.register(User)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username','email','password']
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email","password1", "password2"),
            },
        ),
    )