from django import forms

class KursArizaForm(forms.Form):
    YONALISHLAR = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('dizayn', 'Dizayn'),
    ]

    toliq_ism = forms.CharField(
        label="Ism va familiyangiz", 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}) # Bootstrap klassi
    )
    telefon = forms.CharField(
        label="Telefon raqamingiz",
        help_text="Format: +99890...",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+998'})
    )
    yosh = forms.IntegerField(
        label="Yoshingiz",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    yonalish = forms.ChoiceField(
        label="Yo'nalishni tanlang", 
        choices=YONALISHLAR,
        widget=forms.Select(attrs={'class': 'form-select'}) # Select uchun maxsus klass
    )
    # BooleanField (checkbox) uchun form-control shart emas, u o'zi chiroyli chiqadi
    tajriba_bor = forms.BooleanField(label="Dasturlash tajribangiz bormi?", required=False)
    
    qoshimcha = forms.CharField(
        label="Qo'shimcha izoh", 
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )