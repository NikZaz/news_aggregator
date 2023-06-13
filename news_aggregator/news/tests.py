from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserNews


class NewsIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('create_post')  # Замените 'create_post' на название вашего URL

    def test_create_news(self):
        # Создайте пользователя
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Определите данные для создания новости
        news_data = {
            'user': user,
            'title': 'Test News',
            'image_url': 'https://example.com/photo.jpg',
            'full_text': 'This is a test news',
        }

        # Создайте новость в базе данных
        created_news = UserNews.objects.create(**news_data)

        # Отправьте GET-запрос для получения созданной новости
        response = self.client.get(reverse('news_detail', kwargs={'pk': created_news.pk}))
        self.assertEqual(response.status_code, 200)

        # Проверьте, что полученный ответ содержит ожидаемые данные новости
        self.assertContains(response, 'Test News')
        self.assertContains(response, 'https://example.com/photo.jpg')
        self.assertContains(response, 'This is a test news')

