def reverse_string(string):
    '''print(f'reverse_string, string = {string}')
    print(f'reverse_string, reversed_string = {string[::-1]}')'''
    return string[::-1]

def check_palindrome(string):
    reverse = reverse_string(string)
    palindrome = (string == reverse)
    '''print(f'check_palindrome, string = {string}')
    print(f'check_palindrome, reverse_string = {reverse}')
    print(f'check_palindrome, palindrome = {palindrome}')'''
    return palindrome

def find_palindrome(string):
    len_string = len(string)

    for l in range(2,len_string + 1):
        #print(l)

        list_palindromes = list()
        for i in range(0,len_string - l + 1):
            sub_string = string[i:i+l]
            #print(sub_string)
            if check_palindrome(sub_string):
                list_palindromes.append(sub_string)
                '''min_palindrome = sub_string
                break'''

        if list_palindromes:
            min_palindrome = min(list_palindromes)
            '''print(f'list_palindromes = {list_palindromes}')
            print(f'min_palindrome = {min_palindrome}')'''
            break

    return min_palindrome

if __name__ == '__main__':
    '''reverse_string(('abc'))
    check_palindrome('123')
    check_palindrome('121')'''
    result = find_palindrome('abcbab')
    print(f'find_palindrome = {result}')
