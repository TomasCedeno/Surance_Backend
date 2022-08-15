from django.db import models

#TODO: Importar la clase del modelo Usuario y agregar la relación entre Usuario e Income

class Income(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.IntegerField()
    date = models.DateField()
    category = models.TextField()
    description = models.TextField()