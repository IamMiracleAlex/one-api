from rest_framework import serializers
from rest_framework.validators import ValidationError
import requests
from decouple import config

from app.models import Favourite, Character, Quote
from users.models import User

BASE_URL = config('BASE_URL')
API_KEY = config('API_KEY')
HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class FavouriteCharacterQuoteSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    quotes = QuoteSerializer(read_only=True, many=True)

    class Meta:
        model = Favourite
        fields = '__all__'

    def validate(self, data):
        # check character_id validity
        character_id = self.context['character_id']
        response = requests.get(
            url=f'{BASE_URL}/character/{character_id}',
            headers=HEADERS
            )
        if response.status_code != 200:
            raise ValidationError(detail=response.json())
        data['character'] = response.json()['docs'][0]

        # check quote_id validity
        quote_id = self.context['quote_id']
        if quote_id is not None:
            response = requests.get(
                url=f'{BASE_URL}/quote/{quote_id}',
                headers=HEADERS
            )
            if response.status_code != 200:
                raise ValidationError(detail=response.json())
            data['quote'] = response.json()['docs'][0]

        return data

    def create(self, validated_data):
        # create character and add as to favourites

        character = validated_data.pop('character')
        char = Character.objects.create(**character)
        favourite = Favourite.objects.create(user=self.context['user'])
        favourite.characters.add(char)

        # create quote and add to favourites
        quote = validated_data.pop('quote', None)
        if quote is not None:
            quo = Quote.objects.create(**quote)
            favourite.quotes.add(quo)
        return favourite
