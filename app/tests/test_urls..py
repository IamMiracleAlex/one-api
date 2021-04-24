from django.test import SimpleTestCase
from django.urls import resolve

from app import views



class CharacterUrlTests(SimpleTestCase):

    def test_character_handler_resolves_to_view(self):
        '''Assert that character url resolves to view'''

        # resolves to the func.view_class
        found = resolve('/characters')
        self.assertEquals(found.func.view_class, views.CharacterView)

    def test_character_quote_view_resolves_to_view(self):
        '''Assert that character_quote resolves to view'''

        found = resolve('/characters/<str:id>/quotes', args=[1])
        self.assertEquals(found.func.view_class, views.CharacterQuoteView)