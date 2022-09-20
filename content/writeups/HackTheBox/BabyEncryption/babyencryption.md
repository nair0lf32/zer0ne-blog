---
title: "BabyEncryption"
date: 2022-09-20T15:33:31+01:00
draft: false
categories:
  - HackTheBox
---

aka encryption for babies

basically reverse engineer the [chall.py](chall.py)

It takes an empty list, and appends to that list a complex combination of characters

```
(123 * char + 18) % 256)
```

Then returns the bytes (ascii) of that list and write it as hex in `msg.enc`

what [decode.py](decode.py) script does:

- open the [msg.enc](msg.enc) file and read the ascii from the hex code
- reverse the mathematical operation (hardest part ngl)
- return the ascii characters

its hard to reverse the modulus operation though...you can google that...or use excel (lol)

I have been on the forums and some people just brute forced it

Do some research!

use whatever you want to get the flag...

But try to reverse the operation first for the maximum fun!


```
└──╼ $python decode.py
b'Th3 nucl34r w1ll 4rr1v3 0n fr1d4y.\nHTB{flag_for_modular_operations_experts}'
```
