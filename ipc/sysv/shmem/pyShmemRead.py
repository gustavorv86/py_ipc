#!/usr/bin/env python3

import sysv_ipc
import os
import signal
import sys
import time

SHM_KEY = 1024
SHM_SIZE = 128


def signal_handler(signum, frame):
	print('File ', __file__, ': Signal handler called with signal', signum)
	sys.exit(0)


def main():
	print('Python: ', __file__, ' PID: ', os.getpid())

	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGUSR1, signal_handler)

	shared_memory = None
	while not shared_memory:
		try:
			shared_memory = sysv_ipc.SharedMemory(SHM_KEY, size=SHM_SIZE)
		except sysv_ipc.ExistentialError:
			print('Memory is not initialized, wait...')
			shared_memory = None
			time.sleep(1)

	while True:
		message = shared_memory.read().decode()
		print(message)
		time.sleep(1)


if __name__ == '__main__':
	main()
