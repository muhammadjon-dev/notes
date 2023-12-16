def is_armstrong(n: int) -> bool:
    # 1
    # digits = list(str(n))
    # power = len(digits)
    # sum_n = sum([int(digit)**power for digit in digits])
    # return n == sum_n
    sum_n = 0
    m = n
    power = len(str(n))
    while n > 0:
        sum_n = sum_n +  (n%10)**power
        n = n//10
    return sum_n == m

assert is_armstrong(153) == True
assert is_armstrong(170) == False
assert is_armstrong(9) == True
assert is_armstrong(5) == True
assert is_armstrong(0) == True