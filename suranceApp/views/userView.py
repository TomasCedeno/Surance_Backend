from rest_framework import status, views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

from suranceApp.serializers.userSerializer import UserSerializer
from suranceApp.models import User

class UserAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        details = get_object_or_404(User, id=self.kwargs.get('pk'))
        serializer = UserSerializer(details)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

