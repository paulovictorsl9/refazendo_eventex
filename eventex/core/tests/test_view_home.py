from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    fixtures = ['keynotes.json']

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

    def testa_palestrantes(self):
        """deve mostrar palestrantes"""
        contents = [
                    'href="{}"'.format(r('speaker_detail', slug='grace-hopper')),
                    'Grace Hopper',
                    'https://www.timeforkids.com/wp-content/uploads/2020/08/Grace_003.jpg?w=926',
                    'href="{}"'.format(r('speaker_detail', slug='alan-turing')),
                    'Alan Turing',
                    'https://cdn.britannica.com/81/191581-050-8C0A8CD3/Alan-Turing.jpg'
                    ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def testa_link_palestrantes(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)

    def testa_link_palestras(self):
        expected = 'href="{}"'.format(r('talk_list'))
        self.assertContains(self.response, expected)



