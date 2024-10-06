def twosum(a,target):
    i = 0
    j = len(a)-1
    while i < j:
        sm = a[i]+a[j]
        if sm == target:
            print(a[i],a[j])
            print(i,j)
            return True
        elif sm < target:
            i = i + 1
        else:
            j = j-1
    return False
t = int(input())
for i in range(t):
    a = list(map(int,input().split()))
    target = int(input())
    print(a)
    print(twosum(a,target))