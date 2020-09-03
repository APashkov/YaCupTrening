import unittest
import factor_of_palindromes as p


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.data_false = 'abcde'
        self.data_false_reversed = 'edcba'
        self.data_true_1 = '1abcba1'
        self.data_true_2 = 'abcbabe'

    def test_reverse_string(self):
        self.assertEqual(p.reverse_string(self.data_false), self.data_false_reversed)

    def test_check_palindrome(self):
        self.assertTrue(p.check_palindrome(self.data_true_1))
        self.assertFalse(p.check_palindrome(self.data_false))

    def test_find_palindrome(self):
        self.assertEqual(p.find_palindrome(self.data_true_1), 'bcb')
        self.assertEqual(p.find_palindrome(self.data_true_2), 'bab')

    '''
    def test_something(self):
        self.assertEqual(True, False)

'''
if __name__ == '__main__':
    unittest.main()
