from django.test import TestCase

class TodoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')