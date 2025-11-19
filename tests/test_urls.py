from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages import views
from pages import buggy_view


class TestUrls(SimpleTestCase):

    def test_welcome_url_resolves(self):
        url = reverse('welcome')
        resolver = resolve(url)
        self.assertEqual(resolver.func, views.welcome)

    def test_screen1_url_resolves(self):
        url = reverse('screen1')
        resolver = resolve(url)
        self.assertEqual(resolver.func, views.screen1)

    def test_buggy_search_url_resolves(self):
        url = reverse('buggy_search')
        resolver = resolve(url)
        self.assertEqual(resolver.func, buggy_view.buggy_search)