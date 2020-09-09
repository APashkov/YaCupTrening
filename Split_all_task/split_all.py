def read_file(file='input.txt'):
    with open(file) as input_file:
        first_line = int(input_file.readline())
        input_data = input_file.readlines()
        print(input_data)
    return first_line, input_data


def write_file(answer, file='output.txt'):
    with open(file, 'w') as output_file:
        output_file.write(answer)
    return


def find_center(data_list):
    points_list = list()
    for line in data_list:
        line = list(map(int, line.split()))

        if line[0] == 0:
            point = [line[2], line[3]]
        elif line[0] == 1:
            point = center_square(line[1:])

        points_list.append(point)
    return points_list


def center_square(square_points):
    x = sum(square_points[::2]) / 4
    y = sum(square_points[1::2]) / 4
    return [x, y]


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
    k = (y1 - y2) / (x1 - x2)
    b = y2 - (k * x2)
    return [k, b]


def point_on_the_straight_line(number_points, center_points):
    point_1 = center_points[0]
    point_2 = center_points[1]
    k, b = straight_line(point_1, point_2)

    for number in range(1, number_points - 1):
        point_first = center_points[number]
        point_second = center_points[number + 1]
        ki, bi = straight_line(point_first, point_second)
        if (k == ki) and (b == bi):
            result = 'Yes'
        else:
            result = 'No'
            break
    return result


if __name__ == '__main__':
    count_points, data = read_file()
    if count_points <= 1:
        contains = 'Yes'
    else:
        points = find_center(data)
        contains = point_on_the_straight_line(count_points, points)

    print(contains)
    write_file(contains)
