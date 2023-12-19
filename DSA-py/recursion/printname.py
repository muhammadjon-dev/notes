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
    
# printtoN(5)

def printItoN(i: int, n: int):
    if i > n:
        return
    print(i)
    i+=1
    printItoN(n)
    
# printItoN(1, 5)

def printNto1(n: int):
    if 0 >= n:
        return
    print(n)
    n-=1
    printNto1(n)
    
# printNto1(5)

sums = 0
def sumNto1(n: int):
    if 0 >= n:
        return
    global sums
    sums+=n
    n-=1
    sumNto1(n)
# sumNto1(5)


