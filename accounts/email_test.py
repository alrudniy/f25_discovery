from django.test import TestCase
from django.urls import reverse
from django.core import mail
from .models import User

class EmailSendingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )

    def test_password_reset_email_sent(self):
        """
        Tests that a password reset email is sent to the correct user.
        """
        self.client.post(reverse('password_reset'), {'email': self.user.email})
        self.assertEqual(len(mail.outbox), 1)
        sent_email = mail.outbox[0]
        self.assertEqual(sent_email.to, [self.user.email])
        self.assertIn('Password reset', sent_email.subject)
