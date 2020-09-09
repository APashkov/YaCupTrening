from Split_all_task import split_all as s

len_data = 100000

data_circle = str(len_data) + '\n'
data_square = data_circle
data_mesh = data_circle

for number in range(1, len_data + 1):
    xy1 = str(number) + ' '
    xy3 = str(number + 2) + ' '
    circle = '0 10 ' + xy1 * 2 + '\n'
    square = '1 ' + xy1 * 3 + xy3 * 4 + xy1 + '\n'
    data_circle += circle
    data_square += square
    if number <= (len_data / 2):
        data_mesh += circle + square

print(f'data_circle: {len(data_circle.splitlines())},'
      f' data_square: {len(data_square.splitlines())},'
      f' data_mesh: {len(data_mesh.splitlines())}')

s.write_file(answer=data_circle, file='input_circle.txt')
s.write_file(answer=data_square, file='input_square.txt')
s.write_file(answer=data_mesh, file='input_mesh.txt')
