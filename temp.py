# from sys import argv

# script, first, second, third = argv

# print ("The script is called:", script)
# print ("Your first variable is:", first)
# print ("Your second variable is:", second)
# print ("Your third variable is:", third)

#GPA Calculator

# num =  int(input("Enter the number of years: \n"))

# marks = []
# total = 0
# for i in range(num):
# 	print ("Enter the %r year marks: \n" %(i+1))
# 	tempmarks = float(input())
# 	marks.append(tempmarks)

# for i in marks:
# 	global total
# 	total += i
# avg = total / num

# print (avg)

# org = "Hello this is a string"

# print (org[::-1])


# total = 0
# for i in range(0,10):
# 	total += i
# print (total)


#!/usr/bin/env python

# from sys import argv, exit
# from PyQt4 import QtCore, QtGui

# class Clock(QtGui.QWidget):
#    def __init__(self, parent=None):
#       super(Clock, self).__init__(parent)
#       #timer
#       timer = QtCore.QTimer(self)
#       timer.timeout.connect(self.update)
#       timer.start(1000)
#       #window
#       self.setWindowIcon(QtGui.QIcon('Default.png'))
#       self.setWindowTitle('Clock')
#       self.resize(200, 200)
#       #hour pointer
#       self.hPointer = QtGui.QPolygon([
#          QtCore.QPoint(6, 7),
#          QtCore.QPoint(-6, 7),
#          QtCore.QPoint(0, -50)
#       ])
#       #minute pointer
#       self.mPointer = QtGui.QPolygon([
#          QtCore.QPoint(6, 7),
#          QtCore.QPoint(-6, 7),
#          QtCore.QPoint(0, -70)
#       ])
#       #second pointer
#       self.sPointer = QtGui.QPolygon([
#          QtCore.QPoint(1, 1),
#          QtCore.QPoint(-1, 1),
#          QtCore.QPoint(0, -90)
#       ])
#       #colors
#       self.bColor = QtGui.QColor('#0000aa') #hours and minutes
#       self.sColor = QtGui.QColor('#aa0087')

#    def paintEvent(self, event):
#       rec = min(self.width(), self.height())
#       tik = QtCore.QTime.currentTime()
#       #painter
#       painter = QtGui.QPainter(self)
#       #zipping code to draw pointers
#       def drawPointer(color, rotation, pointer):
#          painter.setBrush(QtGui.QBrush(color))
#          painter.save()
#          painter.rotate(rotation)
#          painter.drawConvexPolygon(pointer)
#          painter.restore()
#       #tune up painter
#       painter.setRenderHint(QtGui.QPainter.Antialiasing)
#       painter.translate(self.width() / 2, self.height() / 2)
#       painter.scale(rec / 200, rec / 200)
#       painter.setPen(QtCore.Qt.NoPen)
#       #draw pointers
#       drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
#       drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
#       drawPointer(self.sColor, (6 * tik.second()), self.sPointer)
#       #draw face
#       painter.setPen(QtGui.QPen(self.bColor))
#       for i in range(0, 60):
#          if (i % 5) != 6:
#             painter.drawLine(87, 0, 97, 0)
#          painter.rotate(6)
#       painter.end()

# if __name__ == '__main__':
#    app = QtGui.QApplication(argv)
#    win = Clock()
#    win.show()
#    exit(app.exec_())

board = []

# for i in range(0,5):
#     board.append(["O"] *5)

# print board

# def print_board(board):
# 	for i in board:
# 		print i.join()

# print_board([1,2,3,4,5,6,7,8,9])
print ("hello world")

name = "Bob"
food = "lasagna"
print ("{name} wants to eat {food}")

def function_to_do():
    print ("Hello World")

function_to_do()


def damn():
  print ("Hello World!")

damn()