from django.db import models

class Muallif(models.Model):
    ism = models.CharField(max_length=120)
    tugilgan_yili = models.IntegerField()
    davlat = models.CharField(max_length=60)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"


class Janr(models.Model):
    nomi = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = "Janr"
        verbose_name_plural = "Janrlar"


class Kitob(models.Model):
    TIL_CHOICES = [
        ('uz', "O'zbek"),
        ('ru', "Rus"),
        ('en', "Ingliz"),
    ]
    nomi = models.CharField(max_length=200)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    janrlar = models.ManyToManyField(Janr)
    til = models.CharField(max_length=2, choices=TIL_CHOICES, default='uz')
    nashr_yili = models.IntegerField()
    narx = models.DecimalField(max_digits=9, decimal_places=2)
    mavjud = models.BooleanField(default=True)
    qoshilgan_sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"


class KitobNusxa(models.Model):
    HOLAT_CHOICES = [
        ('javonda', 'Javonda'),
        ('berilgan', 'Berilgan'),
        ('yoʻqolgan', 'Yoʻqolgan'),
    ]
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    inventar_raqami = models.CharField(max_length=50)
    holati = models.CharField(max_length=15, choices=HOLAT_CHOICES, default='javonda')

    def __str__(self):
        return f"{self.kitob.nomi} - {self.inventar_raqami}"

    class Meta:
        verbose_name = "Kitob Nusxasi"
        verbose_name_plural = "Kitob Nusxalari"


class Ijara(models.Model):
    nusxa = models.ForeignKey(KitobNusxa, on_delete=models.CASCADE)
    oluvchi = models.CharField(max_length=120)
    olingan_sana = models.DateField()
    qaytarilgan = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.oluvchi} -> {self.nusxa.inventar_raqami}"

    class Meta:
        verbose_name = "Ijara"
        verbose_name_plural = "Ijaralar"