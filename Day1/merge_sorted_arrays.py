# 1. Using Two-Pointer Technique (Efficient & Recommended)

def merge_sorted(arr1, arr2):
    result = []
    i = j = 0

    # Merge both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

print(merge_sorted([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
# 2. Using sorted() + Concatenation (Simplest)

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merged = sorted(arr1 + arr2)

print(merged)  # Output: [1, 2, 3, 4, 5, 6]
# 3. Using heapq.merge() (Best for Iterators / Big Data)

import heapq

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merged = list(heapq.merge(arr1, arr2))
print(merged)  # Output: [1, 2, 3, 4, 5, 6]
# 4. Recursive Method (Not recommended for large arrays)

def merge_recursive(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge_recursive(a[1:], b)
    else:
        return [b[0]] + merge_recursive(a, b[1:])

print(merge_recursive([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
# 5. Using NumPy (if working with arrays)
 
import numpy as np

arr1 = np.array([1, 3, 5])
arr2 = np.array([2, 4, 6])
merged = np.sort(np.concatenate((arr1, arr2)))
print(merged.tolist())  # Output: [1, 2, 3, 4, 5, 6]
