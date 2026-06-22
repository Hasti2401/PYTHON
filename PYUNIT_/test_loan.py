import unittest
from loan import is_eligible, calculate_emi

class TestLoan(unittest.TestCase):

    def test_eligible_customer(self):
        self.assertTrue(is_eligible(25, 30000))

    def test_underage_customer(self):
        self.assertFalse(is_eligible(18, 30000))
    
    def test_low_salary(self):
        self.assertFalse(is_eligible(35, 21000))
    
    def test_calculate_emi(self):
        self.assertEqual(calculate_emi(12000, 12), 1000.0)

if __name__ == "__main__":
        unittest.main()
