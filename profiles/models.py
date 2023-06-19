from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    position = models.CharField(max_length=221, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='profile/')
    is_owner = models.BooleanField(default=False)

    @property
    def full_name_(self):
        full_name = []
        if self.author.first_name:
            full_name.append(self.author.first_name.title())
        if self.author.last_name:
            full_name.append(self.author.last_name.title())
        if full_name:
            return ' '.join(full_name)
        else:
            return self.author.username

    def __str__(self):
        return self.full_name_


def profile_post_save(instance, sender, created, *args, **kwargs):
    if created:
        obj = Profile.objects.create(author=instance)
        return obj
    return None


post_save.connect(profile_post_save, sender=User)
