import sys
import sqlite3 as lite
import time

con = lite.connect("passwords.db")
cur = con.cursor()

cur.execute("CREATE TABLE if not EXISTS passwords(site VARCHAR(50), username VARCHAR(20), password VARCHAR(20));")

print ("\n***** Welcome to Passwords.py. *****\n\n")

choice = None

while choice == None:
	print ("What would you like to do?")
	print ("1.) Add new password.")
	print ("2.) Find existing password.")
	print ("3.) Update existing password.")
	print ("4.) View all passwords.")
	print ("5.) Quit.")
	choice = input("> ")

	if choice == "1":
		s = input("Which website to add? ")
		name = input("Username to add? ")
		passwd = input("Password to add? ")

		cur.execute("INSERT INTO passwords VALUES (?,?,?)", (s,name,passwd,))

		time.sleep(1)

		print ("\nUpdated.\n")

		choice = None

	elif choice == "2":
		s = input("Find info for which website? ")

		cur.execute("SELECT * FROM passwords WHERE site=?", (s,))

		while True:
	  
			row = cur.fetchone()
			
			if row == None:
				break
				
			print ("Website:  " + row[0], "\nUsername: " + row[1], "\nPassword: " + row[2] + "\n")

		choice = None

	elif choice == "3":
		s = input("Update info for which website? ")
		name = input("New username? ")
		passwd = input("New password? ")

		cur.execute("UPDATE passwords SET username=?, password=? WHERE site=?", (name, passwd, s,))

		time.sleep(1)
		print ("\nUpdated.\n")

		choice = None

	elif choice == "4":
		cur.execute("SELECT * FROM passwords")

		while True:
	  
			row = cur.fetchone()
			
			if row == None:
				break
				
			print ("Website:  " + row[0], "\nUsername: " + row[1], "\nPassword: " + row[2] + "\n")

		choice = None

	elif choice == "5":
		print ("\nBye bye\n")
		break

	else:
		print ("Enter 1, 2, 3, or 4.")
		choice = None

### cleaning up.

if con:
	con.commit()
	con.close()