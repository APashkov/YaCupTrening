def func_new_string(string):
    new_string = '1'
    len_string = len(string)
    for index in range(len_string - 1):
        index_plus = string[index + 1]
        new_string += str(int(string[index]) + int(index_plus)) + index_plus
        '''print(f'string[{index}] = {string[index]},'
              f' string[{index + 1}] = {string[index + 1]},'
              f' new_string = {new_string}')'''
    return new_string


def func_new_list(numbers_list):
    if numbers_list == [1, 1]:
        return [1, 2]

    new_numbers_list = [1]
    len_list = len(numbers_list)

    for index_list in range(len_list - 1):
        index_list_plus = numbers_list[index_list + 1]
        new_numbers_list.extend([numbers_list[index_list] + index_list_plus, index_list_plus])
        '''print(f'index_list = {index_list}, '
              f'numbers_list[{index_list}] = {numbers_list[index_list]} '
              f'numbers_list[{index_list + 1}] = {index_list_plus} '
              f'new_numbers_list = {new_numbers_list}')'''
    return new_numbers_list


def cycle(n_cycle):
    n1 = '11'
    for _ in range(n_cycle - 1):
        n1 = func_new_string(n1)
    return n1


def cycle_list(l_cycle):
    n_l = [1, 1]
    for _ in range(l_cycle - 1):
        n_l = func_new_list(n_l)
    return n_l


def recursion(n_recursion, string_for_insert):
    if n_recursion == 1:
        return string_for_insert
    n_recursion -= 1
    string_for_insert = func_new_string(string_for_insert)
    return recursion(n_recursion, string_for_insert)


def recursion_list(l_recursion, list_for_insert):
    if l_recursion == 1:
        return list_for_insert

    list_for_insert = func_new_list(list_for_insert)
    l_recursion -= 1
    return recursion_list(l_recursion, list_for_insert)


def count_n(n_count):
    #return cycle(n_count).count(str(n_count))
    return recursion(n_count, '11').count(str(n_count))


def count_l(l_count):
    if l_count == 1:
        return 2
    return 2 * recursion_list(l_count, [1, 1]).count(l_count)


if __name__ == '__main__':
    s_data = '11'
    print(f'recursion   = {recursion(4, s_data)}')
    data = '13231'
    print(f'func        = {func_new_string(data)}')
    print(f'cycle       = {cycle(4)}')
    x = int(input('Input number: '))
    print(count_l(x))
