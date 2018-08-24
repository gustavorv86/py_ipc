#!/usr/bin/env bash

echo
echo 'Press INTRO to cancel'
echo

./pyShmemRead.py &
pyShmemRead_PID=$!

sleep 3

./pyShmemWrite.py &
pyShmemWrite_PID=$!

## Wait to press INTRO
read

kill -SIGUSR1 ${pyShmemRead_PID}
kill -SIGUSR1 ${pyShmemWrite_PID}

sleep 1

echo 'Done'
