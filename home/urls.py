from django.urls import path
from .views import home_page, home_page_2


app_name = 'home'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('home_page_2/', home_page_2, name='home_page_2')
]