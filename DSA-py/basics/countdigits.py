import math 
def countDigits(n: int) -> int:
    # 1
    # lenth = len(str(n))
    
    # 2
    # lenth = 0
    
    # while n>0:
    #     n=n//10
    #     lenth+=1
    
    # 3
    lenth = int(math.log10(n)+1)

    return lenth

assert countDigits(121) == 3
assert countDigits(1011) == 4
assert countDigits(12) == 2
