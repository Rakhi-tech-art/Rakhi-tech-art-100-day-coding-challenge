# 1. Using String Slicing (Most Common & Pythonic)

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True
#  2. Using reversed() and join()

def is_palindrome(s):
    return s == ''.join(reversed(s))
print(is_palindrome("racecar"))  # True

# 3. Using a for loop
def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

print(is_palindrome("level"))  # True
# 4  Using Recursion

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("radar"))  # True
# 5  Using while loop with two pointers

def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("noon"))  # True
# 6. Using Stack (List as Stack)

def is_palindrome(s):
    stack = list(s)
    for char in s:
        if char != stack.pop():
            return False
    return True

print(is_palindrome("madam"))  # True
#  7. Using deque (Double-ended Queue) from collections
from collections import deque

def is_palindrome(s):
    d = deque(s)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

print(is_palindrome("civic"))  # True
# 8. Ignoring Case and Non-Alphanumeric Characters

import re

def is_palindrome(s):
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal, Panama"))  # True
# 9. Check Palindrome for Integer (as number)

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

print(is_palindrome_number(121))  # True
# 10. Without Converting Number to String

def is_palindrome_number(n):
    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return original == reversed_num

print(is_palindrome_number(12321))  # True