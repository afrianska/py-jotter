# O(2^n) - EXPONENTIAL
def fibonacci_recursive(n):
    """
    Naive recursive fibonacci - exponential time.
    Each call branches into 2 more calls.
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def generate_subsets(arr):
    """
    Generate all possible subsets - exponential time.
    For n elements, there are 2^n subsets.
    """
    if not arr:
        return [[]]

    first = arr[0]
    rest_subsets = generate_subsets(arr[1:])

    # Each subset from rest can either include or exclude first element
    new_subsets = []
    for subset in rest_subsets:
        new_subsets.append(subset)  # Without first element
        new_subsets.append([first] + subset)  # With first element

    return new_subsets


print("O(2^n) - EXPONENTIAL:")
print(f"Fibonacci(10): {fibonacci_recursive(10)}")
print(f"Subsets of [1,2,3]: {generate_subsets([1, 2, 3])}")
print("→ Each step roughly doubles the work\n")
