#!/bin/bash

echo
echo 'Press INTRO to exit...'
echo

./py_queue_read.py &
py_queue_read_PID=$!

sleep 2

./py_queue_write.py &
py_queue_write_PID=$!

## Wait INTRO
read

kill -SIGUSR1 $py_queue_read_PID
kill -SIGUSR1 $py_queue_write_PID

sleep 1
echo 'Done'
