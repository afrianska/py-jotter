# O(log n) - LOGARITHMIC
def binary_search(arr, target):
    """
    Binary search - we eliminate half the search space each time.
    Only works on sorted arrays.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found


# Test data
small_arr = [1, 3, 5, 7, 9, 11, 13, 15]

print("O(log n) - LOGARITHMIC:")
print(f"Binary search for 7: index {binary_search(small_arr, 7)}")
print("→ Eliminates half the elements each step\n")
