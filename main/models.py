from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    muallif = models.CharField(max_length=100)
    matn = models.TextField()
    korishlar = models.PositiveIntegerField(default=0)
    chop_etilgan = models.BooleanField(default=False)
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sarlavha