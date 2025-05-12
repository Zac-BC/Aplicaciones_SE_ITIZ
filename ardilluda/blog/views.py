from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from blessed import Terminal
from .models import Entrada, Categoria

from blessed import Terminal
term = Terminal()

class BlogView(TemplateView):
    template_name = "blog/blog.html"
    TAG:str = "BLOG"

    def get(self, request,*kwargs):
        print(term.bold_white('======================================'))
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(term.bold_white('======================================'))

        entradas = Entrada.objects.all()

        return render(request, self.template_name, {'entradas':entradas})
    

def CategoryView(request, category_id, ):
        TAG:str = "CATEGORIA"

        print(term.bold_white('======================================'))
        print(f'{term.bold_mediumseagreen(TAG)}')
        print(term.bold_white('======================================'))

        entradas = Entrada.objects.all()

        categoria = get_object_or_404(Categoria, id=category_id)

        return render(request, "blog/category.html", {'categoria':categoria})
    
    