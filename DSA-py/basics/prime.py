def prime_num(n :int) -> bool:
    if n == 1: return False
    return len([i for i in range(1, int(n**(1/2))+1) if n%i==0])==1

assert prime_num(3) == True
assert prime_num(29) == True
assert prime_num(31) == True
assert prime_num(8) == False
assert prime_num(25) == False
assert prime_num(1) == False