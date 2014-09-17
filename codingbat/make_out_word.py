def make_out_word(out, word):
	halfout = int(len(out)/2)
	return out[:halfout] + word + out[halfout:]


print (make_out_word('<<>>', 'Yay'))
print (make_out_word('<<>>', 'WooHoo'))
print (make_out_word('[[]]', 'word'))