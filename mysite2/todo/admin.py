from django.contrib import admin
from todo.models import List, Task

class TaskInline(admin.TabularInline):
	model = Task
	extra = 3

class ListAdmin(admin.ModelAdmin):
	fields=['list_name']
	inlines = [TaskInline]
    


admin.site.register(List, ListAdmin)

