def fibnums(n, k=-1, m=1):
    if n<0:
        return
    print(k+m, end=" ")
    fibnums(n-1, m, k+m)
    
    
# fibnums(5)

def fibnum(n):
    if n<=1:
        return n
    return fibnum(n-1)+fibnum(n-2)

print(fibnum(5))