def array_front9(nums):
	for i in nums:
		if nums.index(i) <= 3:
			if i == 9:
				return True
	return False


print ( array_front9([1,9,3,4,5,6,7]))


