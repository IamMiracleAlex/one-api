from rest_framework.test import APITestCase
from rest_framework import status

from app.tests.factories import CharacterFactory
from users.tests.factories import UserFactory



class CharacterViewTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
      
    def test_character_list(self):
        '''Assert that character are returned'''

        country = CharacterFactory()
        url = '/characters'
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        