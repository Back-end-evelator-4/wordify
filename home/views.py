from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from .forms import CommentForm
from .models import Tag, Category, Blog
from django.contrib import messages


def home(request):
    blog_list = Blog.objects.order_by('-id')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    paginator = Paginator(blog_list, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    ctx = {
        'blogs': page_obj,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'home/index.html', ctx)


def blogs(request):
    blog_list = Blog.objects.order_by('-id')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    tag = request.GET.get('tag')
    if tag:
        blog_list = blog_list.filter(tags__title__exact=tag)
    category = request.GET.get('category')
    if category:
        blog_list = blog_list.filter(tags__title__exact=category)
    travel = request.GET.get('travel')
    if travel:
        blog_list = blog_list.filter(tags__title__exact=travel)

    paginator = Paginator(blog_list, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    ctx = {
        'blogs': page_obj,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'home/blog.html', ctx)


def detail_blog(request, **kwargs):
    obj = get_object_or_404(Blog, slug=kwargs['slug'], created_date__day=kwargs['day'],
                            created_date__month=kwargs['month'], created_date__year=kwargs['year'])
    form = CommentForm()
    has_image = False
    if request.method == "POST":
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj1 = form.save(commit=False)
            if obj1.image:
                has_image = True
            obj1.blog = obj
            if request.user.is_authenticated:
                full_name = []
                if request.user.first_name:
                    full_name.append(request.user.first_name)
                if request.user.last_name:
                    full_name.append(request.user.last_name)
                if full_name:
                    obj1.name = " ".join(full_name)
                else:
                    obj1.name = request.user.username
                if request.user.email:
                    obj1.email = request.user.email
                if request.user.profile.image:
                    obj1.image = request.user.profile.image
                    has_image = True
            obj1.save()
            print(obj1.image)

            messages.success(request, 'your comment was successfully accepted')
            return redirect('.')
        messages.info(request, 'fields must not be empty')
    ctx = {
        'has_image': has_image,
        'obj': obj,
        'form': form
    }
    return render(request, 'home/blog-single.html', ctx)


def views_blogs(request, **kwargs):
    obj = get_object_or_404(Blog, slug=kwargs['slug'], created_date__day=kwargs['day'],
                            created_date__month=kwargs['month'], created_date__year=kwargs['year'])
    obj.views += 1
    obj.save()
    return redirect(obj.url_detail_views_blog)
