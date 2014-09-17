# def xyz_there(str):
# 	print (str.count("xyz"))
# 	if "xyz" in str:
# 		if ".xyz" in str:
# 			return False
# 		return True
# 	return False


def xyz_there(str):
	for i in range(len(str)-2):
		print (str[i:2])

print(xyz_there('abc.xyzxyz'))