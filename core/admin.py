from django.contrib import admin
from .models import Chassi, Carro, Montadora

@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero',)


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora', 'modelo', 'chassi', 'preco', 'get_motorista')

    def get_motorista(self, obj):
        return ', '.join(m.username for m in obj.motorista.all()[0:3])

    get_motorista.short_description = 'Motoristas'

