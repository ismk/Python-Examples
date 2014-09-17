def make_ends(nums):
	newnums = [nums[0], nums[len(nums)-1]]
	return newnums


print (make_ends([1, 2, 3]))
print (make_ends([1, 2, 3, 4]))
print (make_ends([7, 4, 6, 2]))