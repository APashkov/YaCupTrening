import string
import factor_of_palindromes as p

alphabet = string.ascii_lowercase
print(200000/26)
data = (200*alphabet)
print(len(data))
p.write_file(file='input.txt', min_palindrome=data)