# Generated by Django 4.2.2 on 2023-06-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
