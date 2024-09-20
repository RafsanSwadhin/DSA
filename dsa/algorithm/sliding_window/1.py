l = [1, 2, 3, 2, 7]

def f(l: list) -> int:
    result = anchor = 0
    for i in range(len(l)):
        if i > 0 and l[i-1] >= l[i]:
            anchor = i
        result = max(result, i - anchor + 1)
    return result  # Return the result instead of printing it

print(f(l))  # This will print the returned value
