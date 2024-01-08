def countnums(nums: list):
    nums_dict = {}
    for i in nums:
        if i in nums_dict:
            nums_dict[i]+=1
        else:
            nums_dict[i]=1
    for k, v in nums_dict.items():
        print(f"{k} -> {v}")
    
countnums([10,5,10,15,10,5])