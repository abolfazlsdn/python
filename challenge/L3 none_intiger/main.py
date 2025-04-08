def remove_nonints(nums):
    int_nums=[]
    for num in nums:
        if type(num)== int:
            
            int_nums.append(num)
    
    return int_nums
