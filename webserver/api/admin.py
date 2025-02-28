from django.contrib import admin
from .models import Pokemon, Sensor
# Register your models here.

class PokemonAdmin (admin.ModelAdmin):
    readonly_fields= ('creado', 'modificado')

admin.site.register(Pokemon, PokemonAdmin)

class SensorAdmin (admin.ModelAdmin):
    readonly_fields= ('creado', 'modificado')

    list_display =('id', 'temperatura', 'humedad')
    ordering = ('-id',)

admin.site.register(Sensor, SensorAdmin)




    