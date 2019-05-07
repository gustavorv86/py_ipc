#!/usr/bin/env python3

import sysv_ipc
import os
import random
import signal
import sys
import time

MQ_KEY = 1024
mqueue = None


def signal_handler(signum, frame):
	print('Signal handler called with signal', signum)
	sys.exit(0)


def main():
	global mqueue
	print('Python: ', __file__, ' PID: ', os.getpid())

	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGUSR1, signal_handler)

	while not mqueue:
		try:
			mqueue = sysv_ipc.MessageQueue(MQ_KEY)
		except sysv_ipc.ExistentialError:
			print('Queue is not initialize, wait...')
			time.sleep(1)

	while True:
		message, ntype = mqueue.receive()
		print('Type: ', ntype, ' message: ', message.decode())

		sec_sleep = random.randint(1, 5)
		time.sleep(sec_sleep)


if __name__ == '__main__':
	main()
