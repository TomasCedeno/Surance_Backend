from suranceApp.models import Income
from rest_framework import serializers

class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = ['id', 'value', 'date', 'category', 'description']
        read_only_fields = ['id']