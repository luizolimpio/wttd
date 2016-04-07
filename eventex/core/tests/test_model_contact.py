from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb-pic'
        )
    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='henrique@bastos.net'
        )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='021-35411611'
        )

        self.assertTrue(Contact.objects.exists())
    def test_choice(self):
        """contatos é limitado apenas E ou P"""
        contact = Contact(
            speaker=self.speaker,
            kind='A',
            value='B'
        )
        self.assertRaises(ValidationError,contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='luiz-olimpio@hotmail.com'
        )
        self.assertEqual('luiz-olimpio@hotmail.com',str(contact))

class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Henrique Bastos',
                                   slug ='henrique-bastos',
                                   photo = 'http://hbn.link/hb-pic',
                                   )

        s.contact_set.create(kind=Contact.EMAIL,value='henrique@bastos.net')
        s.contact_set.create(kind=Contact.PHONE,value='079-999438361')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected =['henrique@bastos.net']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phone(self):
        qs = Contact.objects.phones()
        expected = ['079-999438361']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)






