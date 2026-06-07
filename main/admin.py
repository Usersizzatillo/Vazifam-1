from django.contrib import admin
from .models import Mahsulot

@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi', 'narx', 'kategoriya', 'soni', 'faol', 'qoshilgan_sana')