# Generated by Django 4.2.1 on 2023-06-10 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_usernews_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usernews',
            name='image',
        ),
    ]