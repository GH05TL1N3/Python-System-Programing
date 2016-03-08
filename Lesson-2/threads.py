#!/usr/bin/python

import thread
import time

def worker_thread(id) :
	count = 1
	while True :
		print str(count) +" Hello - thread : %d " % id
		count += 1
		time.sleep(5)

for id in range(1,3) :
	thread.start_new_thread(worker_thread, (id,))

print "Main thread going for infinite loop"
while True :
	pass
