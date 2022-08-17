from django.db import models
from .user import User

class Income(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.IntegerField()
    value = models.IntegerField()
    date = models.DateField()
    category = models.TextField()
    description = models.TextField()