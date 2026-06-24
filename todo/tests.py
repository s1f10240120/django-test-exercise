from django.test import TestCase

# Create your tests here.
class TodoTestCase(TestCase):
    def test_sample1(self):
        self.assertEqual(1 + 2, 3)