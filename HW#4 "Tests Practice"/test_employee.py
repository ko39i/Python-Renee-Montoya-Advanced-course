from unittest import TestCase
from employee import Employee

class TestEmployee(TestCase):

    def test_eml(self):
        self.empl = Employee('Jon', 'Sina', 120)

    def test_first(self):
        self.assertEqual(self.empl.first, 'Jon')

    def test_email(self):
        self.assertEqual(self.empl.email, 'Jon.Sina@email.com')
