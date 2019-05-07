#!/usr/bin/env python3

import sysv_ipc
import os
import json
import signal
import sys
import time

SHM_KEY = 1024
SHM_SIZE = 128
shared_memory = None


def signal_handler(signum, frame):
	global shared_memory

	print('File ', __file__, ': Signal handler called with signal', signum)
	if shared_memory:
		shared_memory.remove()
	sys.exit(0)


def main():
	global shared_memory
	print('Python: ', __file__, ' PID: ', os.getpid())

	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGUSR1, signal_handler)

	# open
	shared_memory = sysv_ipc.SharedMemory(SHM_KEY, sysv_ipc.IPC_CREX, size=SHM_SIZE)

	data = dict()
	while True:
		data['time'] = int(time.time())
		data['asctime'] = time.asctime()
		message = json.dumps(data)
		shared_memory.write(message.encode())
		time.sleep(0.5)


if __name__ == '__main__':
	main()
