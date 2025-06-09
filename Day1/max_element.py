# 1. Using max() with key=len

data = ["apple", "banana", "kiwi", "watermelon"]
longest = max(data, key=len)
print(longest)               # Output: watermelon
print(len(longest))          # Output: 10
# 2. Using map(len, ...) + max()

data = ["apple", "banana", "kiwi", "watermelon"]
max_length = max(map(len, data))
print(max_length)            # Output: 10
#  3. Using a for loop (Manual way)

data = ["apple", "banana", "kiwi", "watermelon"]
max_len = 0
for item in data:
    if len(item) > max_len:
        max_len = len(item)

print(max_len)               # Output: 10
# 4. Using List Comprehension + max()
 
data = ["apple", "banana", "kiwi", "watermelon"]
max_len = max([len(word) for word in data])
print(max_len)               # Output: 10
# 5. Using reduce() from functools
 
from functools import reduce

data = ["apple", "banana", "kiwi", "watermelon"]
max_len = reduce(lambda acc, x: max(acc, len(x)), data, 0)
print(max_len)               # Output: 10
# 6. With Enumerate (to get index of max length)
 
data = ["apple", "banana", "kiwi", "watermelon"]
max_len = 0
index = -1
for i, word in enumerate(data):
    if len(word) > max_len:
        max_len = len(word)
        index = i

print(f"Max length: {max_len}, at index {index}")  # Output: Max length: 10, at index 3
# 7. If Nested Lists – Find Longest Inner List
 
lists = [[1, 2], [3, 4, 5, 6], [7]]
max_len_list = max(lists, key=len)
print(max_len_list)          # Output: [3, 4, 5, 6]
print(len(max_len_list))     # Output: 4
# 8. Using numpy for numeric arrays
 
import numpy as np

arr = np.array([[1, 2, 3], [4, 5], [6]])
lengths = [len(row) for row in arr]
print(max(lengths))          # Output: 3
# 9. Using pandas Series
 
import pandas as pd

data = pd.Series(["apple", "banana", "kiwi", "watermelon"])
max_len = data.str.len().max()
print(max_len)               # Output: 10
# 10. With Dictionary – Find Key/Value with Max Length
 
data = {"a": "apple", "b": "banana", "c": "kiwi"}
max_key = max(data, key=lambda k: len(data[k]))
print(data[max_key])         # Output: banana
print(len(data[max_key]))    # Output: 6