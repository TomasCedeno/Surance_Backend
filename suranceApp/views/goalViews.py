from rest_framework import status, views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from suranceApp.models.goal import Goal
from suranceApp.serializers.goalSerializer import GoalSerializer


#TODO: Crear vista para obtener Metas por el Id del usuario al que pertenecen

class GoalAPIView(views.APIView):

    serializer_class = GoalSerializer

    #PROVISIONAL: EN REALIDAD EL GET DEBE DEVOLVER TODOS LAS METAS POR USUARIO
    def get(self, request):
        goals = Goal.objects.all()
        serializer = self.serializer_class(goals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Crea una meta"""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        """Abona dinero a una meta, recibiendo el ID de la meta
        \n- moneyToPay: Dienro a abonar"""

        goal = get_object_or_404(Goal, id=self.kwargs.get('pk'))

        try:
            savedMoney = goal.savedMoney
            moneyToPay = request.data['moneyToPay']

            if goal.isCompleted:
                return Response({'message': 'This goal is already completed'}, status=status.HTTP_406_NOT_ACCEPTABLE)

            elif (savedMoney + moneyToPay) > goal.goalMoney:
                return Response({'message':'moneyToPay must be less than the remaining money to complete the goal'}, status=status.HTTP_400_BAD_REQUEST)
                
            savedMoney += moneyToPay
        
        except KeyError:
            return Response({'message': 'Missing moneyToPay param'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except:
            return Response({'message':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(goal, data={'savedMoney':savedMoney}, partial=True) # partial=True para actualizar objeto parcialemnte
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


    def delete(self, request, *args, **kwargs):
        """Elimina una meta"""

        goal = get_object_or_404(Goal, id=self.kwargs.get('pk'))
        goal.delete()
        return Response({'message': 'Goal Deleted'} ,status=status.HTTP_204_NO_CONTENT)