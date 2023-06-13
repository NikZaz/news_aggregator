from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.db.models import Q
from .models import News, UserNews
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class CreatePostForm(forms.Form):
    """
    Форма для создания новой записи.
    Содержит поля: title, image_url, full_text.
    """
    title = forms.CharField(max_length=200)
    image_url = forms.URLField(required=False)
    full_text = forms.CharField(widget=forms.Textarea)


def index_view(request):
    """
    Отображает главную страницу с новостями.
    Получает список новостей из модели News и передает его в шаблон 'index.html'.
    """
    news = News.objects.order_by('-published_date')
    return render(request, 'index.html', {'news': news})


def registration_view(request):
    """
    Обрабатывает регистрацию пользователей.
    При отправке POST-запроса проверяет введенные данные, создает нового пользователя и осуществляет вход в систему.
    """
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST and 'email' in request.POST:
            # Обработка введенных данных
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']

            username = username.lower()

            # Проверка наличия пользователя с таким же именем или email
            if User.objects.filter(Q(username__iexact=username) | Q(email__iexact=email)).exists():
                messages.error(
                    request, 'Пользователь с таким именем или email уже существует.')
                return redirect('registration')

            try:
                validate_email(email)
            except ValidationError:
                messages.error(request, 'Некорректный email.')
                return redirect('registration')

            email = email.lower()

            try:
                validate_password(password, user=User(username=username))
            except ValidationError as e:
                messages.error(request, ', '.join(e.messages))
                return redirect('registration')

            # Создание нового пользователя
            user = User.objects.create_user(
                username=username, password=password, email=email)
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Не все поля формы были заполнены.')
            return redirect('registration')

    return render(request, 'registration.html')


def login_view(request):
    """
    Обрабатывает вход пользователя в систему.
    При отправке POST-запроса проверяет введенные данные и осуществляет вход в систему.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
            return redirect('login')

    return render(request, 'login.html')


def logout_view(request):
    """
    Выполняет выход пользователя из системы.
    """
    logout(request)
    return redirect('index')


def news_detail(request, news_id):
    """
    Отображает детали новости.
    Получает объект новости по заданному идентификатору и передает его в шаблон 'news_detail.html'.
    """
    news = get_object_or_404(News, pk=news_id)
    can_delete = request.user.is_superuser
    confirm_delete = False

    if request.method == 'POST' and can_delete:
        if 'delete' in request.POST:
            confirm_delete = True
        elif 'confirm_delete' in request.POST:
            confirm = request.POST.get('confirm_delete')

            if confirm == 'yes':
                news.delete()
                messages.success(request, 'Новость успешно удалена.')
                return redirect('index')
            else:
                messages.info(request, 'Удаление новости отменено.')

    return render(request, 'news_detail.html', {'news': news, 'can_delete': can_delete, 'confirm_delete': confirm_delete})


@login_required(login_url='login')
def create_post_view(request):
    """
    Отображает форму для создания новой записи.
    При отправке POST-запроса проверяет введенные данные, создает новую запись и перенаправляет на главную страницу.
    """
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            image_url = form.cleaned_data['image_url']
            full_text = form.cleaned_data['full_text']

            user_news = UserNews(user=request.user, title=title,
                                 image_url=image_url, full_text=full_text)
            user_news.save()

            return redirect('create_post')
    else:
        form = CreatePostForm()

    return render(request, 'create_post.html', {'form': form})


class ModerationForm(forms.Form):
    """
    Форма для модерации записей.
    Содержит поля: moderation_decision (выбор одного из вариантов: 'approve' - принять, 'reject' - отклонить) и comment (комментарий модератора).
    """
    moderation_decision = forms.ChoiceField(
        choices=[('approve', 'Принять'), ('reject', 'Отклонить')])
    comment = forms.CharField(widget=forms.Textarea, required=False)


@user_passes_test(lambda u: u.is_superuser)
def moder_post_view(request):
    """
    Обрабатывает модерацию записей.
    При отправке POST-запроса проверяет введенные данные и изменяет статус модерации записи.
    """
    if request.method == 'POST':
        form = ModerationForm(request.POST)
        if form.is_valid():
            user_news_id = request.POST.get('user_news_id')
            moderation_decision = form.cleaned_data['moderation_decision']
            comment = form.cleaned_data['comment']

            user_news = UserNews.objects.get(id=user_news_id)
            user_news.moderated = True

            if moderation_decision == 'approve':
                user_news.save()
                news = News.objects.create(
                    title=user_news.title,
                    image_url=user_news.image_url,
                    full_text=user_news.full_text
                )
                messages.success(
                    request, 'Пост успешно одобрен и опубликован.')
            elif moderation_decision == 'reject':
                if not comment:
                    messages.error(
                        request, 'Пожалуйста, укажите причину отказа.')
                    return redirect('moder_post')

                user_news.comment = comment
                user_news.save()
                messages.success(request, 'Пост отклонен.')

            return redirect('moder_post')
    else:
        user_news = UserNews.objects.filter(moderated=False)
        form = ModerationForm()
        return render(request, 'moder_post.html', {'user_news': user_news, 'form': form, 'notification': 'Появился новый пост на модерацию.'})


@login_required(login_url='login')
def profile_view(request):
    """
    Отображает профиль пользователя.
    При наличии прав администратора перенаправляет на страницу администратора.
    """
    if request.user.is_superuser:
        return redirect('profile_admin')
    return render(request, 'profile.html')


@login_required(login_url='login')
def profile_admin_view(request):
    """
    Отображает профиль администратора.
    Проверяет наличие новых записей на модерацию и передает соответствующее уведомление в шаблон 'profile_admin.html'.
    """
    user = request.user
    if not user.is_superuser:
        return redirect('profile')

    # Проверка наличия нового поста на модерацию
    user_news = UserNews.objects.filter(moderated=False).exists()
    notification = 'Появился новый пост на модерацию!' if user_news else None

    return render(request, 'profile_admin.html', {'notification': notification})


@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    """
    Отображает панель управления (для администратора).
    """
    return "View"


def binf_information_view(request):
    """
    Отображает страницу с информацией о БИНФ.
    """
    return render(request, 'binf_information.html')


def binf_client_view(request):
    """
    Отображает страницу с информацией о клиентах БИНФ.
    """
    return render(request, 'binf_client.html')


def binf_partnership_view(request):
    """
    Отображает страницу с информацией о партнерстве БИНФ.
    """
    return render(request, 'binf_partnership.html')


def binf_advertisement_view(request):
    """
    Отображает страницу с информацией о рекламе БИНФ.
    """
    return render(request, 'binf_advertisement.html')
