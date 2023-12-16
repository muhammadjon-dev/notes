def alldivisors(n: int):
    return [k for k in range(1, n+1) if n%k==0]

assert alldivisors(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]
assert alldivisors(97) == [1, 97]

import math

def checkPerfectNumber(num: int) -> bool:
        return sum([k for k in range(1, int(math.sqrt(num))) if num%k==0])
    
print(checkPerfectNumber(28))
num=28
print([k for k in range(1, int(math.sqrt(num))) if num%k==0])