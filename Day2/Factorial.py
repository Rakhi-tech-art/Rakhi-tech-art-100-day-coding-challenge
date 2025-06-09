# Method 1: Iterative Method
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Method 2: Recursive Method
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Method 3: One-liner using lambda (recursive)
factorial_lambda = lambda n: 1 if n == 0 else n * factorial_lambda(n - 1)

# Method 4: Using math library
import math
def factorial_math(n):
    return math.factorial(n)

# Method 5: Using Memoization (Dynamic Programming)
memo = {}
def factorial_memo(n):
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 1
    else:
        memo[n] = n * factorial_memo(n - 1)
    return memo[n]

# Test all methods with n = 5
n = 5
print("Iterative:", factorial_iterative(n))
print("Recursive:", factorial_recursive(n))
print("Lambda One-liner:", factorial_lambda(n))
print("Math Library:", factorial_math(n))
print("Memoization:", factorial_memo(n))
