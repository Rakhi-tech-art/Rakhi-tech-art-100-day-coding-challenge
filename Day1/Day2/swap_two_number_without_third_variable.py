# Method 1: Using Arithmetic Operators (+ and -)

# Method 1: Swap using addition and subtraction
a = 5
b = 3

a = a + b  # a becomes 8
b = a - b  # b becomes 5
a = a - b  # a becomes 3

print("a =", a)
print("b =", b)
# Method 2: Using XOR Bitwise Operator

# Method 2: Swap using XOR
a = 5
b = 3

a = a ^ b
b = a ^ b
a = a ^ b

print("a =", a)
print("b =", b)
# Method 3: Pythonic Way (Tuple Unpacking)

# Method 3: Swap using Python tuple unpacking
a = 5
b = 3

a, b = b, a

print("a =", a)
print("b =", b)