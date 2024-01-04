numm = []
def reversearr(nums: list) -> list:
    if not len(nums):
        return
    numm.append(nums[-1])
    del nums[-1]
    reversearr(nums)
    
def reverse1(nums: list, l, r) -> list:
    if l>=r:
        return
    nums[l], nums[r] = nums[r], nums[l]
    reverse1(nums, l+1, r-1)
reversearr([10,20,30])
lst = [10,20,30]
reverse1(lst, 0, 2)
print(lst)

