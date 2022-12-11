from django.contrib import admin
from .models import Piloto

class PilotoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Piloto, PilotoAdmin)
