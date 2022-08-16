from django.contrib import admin

from .models.goal import Goal
from .models.user import User

# Register your models here.
admin.site.register(Goal)
admin.site.register(User)