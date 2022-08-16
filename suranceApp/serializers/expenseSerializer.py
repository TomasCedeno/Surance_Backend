from suranceApp.models import Expense
from rest_framework import serializers

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ['id', 'value', 'date', 'category', 'description']
        read_only_fields = ['id']