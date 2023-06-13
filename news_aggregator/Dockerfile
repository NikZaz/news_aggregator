# Используем базовый образ Python
FROM python:3.9

# Установливаем среду
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Установливаем зависимости проекта
COPY requirements.txt .
RUN pip install -r requirements.txt

# Скопируем код проекта в контейнер
COPY . .

# Скопируем файл manage.py в контейнер
COPY manage.py .

# Запускаем сервер Django
CMD python manage.py runserver 0.0.0.0:8000
