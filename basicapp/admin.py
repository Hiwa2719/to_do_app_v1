from django.contrib import admin

from .models import ToDo


@admin.register(ToDo)
class ToDoModelAdmin(admin.ModelAdmin):
    pass
