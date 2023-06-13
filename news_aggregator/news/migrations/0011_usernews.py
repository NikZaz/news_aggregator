# Generated by Django 4.2.1 on 2023-06-10 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0010_remove_news_moderated_remove_news_moderator'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image_url', models.URLField(blank=True)),
                ('full_text', models.TextField()),
                ('moderated', models.BooleanField(default=False)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
