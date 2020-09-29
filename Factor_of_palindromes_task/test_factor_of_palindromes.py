import unittest, timeit
from Factor_of_palindromes_task import factor_of_palindromes as p
from memory_profiler import profile


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.data_false = 'abcde'
        self.data_true_1 = '1abcba1'
        self.data_true_2 = 'abcbabe'
        self.data_file = p.read_file()

    def test_check_palindrome(self):
        self.assertTrue(p.check_palindrome(self.data_true_1))
        self.assertFalse(p.check_palindrome(self.data_false))

    def test_find_palindrome(self):
        self.assertEqual(p.find_palindrome(self.data_true_1), 'bcb')
        self.assertEqual(p.find_palindrome(self.data_true_2), 'bab')

    def test_time(self):
        func_find_palindrome = f'p.find_palindrome(p.read_file())'
        print(f'def find_palindrome time: '
              f'{timeit.timeit(stmt=func_find_palindrome, number=1, globals=globals())}')

        func_write_file = f'p.write_file(p.read_file())'
        print(f'def write_file time: '
              f'{timeit.timeit(stmt=func_write_file, number=1, globals=globals())}')

        func_full = f'p.write_file(p.find_palindrome(p.read_file()))'
        print(f'factor_of_palindromes time: '
              f'{timeit.timeit(stmt=func_full, number=1, globals=globals())}')

    @profile
    def test_memory(self):
        p.write_file(self.data_file)
        p.check_palindrome(self.data_file)
        p.find_palindrome(self.data_file)


if __name__ == '__main__':
    unittest.main()
