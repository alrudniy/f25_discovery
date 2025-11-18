from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User
from django.contrib.auth import get_user_model

class NotificationsTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a user to log in for accessing protected views
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123',
            user_type=User.UserType.UNIVERSITY # User type might not matter for notifications view itself
        )
        self.notifications_url = reverse('notifications')

    def test_notifications_access_control(self):
        """
        Confirms that only authenticated users can view the notifications page,
        while unauthenticated visitors are redirected to the login page.
        """
        # Unauthenticated user should be redirected to login
        response = self.client.get(self.notifications_url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

        # Authenticated user should access the page successfully
        self.client.login(email='test@example.com', password='password123')
        response = self.client.get(self.notifications_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/notifications.html')
        self.client.logout()

    def test_notifications_template_rendering(self):
        """
        Confirms the correct template is used and the page displays expected elements.
        """
        self.client.login(email='test@example.com', password='password123')
        response = self.client.get(self.notifications_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/notifications.html')
        self.assertContains(response, 'Your Notifications')
        self.assertContains(response, 'Stay updated with the latest activities.')
        self.assertContains(response, 'Current Notifications')
        self.assertContains(response, 'Previous Notifications')
        # Check for the "No new notifications" message when context is empty
        self.assertContains(response, 'No new notifications.')
        self.assertContains(response, 'No previous notifications.')
        self.client.logout()
