def small(*nums):
    small_num=nums[0]
    for i in range(1,len(nums)):
        if nums[i]<small_num:
            small_num=nums[i]
    return small_num
res=small(10,30,50,90,40)
print(res)

