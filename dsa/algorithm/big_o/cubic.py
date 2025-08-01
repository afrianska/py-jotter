# O(n³) - CUBIC
def matrix_multiply_naive(A, B):
    """
    Naive matrix multiplication - three nested loops.
    For n×n matrices, this is O(n³).
    """
    n = len(A)
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


def find_triplets_sum(arr, target):
    """
    Finding all triplets that sum to target.
    Three nested loops = cubic time.
    """
    triplets = []
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    triplets.append((arr[i], arr[j], arr[k]))

    return triplets


print("O(n³) - CUBIC:")
# Small matrices for demo
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("Matrix multiplication:")
print(f"A × B = {matrix_multiply_naive(A, B)}")
print(f"Triplets summing to 6: {find_triplets_sum([1, 2, 3, 4, 5], 6)}")
print("→ Three nested loops\n")
