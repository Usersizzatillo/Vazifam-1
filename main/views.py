from django.shortcuts import render, redirect, get_object_or_404
from .models import Mahsulot
from .forms import MahsulotForm

def royxat_view(request):
    mahsulotlar = Mahsulot.objects.all().order_by('-id')
    return render(request, 'royxat.html', {'mahsulotlar': mahsulotlar})

def qoshish_view(request):
    if request.method == 'POST':
        form = MahsulotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('royxat')
    else:
        form = MahsulotForm()
    return render(request, 'forma.html', {'form': form, 'sarlavha': "Yangi mahsulot qo'shish"})

def tahrirlash_view(request, pk):
    mahsulot = get_object_or_404(Mahsulot, pk=pk)
    if request.method == 'POST':
        form = MahsulotForm(request.POST, instance=mahsulot)
        if form.is_valid():
            form.save()
            return redirect('royxat')
    else:
        form = MahsulotForm(instance=mahsulot)
    return render(request, 'forma.html', {'form': form, 'sarlavha': "Mahsulotni tahrirlash"})

def ochirish_view(request, pk):
    mahsulot = get_object_or_404(Mahsulot, pk=pk)
    if request.method == 'POST':
        mahsulot.delete()
        return redirect('royxat')
    return render(request, 'ochirish_tasdiq.html', {'mahsulot': mahsulot})