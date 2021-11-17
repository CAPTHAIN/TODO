from django.contrib import admin
from .models import Problem


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'author', 'recipient', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description')
    list_filter = ('author',)


admin.site.register(Problem, TodoAdmin)
