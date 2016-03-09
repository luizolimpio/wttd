from unittest.mock import Mock

from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionsModelAdmin, Subscription,admin

class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
         Subscription.objects.create(name='Henrique Bastos',cpf='12345678901',email='henrique@bastos.net',phone='21-996186180')
         self.model_admin = SubscriptionsModelAdmin(Subscription,admin.site)

    def test_has_action(self):
        """Action mark_as_paid should be installed."""
        self.assertIn('mark_as_paid',self.model_admin.actions)

    def test_mark_all(self):
        """It should mark all selected subscriptions as paid."""
        self.call_action()
        self.assertEqual(1,Subscription.objects.filter(paid=True).count())



    def test_message(self):
        """It should send a message to the user."""
        mock = self.call_action()
        mock.assert_called_once_with(None,'1 inscrição foi marcada como paga.')



    def call_action(self):
        model_admin = SubscriptionsModelAdmin(Subscription,admin.site)
        queryset = Subscription.objects.all()

        mock = Mock()
        old_menssage_user =SubscriptionsModelAdmin.message_user
        SubscriptionsModelAdmin.message_user = mock

        model_admin.mark_as_paid(None,queryset)

        SubscriptionsModelAdmin.message_user = old_menssage_user
        return mock










