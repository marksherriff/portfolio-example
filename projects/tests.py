from django.test import TestCase

class DummyTests(TestCase): 
    def test_dummy_text(self):
        self.assertEqual("Dummy Test", "Dummy Test")