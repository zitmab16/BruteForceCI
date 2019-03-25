from unittest import TestCase
from password import Password

class TestPassword(TestCase):
    def test_check(self):
        pwd = Password("abc")
        self.assertEqual(True,pwd.check("abc"))

    def test_check2(self):
        pwd = Password("adc")
        self.assertEqual(False,pwd.check("abc"))

    def test_check3(self):
        pwd = Password("adc")
        self.assertEqual(True,pwd.check("abc"))
