# news_aggregator

<img width="1429" alt="Main" src="https://github.com/NikZaz/news_aggregator/assets/115639869/99647893-63ed-4920-9a62-c1f38ec09098">
<img width="1432" alt="Main_2" src="https://github.com/NikZaz/news_aggregator/assets/115639869/1e99f909-5ec1-4fdb-ac68-6ae5efdee41c">
<img width="1430" alt="Registration" src="https://github.com/NikZaz/news_aggregator/assets/115639869/6ab919f2-e6ed-4954-8385-2898a5b92a8d">
<img width="1428" alt="Login" src="https://github.com/NikZaz/news_aggregator/assets/115639869/065d15c1-17f1-42dd-9ba4-1fd3a6d40a86">
<img width="1426" alt="Create_post" src="https://github.com/NikZaz/news_aggregator/assets/115639869/b14cb9d0-48aa-4b35-bf6c-9660a88cf50a">



News web application:
This web application is designed for parsing and displaying a list of articles from the news resources Lenta.ru and RIA.ru.



Functionality:

Parsing news: The application automatically parses news from Lenta.ru and RIA.ru and stores it in the database.
Article list display: Users can view a list of articles with posters, titles and brief descriptions.
Full information about the article: When clicking on the article, the user can view full information including text content, pictures and links to the source.

User registration: Users can register with the app to create and publish their own articles.
Publication Requests: Registered users can submit requests to publish their articles. The application administrator reviews the requests and decides whether to publish.



Technology:

Programming language: Python;

Framework: Django;

Database: PostgreSQL;

Task queue: Celery;

Message broker: Redis;

Front-end: HTML, CSS, JavaScript;

Containerization system: Docker;



Running the project:

Install - Docker, PostgreSQL, Celery, Redis on your machine.

Clone the project repository.

Navigate to the project directory.

In the terminal, run the following command to start the application:
```
docker-compose up --build
```
Open a browser and go to http://....:8000 to access the application.




Project Development:

Further development of the project may include the following improvements and additional features:

Expansion of the list of supported news resources.

The ability to comment on articles.

Filtering and search for articles by various criteria.

Automatic categorization of articles and providing recommendations to the user.

Improvement of the interface and design of the application.

I welcome any contributions to the project and invite you to join in its development and improvement.



На русском:


Новостное веб-приложение:
Это веб-приложение разработано для парсинга и отображения списка статей с новостных ресурсов Lenta.ru и RIA.ru.



Функциональность:

Парсинг новостей: Приложение автоматически парсит новости с ресурсов Lenta.ru и RIA.ru и сохраняет их в базе данных.
Отображение списка статей: Пользователи могут просматривать список статей с постерами, заголовками и краткими описаниями.
Полная информация о статье: При клике на статью, пользователь может просмотреть полную информацию, включая текстовый контент, картинки и ссылки на источник.

Регистрация пользователей: Пользователи могут зарегистрироваться в приложении для создания и публикации своих собственных статей.
Запросы на публикацию: Зарегистрированные пользователи могут отправлять запросы на публикацию своих статей. Администратор приложения просматривает запросы и принимает решение о публикации.



Технологии:

Язык программирования: Python;

Фреймворк: Django;

База данных: PostgreSQL;

Очередь задач: Celery;

Брокер сообщений: Redis;

Front-end: HTML, CSS, JavaScript;

Система контейнеризации: Docker;



Запуск проекта:

Установите - Docker, PostgreSQL, Celery, Redis на свою машину.

Склонируйте репозиторий проекта.

Перейдите в каталог проекта.

В терминале выполните следующую команду для запуска приложения:

docker-compose up --build

Откройте браузер и перейдите по адресу http://....:8000 для доступа к приложению.



Развитие проекта:

Дальнейшее развитие проекта может включать следующие улучшения и дополнительные функции:

Расширение списка поддерживаемых новостных ресурсов.

Возможность комментирования статей.

Фильтрация и поиск статей по различным критериям.

Автоматическая категоризация статей и предоставление пользователю рекомендаций.

Улучшение интерфейса и дизайна приложения.

Я приветсвую любые вклады в развитие проекта и приглашаем вас присоединиться к его разработке и улучшению.
