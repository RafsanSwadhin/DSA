def bubble_sort(L):
    n = len(L)
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
# Example list
L = [100, 55, 2, 1, 77, 5]
print("before",L)
# Call the bubble_sort function
bubble_sort(L)
# Print the sorted list
print(L)

