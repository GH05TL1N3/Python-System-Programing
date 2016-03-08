#!/usr/bin/python

class Calculator :
	def __init__(self, inpa, inpb) :
		self.a = inpa
		self.b = inpb

	def add(self) :
		return self.a + self.b
	def mul(self) :
		return self.a * self.b


class SciCal(Calculator) :
	def power(self) :
		return pow(self.a, self.b) 



def quickAdd(a,b) :
	return a + b


