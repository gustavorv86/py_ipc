#!/bin/bash

echo
echo 'Press INTRO to exit...'
echo

./pyQueueRead.py &
pyQueueRead_PID=$!

sleep 2

./pyQueueWrite.py &
pyQueueWrite_PID=$!

## Wait INTRO
read

kill -SIGUSR1 $pyQueueRead_PID
kill -SIGUSR1 $pyQueueWrite_PID

sleep 1
echo 'Done'
