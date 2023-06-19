from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'is_owner', 'position')
    fields = ('author', 'image', 'bio', 'position', 'is_owner')
    search_fields = ('author__username', )

