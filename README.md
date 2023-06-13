# news_aggregator

Git описание проекта:

Новостное веб-приложение
Это веб-приложение разработано для парсинга и отображения списка статей с новостных ресурсов Lenta.ru и RIA.ru.

Функциональность
Парсинг новостей: Приложение автоматически парсит новости с ресурсов Lenta.ru и RIA.ru и сохраняет их в базе данных.
Отображение списка статей: Пользователи могут просматривать список статей с постерами, заголовками и краткими описаниями.
Полная информация о статье: При клике на статью, пользователь может просмотреть полную информацию, включая текстовый контент, картинки и ссылки на источник.
Регистрация пользователей: Пользователи могут зарегистрироваться в приложении для создания и публикации своих собственных статей.
Запросы на публикацию: Зарегистрированные пользователи могут отправлять запросы на публикацию своих статей. Администратор приложения просматривает запросы и принимает решение о публикации.

Технологии:
Язык программирования: Python
Фреймворк: Django
База данных: PostgreSQL
Front-end: HTML, CSS, JavaScript
Веб-сервер: Gunicorn
Система контейнеризации: Docker
Запуск проекта
Установите Docker на свою машину.
Склонируйте репозиторий проекта.
Перейдите в каталог проекта.
В терминале выполните следующую команду для запуска приложения:

docker-compose up --build

Откройте браузер и перейдите по адресу http://localhost:8000 для доступа к приложению.

Развитие проекта:
Дальнейшее развитие проекта может включать следующие улучшения и дополнительные функции:

Расширение списка поддерживаемых новостных ресурсов.
Возможность комментирования статей.
Фильтрация и поиск статей по различным критериям.
Автоматическая категоризация статей и предоставление пользователю рекомендаций.
Улучшение интерфейса и дизайна приложения.
Мы приветствуем любые вклады в развитие проекта и приглашаем вас присоединиться к его разработке и улучшению.
