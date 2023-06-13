"""
URL configuration for news_aggregator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name="home"),
    path('home/', views.index_view, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', views.registration_view, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile_admin/', views.profile_admin_view, name='profile_admin'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('create_post/', views.create_post_view, name='create_post'),
    path('moder_post/', views.moder_post_view, name='moder_post'),
    path('binf_information/', views.binf_information_view, name='binf_information'),
    path('binf_client/', views.binf_client_view, name='binf_client'),
    path('binf_partnership/', views.binf_partnership_view, name='binf_partnership'),
    path('binf_advertisement/', views.binf_advertisement_view, name='binf_advertisement'),
]