nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6] 
n = 3

if m != 0 and n !=0:
    res = [0]*(m+n)
    for i in range(len(res)):
        if nums1[i] < nums2[i]:
            res.append(nums1[i])

