pyIPC
=====

Inter-Process Communication examples (Semaphores, Shared Memory and Queues) with SysV and POSIX

What you need
-------------

Install the next software.

`sudo apt-get install git`

Install python **posix_ipc** and **sysv_ipc**  modules.

`pip3 install posix_ipc`
`pip3 install sysv_ipc`

Clone this repository.

`git clone https://github.com/gustavorv86/pyIPC`

Run examples
------------

Execute the **start.sh** scripts into the folders.

Command and Utilities
---------------------

Show SysV IPC information

`ipcs -a`

Remove SysV IPC

`ipcrm -[M|S|Q] [key]`

Show POSIX IPC devices

```
ls -al /dev/shm
ls -al /dev/mqueue
```

Dump POSIX IPC information

`hexdump -Cv /dev/shm/<MY_KEY>`
