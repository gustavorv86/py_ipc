#!/usr/bin/env python3

import sysv_ipc
import json
import os
import time
import random
import signal
import sys

MQ_KEY = 1024
mqueue = None


def signal_handler(signum, frame):
	global mqueue
	print('Signal handler called with signal', signum)
	if mqueue:
		mqueue.remove()
	sys.exit(0)


def main():
	global mqueue
	print('Python: ', __file__, ' PID: ', os.getpid())

	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGUSR1, signal_handler)

	mqueue = sysv_ipc.MessageQueue(MQ_KEY, sysv_ipc.IPC_CREX, max_message_size=4096)

	data = dict()
	while True:
		data['time'] = int(time.time())
		data['asctime'] = time.asctime()
		message = json.dumps(data)
		mqueue.send(message.encode())

		sec_sleep = random.randint(1, 5)
		time.sleep(sec_sleep)


if __name__ == '__main__':
	main()
