def read_file(file='input.txt'):
    with open(file) as input_file:
        first_line = int(input_file.readline())
        input_data = set(input_file.readlines())
    return first_line, input_data


def write_file(answer, file='output.txt'):
    with open(file, 'w') as output_file:
        output_file.write(answer)
    return


def find_center(data_list):
    points_set = set()
    for line in data_list:
        line = tuple(map(int, line.split()))

        line_0 = line[0]
        if line_0 == 0:
            point = (line[2], line[3])
        elif line_0 == 1:
            x = int(sum(line[1::2]) / 4)
            y = int(sum(line[2::2]) / 4)
            point = (x, y)
        points_set.add(point)
    return tuple(points_set)


def straight_line(point_1, point_2):
    '''Вывод общих выражений для вычисления b и k:
    y1 = kx1 + b
    y2 = kx2 + b
    b = y2 - kx2
    y1 = kx1 + y2 - kx2
    k = (y1 - y2) / (x1 - x2)'''

    x1 = point_1[0]
    y1 = point_1[1]
    x2 = point_2[0]
    y2 = point_2[1]
    if x1 == x2:
        k = '~'
        b = -x2
    else:
        k = (y1 - y2) / (x1 - x2)
        b = y2 - (k * x2)

    return [k, b]


def point_on_the_straight_line(center_points):
    point_1 = center_points[0]
    point_2 = center_points[1]
    k, b = straight_line(point_1, point_2)

    for point_next in center_points[2:]:
        ki, bi = straight_line(point_1, point_next)
        if (k != ki) or (b != bi):
            return 'No'
    return 'Yes'


def begin(data_file_input):
    count_points, data = read_file(data_file_input)
    if count_points == 1:
        contains = 'Yes'
    else:
        points = find_center(data)
        if len(points) <= 2:
            contains = 'Yes'
        else:
            contains = point_on_the_straight_line(points)

    write_file(contains)
    return contains


if __name__ == '__main__':
    begin('input.txt')

