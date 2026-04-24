from django.urls import path
from . import views

app_name = 'articleApp'

urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:id>/', views.article_detail, name='article_detail'),
    path('articles/<int:article_id>/share/', views.article_share, name='article_share'),
]