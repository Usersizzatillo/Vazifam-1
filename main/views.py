from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Talaba
# 1. Talabalar ro'yxati (ListView)
class TalabaList(ListView):
    model = Talaba
    template_name = 'royxat.html'
    context_object_name = 'talabalar'  # <-- Shu yerini 'talabalar' deb to'g'rilang

# 2. Yangi talaba qo'shish (CreateView)
class TalabaCreate(CreateView):
    model = Talaba
    fields = ['ism', 'familiya', 'guruh', 'yosh', 'faol']
    template_name = 'maqola_form.html'
    success_url = reverse_lazy('royxat')

# 3. Talaba ma'lumotlarini tahrirlash (UpdateView)
class TalabaUpdate(UpdateView):
    model = Talaba
    fields = ['ism', 'familiya', 'guruh', 'yosh', 'faol']
    template_name = 'maqola_form.html'
    success_url = reverse_lazy('royxat')

# 4. Talabani o'chirish (DeleteView)
class TalabaDelete(DeleteView):
    model = Talaba
    template_name = 'maqola_confirm_delete.html'
    success_url = reverse_lazy('royxat')