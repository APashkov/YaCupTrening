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


def cycle(nn):
    a = '11'
    for _ in range(nn - 1):
        a = func_new_string(a)
    return a


def recursion(n, aa):
    if n == 1:
        return aa
    n -= 1
    aa = func_new_string(aa)
    return recursion(n, aa)


def count_n(nnn):
    qqq = recursion(nnn, '11')
    count = qqq.count(str(nnn))
    return count


if __name__ == '__main__':
    s_data = '11'
    #print(f'recursion   = {recursion(4, s_data)}')
    #data = '13231'
    #print(f'func = {func_new_string(data)}')
    #print(f'aaa         = {aaa(4)}')
    print(f'count_n     = {count_n(20)}')