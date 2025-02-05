from django.contrib import admin
from .models import Pokemon

# Register your models here.

class PokemonAdmin (admin.ModelAdmin):
    readonly_fileds= ('creado', 'modificado')

admin.site.register(Pokemon,PokemonAdmin)