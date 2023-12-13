def pat1(n: int):
    for i in range(n):
        for j in range(n):
            print('*', end='')
        print()
        
# pat1(6)

def pat2(n: int):
    for i in range(1, n+1):
        # for j in range(i):
        #     print('*', end='')
        # print()
        
        print(i*'*')

# pat2(5)

def pat3(n: int):
    for i in range(n):
        for j in range(i+1): 
            print(str(j+1), end='')
        print()

# pat3(6)

def pat4(n: int):
    for i in range(1, n+1):
        # for j in range(i): 
        #     print(str(i), end='')
        # print()
        
        print(str(i)*i)

# pat4(5)

def pat5(n: int):
    # for i in range(n, 0, -1):
    #     for j in range(i):
    #         print('*', end='')
    #     print()
    
    for i in range(n):
        print('*'*(n-i))
        

# pat5(5)

def pat6(n: int):
    # for i in range(n, 0, -1):
    #     for j in range(1, i+1):
    #         print(str(j), end='')
    #     print()

    for i in range(n):
        for j in range(1, n-i+1):
            print(str(j), end='')
        print()
        
# pat6(5)

def pat7(n: int):
    for i in range(n):
        spaces = n-i-1
        stars=2*i+1
        print(spaces*' ', end='')
        # for j in range(2*i+1):
        #     print('*', end='')
        print('*'*stars, end='')
        print(spaces*' ')

# pat7(5)

def pat8(n: int):
    for i in range(n, 0, -1):
        spaces = n-i
        stars=2*i-1
        print(spaces*' ', end='')
        # for j in range(2*i-1):
        #     print('*', end='')
        print('*'*stars, end='')
        print(spaces*' ')

# pat8(10)

def pat9(n: int):
    # for i in range(n):
    #     counts = n-i-1
    #     print(counts*' ', end='')
    #     for j in range(2*i+1):
            
    #         print('*', end='')
    #     print(counts*' ')    
    
    # for i in range(n, 0, -1):
    #     counts = n-i
    #     print(counts*' ', end='')
    #     for j in range(2*i-1):
            
    #         print('*', end='')
    #     print(counts*' ')
    pat7(n)
    pat8(n)

# pat9(3)

def pat10(n: int):
    for i in range(1, 2*n):
        stars = i
        if stars > 5:
            stars=n-i%n #2*n-i
        print('*'*stars)
        
# pat10(5)

def pat11(n: int):
    for i in range(n):
        for j in range(i+1):
            if (i + j)%2:
                print(0, end='')
            else:
                print(1, end='')
        print()

# pat11(5)
        
def pat12(n: int):
    for i in range(1, n+1):
        for j in range(i):
            print(j+1, end='')
            
        spaces = 2*n-2*i
        print(spaces*' ', end='')
        
        for j in range(i, 0, -1):
            print(j, end='')
        print()
# pat12(4)

def pat13(n: int):
    num=0
    for i in range(n):
        for j in range(i+1):
            num+=1
            print(num, end=' ')
        print()

# pat13(5)

def pat14(n: int):
    for i in range(n):
        num = 65
        for j in range(i+1):
            print(chr(num+j), end='')
        print()

# pat14(4)

def pat15(n: int):
    for i in range(n):
        num = 65
        for j in range(n-i):
            print(chr(num+j), end='')
        print()

# pat15(4)

def pat16(n: int):
    for i in range(n):
        num = 65
        for j in range(i+1):
            print(chr(num+i), end='')
        print()

# pat16(4)

def pat17(n: int):
    num = 65
    for i in range(n):
        print(' '*(n-i), end='')
        for k in range(i):
            print(chr(num+k), end='')
        print(chr(num+i), end='')
        for k in range(i-1, -1, -1):
            print(chr(num+k), end='')
        print(' '*(n-i), end='')
        print()
        

# pat17(5)

def pat18(n: int):
    num = 65
    for i in range(n):
        for j in range(n-i-1, n):
            print(chr(num+j), end=' ')
        print()

# pat18(5)

def pat19(n: int):
    for i in range(n):
        print('*'*(n-i), end='')
        print(2*i*' ', end='')
        print('*'*(n-i))
        
    for i in range(n-1, -1, -1):
        print('*'*(n-i), end='')
        print(2*i*' ', end='')
        print('*'*(n-i))

        
# pat19(5)

def pat20(n: int):
    for i in range(n-1, -1, -1):
        print('*'*(n-i), end='')
        print(2*i*' ', end='')
        print('*'*(n-i))

    for i in range(n):
        print('*'*(n-i), end='')
        print(2*i*' ', end='')
        print('*'*(n-i))
# pat20(5) 
    
def pat21(n: int):
    print('*'*n)
    for i in range(n-2):
        print('*', end='')
        print((n-2)*' ', end='')
        print('*')
    print('*'*n)

# pat21(4)

def pat22(n: int):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            left = j
            right = 2*n-2-j
            down = 2*n-2-i
            
            val = min(min(top, left), min(right, down))
            print(n-val, end='')
        print()

pat22(3)
