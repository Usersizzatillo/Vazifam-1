from django.shortcuts import render, redirect
from django.contrib import messages  # Bonus topshiriq uchun
from .forms import KursArizaForm
from .models import KursAriza

def ariza_view(request):
    if request.method == 'POST':
        # Agar foydalanuvchi tugmani bosgan bo'lsa, kelgan ma'lumotlar formaga yuklanadi
        form = KursArizaForm(request.POST)
        
        # Formadagi barcha qoidalar (clean metodlari) tekshiriladi
        if form.is_valid():
            # Ma'lumotlar tozalangan va xavfsiz holatda cleaned_data'ga o'tadi
            data = form.cleaned_data
            
            # KursAriza modeliga ma'lumotlarni qo'lda saqlaymiz
            KursAriza.objects.create(
                toliq_ism=data['toliq_ism'],
                telefon=data['telefon'],
                yosh=data['yosh'],
                yonalish=data['yonalish'],
                tajriba_bor=data['tajriba_bor'],
                qoshimcha=data['qoshimcha']
            )
            
            # Bonus topshiriq: Muvaffaqiyat xabari
            messages.success(request, "Arizangiz muvaffaqiyatli qabul qilindi!")
            
            # PRG (Post/Redirect/Get) patterni: sahifani qayta yuklaganda ma'lumot takroran ketmasligi uchun redirect qilinadi
            return redirect('ariza_url_nomi') 
    else:
        # Agar foydalanuvchi sahifaga shunchaki kirgan bo'lsa (GET so'rovi), bo'sh forma ko'rsatamiz
        form = KursArizaForm()
        
    return render(request, 'ariza.html', {'form': form})