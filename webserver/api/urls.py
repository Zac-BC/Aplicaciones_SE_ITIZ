from django.urls import path
from .views import PokemonAPIView

app_name = 'api'
urlspattern_api = [
    path('acciones/', PokemonAPIView.as_view(), name='listar')
]