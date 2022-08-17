from rest_framework import status, views
from rest_framework.response import Response
from django.db import models
from django.db.models import Sum, Func

from suranceApp.models import Income, User
from suranceApp.serializers import IncomeSerializer, UserSerializer
from django.shortcuts import get_object_or_404


class IncomeAPIView(views.APIView):

    serializer_class = IncomeSerializer

    def get(self, request, *args, **kwargs):
        incomes = Income.objects.filter(user=self.kwargs.get('pk')).order_by('id')
        serializer = self.serializer_class(incomes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Crea Ingreso"""

        user = get_object_or_404(User, id=request.data['user'])
        balance = user.balance + request.data['value']
        userSerializer = UserSerializer(user, data={'balance':balance}, partial=True)
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    
    def delete(self, request):

        user = get_object_or_404(User, id=request.data['user'])
        income = get_object_or_404(Income, id=request.data['id'])

        balance = user.balance - income.value
        userSerializer = UserSerializer(user, data={'balance':balance}, partial=True)
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()
        
        income.delete()
        return Response({'message': 'Income Deleted'}, status=status.HTTP_204_NO_CONTENT)



class ExtractMonth(Func):
    """Extrae el mes de una fecha"""
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()

class ExtractYear(Func):
    """Extrae el año de una fecha"""
    function = 'EXTRACT'
    template = '%(function)s(YEAR from %(expressions)s)'
    output_field = models.IntegerField()


class MonthlyIncomeView(views.APIView):
    serializer_class = IncomeSerializer

    def get(self, request, *args, **kwargs):
        """Retorna el total de ingresos por cada mes"""
        incomesByMonth = ( Income.objects.filter(user=self.kwargs.get('pk'))
            .annotate(month=ExtractMonth('date'), year=ExtractYear('date'))
            .values('month', 'year')
            .annotate(total=Sum('value'))
            .order_by('-year', '-month')
        )
        return Response(incomesByMonth, status=status.HTTP_200_OK)

 