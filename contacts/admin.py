from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','course', 'email', 'contact_date')
    list_disply_links = ('id', 'name')
    search_fields = ('name', 'email', 'course')
    list_per_page =25


admin.site.register(Contact, ContactAdmin)

