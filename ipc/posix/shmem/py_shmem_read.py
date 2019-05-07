#!/usr/bin/env python3

import posix_ipc
import mmap
import os
import signal
import sys
import time

SHM_KEY = "SHARED_MEMORY_ID_1024"
map_memory = None


def signal_handler(signum, frame):
	global map_memory

	print('File ', __file__, ': Signal handler called with signal', signum)
	if map_memory:
		map_memory.close()

	sys.exit(0)


def main():
	global map_memory
	print('Python: ', __file__, ' PID: ', os.getpid())

	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGUSR1, signal_handler)

	map_memory = None
	while not map_memory:
		try:
			shared_memory = posix_ipc.SharedMemory(SHM_KEY)
			map_memory = mmap.mmap(shared_memory.fd, shared_memory.size)
			shared_memory.close_fd()
		except posix_ipc.ExistentialError:
			print('Memory is not initialized, wait...')
			map_memory = None
			time.sleep(1)

	while True:
		map_memory.seek(0)
		message = map_memory.read().decode()
		print(message)
		time.sleep(1)


if __name__ == '__main__':
	main()
