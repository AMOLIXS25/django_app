from django.test import SimpleTestCase
from django.urls import reverse


class HomePageViewTests(SimpleTestCase):
    def test_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Home Page</h1>')

    def test_if_base_html_is_extended(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<nav class="navbar">')


class AboutPageViewTests(SimpleTestCase):
    def test_url_exists_at_desired_location(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')

    def test_template_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, '<h1>About</h1>')

    def test_if_base_html_is_extended(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, '<nav class="navbar">')