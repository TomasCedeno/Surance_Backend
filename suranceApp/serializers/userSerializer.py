from suranceApp.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'userName', 'password', 'name', 'email', 'balance']
        read_only_fields = ['id', 'balance']