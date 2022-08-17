from django.db import models
from .user import User

class Goal(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.IntegerField()
    name = models.TextField()
    description = models.TextField()
    goalMoney = models.IntegerField()
    savedMoney = models.IntegerField(default=0)

    @property
    def isCompleted(self):
        return self.savedMoney == self.goalMoney