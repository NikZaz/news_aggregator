# Generated by Django 4.2.1 on 2023-06-10 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_delete_usernotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='source',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
