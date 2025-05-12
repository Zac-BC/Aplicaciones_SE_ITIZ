from django.urls import path
from .views import HomeView, AboutView, StoreView, ContactoView, ServiceView

main_urlspatther = ([
    path('',HomeView.as_view(),name='home'),
    path('acerca/',AboutView.as_view(),name='about'),
    path('tienda/',StoreView.as_view(),name='store'),
    path('contacto/',ContactoView.as_view(),name='contacto'),
    path('servicios/',ServiceView.as_view(),name='servicios'),
], 'main')