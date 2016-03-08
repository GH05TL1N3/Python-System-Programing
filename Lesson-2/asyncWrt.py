#!/usr/bin/python
# Threading lesson [subclass with AsyncWrite]
# coded by NETMONSTERZ

import threading
import time

class AsyncWrt(threading.Thread) :
	def __init__(self, text, outfile) :
		threading.Thread.__init__(self)
		self.text = text
		self.outfile = outfile

	def run(self):
		fdesc = open(self.outfile, "a")
		fdesc.write(self.text + "\n")
		fdesc.close()
		time.sleep(2)
		print "\nFinished Background file write to : " + self.outfile


def Main() :
	while True :
		message = raw_input("Enter string to store: ")
		background = AsyncWrt(message, "outputstr.txt")
		background.start()
		print "The program can continue to run while it write in another thread"

		background.join()
		print "Waited utill thread was complete\n"

if __name__ == '__main__' :
	Main()
