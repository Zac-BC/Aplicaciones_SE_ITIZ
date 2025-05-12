from django.urls import path
from .views import BlogView, CategoryView

blog_urlspatther = ([
    path('',BlogView.as_view(),name='blog'),
    path('/categoria/<int:category_id>/',CategoryView, name='categoria')
], 'blog')