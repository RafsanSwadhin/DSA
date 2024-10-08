def sum_(n,result):
    if n == 0:
        return result
    result +=n
    return sum_(n-1,result)
    
print(sum_(10,result=0))