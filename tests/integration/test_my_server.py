from unittest import TestCase

import requests


class TestMyServer(TestCase):
    def test_my_server(self):
        result = requests.get("http://localhost:8081/generichttpws/")

        self.assertEquals(200, result.status_code)
        self.assertTrue("Service description here." in result.text)