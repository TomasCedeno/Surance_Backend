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
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        goal = get_object_or_404(Goal, id=self.kwargs.get('pk'))
        serializer = self.serializer_class(goal, data=request.data, partial=True) # partial=True para actualizar objeto parcialemnte
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        goal = get_object_or_404(Goal, id=self.kwargs.get('pk'))
        goal.delete()
        return Response({'message': 'Meta Eliminada'} ,status=status.HTTP_204_NO_CONTENT)
