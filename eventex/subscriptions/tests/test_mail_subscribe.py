from django.test import TestCase
from django.core import mail


class InscricaoValida(TestCase):
    def setUp(self):
        data = dict(name='Paulo Costa',
                    cpf='12345678901',
                    email='paulovictorsl9@hotmail.com',
                    phone='31-3772-5656')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def testa_envio_de_confirmacao_inscricao(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def testa_remetente(self):
        expect = 'paulovictorsl9@hotmail.com'
        self.assertEqual(expect, self.email.from_email)

    def testa_destinatario(self):
        expect = ['paulovictorsl9@hotmail.com', 'paulovictorsl9@hotmail.com']
        self.assertEqual(expect, self.email.to)

    def testa_mensagem_enviada(self):
        contents = [
            'Paulo Costa',
            '12345678901',
            'paulovictorsl9@hotmail.com',
            '31-3772-5656',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
