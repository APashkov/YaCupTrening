def reverse_string(string):
    return string[::-1]

def check_palindrome(string):
    reverse = reverse_string(string)
    palindrome = (string == reverse)
    return palindrome

def find_palindrome(string):
    len_string = len(string)

    for l in range(2,len_string + 1):

        list_palindromes = list()
        for i in range(0,len_string - l + 1):
            sub_string = string[i:i+l]
            if check_palindrome(sub_string):
                list_palindromes.append(sub_string)

        if list_palindromes:
            min_palindrome = min(list_palindromes)
            break

    return min_palindrome

if __name__ == '__main__':
    result = find_palindrome('abcbab')
    print(f'find_palindrome = {result}')
