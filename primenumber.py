def big(*nums):
    big_num=nums[0]
    for i in range(1,len(nums)):
        if nums[i]>big_num:
            big_num=nums[i]
    return big_num
res=big(10,30,50,90,40)
print(res)

