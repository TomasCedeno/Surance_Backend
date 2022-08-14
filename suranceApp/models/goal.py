from django.db import models

#TODO: Importar la clase del modelo Usuario y agregar la relación entre Usuario y Meta

class Goal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    goalMoney = models.IntegerField()
    savedMoney = models.IntegerField(default=0)