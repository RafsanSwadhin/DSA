def binary(array,target):
    left,right = 0,len(array)-1

    while left <= right:
        mid = (left+right)//2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid+1

        else:
            right = mid-1
    return -1

array = [10,20,30,40,50,60,70,80,90,100,110,120,130]
target = 120

print(binary(array,target))