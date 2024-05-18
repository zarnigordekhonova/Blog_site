from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home_page(request):
    return render(request, 'home_page.html')

def home_page_2(request):
    return render(request, 'home_page_2.html')