from django.contrib import admin
from .models import Talaba

@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ('ism', 'familiya', 'guruh', 'yosh', 'faol')