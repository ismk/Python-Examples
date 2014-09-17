def array_count9(nums):
	count = 0
	for i in nums:
		if i == 9:
			count +=1
	return count


print (array_count9([1,2,3,4,5,6,9,9,9,9,9]))s