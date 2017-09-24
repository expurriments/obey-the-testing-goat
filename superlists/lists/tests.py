from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase

from .views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        self.assertEqual(resolve('/').func, home_page)

    def test_home_page_returns_welcome_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Superlists</title>', html)
        self.assertTrue(html.endswith('</html>'))