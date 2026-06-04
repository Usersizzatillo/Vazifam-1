import os
import django
import sys
import random

# Loyiha yo'lini ko'rsatish
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from main.models import Branch, Student, Subject, Teacher, Room, Group

print("Eski ma'lumotlar tozalanmoqda...")

# Dublikat bo'lmasligi uchun hamma narsani tozalaymiz
Student.objects.all().delete()
Group.objects.all().delete()
Room.objects.all().delete()
Teacher.objects.all().delete()
Subject.objects.all().delete()
Branch.objects.all().delete()

# 1. Filiallar yaratish
b1 = Branch.objects.create(name="Toshkent Filiali")
b2 = Branch.objects.create(name="Farg'ona Filiali")
branches = [b1, b2]

# 2. Fanlar yaratish
s1 = Subject.objects.create(name="Python Dasturlash", description="Python asoslari va Django")
s2 = Subject.objects.create(name="Frontend", description="HTML, CSS, JavaScript va React")
s3 = Subject.objects.create(name="Backend", description="Node.js va ma'lumotlar bazasi")
s4 = Subject.objects.create(name="Matematika", description="Oliy matematika va mantiq")
s5 = Subject.objects.create(name="Ingliz tili", description="IELTS va Speaking")

# 3. 10 ta guruh yaratish
groups_pool = [
    Group.objects.create(name="Python-01 (Ertalabki)", subject=s1),
    Group.objects.create(name="Python-02 (Kechki)", subject=s1),
    Group.objects.create(name="Frontend-01 (Juft kunlar)", subject=s2),
    Group.objects.create(name="Frontend-02 (Toq kunlar)", subject=s2),
    Group.objects.create(name="Backend-01", subject=s3),
    Group.objects.create(name="Math-Elementary", subject=s4),
    Group.objects.create(name="Math-Advanced", subject=s4),
    Group.objects.create(name="English-Grammar", subject=s5),
    Group.objects.create(name="English-IELTS 7+", subject=s5),
    Group.objects.create(name="English-Kids", subject=s5),
]

# 4. 15 ta O'qituvchilarni avtomatik yaratish 🚀
print("15 ta tajribali o'qituvchi bazaga qo'shilmoqda...")
oat_ism = ["Anvar", "Zilola", "Bobur", "Nodira", "Jasur", "Malika", "Sardor", "Gulnoza", "Farruh", "Shaxnoza", "Dilshod", "Laylo", "Olim", "Eldor", "Kamola"]
oat_familiya = ["Aliyev", "Karimova", "Soliyeff", "Umarova", "Toshpulatov", "Aslanova", "Hikmatov", "X Khalilova", "Rustamov", "Ismoilova", "Jo'rayev", "Ahmedova", "G'ofurov", "Sultonov", "Abduvaliyeva"]

for i in range(15):
    Teacher.objects.create(
        first_name=oat_ism[i],
        last_name=oat_familiya[i],
        phone=f"+99893{random.randint(1000000, 9999999)}",
        email=f"{oat_ism[i].lower()}{i}@gmail.com",
        salary=random.randint(4000000, 9000000), # 4 mln dan 9 mln gacha maosh
        branch=random.choice(branches) # Tasodifiy filial
    )

# 5. 350 ta O'quvchilarni avtomatik yaratish
print("350 ta o'quvchi guruhlarga taqsimlanmoqda...")
viloyatlar = ["Toshkent", "Farg'ona", "Andijon", "Namangan", "Samarqand", "Buxoro", "Xorazm", "Navoiy", "Qashqadaryo"]

students_list = []
for i in range(1, 351):
    random_group = random.choice(groups_pool)
    random_viloyat = random.choice(viloyatlar)
    random_phone = f"+99891{random.randint(1000000, 9999999)}"
    
    students_list.append(
        Student(
            name=f"O'quvchi #{i}",
            address=f"{random_viloyat} viloyati",
            phone=random_phone,
            group=random_group
        )
    )

Student.objects.bulk_create(students_list)

print("\n🔥 DAXSHAT! Baza to'liq shakllantirildi!")
print(f"✅ Jami O'qituvchilar: {Teacher.objects.count()} ta")
print(f"✅ Jami Guruhlar: {Group.objects.count()} ta")
print(f"✅ Jami O'quvchilar: {Student.objects.count()} ta guruhlarga bo'lindi!")