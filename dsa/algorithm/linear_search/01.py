print("1st")
def linear_search(l, x):
    n = len(l)
    i = 0
    while i < n:
        if l[i] == x:
            return i
        i += 1
    i = -1
    return i
l = [1, 5, 6, 9, 7, 8, 100]
x = 2
result = linear_search(l, x)
print(result)

print()
print("2nd")

def linear_search(l,x):
    n = len(l)
    for i in range(n):
        if l[i] == x:
            return i
    
    return -1

l = [1, 5, 6, 9, 7, 8, 100]
x = 1
result = linear_search(l,x)
print(result)