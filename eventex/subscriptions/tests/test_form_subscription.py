from unittest import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class TestaFormularioDeInscricao(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def testa_se_form_tem_campos(self):
        """form deve ter campos"""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))
