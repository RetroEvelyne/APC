nums = [0,1,0,3,12]

nums2 = [num for num in nums if num != 0] + ([0]*nums.count(0))

print(nums2)
