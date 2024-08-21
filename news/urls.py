from django.urls import path
from .views import *


urlpatterns = [
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/full/', NewsListViewFull.as_view(), name='news_list_full'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    
    # Real delete
    path('news/delete/<int:pk>/', DeleteNewsAPI.as_view(), name='delete_news'),
    path('category/delete/<int:pk>/', DeleteCategoryAPI.as_view(), name='delete_category'),
]