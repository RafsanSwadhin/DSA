# Define the list and the subarray length
a = [8, 3, -11, 4, 5, -1, 0, 5, 3, 9, -6]
k = 5

# Calculate the sum of the first 'k' elements and initialize the best sum
cur = best = sum(a[:k])

# Iterate through the array, updating the current sum and the best sum
for r in range(k, len(a)):
    cur = cur + a[r] - a[r - k]  # Slide the window by adding and subtracting elements
    best = max(best, cur)  # Update the best sum if the current sum is larger

# Print the maximum sum of any subarray of length 'k'
print("Maximum sum of any subarray of length", k, "is:", best)
