from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Note: For these tests to pass, you must have URL patterns with the names
# 'home' and 'project_detail' in your urls.py. The 'project_detail' URL
# should also accept an integer as an argument. For example:
# path('', HomePageView.as_view(), name='home'),
# path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),

class UrlTests(SimpleTestCase):

    def test_home_url_resolves(self):
        """Test that the URL for the home page resolves correctly."""
        url = reverse('home')
        # The resolve() function finds the view that Django would use for a given URL.
        # We check that the resolved view name matches the URL pattern name.
        self.assertEqual(resolve(url).view_name, 'home')

    def test_project_detail_url_resolves(self):
        """Test that the URL for a project detail page resolves correctly."""
        # The reverse() function can take arguments for URLs that need them.
        url = reverse('project_detail', args=[1])
        self.assertEqual(resolve(url).view_name, 'project_detail')
