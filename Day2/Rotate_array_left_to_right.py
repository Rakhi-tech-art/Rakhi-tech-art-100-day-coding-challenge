from collections import deque
import numpy as np

arr = [1, 2, 3, 4, 5]

# Method 1: Left Rotation using slicing
def rotate_left_slice(arr, d):
    return arr[d:] + arr[:d]

# Method 2: Right Rotation using slicing
def rotate_right_slice(arr, d):
    return arr[-d:] + arr[:-d]

# Method 3: Manual Left Rotation
def rotate_left_manual(arr, d):
    arr_copy = arr[:]
    for _ in range(d):
        first = arr_copy.pop(0)
        arr_copy.append(first)
    return arr_copy

# Method 4: Manual Right Rotation
def rotate_right_manual(arr, d):
    arr_copy = arr[:]
    for _ in range(d):
        last = arr_copy.pop()
        arr_copy.insert(0, last)
    return arr_copy

# Method 5: Using deque (Left)
def rotate_left_deque(arr, d):
    dq = deque(arr)
    dq.rotate(-d)
    return list(dq)

# Method 6: Using deque (Right)
def rotate_right_deque(arr, d):
    dq = deque(arr)
    dq.rotate(d)
    return list(dq)

# Method 7: Using numpy (Left)
def rotate_left_numpy(arr, d):
    return np.roll(arr, -d).tolist()

# Method 8: Using numpy (Right)
def rotate_right_numpy(arr, d):
    return np.roll(arr, d).tolist()

# Testing with d = 2
d = 2
print("Left Slice:", rotate_left_slice(arr, d))
print("Right Slice:", rotate_right_slice(arr, d))
print("Left Manual:", rotate_left_manual(arr, d))
print("Right Manual:", rotate_right_manual(arr, d))
print("Left Deque:", rotate_left_deque(arr, d))
print("Right Deque:", rotate_right_deque(arr, d))
print("Left Numpy:", rotate_left_numpy(arr, d))
print("Right Numpy:", rotate_right_numpy(arr, d))
