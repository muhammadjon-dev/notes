x=0
nums = []
def printNums(n: int):
    global x
    x+=1
    nums.append(x)
    if x >= n:
        return 
    printNums(n)
    return nums
    
  
print(printNums(4))
    
