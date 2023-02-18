from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact
from django.shortcuts import resolve_url as r


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Pevas Costa',
            slug='pevas-costa',
            photo='https://static.vecteezy.com/ti/vetor-gratis/p1/2406611-homem-de-negocios-personagem-de-desenho-animado-vetor.jpg'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='paulovictorsl9@hotmail.com'
        )

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='31-3772-5656'
        )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contato deve ser limitado a P ou E"""
        contact = Contact(
            speaker=self.speaker,
            kind='A',
            value='B'
        )
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='paulovictorsl9@hotmail.com'
        )
        self.assertEqual('paulovictorsl9@hotmail.com', str(contact))