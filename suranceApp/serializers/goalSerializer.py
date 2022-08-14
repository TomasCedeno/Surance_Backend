from suranceApp.models.goal import Goal
from rest_framework import serializers

class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = ['id', 'name', 'description', 'goalMoney', 'savedMoney', 'isCompleted']
        read_only_fields = ['id', 'isCompleted']