from django.urls import path
from .views import *


urlpatterns = [
    path('news/', NewsListView.as_view(), name='news_list'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]