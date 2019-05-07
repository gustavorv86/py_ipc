#!/usr/bin/env bash

echo
echo 'Press INTRO to cancel'
echo

./py_shmem_read.py &
py_shmem_read_PID=$!

sleep 3

./py_shmem_write.py &
py_shmem_write_PID=$!

## Wait to press INTRO
read

kill -SIGUSR1 ${py_shmem_read_PID}
kill -SIGUSR1 ${py_shmem_write_PID}

sleep 1

echo 'Done'
