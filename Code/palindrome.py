def is_palindrome(number):
    return str(number) == str(number)[::-1]


number = 121
print(is_palindrome(number))