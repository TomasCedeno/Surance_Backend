from django.contrib import admin

from .models import User, Income, Expense, Goal

# Register your models here.
admin.site.register(User)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Goal)