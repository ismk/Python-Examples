def caught_speeding(speed, is_birthday):
	if is_birthday:
		speed -= 5

	if speed <= 60:
		return 0
	elif speed <=80:
		return 1
	elif speed >= 81:
		return 2


print (caught_speeding(78,1))