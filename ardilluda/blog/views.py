from django.shortcuts import render
from django.views.generic.base import TemplateView
from blessed import Terminal
from .models import Entrada

term = Terminal()

class BlogView(TemplateView):
    template_name = "blog/blog.html"
    TAG:str = "BLOG"

    def get(self, request,args,*kwargs):
        print(term.bold_white('======================================'))
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(term.bold_white('======================================'))
        
        entradas = Entrada.objects.all()
        print(entradas)

        return render(request, self.template_name, {'entradas':entradas})