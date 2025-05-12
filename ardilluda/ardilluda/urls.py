"""
URL configuration for ardilluda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.urls import main_urlspatther
from core.urls import path
from blog.urls import blog_urlspatther
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include(main_urlspatther)),
    path('blog',include(blog_urlspatther)),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
