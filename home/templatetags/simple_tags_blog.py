from django import template
from home.models import Blog, Tag, Category, Travel
from django.core.paginator import Paginator
from main.models import Profile

register = template.Library()


@register.simple_tag()
def latest_three_blogs():
    return Blog.objects.order_by('-id')[:3]


@register.simple_tag()
def popular_three_blogs():
    return Blog.objects.order_by('-views')[:3]


@register.simple_tag()
def tags_list():
    return Tag.objects.all()


@register.simple_tag()
def categories_list():
    return Category.objects.all()


@register.simple_tag()
def travels_list():
    return Travel.objects.all()


@register.simple_tag()
def pagination(request):
    b_list = Blog.objects.order_by('-id')
    paginator = Paginator(b_list, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj


@register.simple_tag()
def about_owner():
    owner = Profile.objects.get(is_owner=True)
    return owner


