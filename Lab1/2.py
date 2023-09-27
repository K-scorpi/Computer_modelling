n=int(input("How much chisel?:"))
s=int(input("S kakogo nachat?:"))
A=[]
def fib(n):
    i=2
    k=0
    global A
    A.append(s)
    A.append(s)
    while k<n-2:
        A.append(A[i-2]+A[i-1])
        k+=1
        i+=1
    print(A)    
    return fib
print (fib(n))