def binary_search_iterative(arr_of_elem, target):
    low, high = 0, len(arr_of_elem) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr_of_elem[mid] == target:
            return mid
        elif arr_of_elem[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
