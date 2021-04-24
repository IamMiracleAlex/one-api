from django.test import TestCase
from django.urls import reverse

from users.tests.factories import UserFactory
from app.tests import factories


class CharacterAdminTest(TestCase):

    def setUp(self):
        self.user = UserFactory(is_staff=True, is_superuser=True)
        self.client.force_login(self.user) 
        self.char = factories.CharacterFactory() 

    def test_changelist_view(self):
        '''Test character change list view'''

        url = reverse("admin:%s_%s_changelist" % (self.char._meta.app_label, self.char._meta.model_name))
        page = self.client.get(url)
        # Assert page loads
        self.assertEqual(page.status_code, 200)

    def test_change_view(self):
        '''Test character change view page loads'''

        url = reverse("admin:%s_%s_change" % (self.char._meta.app_label, self.char._meta.model_name), args=(self.char.pk,))
        page = self.client.get(url)
        self.assertEqual(page.status_code, 200)