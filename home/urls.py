from django.urls import path
from .views import home, blogs, detail_blog, views_blogs

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('blogs/', blogs, name='blogs'),
    path('blog/detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', detail_blog, name='detail'),
    path('blog/views/<int:year>/<int:month>/<int:day>/<slug:slug>/', views_blogs, name='views'),
]
