import os

def getPath():
	dirname = input("Enter the Drive Letter:\n")
	dirname.upper()
	foldername = input("Name the Root Folder:\n")
	basedir = str(dirname) + ":\\" + str(foldername)
	thelist = [x for x in os.listdir(basedir) if os.path.isdir(os.path.join(basedir, x))]
	return (basedir, thelist)

#-------adds index number ex. 00, 01 and so on-----------#
def IndexExs():
	basedir, thelist = getPath()

	new_name =""
	for name in thelist:
		if name[0] not in numbers:
			index = thelist.index(name)
			if (index > 9):
				new_name = str(index) +" "+ name
			else:
				new_name = "0"+ str(index) +" "+ name
			os.rename(os.path.join(basedir, name), os.path.join(basedir, new_name))
	print ("All done check your folders!")


#-------------to remove the index number starting of the folder------------#
def RemoveExs():
	basedir, thelist = getPath()
	for name in thelist:
		if name[0] in numbers:
			new_name = name[3:]
			os.rename(os.path.join(basedir, name), os.path.join(basedir, new_name))
	print ("Removed the numbers, check the folders!")


#-----Creating Index of Folders----------#
def CreaIndex():
	basedir, thelist = getPath()
	nof = input ("How many folders do you require?\n")
	for i in range(0,int(nof)):
		namef = input("Enter Name of Folder\n")
		newstr = basedir + '\\0' + str(i) + ' ' + namef
		os.makedirs(newstr)
	print ("Done Creating the folders!")


#-------------------------------------------------------------#
#-----------------------MAIN---------------------------------#

global numbers
numbers = ["0","1","2","3","4","5","6","7","8","9"]

ok = True
while ok:
	print ("\n1. Adding index to the existing fodler structure")
	print ("2. Removing index to the exisiting folder structure")
	print ("3. Creating index of folders with their respective names")
	print ("4. Exit")
	print ("Enter your choice: \n")

	usrsel = input()

	if usrsel == "1":
		IndexExs()
	elif usrsel == "2":
		RemoveExs()
	elif usrsel == "3":
		CreaIndex()
	elif usrsel == "4":
		print ("Goodbye!")
		ok = False
	else:
		print("Enter Valid Option Please")