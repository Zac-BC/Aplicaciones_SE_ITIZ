from django.urls import path
from .views import BlogView 

blog_urlspatther = ([
    path('',BlogView.as_view(),name='blog'),
], 'blog')