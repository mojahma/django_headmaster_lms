from django.contrib import admin
from .models import StaffProfile

@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'hire_date')
    search_fields = ('user__username', 'position')
    list_filter = ('position',)
    ordering = ('position',)  # Optional, but ensures default ordering in admin interface
