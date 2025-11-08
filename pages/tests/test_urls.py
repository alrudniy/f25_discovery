from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import welcome, screen1, screen2, screen3

class TestUrls(SimpleTestCase):
    
    def test_welcome_url_resolves(self):
        url = reverse('welcome') #generates the URL for the 'welcome' view
        self.assertEqual(resolve(url).func, welcome) #resolve(url) matches the URL to the corresponding view function
        #assertEqual(resolve(url).func, project_list) → ensures the URL actually resolves to the right view.
        #basically, the test is not testing the database or the models, just that the URLs point to the right views.
        #If someone changes the URL patterns in the urls.py file, this test will catch that mistake.
        #It's a way to ensure that the URL routing is set up correctly.
        #That’s why it can run fast 


    def test_screen1_url_resolves(self):
        url = reverse('screen1') #generates the URL for the 'screen1' view
        self.assertEqual(resolve(url).func, screen1) 

    def test_screen2_url_resolves(self):
        url = reverse('screen2')#generates the URL for the 'detail' view with a sample slug
        self.assertEqual(resolve(url).func, screen2)

    def test_screen3_url_resolves(self):
        url = reverse('screen3')#generates the URL for the 'detail' view with a sample slug
        self.assertEqual(resolve(url).func, screen3)
