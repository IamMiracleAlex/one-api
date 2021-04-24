from django.test import TestCase

from users.tests.factories import UserFactory
from app.tests.factories import CharacterFactory


class CharacterFactoryTest(TestCase):

    def test_model_creation(self):
        '''Assert that the character model was created with correct defaults'''

        character = CharacterFactory()

        self.assertIsNotNone(character.race) 
        self.assertIsNotNone(character.gender) 
        self.assertIsNotNone(character.birth) 
        self.assertIsNotNone(character.spouse) 
        self.assertIsNotNone(character.realm) 
