# SFTP (181 pts, 60 solves)

* Server: sftp.ctfcompetition.com:1337
* Binary: [sftp](sftp)

## Writeup

TL;DR: pass a password check, obtain a write-what-where and read-what-where using overlapping malloc chunks, leak a libc pointer, and overwrite a GOT table entry to pop a shell.

You can read our full writeup [here](https://hackmd.io/s/SkUhP4fGX).

## Challenge files

* [sftp](sftp) - the binary
* [sftp.c](sftp.c) - the source code (header files not provided)
* [sftp.i64](sftp.i64) - our IDA database
* [sftp_pwn.py](sftp_pwn.py) - our exploit script
* [sftp_interact.py](sftp_interact.py) - script that passes the password check
