def array123(nums):

	one = 1
	two = 2
	three = 3

	if (one and two and three) in nums:
		return (True)
	else:
		return (False)



def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False