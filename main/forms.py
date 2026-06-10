from django import forms
from .models import Mahsulot

class MahsulotForm(forms.ModelForm):
    class Meta:
        model = Mahsulot
        fields = ['nomi', 'narx', 'kategoriya', 'soni', 'faol', 'tavsif']
        widgets = {
            'nomi': forms.TextInput(attrs={'class': 'form-control'}),
            'narx': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'kategoriya': forms.Select(attrs={'class': 'form-select'}),
            'soni': forms.NumberInput(attrs={'class': 'form-control'}),
            'faol': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tavsif': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_narx(self):
        narx = self.cleaned_data.get('narx')
        if narx is not None and narx <= 0:
            raise forms.ValidationError("Mahsulot narxi 0 dan katta bo'lishi kerak!")
        return narx

    def clean(self):
        cleaned_data = super().clean()
        faol = cleaned_data.get('faol')
        soni = cleaned_data.get('soni')

        if faol is True and (soni is None or soni == 0):
            raise forms.ValidationError("Sotuvdagi mahsulotning soni omborda 0 bo'lishi mumkin emas!")
        return cleaned_data
    