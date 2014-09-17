def max_end3(nums):
	if nums[0] > nums[2]:
		n = [nums[0], nums[0], nums[0]]
		return n
	else:
		n = [nums[2], nums[2], nums[2]]
		return n


print (max_end3([1, 2, 3]))
print (max_end3([11, 5, 9]))
print (max_end3([2, 11, 3]))