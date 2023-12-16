def gcd(a :int, b :int) -> int:
    # nums = [i for i in range(1, min(a,b)+1) if a%i==0 and b%i==0]
    # return max(nums)
    a, b = max(a, b), min(a, b)
    
    while a%b:
        a, b = b, a%b
    return b


    
    

assert gcd(4, 8) == 4 
assert gcd(4, 4) == 4 
assert gcd(3, 6) == 3 
assert gcd(4, 6) == 2 