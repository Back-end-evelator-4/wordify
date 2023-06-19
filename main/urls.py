from django.urls import path
from .views import about
app_name = 'main'

urlpatterns = [
    path('', about, name='about'),
]
