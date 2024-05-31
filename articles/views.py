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



class ArticlesListView(View):
    def get(self, request, pk):
        articles = Articles.objects.filter(category=pk)
        context = {
            'articles': articles
        }

        return render(request, 'aricle_list_view.html', context=context)


class ArticlesCreateView(CreateView):
    model = Articles
    template_name = 'create_view.html'
    fields = '__all__'
    success_url = reverse_lazy('articles:category_view')


class ArticleDetailView(View):
    def get(self, request, pk):
        article = Articles.objects.get(pk=pk)
        return render(request, 'detail.html', {'article': article})