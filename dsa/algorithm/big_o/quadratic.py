# O(n²) - QUADRATIC
def bubble_sort(arr):
    """
    Bubble sort - for each element, we compare with all others.
    Nested loops = quadratic time.
    """
    arr = arr.copy()  # Don't modify original
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def find_all_pairs(arr):
    """
    Another quadratic example - finding all pairs in array.
    """
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pairs.append((arr[i], arr[j]))
    return pairs


# Test data
unsorted_arr = [64, 34, 25, 12, 22, 11, 90]

print("O(n²) - QUADRATIC:")
print(f"Bubble sort: {bubble_sort(unsorted_arr)}")
print(f"All pairs: {find_all_pairs([1, 2, 3, 4])}")
print("→ Nested loops, each element compared with others\n")
