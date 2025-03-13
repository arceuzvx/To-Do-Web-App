from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed', 'created_date')
    list_filter = ('completed', 'created_date', 'user')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_date'
