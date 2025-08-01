# O(n) - LINEAR
def linear_search(arr, target):
    """
    We might need to check every element once.
    Time grows proportionally with input size.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def find_max(arr):
    """
    Another linear example - finding maximum element.
    Must check each element once.
    """
    if not arr:
        return None

    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val


# Test data
small_arr = [1, 3, 5, 7, 9, 11, 13, 15]
unsorted_arr = [64, 34, 25, 12, 22, 11, 90]

print("O(n) - LINEAR:")
print(f"Linear search for 7: index {linear_search(small_arr, 7)}")
print(f"Max element: {find_max(unsorted_arr)}")
print("→ May need to check every element\n")
