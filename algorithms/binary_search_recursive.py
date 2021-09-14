def binary_search(sorted_list, target):
    if not sorted_list:
        return "Value not found."
    mid_idx = len(sorted_list) // 2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
        return mid_idx
    if mid_val > target:
        left_half = sorted_list[:mid_idx]
        return binary_search(left_half, target)
    if mid_val < target:
        right_half = sorted_list[mid_idx + 1:]
        result = binary_search(right_half, target)

        if result == "Value not found.":
            return result
        else:
            return result + mid_idx + 1
    return result + mid_idx + 1


'''
sorted_values = [1, 4, 6, 9, 12, 25, 28, 29, 34, 36, 59, 77, 101, 112]
print(binary_search(sorted_values, 101))
'''
