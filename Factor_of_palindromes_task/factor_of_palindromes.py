def read_file(file='input.txt'):
    with open(file) as input_file:
        string = input_file.readline()
    return string


def write_file(min_palindrome, file='output.txt'):
    with open(file, 'w') as output_file:
        output_file.write(min_palindrome)
    return


def check_palindrome(string):
    return string == string[::-1]


def find_palindrome(string):
    len_string = len(string) + 1

    for len_sub_string in range(2, 4):

        list_palindromes = list()
        for begin_sub_string in range(0, len_string - len_sub_string):
            sub_string = string[begin_sub_string:begin_sub_string + len_sub_string]

            if check_palindrome(sub_string):
                list_palindromes.append(sub_string)

        if list_palindromes:
            min_palindrome = min(list_palindromes)
            break
        else:
            min_palindrome = '-1'

    return min_palindrome


if __name__ == '__main__':
    write_file(find_palindrome(read_file()))
