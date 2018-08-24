#!/usr/bin/env python3

import posix_ipc
import os
import signal
import sys
import time

MQ_KEY = "/MQUEUE_ID_1024"


def signal_handler(signum, frame):
	print('Signal handler called with signal', signum)
	sys.exit(0)


def main():
	print('Python: ', __file__, ' PID: ', os.getpid())

	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGUSR1, signal_handler)

	mqueue = None
	while not mqueue:
		try:
			mqueue = posix_ipc.MessageQueue(MQ_KEY)
		except posix_ipc.ExistentialError:
			print('Queue is not initialize, wait...')
			time.sleep(1)

	while True:
		message, priority = mqueue.receive()
		print('Priority: ', priority, ' message: ', message.decode())

		time.sleep(0.250)


if __name__ == '__main__':
	main()
