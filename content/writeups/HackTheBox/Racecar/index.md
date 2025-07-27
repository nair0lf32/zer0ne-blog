---
title: "Racecar"
date: 2022-09-20T15:03:31+01:00
draft: false
categories:
  - HackTheBox
---

Simple [pwn challenge](https://github.com/nair0lf32/CTF-Scripts/blob/master/Hackthebox/racecar/racecar) they said

```bash
└──╼ $file racecar
racecar: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=c5631a370f7704c44312f6692e1da56c25c1863c, not stripped
```

```bash
└──╼ $checksec racecar
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of /home/nair0lf32/.cache/.pwntools-cache-3.9/update to 'never' (old way).
    Or add the following lines to ~/.pwn.conf or ~/.config/pwn.conf (or /etc/pwn.conf system-wide):
        [update]
        interval=never
[*] You have the latest version of Pwntools (4.7.0)
[*] '/Racecar/racecar'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```
It is an easy one they said!

```bash
(gdb) info function
All defined functions:

Non-debugging symbols:
0x00000618  _init
0x00000650  strcmp@plt
...

0x00000929  banner
0x00000b93  setup
0x00000c02  race_type
0x00000c91  car_menu
0x00001082  info
0x000011d2  car_info
0x00001352  menu
0x000013e1  main

...

(gdb) disassemble main
Dump of assembler code for function main:
...

```
There is a format string vulnerability in `printf()` in the `race_menu` function

the flag is right in the stack so [use this](https://github.com/nair0lf32/CTF-Scripts/blob/master/Hackthebox/racecar/exploit.py)

```bash
└──╼ $python exploit.py
[+] Opening connection to 138.68.129.154 on port 31614: Done
/Racecar/exploit.py:8: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  p.sendline("Name")
[DEBUG] Sent 0x5 bytes:
    b'Name\n'
[DEBUG] Received 0x438 bytes:

...

b'\n[*] Waiting for the race to finish...\x1b[1;32m\n\n[+] You won the race!! You get 100 coins!\n[+] Current coins: [169]\x1b[1;36m\n\n[!] Do you have anything to say to the press after your big victory?\n> \x1b[0m'
[*] Switching to interactive mode
[DEBUG] Received 0x116 bytes:

...

The Man, the Myth, the Legend! The grand winner of the race wants the whole world to know this:
57d6f1c0170565b8d858152612565b996c57d6f1c057d6f340---FLAG: 0x7b4254480x5f7968770x5f6431640x34735f310x745f33760x665f33680x5f67346c0x745f6e300x355f33680x6b6334740x7d213f ---
[*] Got EOF while reading in interactive
$
```
Now [decode](https://github.com/nair0lf32/CTF-Scripts/blob/master/Hackthebox/racecar/decode.py)

```bash
└──╼ $python decode.py
b'HTB{'
b'HTB{why_'
b'HTB{why_d1d_'
b'HTB{why_d1d_1_s4'
...

b'HTB{SIKE_REDACTED_XD}\x00'
```
How easy that was!
