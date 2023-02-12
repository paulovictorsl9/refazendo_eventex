from unittest import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class TestaFormularioDeInscricao(TestCase):
    def testa_se_form_tem_campos(self):
        form = SubscriptionForm()
        """form deve ter campos"""
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def testa_se_cpf_e_digito(self):
        """CPF só aceita digitos"""
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def testa_se_cpf_tem_11_digitos(self):
        """CPF deve ter 11 dígitos"""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)



    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    # função auxiliar
    def make_validated_form(self, **kwargs):
        valid = dict(
            name='Paulo Costa',
            cpf='12345678901',
            email='paulovictorsl9@hotmail.com',
            phone='31-3772-5656'
        )
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

