def highestfreq(nums):
    nums_dict = {}
    for i in nums:
        if i in nums_dict:
            nums_dict[i]+=1
        else:
            nums_dict[i]=1
    sorted_dict = sorted(nums_dict.items(), key=lambda item: item[1])
    print(f"lowest: {sorted_dict[0][0]}")
    print(f"highest: {sorted_dict[-1][0]}")
    
highestfreq([10,5,10,15,10,5])
        
    