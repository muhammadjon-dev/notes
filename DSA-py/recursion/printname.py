def printname(n: int):
    if n == 0:
        return
    print("Muhammadjon", n)
    n-=1
    printname(n)
    
# printname(5)

x=1
def printtoN(n: int):
    global x
    if x > n:
        return
    print(x)
    x+=1
    printtoN(n)
    
printtoN(5)

def printItoN(i: int, n: int):
    if x > n:
        return
    print(i)
    i+=1
    printtoN(n)
    
printItoN(1, 5)