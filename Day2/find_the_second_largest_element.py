# Sample array
arr = [12, 45, 1, -1, 45, 54, 23, 54]

# Method 1: Manual Scan
def second_largest_manual(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second

# Method 2: Sorting
def second_largest_sort(arr):
    unique_sorted = sorted(set(arr))
    return unique_sorted[-2] if len(unique_sorted) >= 2 else None

# Method 3: Set and Remove Max
def second_largest_set_remove(arr):
    s = set(arr)
    s.remove(max(s))
    return max(s)

# Method 4: Using heapq
import heapq
def second_largest_heap(arr):
    return heapq.nlargest(2, set(arr))[1] if len(set(arr)) >= 2 else None

# Method 5: Remove max and find max again
def second_largest_twice_max(arr):
    max_val = max(arr)
    arr_copy = [x for x in arr if x != max_val]
    return max(arr_copy) if arr_copy else None

# Test with array
print("Manual:", second_largest_manual(arr))
print("Sort:", second_largest_sort(arr))
print("Set Remove Max:", second_largest_set_remove(arr))
print("Heap:", second_largest_heap(arr))
print("Twice Max:", second_largest_twice_max(arr))
