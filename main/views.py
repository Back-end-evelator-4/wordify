from django.shortcuts import render
from home.models import Blog
from django.core.paginator import Paginator
from profiles.models import Profile
from .models import About


def about(request):
    abouts = About.objects.order_by('-id')
    blogs = Blog.objects.order_by('-id')
    paginator = Paginator(blogs, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    ctx = {
        "blogs": page_obj,
        "abouts": abouts
    }
    return render(request, 'main/about.html', ctx)
