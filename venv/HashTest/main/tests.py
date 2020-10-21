from django.test import TestCase
from selenium import webdriver
from .forms import HashForm
import hashlib
from .models import Hash
from django.core.exceptions import ValidationError

# class FunctionalTest(TestCase):

#     def setUp(self):
#         self.browser = webdriver.Safari()

#     def test_homepage_exists(self):
#         self.browser.get("http://127.0.0.1:8000/")
#         self.assertIn("Enter the text to see the hash", self.browser.page_source)

#     def test_hash(self):
#         self.browser.get("http://127.0.0.1:8000/")
#         text = self.browser.find_element_by_id('id_text')
#         text.send_keys("hello")
#         self.browser.find_element_by_name('Submit').click()
#         self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

#     def tearDown(self):
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


    def save(self):
        hash = Hash()
        hash.text = 'hello'
        hash.hashed = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        hash.save()
        return hash

    def test_save_hash(self):
        hash = self.save()
        pulled_hash = Hash.objects.get(hashed='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertEqual(hash.text, pulled_hash.text)

    def test_viewing_hash(self):
        hash = self.save()
        response = self.client.get('/hash/2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertContains(response, 'hello')

    def test_bad_data_(self):
        def bad_hash():
            hash = Hash()
            hash.hashed = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824het'
            hash.full_clean()
        self.assertRaises(ValidationError, bad_hash)
