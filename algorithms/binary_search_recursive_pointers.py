def binary_search_pointers(sorted_list, left_pointer, right_pointer, target):
    # this condition indicates the search has reached an empty sublist
    if left_pointer >= right_pointer:
        return "Value Not Found."

    # Calculate the middle index from the pointers now
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx
    if mid_val > target:  # we reduce sub-list by passing in a new right pointer
        return binary_search_pointers(sorted_list, left_pointer, mid_idx, target)
    if mid_val < target:  # we reduce sub-list by passsing in a new left pointer
        return binary_search_pointers(sorted_list, mid_idx + 1, right_pointer, target)
