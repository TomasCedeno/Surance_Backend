from django.contrib import admin

from .models.goal import Goal
from .models.income import Income
from .models.expense import Expense
# Register your models here.
admin.site.register(Goal)
admin.site.register(Income)
admin.site.register(Expense)