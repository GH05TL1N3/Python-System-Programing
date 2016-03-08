#!/usr/bin/python

import os 

def child_process() :
	print "I am child process and my PID is : %d" % os.getpid()
	print "The child exiting"

def parent_process() :
	print "I am parent process with PID : %d" % os.getpid()
	childpid = os.fork()

	if childpid == 0 :
		# we are inside the child
		child_process()
	else :
		# we are inside the parent
		print "We are inside the parent process"
		print "Our child has PID : %d" % childpid

	while True :
		pass



parent_process()
