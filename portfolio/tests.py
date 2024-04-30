from django.test import TestCase, tag, Client
from . import forms

# Create your tests here.
class WebsiteTestCase(TestCase):
    @tag("form", "contact")
    def test_form_is_valid(self):
        form = forms.ContactForm()