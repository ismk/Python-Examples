# class Bird:
# 	def __init__(self, kind, call):
# 		self.call = call
# 		self.kind = kind

# 	def do_call(self):
# 		print ("a %s goes %s" % (self.kind, self.call))

# 	def anotherfunct(self):
# 		if (self.kind == "Parrot"):
# 			print ("yes its a parrot")
# 		else:
# 			print ("Wrong Bird")


# Parrot = Bird("Parrot", "Kaw!")
# Parrot.do_call()
# Parrot.anotherfunct()

# import sys
# def repeat(s, exclaim):
# 	result = (s +" ") * 3
# 	if exclaim:
# 		result = result + "!!!"
# 	return result
# def main():
# 	print ("Hello there "+repeat(sys.argv[1], True));
# if __name__ == "__main__":
# 	main()


# s = "           HELLO this a string to be experimented upon woo hoo"
# print ("s.lower() = " + s.lower())
# print ("s.upper() = " + s.upper())
# print ("s.strip() = " + s.strip())

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

in_file = open(from_file, "r+")
indata = in_file.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")

input("")

out_file = open(to_file, "r+")
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()