def common_end(a, b):
	return ((len(a) or len(b) > 1) and a[0] == b[0] or a[len(a)-1] == b[len(b)-1])



print (common_end([1, 2, 3], [7, 3]))
print (common_end([1, 2, 3], [7, 3, 2]))
print (common_end([1, 2, 3], [1, 3]))