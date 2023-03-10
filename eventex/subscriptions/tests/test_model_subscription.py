from datetime import datetime
from django.shortcuts import resolve_url as r
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Paulo Costa',
            cpf='12345678901',
            email='paulovictorsl9@hotmail.com',
            phone='31-3772-5656'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        """Subscription precisa conter um auto_created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Paulo Costa', str(self.obj))

    def test_pagamento_default_to_False(self):
        """Por padrão pagamento deve ser falso"""
        self.assertEqual(False, self.obj.paid)

    def get_test_absolute_url(self):
        url = r('subscriptions:detail', self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())



