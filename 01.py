class Fruit(object):

    """A class that makes various tasty fruits."""

    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print("I'm a %s %s and I taste %s." %
             (self.color, self.name, self.flavor))

    def is_edible(self):
        if not self.poisonous:
            print("Yep! I'm edible.")
        else:
            print("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()


class studdb(object):

    def __init__(self):
        self.sname = sname

    def getinfo(self, sname, sid, ssubs, marklist, smarks):

        self.sid = sid
        self.ssubs = ssubs
        self.marklist = marklist
        self.smarks = smarks
        self.sname = str(input("Enter Student's Name: "))
        self.sid = int(input("Enter Student's ID: "))
        self.ssubs = int(
            input("Enter the Number of Subjects the Student's Taken: "))
        self.marklist = []
        for i in range(self.ssubs):
            self.smarks = int(input("Enter Subject Number %d: " % (i + 1)))
            self.marklist.append(smarks)

    def descript(self):
        print("Student: %s" % self.sname)
        print("Student ID: %d" % self.sid)
        print("Student Subjects: %d" % self.ssubs)


studdb.getinfo()
