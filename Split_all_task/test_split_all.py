import unittest, timeit
from Split_all_task import split_all as s
from memory_profiler import profile


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.data_file = s.read_file()
        self.data_circle = [0, 1, 1, 1]
        self.data_square_1 = [1, 1, 1, 3, 3, 3, 3, 1]
        self.data_point_1 = [1, 1]
        self.data_point_2 = [2, 2]
        self.data_points_string = [
            '0 1 1 1\n',
            '0 2 2 2\n',
            '0 3 3 3\n',
            '1 1 1 1 3 3 3 3 1']
        self.data_points_string_centers = [
            [1, 1],
            [2, 2],
            [3, 3],
            [2, 2]
        ]
        self.data_points_centers_false = [
            [1, 1],
            [2, 2],
            [3, 3],
            [2, 1]
        ]

    def test_center_square(self):
        self.assertEqual(s.center_square(self.data_square_1), self.data_point_2)

    def test_find_center(self):
        self.assertEqual(s.find_center(self.data_points_string), self.data_points_string_centers)

    def test_straight_line(self):
        self.assertEqual(s.straight_line(self.data_point_1, self.data_point_2), [1, 0])

    def test_point_on_the_straight_line(self):
        self.assertEqual(s.point_on_the_straight_line(4, self.data_points_string_centers), 'Yes')
        self.assertEqual(s.point_on_the_straight_line(4, self.data_points_centers_false), 'No')

    def test_time(self):
        print(f'def find_center time: {timeit.timeit(stmt=str(s.find_center(self.data_file[1])))}')

    @profile
    def test_memory(self):
        s.read_file()
        s.write_file('Yes/No')
        s.find_center(self.data_file[1])


if __name__ == '__main__':
    unittest.main()
