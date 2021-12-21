from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name',
                   'is_active', 'is_staff', )
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name',
                    'is_active', 'is_staff', 'is_superuser', 'last_login')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'password')}),
        ('Permissions', {'fields': ('is_staff',
                                    'is_active', 'is_client', 'is_superuser', 'groups','user_permissions')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_client', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )


admin.site.register(User, UserAdminConfig)
