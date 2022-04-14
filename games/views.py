from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import GameSerializer
from .models import Game

@api_view(['GET', 'POST'])
def games_list(request):

    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GameSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def game_detail(request, pk):
        game = get_object_or_404(Game, pk = pk)
        if request.method == 'GET':
            serializer = GameSerializer(game)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = GameSerializer(game, data = request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'DELETE':
            game.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
