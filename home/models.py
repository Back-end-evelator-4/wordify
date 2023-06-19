from django.db import models
from profiles.models import Profile
from django.shortcuts import reverse


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Travel(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=221)
    slug = models.SlugField(null=True, blank=True, unique_for_date='created_date', max_length=221)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    description = models.TextField()
    views = models.IntegerField(default=0, editable=False)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modifate_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    @property
    def url_detail_blog(self):
        return reverse('home:views', kwargs={
            'slug': self.slug,
            'year': self.created_date.year,
            'month': self.created_date.month,
            'day': self.created_date.day
        })

    @property
    def url_detail_views_blog(self):
        return reverse('home:detail', kwargs={
            'slug': self.slug,
            'year': self.created_date.year,
            'month': self.created_date.month,
            'day': self.created_date.day
        })

    def __str__(self):
        return self.title


class SubBlog(models.Model):
    description = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blog.title}'s sub blog"


class Image(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='blog')
    sub_blog = models.ForeignKey(SubBlog, on_delete=models.CASCADE)
    is_vide = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sub_blog.blog.title}'s sub blog's image"


class Feedback(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.blog.title}'s feedback"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=221, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='comment')
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.blog.title}'s comment"
