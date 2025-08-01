import math

from a_constant import constant_example
from b_logarithmic import binary_search
from c_linear import linear_search
from c_linear import find_max
from d_log_linear import merge_sort
from e_quadratic import bubble_sort
from e_quadratic import find_all_pairs
from f_cubic import matrix_multiply_naive
from f_cubic import find_triplets_sum
from g_exponential import fibonacci_recursive
from g_exponential import generate_subsets


def demonstrate_complexities():
    """
    Demonstrates each time complexity with examples.
    """
    print("=== TIME COMPLEXITY EXAMPLES ===\n")

    # Test data
    small_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    unsorted_arr = [64, 34, 25, 12, 22, 11, 90]

    print("1. O(1) - CONSTANT:")
    print(f"   First element: {constant_example(small_arr)}")
    print("   → Always same time regardless of array size\n")

    print("2. O(log n) - LOGARITHMIC:")
    print(f"   Binary search for 7: index {binary_search(small_arr, 7)}")
    print("   → Eliminates half the elements each step\n")

    print("3. O(n) - LINEAR:")
    print(f"   Linear search for 7: index {linear_search(small_arr, 7)}")
    print(f"   Max element: {find_max(unsorted_arr)}")
    print("   → May need to check every element\n")

    print("4. O(n log n) - LOG LINEAR:")
    print(f"   Merge sort: {merge_sort(unsorted_arr)}")
    print("   → Divide array log n times, merge n elements each time\n")

    print("5. O(n²) - QUADRATIC:")
    print(f"   Bubble sort: {bubble_sort(unsorted_arr)}")
    print(f"   All pairs: {find_all_pairs([1, 2, 3, 4])}")
    print("   → Nested loops, each element compared with others\n")

    print("6. O(n³) - CUBIC:")
    # Small matrices for demo
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print("   Matrix multiplication:")
    print(f"   A × B = {matrix_multiply_naive(A, B)}")
    print(f"   Triplets summing to 6: {find_triplets_sum([1, 2, 3, 4, 5], 6)}")
    print("   → Three nested loops\n")

    print("7. O(2^n) - EXPONENTIAL:")
    print(f"   Fibonacci(10): {fibonacci_recursive(10)}")
    print(f"   Subsets of [1,2,3]: {generate_subsets([1, 2, 3])}")
    print("   → Each step roughly doubles the work\n")

    print("=== GROWTH COMPARISON ===")
    print("Input Size | O(1) | O(log n) | O(n) | O(n log n) | O(n²) | O(n³) | O(2^n)")
    print("-----------|------|----------|------|------------|-------|-------|--------")
    for n in [1, 10, 100, 1000]:
        log_n = math.log2(n) if n > 0 else 0
        n_log_n = n * log_n
        print(
            f"{n:10} | {1:4} | {log_n:8.1f} | {n:4} | {n_log_n:10.0f} | {n**2:5} | {n**3:7} | {'∞' if n > 20 else 2**n}"
        )


if __name__ == "__main__":
    demonstrate_complexities()
