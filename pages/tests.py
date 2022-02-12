from django.test import SimpleTestCase
from django.urls import reverse

class SimpleTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_users_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "index.html")

    def test_home_page_extends_base_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "base.html")

    def test_home_page_contains_correct_content(self):
        response = self.client.get("/")
        self.assertContains(response, "Hello World")

    def test_home_page_url_reverse_lookup(self):
        response = self.client.get(reverse("home"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")



    def test_about_page_users_correct_template(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "about.html")

    def test_about_page_extends_base_template(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "base.html")

    def test_about_page_contains_correct_content(self):
        response = self.client.get("/about/")
        self.assertContains(response, "Will Cisneros")

    def test_about_page_url_reverse_lookup(self):
        response = self.client.get(reverse("about"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")