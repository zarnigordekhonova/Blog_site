from django.urls import path
from .views import CategoryView, ArticlesListView, ArticlesCreateView, ArticleDetailView

app_name = 'articles'
urlpatterns = [
    path('category', CategoryView.as_view(), name='category_view'),
    path('list/<int:pk>', ArticlesListView.as_view(), name='detail_view'),
    path('art/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('create', ArticlesCreateView.as_view(), name='create_view'),
]
