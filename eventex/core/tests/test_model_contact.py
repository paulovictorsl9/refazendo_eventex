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


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Pevas Costa',
            slug='pevas-costa',
            photo='https://static.vecteezy.com/ti/vetor-gratis/p1/2406611-homem-de-negocios-personagem-de-desenho-animado-vetor.jpg'
        )
        s.contact_set.create(kind=Contact.EMAIL, value='paulovictorsl9@hotmail.com')
        s.contact_set.create(kind=Contact.PHONE, value='31-3772-5656')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['paulovictorsl9@hotmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['31-3772-5656']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)