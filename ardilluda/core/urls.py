from django.urls import path
from .views import HomeView

main_urlspatther = ([
    path('',HomeView.as_view(),name='home')
], 'main')