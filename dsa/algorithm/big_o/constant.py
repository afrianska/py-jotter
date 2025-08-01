# O(1) - CONSTANT
def constant_example(arr):
    """
    Always takes the same time regardless of input size.
    Just accessing the first element.
    """
    if arr:
        return arr[0]  # Always one operation
    return None


# Test data
small_arr = [1, 3, 5, 7, 9, 11, 13, 15]

print("O(1) - CONSTANT:")
print(f"First element: {constant_example(small_arr)}")
print("→ Always same time regardless of array size\n")
