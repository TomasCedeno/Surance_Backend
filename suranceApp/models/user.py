from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField('UserName', max_length=30, unique=True)
    password = models.CharField('Password', max_length=256)
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email', max_length=200)
    balance = models.IntegerField('Saldo', default=0)

    def save(self, **kwargs):
        some_salt = 'mMuj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)