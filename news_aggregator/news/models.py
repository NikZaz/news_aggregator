from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User



class News(models.Model):
    """
    Модель новости.

    Представляет собой новость с заголовком, ссылкой, изображением (необязательно),
    полным текстом, датой публикации.

    Attributes:
        title (CharField): Заголовок новости.
        url (URLField): URL новости.
        image_url (URLField, optional): URL изображения новости.
        full_text (TextField): Полный текст новости.
        published_date (DateTimeField): Дата публикации новости.
    """
    title = models.CharField(max_length=255)
    url = models.URLField()
    image_url = models.URLField(blank=True)
    full_text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)


class UserNews(models.Model):
    """
    Модель новости пользователя.

    Представляет собой новость, связанную с конкретным пользователем, с заголовком,
    изображением (необязательно), полным текстом, флагом модерации и датой публикации.

    Attributes:
        user (ForeignKey): Пользователь, связанный с новостью.
        title (CharField): Заголовок новости.
        image_url (URLField, optional): URL изображения новости.
        full_text (TextField): Полный текст новости.
        moderated (BooleanField): Флаг модерации новости.
        published_date (DateTimeField): Дата публикации новости.
        comment (TextField): Комментарий администратора при модерации.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image_url = models.URLField(blank=True)
    full_text = models.TextField()
    moderated = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)

