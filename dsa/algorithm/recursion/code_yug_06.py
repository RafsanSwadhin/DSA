def power(n,p):
    if p == 0:
        return 1
    return 2*power(n,p-1)
print(power(2,3))