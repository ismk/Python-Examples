def same_first_last(lst):
	if len(lst) >= 1:
		return lst[0] == lst[-1]
	else:
		return False


print (same_first_last([1, 2, 3]))
print (same_first_last([1, 2, 3, 1]))
print (same_first_last([1, 2, 1]))