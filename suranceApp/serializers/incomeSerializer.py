from asyncore import read
from suranceApp.models import Income, User
from rest_framework import serializers
from suranceApp.serializers import UserSerializer

class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = ['id', 'user', 'value', 'date', 'category', 'description']
        read_only_fields = ['id']