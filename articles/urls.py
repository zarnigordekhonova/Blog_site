from django.urls import path
from .views import CategoryView, ArticlesDetailView, ArticlesCreateView

app_name = 'articles'
urlpatterns = [
    path('category', CategoryView.as_view(), name='category_view'),
    path('articles/<int:pk>', ArticlesDetailView.as_view(), name='detail_view'),
    path('create', ArticlesCreateView.as_view(), name='create_view'),
]
