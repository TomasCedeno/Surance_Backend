from rest_framework import status, views
from rest_framework.response import Response
from django.db import models
from django.db.models import Sum, Func
from django.shortcuts import get_object_or_404

from suranceApp.models.expense import Expense
from suranceApp.serializers.expenseSerializer import ExpenseSerializer

# TODO: Crear vista para obtener los ingresos por el Id del usuario al que pertenecen

class ExpenseAPIView(views.APIView):

    serializer_class = ExpenseSerializer

    # PROVISIONAL: DEBERIA DEVOLVER LOS EGRESOS POR USUARIO
    def get(self, request):
        expenses = Expense.objects.all()
        serializer = self.serializer_class(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Crea Egreso"""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):

        expense = get_object_or_404(Expense, id=self.kwargs.get('pk'))
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

    """
    TODO: Hacer que el calculo del total de ingresos sea solamente partir de los egresos de un usuario
        y no a partir de todos los ingresos.
    """

    def get(self, request):
        """Retorna el total de ingresos por cada mes"""
        expensesByMonth = (Expense.objects.annotate(month=ExtractMonth('date'), year=ExtractYear('date'))
                           .values('month', 'year')
                           .annotate(total=Sum('value'))
                           .order_by('-year', '-month'))
        return Response(expensesByMonth, status=status.HTTP_200_OK)

    
