import unittest, timeit
from Interview_task import Interview as i
from memory_profiler import profile


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.input_1 = 4
        self.output_1 = 2
        self.input_2 = 1
        self.output_2 = 2
        self.start_string = '11'
        self.n = 17
        print(self.n)

    def test_func_new_string(self):
        self.assertEqual(i.func_new_string('11'), '121')
        self.assertEqual(i.func_new_string('121'), '13231')
        self.assertEqual(i.func_new_string('13231'), '143525341')

    def test_count_n(self):
        self.assertEqual(i.count_n(self.input_1), self.output_1)
        self.assertEqual(i.count_n(self.input_2), self.output_2)

    def test_time(self):
        print(f'count_n time for n = {self.n} is {timeit.timeit(str(i.count_n(self.n)))}')
        print(f'recursion time for n = {self.n} is {timeit.timeit(str(i.recursion(self.n, self.start_string)))}')
        print(f'cycle time for n = {self.n} is {timeit.timeit(str(i.cycle(self.n)))}')

    @profile
    def test_memory(self):
        i.count_n(self.n)


if __name__ == '__main__':
    unittest.main()
