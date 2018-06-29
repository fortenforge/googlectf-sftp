from pwn import *

if len(sys.argv) > 1 and sys.argv[1] == 'remote':
    p = remote("sftp.ctfcompetition.com", 1337 )
else:
    p = process("./sftp")

p.recvuntil("(yes/no)?")
p.sendline("yes")
p.recvuntil("password:")
p.sendline("(AAAAA\x7e" + "\x80\x01\x01\x80\x01\x80\x80\x95")
p.interactive()
