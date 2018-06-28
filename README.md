# SFTP (181 pts, 60 solves)

Server: sftp.ctfcompetition.com:1337
Binary: [sftp](sftp)

## Writeup

TL;DR: pass a password check, obtain a write-what-where and read-what-where using overlapping malloc chunks, and overwrite a GOT table entry to pop a shell.

You can read our full writeup [here](#)

## Challenge files

* [sftp](sftp) - the binary
* [sftp.c](sftp.c) - the source code (header files not provided)
* [sftp.i64](sftp.i64) - our IDA database
* [exploit.py](sftp_pwn.py) - our exploit script

## Passing the password check

- We start out with 0x5417
- We repeatedly xor in the next (signed!) byte of the password
  - for example if the byte is 0x41, we xor 0x0041
  - but if the byte is 0x83, we xor 0xff83
- After the xor, we double
- After 15 of these steps, we want to end up with 0x8dfa
- Consider the upper and lower bytes separately. We have easy control over the lower byte, since we can xor into it directly. The upper byte is much more difficult to control.
- Consider the upper byte in binary. Each double shifts it one bit to the left, potentially shifting a 1 into the lower bit if the upper bit of the lower byte is 1
- Each xor either doesn't do anything to the upper byte, or flips all the bits (0xff)
- We start out with 0x54. In binary: 01010100. We can turn this into 0x00 with six doubles
- First xor in 0x28 to make the lower byte 0x28 ^ 0x17 = 0x3f. After a double this is 0x7e.
- 0x7e has the property that (0x7e ^ 0x41) * 2 = 0x7e. So now we can xor in 0x41 == 'A' five times
- We've done a total of six doubles, so the upper byte is now 01010100 << 6 = 00000000
- The lower byte is 0x7e, so together: 0x007e
- Now xor in 0x7e. After the next double we have 0x0000
- Now we have 8 doubles left in order to make the upper byte 0x8d
