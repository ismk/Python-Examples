from Tkinter import *
 
#### translating english to pig-Latin functiom
def pigTrans():
    eng_word = word.get()
    print(eng_word)
    ay_end = 'ay'
    vowels = ['a', 'e', 'i', 'o', 'u']
 
    for v in vowels: # Checking for vowels
        if eng_word[1] == v:
            sec_last = eng_word[0]
            changed_word = eng_word[1:]
            break    
        elif eng_word[1] != v:
            sec_last = eng_word[:2]
            changed_word = eng_word[2:]
        else:
            print ('something went wrong')
    pig_word = changed_word + sec_last + ay_end
    print(pig_word)
 
pig_win = Tk()
label_enterword = Label(pig_win,text='Enter a word')
label_enterword.pack()
 
word = StringVar()
entry_word = Entry(pig_win, textvariable=word)
entry_word.pack()
 
translate_button=Button(pig_win, command=lambda: pigTrans())
translate_button.pack()
 
mainloop()