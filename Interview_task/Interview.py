def func_new_string(string):
    new_string = '1'
    len_string = len(string)
    for index in range(len_string - 1):
        index_plus = string[index + 1]
        new_string += str(int(string[index]) + int(index_plus)) + index_plus
        '''print(f'string[{index}] = {string[index]},'
              f' string[{index + 1}] = {string[index + 1]},'
              f' new_string = {new_string}')'''
        #print(new_string[::-1])
    return new_string


def cycle(n_cycle):
    n1 = '11'
    for _ in range(n_cycle - 1):
        n1 = func_new_string(n1)
    return n1


def recursion(n_recursion, string_for_insert):
    if n_recursion == 1:
        return string_for_insert
    n_recursion -= 1
    string_for_insert = func_new_string(string_for_insert)
    return recursion(n_recursion, string_for_insert)


def count_n(n_count):
    return recursion(n_count, '11').count(str(n_count))


if __name__ == '__main__':
    s_data = '11'
    print(f'recursion   = {recursion(4, s_data)}')
    data = '13231'
    print(f'func        = {func_new_string(data)}')
    print(f'cycle       = {cycle(4)}')
    print(f'count_n = {count_n(4)}')