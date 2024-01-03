# facts = 1
def factor(n, facts):
    if n == 1:
        print(facts)
        return
    
    factor(n-1, facts*n)
    
def factor1(n):
    if n == 1:
        return 1
    
    return n * factor1(n-1)

    
print(factor1(5))