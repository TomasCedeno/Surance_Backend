from rest_framework import status, views
from rest_framework.response import Response
from django.db import models
from django.db.models import Sum, Func

from suranceApp.models import Income
from suranceApp.serializers import IncomeSerializer


#TODO: Crear vista para obtener los ingresos por el Id del usuario al que pertenecen

class IncomeAPIView(views.APIView):

    serializer_class = IncomeSerializer

    #PROVISIONAL: DEBERIA DEVOLVER LOS INGRESOS POR USUARIO
    def get(self, request):
        goals = Income.objects.all()
        serializer = self.serializer_class(goals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Crea Ingreso"""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)



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

    """
    TODO: Hacer que el calculo del total de ingresos sea solamente partir de los ingresos de un usuario
        y no a partir de todos los ingresos.
    """

    def get(self, request):
        """Retorna el total de ingresos por cada mes"""
        incomesByMonth = ( Income.objects.annotate(month=ExtractMonth('date'), year=ExtractYear('date'))
        .values('month', 'year')
        .annotate(total=Sum('value'))
        .order_by('-year', '-month') )
        return Response(incomesByMonth, status=status.HTTP_200_OK)
