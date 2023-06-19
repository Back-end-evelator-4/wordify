from django.db.models.signals import pre_save, post_save
from .models import Blog
from django.utils.text import slugify


def blog_post_save(instance, sender, created, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        print([slug[0] for slug in sender.objects.values_list('slug')])
        if instance.slug in [slug[0] for slug in sender.objects.values_list('slug')]:
            instance.slug += str(instance.id)
        instance.save()
    return instance


post_save.connect(blog_post_save, sender=Blog)
