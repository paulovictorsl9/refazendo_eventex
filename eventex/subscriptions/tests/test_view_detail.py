from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Paulo Costa',
            cpf='12345678901',
            email='paulovictorsl9@hotmail.com',
            phone='31-3772-5656'
        )
        self.response = self.client.get('/inscricao/{}/'.format(self.obj.pk))


    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)
        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)


class SubscriptionDetailNotFound(TestCase):
    def teste_nao_encontrado(self):
        response = self.client.get('/inscricao/0/')
        self.assertEqual(404, response.status_code)
