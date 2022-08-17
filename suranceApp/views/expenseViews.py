from rest_framework import status, views
from rest_framework.response import Response
from django.db import models
from django.db.models import Sum, Func
from django.shortcuts import get_object_or_404

from suranceApp.models.expense import Expense, User
from suranceApp.serializers import ExpenseSerializer, UserSerializer


class ExpenseAPIView(views.APIView):

    serializer_class = ExpenseSerializer

    def get(self, request, *args, **kwargs):
        expenses = Expense.objects.filter(user=self.kwargs.get('pk')).order_by('id')
        serializer = self.serializer_class(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Crea Egreso"""

        user = get_object_or_404(User, id=request.data['user'])
        balance = user.balance - request.data['value']
        userSerializer = UserSerializer(user, data={'balance':balance}, partial=True)
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def delete(self, request):

        user = get_object_or_404(User, id=request.data['user'])
        expense = get_object_or_404(Expense, id=request.data['id'])

        balance = user.balance + expense.value
        userSerializer = UserSerializer(user, data={'balance':balance}, partial=True)
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()
        
        expense.delete()
        return Response({'message': 'Expense Deleted'}, status=status.HTTP_204_NO_CONTENT)


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


class MonthlyExpenseView(views.APIView):
    serializer_class = ExpenseSerializer

    def get(self, request, *args, **kwargs):
        """Retorna el total de ingresos por cada mes"""
        expensesByMonth = (Expense.objects.filter(user=self.kwargs.get('pk'))
            .annotate(month=ExtractMonth('date'), year=ExtractYear('date'))
            .values('month', 'year')
            .annotate(total=Sum('value'))
            .order_by('-year', '-month')
        )
        return Response(expensesByMonth, status=status.HTTP_200_OK)

    
