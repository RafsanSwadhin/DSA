l = [1, 3, 2, 5, 7, 2, 4, 6]
k = 3

# Step 1: Calculate the sum of the first window
window_sum = sum(l[:k])
max_sum = window_sum

# Step 2: Slide the window across the list
for i in range(k, len(l)):
    window_sum += l[i] - l[i - k]  # Slide the window
    max_sum = max(max_sum, window_sum)

print(max_sum)  # Output will be 16 (from the subarray [7, 2, 4])