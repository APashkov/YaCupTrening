from Split_all_task import split_all as s

data = ''
for number in range(1, 100001):
    print(f'number = {number}')
    data += str(number) + ' ' + str(number + 100) + '\n'

print(data)
s.write_file(answer=data, file='input_new.txt')
