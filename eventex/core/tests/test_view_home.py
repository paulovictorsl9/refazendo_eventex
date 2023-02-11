from django.test import TestCase
from django.shortcuts import resolve_url as r

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))
    def test_get(self):
        """GET / deve retornar status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Deve usar o index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def testa_link_de_inscricao(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)

