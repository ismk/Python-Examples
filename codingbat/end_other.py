def end_other(a, b):
	a = a.lower()
	b = b.lower()
	if a[-len(b):] == b or b[-len(a):] == a:
		return True
	return False


print (end_other("incredbilelasanewism", "ism"))

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))