from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Speaker


class DetalhesPalestrantesGet(TestCase):
    def setUp(self):
        Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='https://www.timeforkids.com/wp-content/uploads/2020/08/Grace_003.jpg?w=926',
            website='https://pt.wikipedia.org/wiki/Grace_Hopper',
            description='Programadora e Almirante.'
        )
        self.response = self.client.get(r('speaker_detail', slug='grace-hopper'))

    def test_get(self):
        """GET deve retornar status code 200"""
        self.assertEqual(200, self.response.status_code)

    def testa_template(self):
        self.assertTemplateUsed(self.response, 'core/speaker_detail.html')

    def testa_html(self):
        contents = [
            'Grace Hopper',
            'https://www.timeforkids.com/wp-content/uploads/2020/08/Grace_003.jpg?w=926',
            'https://pt.wikipedia.org/wiki/Grace_Hopper'
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def testa_context(self):
        """palestrantes deve ter contexto"""
        speaker = self.response.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class PalestranteNaoEncontrado(TestCase):
    def test_nao_encontrado(self):
        response = self.client.get(r('speaker_detail', slug='not-found'))
        self.assertEqual(404, response.status_code)

