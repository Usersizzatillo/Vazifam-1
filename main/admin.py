from django.contrib import admin
from .models import Maqola

@admin.register(Maqola)
class MaqolaAdmin(admin.ModelAdmin):
    # Admin panel ro'yxatida ko'rinadigan ustunlar
    list_display = ('id', 'sarlavha', 'muallif', 'chop_etilgan', 'korishlar', 'sana')
    
    # Ro'yxatda qaysi ustunlar orqali batafsil sahifaga kirish mumkinligi
    list_display_links = ('id', 'sarlavha')
    
    # Admin panelning o'zida tezkor tahrirlash imkoniyati
    list_editable = ('chop_etilgan',)
    
    # O'ng tomonda turadigan filtrlar bloki
    list_filter = ('chop_etilgan', 'sana', 'muallif')
    
    # Sarlavha va matn bo'yicha qidiruv tizimi
    search_fields = ('sarlavha', 'matn', 'muallif')
    
    # Sanaga qarab ierarxik navigatsiya (filtr)
    date_hierarchy = 'sana'