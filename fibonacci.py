def fibonacci(n):
    import array
    arr=[]
    a,b=0,1
    sum=0
    while (n>0):
        arr.append(a)
        a,b=b,a+b
        n-=1
    return arr
no=int(input("enter the value of n for the fibonacci series:"))
a=fibonacci(no)
print(a)
