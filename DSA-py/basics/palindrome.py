def palindrome(n: int) -> bool:
    # 1
    # return str(n) == str(n)[::-1]

    # 2
    num = str(n)
    start = 0
    end = len(num)-1
    while start <= end:
        if num[start] != num[end]:
            return False
        start+=1
        end-=1
    return True

    
    
assert palindrome(121) == True
assert palindrome(-121) == False
assert palindrome(7) == True