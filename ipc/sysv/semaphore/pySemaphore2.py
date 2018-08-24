#!/usr/bin/env python3

import sysv_ipc
import os
import random
import signal
import sys
import time

SEM_KEY = 1024


def signal_handler(signum, frame):
	print('File ', __file__, ': Signal handler called with signal', signum)
	sys.exit(0)


def main():
	print('Python: ', __file__, ' PID: ', os.getpid())

	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGUSR1, signal_handler)

	semaphore = None
	while not semaphore:
		try:
			semaphore = sysv_ipc.Semaphore(SEM_KEY)
		except sysv_ipc.ExistentialError:
			print('Semaphore is not initialized, wait...')
			semaphore = None
			time.sleep(1)

	while True:
		semaphore.acquire()

		print('')
		print('Lock ', __file__, '...')

		sec_sleep = random.randint(1, 5)
		print('Sleep: ', sec_sleep)
		time.sleep(sec_sleep)

		semaphore.release()
		print('Unock ', __file__, '...')
		print('')


if __name__ == '__main__':
	main()
