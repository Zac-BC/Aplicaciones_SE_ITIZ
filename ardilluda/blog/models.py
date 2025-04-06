from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=100, verbose_name= "Nombre")
    created = models.DateTimeField(auto_now_add= True, verbose_name= "Fecha creacion")
    updated = models.DateTimeField(auto_now= True, verbose_name= "Fecha de actualizacin")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name
    
class Entrada(models.Model):
    title= models.CharField(max_length=200, verbose_name= "Titulo")
    content = models.TextField(verbose_name= "Contenido")
    published = models.DateTimeField(verbose_name= "Fecha de publicacion")
    image = models.ImageField(upload_to= "blog", verbose_name= "Imagen", null= True, blank= True)
    author = models.ForeignKey(User,verbose_name="Usuario",on_delete=models.CASCADE)                     #"auth.User", on_delete= models.CASCADE, verbose_name= "Autor") #models.CharField(max_length=100, verbose_name= "Autor")
    cathegories = models.ManyToManyField(Categoria, verbose_name= "Categoria",related_name="get_post")
    created = models.DateTimeField(auto_now_add= True, verbose_name= "Fecha creacion")
    updated = models.DateTimeField(auto_now= True, verbose_name= "Fecha de actualizacin")