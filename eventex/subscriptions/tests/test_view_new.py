from django.shortcuts import resolve_url as r
from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class NovaInscricaoGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('subscriptions:new'))

    def test_get(self):
        """GET /inscricao/ deve retornar status code 200"""
        self.assertEqual(200, self.response.status_code)

    def testa_template(self):
        """deve usar subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def testa_html(self):
        """html deve conter tags de entradas"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def testa_csrf(self):
        """html deve conter csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def testa_se_tem_form(self):
        """deve conter formulário de inscrição"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class NovaInscricaoValida(TestCase):
    def setUp(self):
        data = dict(name='Paulo Costa',
                    cpf='12345678901',
                    email='paulo@costa.com.br',
                    phone='31-3772-5656')
        self.response = self.client.post(r('subscriptions:new'), data)

    def test_post(self):
        """POST válido deve redirecionar para /inscricao/1"""
        self.assertRedirects(self.response, r('subscriptions:detail', 1))

    def testa_envio_de_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_salvar_inscricao_no_banco(self):
        self.assertTrue(Subscription.objects.exists())


class InscricaoInvalida(TestCase):
    def setUp(self):
        self.response = self.client.post(r('subscriptions:new'), {})

    def test_post(self):
        """POST inválido não redireciona"""
        self.assertEqual(200, self.response.status_code)

    def teste_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def testa_se_tem_form(self):
        """deve conter formulário de inscrição"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def testa_se_form_tem_erros(self):
        """form apresenta erros"""
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_nao_salvar_inscricao_no_banco(self):
        self.assertFalse(Subscription.objects.exists())


class TesteDeRegressaoDeTemplate(TestCase):
    def testa_template_nao_tem_erros(self):
        invalid_data = dict(name='Paulo Costa',
            cpf='12345678901')
        response = self.client.post(r('subscriptions:new'), invalid_data)

        self.assertContains(response, '<ul class="errorlist nonfield">')



