from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Note: For these tests to pass, you must have the Django admin app
# enabled in your project's INSTALLED_APPS and urls.py, which is
# the default for new Django projects.

class UrlTests(SimpleTestCase):

    def test_admin_login_url_resolves(self):
        """Test that the URL for the admin login page resolves correctly."""
        url = reverse('admin:login')
        self.assertEqual(resolve(url).view_name, 'admin:login')
