import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from .models import Article

def index_view(request):
    return render(request, 'index.html')