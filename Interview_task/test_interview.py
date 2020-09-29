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
        self.n = 27
        self.l_n1 = [1, 1]
        self.l_n2 = [1, 2]
        self.l_n3 = [1, 3, 2]
        self.l_n4 = [1, 4, 3, 5, 2]
        self.setup = 'from Interview_task import Interview'

    def test_func_new_string(self):
        self.assertEqual(Interview.func_new_string(self.n1), self.n2)
        self.assertEqual(Interview.func_new_string(self.n2), self.n3)
        self.assertEqual(Interview.func_new_string(self.n3), self.n4)

    def test_func_new_list(self):
        self.assertEqual(Interview.func_new_list(self.l_n1), self.l_n2)
        self.assertEqual(Interview.func_new_list(self.l_n2), self.l_n3)
        self.assertEqual(Interview.func_new_list(self.l_n3), self.l_n4)

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

    def test_recursion_list(self):
        self.assertEqual(Interview.recursion_list(1, self.l_n1), self.l_n1)
        self.assertEqual(Interview.recursion_list(2, self.l_n1), self.l_n2)
        self.assertEqual(Interview.recursion_list(3, self.l_n1), self.l_n3)
        self.assertEqual(Interview.recursion_list(4, self.l_n1), self.l_n4)

    def test_count_n(self):
        self.assertEqual(Interview.count_n(self.input_1), self.output_1)
        self.assertEqual(Interview.count_n(self.input_2), self.output_2)

    def test_count_l(self):
        self.assertEqual(Interview.count_l(self.input_1), self.output_1)
        self.assertEqual(Interview.count_l(self.input_2), self.output_2)

    def test_time(self):
        '''func_recursion = f'Interview.recursion({self.n}, \'{self.n1}\')'
        print(f'recursion time for n = {self.n} is '
              f'{timeit.timeit(stmt=func_recursion, number=1, globals=globals())}')

        func_cycle = f'Interview.cycle({self.n})'
        print(f'cycle time for n = {self.n} is '
              f'{timeit.timeit(stmt=func_cycle, number=1, globals=globals())}')

        func_count_n = f'Interview.count_n({self.n})'
        print(f'for n = {self.n} count_n time = '
              f'{timeit.timeit(stmt=func_count_n, number=1, globals=globals(), setup=self.setup)}')'''

        func_count_l = f'Interview.count_l({self.n})'
        print(f'for n = {self.n} count_l time = '
              f'{timeit.timeit(stmt=func_count_l, number=1, globals=globals())}')

    @profile
    def test_memory(self):
        #Interview.cycle(n_cycle=self.n)
        #Interview.recursion(n_recursion=self.n, string_for_insert=self.n1)
        #Interview.count_n(n_count=self.n)
        Interview.count_l(l_count=self.n)


if __name__ == '__main__':
    unittest.main()
