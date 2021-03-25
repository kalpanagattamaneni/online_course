from django.contrib import admin

from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','price', 'next_batch_start_date', 'instructor')
    list_display_links = ('id','title')
    list_filter = ('instructor',)
    list_editable = ('is_published',)
    search_fields = ('title','description', 'course_curriculum')
    list_per_page = 10
admin.site.register(Course, CourseAdmin)
