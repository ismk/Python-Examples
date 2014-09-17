import os
from random import choice
showlist = []


# dirname = input("Enter the Drive Letter:\n")
# dirname.upper()
# foldername = input("Name the Root Folder:\n")
# basedir = str(dirname) + ":\\" + str(foldername)

basedir = "D:\Shows\THE OFFICE"


for ROOT, DIR, FILES in os.walk(basedir):
    for i in FILES:
        if i.endswith(('.mkv', '.avi', '.mp4')):
            showlist.append((os.path.join(ROOT, i)))

randomshow = choice(showlist)
print(randomshow)
os.startfile(randomshow)

# Powershell
# dir -Path D:\Shows -Include @("*.avi","*.mp4", "*.mkv") -Recurse |
# Get-Random | Invoke-Item
