import os

path = "C:/Users/Administrator/Videos/TwistedEquations"
files = []
files = os.listdir(path)
strfile = open("C:/titles.txt")
titlelist = []
for title in strfile:
    titlelist.append(title[:-1])
i = 0
while i < len(os.listdir(path)):
    newstring = os.path.join(path, titlelist[i] + ".mp4")
    filename = os.path.join(path, files[i])
    os.rename(filename, newstring)
    i = i + 1


# for filename in os.listdir(path):
#     for title in strfile:
#         newstring = title
#         newstring = os.path.join(path, newstring)
#         filename = os.path.join(path, filename)

# from os import listdir, getcwd, rename
# import re
# list_names = ['new_name1', 'new_name2']
# list_files = listdir(getcwd())
# filtre = re.compile("jpg$", re.IGNORECASE)
# list_jpg = filter(filtre.search, list_files)
# strip all element of list list_jpg
# list_jpg_strip = []
# for nom in list_jpg:
# print nom.strip()
#     list_jpg_strip.append(nom.strip())
# let's rename :
# i = 0
# while i <= len(list_jpg_strip):
#     rename(list_jpg_strip[i], list_names[i])
# i = i + 1
