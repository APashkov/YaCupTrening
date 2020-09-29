import unittest, timeit
from Split_all_task import split_all as s
from memory_profiler import profile


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.data_circle_name = 'input_circle.txt'
        self.data_square_name = 'input_square.txt'
        self.data_mesh_name = 'input_mesh.txt'
        self.data_one_point_name = 'input_one_point.txt'
        self.data_one_center_name = 'input_one_center.txt'
        self.data_file = s.read_file('input.txt')
        self.data_file_circle = s.read_file(self.data_circle_name)
        self.data_file_square = s.read_file(self.data_square_name)
        self.data_file_mesh = s.read_file(self.data_mesh_name)
        self.data_circle = [0, 1, 1, 1]
        self.data_square_1 = [1, 1, 1, 3, 3, 3, 3, 1]
        self.data_square_3 = [0, 0, 4, 4, 8, 0, 4, -4]
        self.data_center = (0, 0)
        self.data_point_0 = 0
        self.data_point_1 = [1, 1]
        self.data_point_2 = (2, 2)
        self.data_point_3 = (4, 0)
        self.data_points_string = [
            '0 1 1 1\n',
            '0 2 2 2\n',
            '0 3 3 3\n',
            '1 1 1 1 3 3 3 3 1']
        self.data_points_string_centers = [
            (1, 1),
            (2, 2),
            (3, 3)
        ]

        self.data_points_centers_false = [
            (1, 1),
            (2, 2),
            (3, 2)
        ]

        self.data_two_points_string_centers = [
            (1, 1),
            (2, 2)
        ]

    '''def test_center_square(self):
        self.assertEqual(s.center_square(self.data_square_1), self.data_point_2)
        self.assertEqual(s.center_square(self.data_square_3), self.data_point_3)'''

    def test_find_center(self):
        self.assertEqual(set(s.find_center(self.data_points_string)), set(self.data_points_string_centers))

    def test_straight_line(self):
        self.assertEqual(s.straight_line(self.data_point_1, self.data_point_2), [1, 0])
        self.assertEqual(s.straight_line(self.data_point_1, self.data_point_1), ['~', -1])

    def test_point_on_the_straight_line(self):
        self.assertEqual(s.point_on_the_straight_line(self.data_points_string_centers), 'Yes')
        self.assertEqual(s.point_on_the_straight_line(self.data_points_centers_false), 'No')
        self.assertEqual(s.point_on_the_straight_line(self.data_two_points_string_centers), 'Yes')

    def test_begin(self):
        self.assertEqual(s.begin(self.data_one_point_name), 'Yes')
        self.assertEqual(s.begin(self.data_one_center_name), 'Yes')

    def test_time(self):
        func_circle = 's.begin(\'input_circle.txt\')'
        print(f'def begin time for circle data: '
              f'{timeit.timeit(stmt=func_circle, number=1, globals=globals())}')

        func_square = 's.begin(\'input_square.txt\')'
        print(f'def begin time for square data: '
              f'{timeit.timeit(stmt=func_square, number=1, globals=globals())}')

        func_mesh = 's.begin(\'input_mesh.txt\')'
        print(f'def begin time for mesh data: '
              f'{timeit.timeit(stmt=func_mesh, number=1, globals=globals())}')

    @profile
    def test_memory(self):
        s.read_file()
        s.write_file('Yes/No')
        s.find_center(self.data_file[1])
        s.begin(self.data_circle_name)
        s.begin(self.data_square_name)
        s.begin(self.data_mesh_name)


if __name__ == '__main__':
    unittest.main()
