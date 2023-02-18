from django.test import TestCase
from eventex.core.models import Speaker
from django.shortcuts import resolve_url as r


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='https://www.timeforkids.com/wp-content/uploads/2020/08/Grace_003.jpg?w=926',
            website='https://pt.wikipedia.org/wiki/Grace_Hopper',
            description='Programadora e Almirante'
        )

    def test_create(self):
        self.assertTrue(Speaker.objects.exists())

    def test_descricao_pode_ser_em_branco(self):
        field = Speaker._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_website_pode_ser_em_branco(self):
        field = Speaker._meta.get_field('website')
        self.assertTrue(field.blank)

    def test_str(self):
        self.assertEqual('Grace Hopper', str(self.speaker))

    def test_get_absolut_url(self):
        url = r('speaker_detail', slug=self.speaker.slug)
        self.assertEqual(url, self.speaker.get_absolute_url())