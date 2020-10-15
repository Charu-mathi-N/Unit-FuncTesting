from django.test import TestCase
from selenium import webdriver
from .forms import HashForm
import hashlib
from . import models

# class FunctionalTest(TestCase):

#     def setUp(self):
#         self.browser = webdriver.Safari()

#     def test_homepage_exists(self):
#         self.browser.get("http://127.0.0.1:8000/")
#         self.assertIn("install", self.browser.page_source)

#     def test_hash(self):
#         self.browser.get("http://127.0.0.1:8000/")
#         text = self.browser.find_element_by_id('id_text')
#         text.send_keys("hello")
#         self.browser.find_element_by_name('submit').click()
#         self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

#     def teardown(self):
#         self.browser.quit()

class UnitTest(TestCase):

    def test_homepage(self):
         response = self.client.get('/')
         self.assertTemplateUsed(response, 'home.html')

    def test_form(self):
        form = HashForm(data = {'text': 'Hello'})
        self.assertTrue(form.is_valid())

    def test_hash(self):
        text_form = hashlib.sha256('hello'.encode('UTF-8')).hexdigest()
        self.assertEqual("2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824" , text_form)

    def test_save_hash(self):

        Hash = hash()
        Hash.text = 'hello'
        Hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        Hash.save()
        pulled_hash = Hash.objects.get(hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertEqual(Hash.text, pulled_hash.text)

