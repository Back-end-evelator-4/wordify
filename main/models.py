from django.db import models
from profiles.models import Profile


class About(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='about')

    def __str__(self):
        return f"Hi There! I'm {self.profile.author}"
