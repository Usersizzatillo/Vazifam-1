from django.views.generic import ListView, DetailView, TemplateView, RedirectView
from .models import Maqola


class MaqolaList(ListView):
    model = Maqola
    template_name = 'royxat.html'
    context_object_name = 'maqolalar'

    def get_queryset(self):
        return Maqola.objects.filter(
            chop_etilgan=True
        ).order_by('-sana')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jami'] = Maqola.objects.count()
        context['sarlavha'] = 'Barcha maqolalar roʻyxati'
        return context


class MaqolaDetail(DetailView):
    model = Maqola
    template_name = 'detail.html'
    context_object_name = 'maqola'


class BizHaqimizda(TemplateView):
    template_name = 'about.html'


class EskiBlog(RedirectView):
    pattern_name = 'royxat'