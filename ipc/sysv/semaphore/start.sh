#!/usr/bin/env bash

echo
echo 'Press INTRO to cancel'
echo

./py_semaphore_2.py &
py_semaphore_1_PID=$!

sleep 3

./py_semaphore_1.py &
py_semaphore_2_PID=$!

## Wait to press INTRO
read

kill -SIGUSR1 ${py_semaphore_1_PID}
kill -SIGUSR1 ${py_semaphore_2_PID}

sleep 1

echo 'Done'
