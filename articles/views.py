from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class CategoryView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'



class ArticlesDetailView(View):
    def get(self, request, pk):
        articles = Articles.objects.filter(category=pk)
        context = {
            'articles': articles
        }

        return render(request, 'detail_view.html', context=context)


class ArticlesCreateView(CreateView):
    model = Articles
    template_name = 'create_view.html'
    fields = '__all__'
    success_url = reverse_lazy('articles:category_view')