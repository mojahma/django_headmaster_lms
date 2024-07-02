from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Teacher, Student

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Roles',
            {
                'fields': (
                    'is_teacher',
                    'is_student',
                ),
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
