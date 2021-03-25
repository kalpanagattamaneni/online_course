from django.contrib import admin

from .models import Instructor

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id','name')
    list_filter = ('name',)
    search_fields = ('title','description')
    list_per_page = 10
    
admin.site.register(Instructor, InstructorAdmin)