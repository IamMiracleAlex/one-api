from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from decouple import config

from app.models import Favourite
from.seriliazers import FavouriteCharacterQuoteSerializer


BASE_URL = config('BASE_URL')
API_KEY = config('API_KEY')
HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}


class CharacterView(APIView):
    '''Gets all characters..
       GET -- /characters
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        response = requests.get(
            url='{}/character'.format(BASE_URL), 
            headers=HEADERS).json()
        
        return Response(data=response, status=status.HTTP_200_OK)


class CharacterQuoteView(APIView):
    '''Gets all quotes from a specific character
        GET -- /characters/{id}/quotes
    '''
    permission_classes = [IsAuthenticated]

    def get(self, request, id, *args, **kwargs):
        response = requests.get(
            url=f'{BASE_URL}/quote?sort={id}:desc',
            headers=HEADERS).json()
    
        return Response(data=response, status=status.HTTP_200_OK)


class FavouriteCharacterQuoteView(APIView):
    '''Allows a user to favourite a character
        POST -- /characters/<str:id>/favorites
    '''
    permission_classes = [IsAuthenticated]

    def post(self, request, character_id, quote_id=None, *args, **kwargs):
        serializer = FavouriteCharacterQuoteSerializer(
            data=request.data, 
            context={'user': request.user, 'character_id': character_id, 'quote_id': quote_id})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'detail': 'Success'}, status=status.HTTP_201_CREATED)
  

    def get(self, request, *args, **kwargs):
        favourites = Favourite.objects.filter(user=request.user)
        data = FavouriteCharacterQuoteSerializer(favourites, many=True).data
        return Response(data, status.HTTP_200_OK)

        