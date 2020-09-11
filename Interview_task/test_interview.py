import unittest, timeit
from Interview_task import Interview as i
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
        self.n = 18
        print(f'n = {self.n}')

    def test_func_new_string(self):
        self.assertEqual(i.func_new_string(self.n1), self.n2)
        self.assertEqual(i.func_new_string(self.n2), self.n3)
        self.assertEqual(i.func_new_string(self.n3), self.n4)

    def test_cycle(self):
        self.assertEqual(i.cycle(1), self.n1)
        self.assertEqual(i.cycle(2), self.n2)
        self.assertEqual(i.cycle(3), self.n3)
        self.assertEqual(i.cycle(4), self.n4)

    def test_recursion(self):
        self.assertEqual(i.recursion(1, self.n1), self.n1)
        self.assertEqual(i.recursion(2, self.n1), self.n2)
        self.assertEqual(i.recursion(3, self.n1), self.n3)
        self.assertEqual(i.recursion(4, self.n1), self.n4)

    def test_count_n(self):
        self.assertEqual(i.count_n(self.input_1), self.output_1)
        self.assertEqual(i.count_n(self.input_2), self.output_2)

    def test_time(self):
        print(f'count_n time for n = {self.n} is {timeit.timeit(str(i.count_n(nnn=self.n)))}')
        print(f'recursion time for n = {self.n} is {timeit.timeit(str(i.recursion(n=self.n, aa=self.n1)))}')
        print(f'cycle time for n = {self.n} is {timeit.timeit(str(i.cycle(nn=self.n)))}')

    @profile
    def test_memory(self):
        i.cycle(nn=self.n)
        i.recursion(n=self.n, aa=self.n1)
        i.count_n(nnn=self.n)


if __name__ == '__main__':
    unittest.main()
