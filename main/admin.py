from django.contrib import admin
from .models import Muallif, Janr, Kitob, KitobNusxa, Ijara

# Admin panel sarlavhalarini o'zbekcha qilish
admin.site.site_header = "Onlayn Kutubxona Admin Paneli"
admin.site.site_title = "Kutubxona Admin"
admin.site.index_title = "Tizimni Boshqarish"

# Sodda register
admin.site.register(Janr)


# KitobNusxa uchun TabularInline sozlamasi
class KitobNusxaInline(admin.TabularInline):
    model = KitobNusxa
    extra = 1  
    verbose_name = "Kitob Nusxasi"
    verbose_name_plural = "Kitob Nusxalari"


# Custom admin actions (Xatolik keltirib chiqargan % belgisi olib tashlandi)
@admin.action(description="Tanlanganlarni 'Mavjud' deb belgilash")
def mavjud_qilish(modeladmin, request, queryset):
    soni = queryset.update(mavjud=True)
    modeladmin.message_user(request, f"{soni} ta kitob holati 'Mavjud' qilib yangilandi.")

@admin.action(description="Narxni 10 foiz tushirish (Chegirma)")
def chegirma_10_foiz(modeladmin, request, queryset):
    for kitob in queryset:
        kitob.narx = kitob.narx * 0.9
        kitob.save()
    modeladmin.message_user(request, "Tanlangan kitoblar narxi 10 foizga pasaytirildi.")


# Mualliflar uchun admin sozlamasi
@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ('ism', 'tugilgan_yili', 'davlat')
    search_fields = ('ism',)  


# Kitoblar uchun asosiy mukammal admin sozlamasi
@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'muallif', 'nashr_yili', 'narx', 'mavjud', 'nusxalar_soni')
    list_filter = ('mavjud', 'til', 'janrlar', 'nashr_yili')
    search_fields = ('nomi', 'muallif__ism')  
    ordering = ('-nashr_yili',)
    readonly_fields = ('qoshilgan_sana',)
    
    fieldsets = (
        ("Asosiy malumotlar", {
            'fields': ('nomi', 'muallif', 'janrlar')
        }),
        ("Qoshimcha sozlamalar", {
            'fields': ('til', 'nashr_yili', 'narx', 'mavjud', 'qoshilgan_sana'),
            'classes': ('collapse',),  
        }),
    )
    
    inlines = [KitobNusxaInline]
    actions = [mavjud_qilish, chegirma_10_foiz]
    
    # BONUS TOPSHIRIQLAR
    list_editable = ('narx', 'mavjud')       
    list_per_page = 20                        
    date_hierarchy = 'qoshilgan_sana'         
    autocomplete_fields = ['muallif']         
    
    def nusxalar_soni(self, obj):
        return obj.kitobnusxa_set.count()
    nusxalar_soni.short_description = "Nusxalar Soni"  


# Ijaralar uchun admin sozlamasi
@admin.register(Ijara)
class IjaraAdmin(admin.ModelAdmin):
    list_display = ('oluvchi', 'nusxa', 'olingan_sana', 'qaytarilgan')
    list_filter = ('qaytarilgan',)