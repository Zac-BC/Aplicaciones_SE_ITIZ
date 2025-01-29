from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

class PokemonAPIView (APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):

        contenido = {
            'Resultado':"Comunicacion exitosa",
            'Pasas': "Las pasas son deliciosas"
        }
        return Response(contenido)

    def post(self, request, format=None):

        contenido = {
            'Resultado':"Comunicacion exitosa",
            'Pasas': "Las pasas son deliciosas"
        }
        return Response(contenido)