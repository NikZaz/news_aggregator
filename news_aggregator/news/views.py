from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.db.models import Q
from .models import News
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django import forms

class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=200)
    image_url = forms.URLField(required=False)
    full_text = forms.CharField(widget=forms.Textarea)

def index_view(request):
    news = News.objects.order_by('-published_date')
    return render(request, 'index.html', {'news': news})

def registration_view(request):
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST and 'email' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']

            if User.objects.filter(Q(username=username) | Q(email=email)).exists():
                messages.error(request, 'Пользователь с таким именем или email уже существует.')
                return redirect('registration')

            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Не все поля формы были заполнены.')
            return redirect('registration')

    return render(request, 'registration.html')


def login_view(request):
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
    logout(request)
    return redirect('index')


def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news_detail.html', {'news': news})

@login_required(login_url='login')
def create_post_view(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            image_url = form.cleaned_data['image_url']
            full_text = form.cleaned_data['full_text']

            news = News.objects.create(title=title, image_url=image_url, full_text=full_text)

            return redirect('index')
    else:
        form = CreatePostForm()

    return render(request, 'create_post.html', {'form': form})

def edit_post_view(request):
    return render(request, 'edit_post.html')

def moder_post_view(request):
    return render(request, 'moder_post.html')

def notice_view(request):
    return render(request, 'notice.html')

def my_posts_view(request):
    return render(request, 'my_posts.html')

@login_required(login_url='login')
def profile_view(request):
    if request.user.is_superuser:
        return redirect('profile_admin')
    return render(request, 'profile.html')

@login_required(login_url='login')
def profile_admin_view(request):
    user = request.user
    if not user.is_superuser:
        return redirect('profile')
    return render(request, 'profile_admin.html')

@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    return "View"

