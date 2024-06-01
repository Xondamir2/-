from django.db import models

# Create your models here.



class Hudud(models.Model):
    name = models.CharField(max_length=255)



class QurilishTashkiloti(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    hudud = models.CharField(max_length=55)



class QuriishBinosi(models.Model):
    qurilish = models.ForeignKey(QurilishTashkiloti, on_delete=models.CASCADE)
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    maydoni = models.CharField(max_length=255)
    qavat = models.IntegerField()
    parkovka = models.BooleanField(default=True)
    bolalar_maydonchasi = models.BooleanField(default=True)
    lift = models.BooleanField(default=True)

