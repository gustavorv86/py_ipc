#!/usr/bin/env python3

import posix_ipc
import mmap
import json
import os
import signal
import sys
import time

SHM_KEY = "SHARED_MEMORY_ID_1024"
SHM_SIZE = 128
map_memory = None


def signal_handler(signum, frame):
	global map_memory

	print('File ', __file__, ': Signal handler called with signal', signum)
	if map_memory:
		map_memory.close()

	posix_ipc.unlink_shared_memory(SHM_KEY)
	sys.exit(0)


def main():
	global map_memory
	print('Python: ', __file__, ' PID: ', os.getpid())

	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGUSR1, signal_handler)

	# open
	shared_memory = posix_ipc.SharedMemory(SHM_KEY, posix_ipc.O_CREX, size=SHM_SIZE)
	map_memory = mmap.mmap(shared_memory.fd, shared_memory.size)
	shared_memory.close_fd()

	data = dict()
	while True:
		data['time'] = int(time.time())
		data['asctime'] = time.asctime()
		message = json.dumps(data)
		map_memory.seek(0)
		map_memory.write(message.encode())
		time.sleep(0.5)


if __name__ == '__main__':
	main()
