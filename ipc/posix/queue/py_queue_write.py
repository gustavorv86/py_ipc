#!/usr/bin/env python3

import posix_ipc
import json
import os
import random
import signal
import sys
import time

MQ_KEY = "/MQUEUE_ID_1024"
mqueue = None


def signal_handler(signum, frame):
	global mqueue
	print('Signal handler called with signal', signum)
	if mqueue:
		mqueue.close()
		mqueue.unlink()
	sys.exit(0)


def main():
	global mqueue
	print('Python: ', __file__, ' PID: ', os.getpid())

	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGUSR1, signal_handler)

	mqueue = posix_ipc.MessageQueue(MQ_KEY, posix_ipc.O_CREX)

	data = dict()
	while True:

		data['time'] = int(time.time())
		data['asctime'] = time.asctime()

		# Write 4 messages and sleep

		for i in range(4):
			data['sequence'] = i
			data['priority'] = random.randint(1, 5)
			message = json.dumps(data)
			mqueue.send(message.encode(), priority=data['priority'])

		time.sleep(5)


if __name__ == '__main__':
	main()
