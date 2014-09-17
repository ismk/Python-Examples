def sum2(nums):
	if len(nums) > 1:
		n = nums[0] + nums[1]
		return n
	elif nums == []:
		return 0
	else:
		return nums[0]


print (sum2([1, 2, 3]))
print (sum2([1, 1]))
print (sum2([1, 1, 1, 1]))