from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

class Homepage(TestCase):

    def test_uses_home_templetes(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')