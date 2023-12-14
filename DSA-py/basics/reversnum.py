def reverseNum(n: int) -> int:
    # 1
    # num = ''
    # while n > 0:
    #     num+=str(n%10)
    #     n=n//10
    # return int(num)
    
    # 2
    # str_num = str(n)[::-1]
    # return int(str_num)

    # 3
    # num = 0
    # while n > 0:
    #     lent = len(str(n))
    #     num+= n%10 * pow(10, lent-1)
    #     n=n//10
    # return num

    # 4
    num = 0
    while n > 0:
        num= num*10 +n%10
        n=n//10
    return num


assert reverseNum(121) == 121
assert reverseNum(1011) == 1101
assert reverseNum(12) == 21
assert reverseNum(10) == 1