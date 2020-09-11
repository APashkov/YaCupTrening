import unittest, timeit
from Interview_task import Interview
from memory_profiler import profile


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.input_1 = 4
        self.output_1 = 2
        self.input_2 = 1
        self.output_2 = 2
        self.n1 = '11'
        self.n2 = '121'
        self.n3 = '13231'
        self.n4 = '143525341'
        self.n = 15
        #print(f'n = {self.n}')

    def test_func_new_string(self):
        self.assertEqual(Interview.func_new_string(self.n1), self.n2)
        self.assertEqual(Interview.func_new_string(self.n2), self.n3)
        self.assertEqual(Interview.func_new_string(self.n3), self.n4)

    def test_cycle(self):
        self.assertEqual(Interview.cycle(1), self.n1)
        self.assertEqual(Interview.cycle(2), self.n2)
        self.assertEqual(Interview.cycle(3), self.n3)
        self.assertEqual(Interview.cycle(4), self.n4)

    def test_recursion(self):
        self.assertEqual(Interview.recursion(1, self.n1), self.n1)
        self.assertEqual(Interview.recursion(2, self.n1), self.n2)
        self.assertEqual(Interview.recursion(3, self.n1), self.n3)
        self.assertEqual(Interview.recursion(4, self.n1), self.n4)

    def test_count_n(self):
        self.assertEqual(Interview.count_n(self.input_1), self.output_1)
        self.assertEqual(Interview.count_n(self.input_2), self.output_2)

    def test_time(self):
        print(f'count_n time for n = {self.n} is {timeit.timeit(str(Interview.count_n(n_count=self.n)))}')
        print(f'recursion time for n = {self.n} is '
              f'{timeit.timeit(str(Interview.recursion(n_recursion=self.n, string_for_insert=self.n1)))}')
        print(f'cycle time for n = {self.n} is {timeit.timeit(str(Interview.cycle(n_cycle=self.n)))}')

    @profile
    def test_memory(self):
        Interview.cycle(n_cycle=self.n)
        Interview.recursion(n_recursion=self.n, string_for_insert=self.n1)
        Interview.count_n(n_count=self.n)


if __name__ == '__main__':
    unittest.main()
