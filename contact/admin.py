from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'time')
    fields = ('name', 'phone', 'email', 'message')
    date_hierarchy = 'time'
    list_filter = ('time', )
    search_fields = ('phone', 'email', 'name')

