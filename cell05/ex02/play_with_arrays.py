#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [new_array + 2 for new_array in array if new_array > 5]

print(array)
print(new_array)