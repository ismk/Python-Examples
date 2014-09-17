pyg = 'ay'

original = input('Enter a word:')

word = original.lower()
n = len(word)
first = word[0]
new_word = word+pyg

if len(original) > 0 and original.isalpha():
    
    if first in ["a" , "e" , "i" , "o" , "u"]:
        print (new_word)
    else:
        first_letter = word[0]
        new_word = word[1:n]
        new_word = new_word+first_letter+pyg
        print (new_word)
    
else:
    print ('empty')
    
