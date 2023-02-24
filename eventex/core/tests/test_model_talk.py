from django.test import TestCase
from eventex.core.models import Talk


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Título da Palestra'
        )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def testa_se_tem_palestrantes(self):
        """Palestra tem muitos palestrantes e vice versa"""
        self.talk.speakers.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            website='http://henriquebastos.net'
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_descricao_em_branco(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_palestrante_em_branco(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_inicio_em_branco(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_inicio_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Título da Palestra', str(self.talk))

