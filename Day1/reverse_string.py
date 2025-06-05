# In Python, there are multiple ways to reverse a string. Here are the most commonly used 7 methods:

# 1. Using Slicing
s = "hello"
reversed_s = s[::-1]
print(reversed_s)  # Output: 'olleh'

# 2. Using reversed() and join()
s = "hello"
reversed_s = ''.join(reversed(s))
print(reversed_s)  # Output: 'olleh'

# 3. Using a for Loop
s = "hello"
reversed_s = ''
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)  # Output: 'olleh'


# 4. Using a while Loop
s = "hello"
i = len(s) - 1
reversed_s = ''
while i >= 0:
    reversed_s += s[i]
    i -= 1
print(reversed_s)  # Output: 'olleh'

# 5. Using Recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # Output: 'olleh'

# 6. Using Stack (List as Stack)
s = "hello"
stack = list(s)
reversed_s = ''
while stack:
    reversed_s += stack.pop()
print(reversed_s)  # Output: 'olleh'


# 7. Using List Comprehension and join()
s = "hello"
reversed_s = ''.join([s[i] for i in range(len(s)-1, -1, -1)])
print(reversed_s)  # Output: 'olleh'


