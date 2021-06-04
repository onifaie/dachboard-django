from django.db import models

# Create your models here.
class cotogery(models.Model):
    categourey=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.categourey

class mychart(models.Model):
    cuentryname=models.CharField(max_length=200)
    counterypepol=models.IntegerField()
    counterycity=models.IntegerField()
    counteryseles=models.IntegerField()

    def  __str__(self) -> str:
        return self.cuentryname

        