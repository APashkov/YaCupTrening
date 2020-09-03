def read_file():
    with open('input.txt') as input_file:
        string = input_file.readline()
    return string


def write_file(min_palindrome):
    with open('output.txt', 'w') as output_file:
        output_file.write(min_palindrome)
    return


def reverse_string(string):
    return string[::-1]


def check_palindrome(string):
    reverse = reverse_string(string)
    palindrome = (string == reverse)
    return palindrome


def find_palindrome(string):
    len_string = len(string) + 1

    for len_sub_string in range(2, len_string):

        list_palindromes = list()
        for begin_sub_string in range(0, len_string - len_sub_string):
            sub_string = string[begin_sub_string:begin_sub_string + len_sub_string]

            if check_palindrome(sub_string):
                list_palindromes.append(sub_string)

        if list_palindromes:
            min_palindrome = min(list_palindromes)
            break

    return min_palindrome


if __name__ == '__main__':
    write_file(find_palindrome(read_file()))
