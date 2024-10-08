# number of digits in a given number
def count_of(n):
    if n < 10:
        return 1
    return 1 + count_of(n//10)
print(count_of(5465461))

