import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.test_employee = Employee('Harry', 'Taylor', 55000)

    def test_give_default_raise(self):
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.salary, 60000)

    def test_give_custom_raise(self):
        self.test_employee.give_raise(15000)
        self.assertEqual(self.test_employee.salary, 70000)

if __name__ == '__main__':
    unittest.main()