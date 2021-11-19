# Crocodile

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.10.14.230
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp            33 Jun 08 10:58 allowed.userlist
|_-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: Smash - Bootstrap Business Template
|_http-favicon: Unknown favicon MD5: 1248E68909EAE600881B8DB1AD07F356
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Unix
```

### gobuster

```
/.hta                 (Status: 403) [Size: 279]
/.htaccess            (Status: 403) [Size: 279]
/.hta.php             (Status: 403) [Size: 279]
/.htpasswd            (Status: 403) [Size: 279]
/.htaccess.php        (Status: 403) [Size: 279]
/.htpasswd.php        (Status: 403) [Size: 279]
/assets               (Status: 301) [Size: 317] [--> http://10.129.143.174/assets/]
/config.php           (Status: 200 [Size:0]
/css                  (Status: 301) [Size: 314] [--> http://10.129.143.174/css/]
/dashboard            (Status: 301) [Size: 320] [--> http://10.129.143.174/dashboard/]
/fonts                (Status: 301) [Size: 316] [--> http://10.129.143.174/fonts/]
/js                   (Status: 301) [Size: 313] [--> http://10.129.143.174/js/]
/login.php            (Status: 200) [Size: 1577]
/logout.php           (Status: 302) [Size: 0] [--> login.php]
/server-status        (Status: 403) [Size: 279]

```

Oh nice `login.php`...but we need credentials!

nmap said ftp as anonymous is allowed...we got fetch for juicy files

login as admin with credentials from ftp lists

we got two. `userlist` and `userlist.passwd`

we connect as admin and get admin flag!
