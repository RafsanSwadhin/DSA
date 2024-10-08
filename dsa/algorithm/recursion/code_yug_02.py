#Basic type of recursion
# direct & indirect
#direct recursion
n= int(input("Enter a number:"))

def natural(n):
    if n == 0:
        return
    print(n)
    return natural(n-1)
    #natural(n-1)
    #print(n) #pritn will work at the end of execution[from python tutor]
natural(n)



#idirect recursion: a function calls another function which calls 
#the first function again
def num(n):
    if n <= 0:
        return 
    print(n,end =" ")
    num1(n-1)

def num1(n):
    print(n,end = " ")
    num(n-1)
num1(4)