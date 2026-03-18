from unittest import TestCase

from example import my_function


class TestMyFunction(TestCase):
    def test_my_function(self):
        self.assertTrue("Bobcat" in my_function("Bobcat"))