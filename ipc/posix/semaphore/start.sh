#!/usr/bin/env bash

echo
echo 'Press INTRO to cancel'
echo

./pySemaphore2.py &
pySemaphore1_PID=$!

sleep 3

./pySemaphore1.py &
pySemaphore2_PID=$!

## Wait to press INTRO
read

kill -SIGUSR1 ${pySemaphore1_PID}
kill -SIGUSR1 ${pySemaphore2_PID}

sleep 1

echo 'Done'
