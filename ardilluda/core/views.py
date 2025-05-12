from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

from blessed import Terminal
term = Terminal()

class HomeView(TemplateView):
    template_name = "core/index.html"
    TAG:str = "HOME"

    def get(self, request,*kwargs):
        print(term.bold_white('======================================'))
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(term.bold_white('======================================'))

        return render(request, self.template_name, {})
    
class AboutView(TemplateView):
    template_name = "core/about.html"
    TAG:str = "ABOUT"

    def get(self, request,*kwargs):
        print(term.bold_white('======================================'))
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(term.bold_white('======================================'))

        return render(request, self.template_name, {})
    
class StoreView(TemplateView):
    template_name = "core/store.html"
    TAG:str = "STORE"

    def get(self, request,*kwargs):
        print(term.bold_white('======================================'))
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(term.bold_white('======================================'))

        return render(request, self.template_name, {})

class ContactoView(TemplateView):
    template_name = "core/contact.html"
    TAG:str = "BLOG"

    def get(self, request,*kwargs):
        print(term.bold_white('======================================'))
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(term.bold_white('======================================'))

        return render(request, self.template_name, {})

class ServiceView(TemplateView):
    template_name = "core/services.html"
    TAG:str = "SERVICE"

    def get(self, request,*kwargs):
        print(term.bold_white('======================================'))
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(f'{term.bold_mediumseagreen(self.TAG)}')
        print(term.bold_white('======================================'))

        return render(request, self.template_name, {})