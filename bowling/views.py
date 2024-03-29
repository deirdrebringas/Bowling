from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import GameSerializer, FrameSerializer, NewGameSerializer, GameSerializerNoFrames
from .models import Game, Frame
import json

class ListGamesView(generics.ListAPIView):
	queryset = Game.objects.all()
	serializer_class = GameSerializerNoFrames


class CreateNewGameView(APIView):
	#Create a new game
	def get(self, request):
		newGame = Game.objects.create()
		newGame.initialiseFrames()
		return Response(NewGameSerializer(newGame).data, status=status.HTTP_201_CREATED)


class BowlingApiView(APIView):
	#Get a certain game
	def get(self, request, gameId):
		try:
			game = Game.objects.get(gameId=gameId)
			return Response(GameSerializer(game).data, status=status.HTTP_200_OK)
		except IndexError as e:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	#Update a game 
	def post(self, request, gameId):
		try:
			body = json.loads(request.body)
			score = body["score"]
			game = Game.objects.get(gameId=gameId)
			game.updateScores(score)
			return Response(status=status.HTTP_200_OK)
		except (IndexError, ValueError) as e:
			return Response(status=status.HTTP_400_BAD_REQUEST)