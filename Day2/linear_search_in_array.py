# Sample array
arr = [10, 20, 30, 20, 40, 20, 50]
target = 20

# Variant 1: Basic Linear Search (returns True if found)
def linear_search_basic(arr, target):
    for item in arr:
        if item == target:
            return True
    return False

# Variant 2: Return index of first occurrence
def linear_search_index(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

# Variant 3: Return all indices of target
def linear_search_all_indices(arr, target):
    indices = []
    for i, item in enumerate(arr):
        if item == target:
            indices.append(i)
    return indices

# Variant 4: Return boolean (True/False) if target found
def linear_search_boolean(arr, target):
    return target in arr

# Variant 5: Recursive linear search (returns index or -1)
def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return linear_search_recursive(arr, target, index + 1)

# Variant 6: Return count of occurrences
def linear_search_count(arr, target):
    count = 0
    for item in arr:
        if item == target:
            count += 1
    return count

# Variant 7: Return True if target exists more than once
def linear_search_multiple(arr, target):
    count = 0
    for item in arr:
        if item == target:
            count += 1
            if count > 1:
                return True
    return False

# Variant 8: Return indices where target does not exist (all other indices)
def linear_search_not_target(arr, target):
    return [i for i, item in enumerate(arr) if item != target]

# Testing all variants
print("Basic:", linear_search_basic(arr, target))
print("First Index:", linear_search_index(arr, target))
print("All Indices:", linear_search_all_indices(arr, target))
print("Boolean (in):", linear_search_boolean(arr, target))
print("Recursive Index:", linear_search_recursive(arr, target))
print("Count:", linear_search_count(arr, target))
print("Multiple Occurrences:", linear_search_multiple(arr, target))
print("Indices without target:", linear_search_not_target(arr, target))
