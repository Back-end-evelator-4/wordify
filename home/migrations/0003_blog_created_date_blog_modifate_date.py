# Generated by Django 4.2.2 on 2023-06-12 06:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='modifate_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
