def recursive_multiply(n, m):
    # Base case: if m is 0, the result is 0
    if m == 0:
        return 0
    # Recursive case: n + recursive_multiply(n, m-1)
    return n + recursive_multiply(n, m - 1)

# Example usage
result = recursive_multiply(4,3)
print(result)  # Output: 12

