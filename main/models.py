from django.db import models

class KursAriza(models.Model):
    # ... (eski maydonlar o'zgarishsiz qoladi) ...
    YONALISHLAR = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('dizayn', 'Dizayn'),
    ]

    toliq_ism = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    yosh = models.PositiveIntegerField()
    yonalish = models.CharField(max_length=20, choices=YONALISHLAR)
    tajriba_bor = models.BooleanField(default=False)
    qoshimcha = models.TextField(blank=True)
    yuborilgan_sana = models.DateTimeField(auto_now_add=True)

    # 🔹 Mana shu qismni qo'shasiz:
    class Meta:
        verbose_name = "Kurs arizasi"
        verbose_name_plural = "Kurs arizalari"

    def __str__(self):
        return self.toliq_ism