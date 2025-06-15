from django.contrib import admin
from .models import Reparto

@admin.register(Reparto)
class RepartoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    filter_horizontal = ('managers',)
