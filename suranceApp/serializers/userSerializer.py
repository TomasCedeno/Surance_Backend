from suranceApp.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'userName', 'password', 'name', 'email', 'balance']
        read_only_fields = ['balance']

    def create(self, validated_data):
        if('id' in validated_data):
            validated_data.pop('id')
        userInstance = User.objects.create(**validated_data)

        return userInstance