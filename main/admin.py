from django.contrib import admin
from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile')
    fields = ('profile', 'bio', 'image')
    list_editable = ('profile', )

