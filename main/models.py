from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    guruh = models.CharField(max_length=50)
    yosh = models.PositiveIntegerField()
    faol = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ism} {self.familiya}"