#!/usr/bin/python

class Calculator :
	def __init__(self, inpa, inpb) :
		self.a = inpa
		self.b = inpb

	def add(self) :
		return self.a + self.b
	def mul(self) :
		return self.a * self.b


calObj = Calculator(10,20)

print "a + b = %d" % calObj.add()

print "a * b = %d" % calObj.mul()



class SciCal(Calculator) :
	def power(self) :
		return pow(self.a, self.b) 




Sciobj = SciCal(3,5)

print "A ^ B = %d" % Sciobj.power()
