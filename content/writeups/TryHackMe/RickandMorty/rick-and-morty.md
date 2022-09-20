---
title: "Rick and Morty"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src="rm.jpeg" width=200 height=200 alt="rm">

My very first ctf in the theme of one of my favorites cartoon

I was not bright enough to take notes doing it so I have to re-do it

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 1b:a2:55:2a:98:72:8b:b1:04:a2:92:04:71:e1:63:e8 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD1h54qxFjtSFt0u71oKQVr2fj0sna5xoDSQTcxNlW7467woiH/Ufj4/ccHN32iwsx6FIMJJPRrdy2LUd38DybkLKSnqn1B6UR0LQ8n3QwnKK54ad7PwdwqXsostLASIXSFdjXo25SttYwh4BUzaNjmjihF5o63Qj533Jx0y8Zbbw0vaqFNzBPBYt3+JqkIF5IiBGfiR4zodHOpvi2g9g6AXAl32OhDvd5kqTRVIRDenk69SeR7awKZo+v0WMdJvrUJIriXhlJ72QmAzJo+D/dZba2lsuM8RR7RJnpfA4swwP+t8x3XztlV4EcOmgdf2bA/bIstkTUF+OcKTvaKFo3j
|   256 33:a4:33:d9:d8:14:45:e5:52:be:f6:f7:ed:93:f4:f7 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBCtRsw3waYPfZ8fzVb3nZb5CDEnzgzwDBIWyMoye7TIE1KWDrD3V3kkqCSyKNKA+I0OGxd3Tcg7Ce3sEuj0gpXk=
|   256 2f:9f:a8:14:a6:aa:72:5d:6c:47:5e:8d:30:63:8f:3d (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPtbWlf0LCQkWzV1oNlITISE9ack8cFh0hoaSH0SNGlC
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Rick is sup4r cool
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

### ffuf

```
.htpasswd               [Status: 403, Size: 296, Words: 22, Lines: 12]
.hta                    [Status: 403, Size: 291, Words: 22, Lines: 12]
.htaccess               [Status: 403, Size: 296, Words: 22, Lines: 12]
assets                  [Status: 301, Size: 313, Words: 20, Lines: 10]
index.html              [Status: 200, Size: 1062, Words: 148, Lines: 38]
robots.txt              [Status: 200, Size: 17, Words: 1, Lines: 2]
server-status           [Status: 403, Size: 300, Words: 22, Lines: 12]
```

lol `robots.txt` is litterally put under or nose

On the website you can see rick turned into a pickle again

haha...funniest thing I ever saw

checking the source code (always)

```
<!--

    Note to self, remember username!

    Username: R1ckRul3s

  -->

```

`robots.txt` just contains `Wubbalubbadubdub`

might be the password! we try to ssh with those...permission denied!

More website enumeration then...I fuzz for more dir or files

```
.htpasswd               [Status: 403, Size: 300, Words: 22, Lines: 12]
                        [Status: 403, Size: 291, Words: 22, Lines: 12]
.hta                    [Status: 403, Size: 295, Words: 22, Lines: 12]
.htaccess               [Status: 403, Size: 300, Words: 22, Lines: 12]
denied                  [Status: 302, Size: 0, Words: 1, Lines: 1]
login                   [Status: 200, Size: 882, Words: 89, Lines: 26]
portal                  [Status: 302, Size: 0, Words: 1, Lines: 1]

```
`login.php` and `portal.php` look interresting!

We login and reach portal...there we have command execution

I immediatelly try `ls`

```
Sup3rS3cretPickl3Ingred.txt
assets
clue.txt
denied.php
index.html
login.php
portal.php
robots.txt
```

The first ingredient is there...so lets read it

Denied! haha..poor meeseeks

there is a filter for some commands `cat` doesnt work but you can use `less`

```
less Sup3rS3cretPickl3Ingred.txt
...
```

`clue.txt` says `Look around the file system for the other ingredient.`

use commands to look around...always check home

hehe this part was a bit tricky but I already completed the linux strenght room

```
total 12
drwxrwxrwx 2 root root 4096 Feb 10  2019 .
drwxr-xr-x 4 root root 4096 Feb 10  2019 ..
-rwxrwxrwx 1 root root   13 Feb 10  2019 second ingredients
```

It was not two folders or files its just one file named "second ingredients"

```
less "/home/rick/second ingredients"
...
```
so now there is only one ingredient left...looking around doesnt help

hmm...wait a second...

## privilege escalation ?

```
sudo -l

Matching Defaults entries for www-data on ip-10-10-153-33.eu-west-1.compute.internal:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ip-10-10-153-33.eu-west-1.compute.internal:
    (ALL) NOPASSWD: ALL
```

LMAO! we are litterally root! yeah now we know where it is

```
sudo less /root/3rd.txt
...
```
Done! Wubbalubbadubdub!!





