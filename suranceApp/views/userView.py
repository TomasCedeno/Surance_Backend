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


class LoginAPIView(views.APIView):

    def post(self, request):
        """Recibe userName y password y si es correcto devuelve el id del usuario correspondiente"""
        try:
            userName = request.data['userName']
            some_salt = 'mMuj0DrIK6vgtdIYepkIxN'
            password = make_password(request.data['password'], some_salt)

            user = get_object_or_404(User, userName=userName)
            
            if (password == user.password):
                return Response({'userId': user.id}, status=status.HTTP_200_OK)

            else:
                return Response({'message': 'Incorrect Password'}, status=status.HTTP_403_FORBIDDEN)

        except KeyError:
            return Response({'message': 'Missing some param'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except:
            return Response({'message':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)