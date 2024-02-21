def selection_sort(L):
    n = len(L)
    # Traverse through all array elements
    for i in range(0, n):
        # Assume the current index is the minimum
        index_min = i
        # Check the rest of the array for a smaller element
        for j in range(i + 1, n):
            if L[j] < L[index_min]:
                index_min = j
        # Swap the found minimum element with the first element
        # (if the minimum element is not the current element)
        if index_min != i:
            L[i], L[index_min] = L[index_min], L[i]
# Example list
L = [6, 1, 4, 5, 9, 34, 655, 3]
# Apply selection sort to the list
selection_sort(L)
# Print the sorted list
print(L)

