from django.urls import path
from .views import login_user, logout_user, create_user

app_name = 'profiles'

urlpatterns = [
    path('account/login/', login_user, name='login'),
    path('account/logout/', logout_user, name='logout'),
    path('account/create/', create_user, name='register'),
]
