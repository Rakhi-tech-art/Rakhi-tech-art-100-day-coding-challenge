# 1 Using set() (Unordered)

my_list = [1, 2, 2, 3, 1]
unique = list(set(my_list))
print(unique)  # Output: [1, 2, 3] — order not guaranteed


# 2. Using dict.fromkeys() (Preserves Order in Python 3.7+)

my_list = [1, 2, 2, 3, 1]
unique = list(dict.fromkeys(my_list))
print(unique)  # Output: [1, 2, 3]

# 3 Using a Loop + set() (Manual Preserving Order)

def remove_duplicates(seq):
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

my_list = [1, 2, 2, 3, 1]
print(remove_duplicates(my_list))  # Output: [1, 2, 3]

#  4. Using List Comprehension + not in (Preserve Order)

my_list = [1, 2, 2, 3, 1]
unique = []
[unique.append(x) for x in my_list if x not in unique]
print(unique)  # Output: [1, 2, 3]

# 5. Using pandas.Series.drop_duplicates()

import pandas as pd

my_list = [1, 2, 2, 3, 1]
unique = pd.Series(my_list).drop_duplicates().tolist()
print(unique)  # Output: [1, 2, 3]

# 6. Using collections.OrderedDict (Older Python versions < 3.7)

from collections import OrderedDict

my_list = [1, 2, 2, 3, 1]
unique = list(OrderedDict.fromkeys(my_list))
print(unique)  # Output: [1, 2, 3]


# 7. Using numpy.unique() (For numeric data)

import numpy as np

my_list = [1, 2, 2, 3, 1]
unique = np.unique(my_list).tolist()
print(unique)  # Output: [1, 2, 3]


# 8. Using a for loop with count() check

my_list = [1, 2, 2, 3, 1]
unique = []
for i in my_list:
    if i not in unique:
        unique.append(i)
print(unique)  # Output: [1, 2, 3]



# 9. Using set + Sorting (Not order preserving of original list)
 
my_list = [3, 1, 2, 2, 1]
unique = sorted(set(my_list))
print(unique)  # Output: [1, 2, 3]

# 10. Using Recursion (For fun, not recommended for large lists)
 
def remove_duplicates(lst, seen=None):
    if seen is None:
        seen = []
    if not lst:
        return []
    if lst[0] in seen:
        return remove_duplicates(lst[1:], seen)
    else:
        return [lst[0]] + remove_duplicates(lst[1:], seen + [lst[0]])

print(remove_duplicates([1, 2, 2, 3, 1]))  # Output: [1, 2, 3]



