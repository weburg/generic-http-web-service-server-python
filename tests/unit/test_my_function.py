from unittest import TestCase

from app.my_function import my_function


class TestMyFunction(TestCase):
    def test_my_function(self):
        self.assertTrue("Python" in my_function("Python"))