from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')
    def test_get(self):
        """GET / deve retornar status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Deve usar o index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def testa_link_de_inscricao(self):
        self.assertContains(self.response, 'href="/inscricao/"')
# Create your tests here.
