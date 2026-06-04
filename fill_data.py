import os
import django
from datetime import date

# Django sozlamalarini yuklash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# Biz yaratgan yangi modellarni chaqiramiz
from main.models import Muallif, Janr, Kitob, KitobNusxa, Ijara


print("Kutubxona ma'lumotlari bazaga qo'shilmoqda...")

# 1. Janrlarni yaratish
j1 = Janr.objects.create(nomi="Badiiy adabiyot")
j2 = Janr.objects.create(nomi="Ilmiy-ommabop")
j3 = Janr.objects.create(nomi="Dasturlash")
j4 = Janr.objects.create(nomi="Psixologiya")

# 2. Mualliflarni yaratish
m1 = Muallif.objects.create(ism="Abdulla Qodiriy", tugilgan_yili=1894, davlat="O'zbekiston")
m2 = Muallif.objects.create(ism="Guido van Rossum", tugilgan_yili=1956, davlat="Niderlandiya")
m3 = Muallif.objects.create(ism="Alisher Navoiy", tugilgan_yili=1441, davlat="O'zbekiston")

# 3. Kitoblarni yaratish
k1 = Kitob.objects.create(
    nomi="O'tkan kunlar",
    muallif=m1,
    til="uz",
    nashr_yili=1925,
    narx=45000.00,
    mavjud=True
)
k1.janrlar.add(j1)  # Ko'pga-ko'p (M2M) bog'liqlikni qo'shish

k2 = Kitob.objects.create(
    nomi="Python Programming",
    muallif=m2,
    til="en",
    nashr_yili=2020,
    narx=120000.00,
    mavjud=True
)
k2.janrlar.add(j3)

k3 = Kitob.objects.create(
    nomi="Xamsa",
    muallif=m3,
    til="uz",
    nashr_yili=1485,
    narx=95000.00,
    mavjud=True
)
k3.janrlar.add(j1, j2)

# 4. Kitob Nusxalarini yaratish (Inline uchun)
n1 = KitobNusxa.objects.create(kitob=k1, inventar_raqami="INV-001", holati="javonda")
n2 = KitobNusxa.objects.create(kitob=k1, inventar_raqami="INV-002", holati="berilgan")
n3 = KitobNusxa.objects.create(kitob=k2, inventar_raqami="INV-003", holati="javonda")
n4 = KitobNusxa.objects.create(kitob=k3, inventar_raqami="INV-004", holati="javonda")

# 5. Ijara ma'lumotlarini yaratish
Ijara.objects.create(
    nusxa=n2,
    oluvchi="Asilbek Olimov",
    olingan_sana=date.today(),
    qaytarilgan=False
)

Ijara.objects.create(
    nusxa=n1,
    oluvchi="Madina Rustamova",
    olingan_sana=date.today(),
    qaytarilgan=True
)

print("URRAO! Barcha kutubxona ma'lumotlari muvaffaqiyatli qo'shildi! Admin panelni tekshiring.")