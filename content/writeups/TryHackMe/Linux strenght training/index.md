---
title: "Linux Strength training"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src="lst.png" width=200 height=200 alt="lst">

> Welcome to the gym! you think you master linux? well...you don't.
> No one does! you think you master those find and grep commands you use everyday? ha! amateur! here are some tiny challenges to show you a glimpse of how you can flex with simple linux commands!
> Just ssh and read those files!

`topson@james:~$ cat ReadMeIfStuck.txt`

```
Looking for flag 1?:It seems you will have to think harder if you want to find the flag. Perhaps try looking for a file called additionalHINT if you can't find it..
Looking for flag 2?: look for a file named readME_hint.txt
```

`topson@james:~$ find . -name additionalHINT -type f ./channels/additionalHINT`

```
topson@james:~$ cat ./channels/additionalHINT
try to find a directory called telephone numbers... Oh wait.. it contains a space.. I wonder how we can find that....
```

`topson@james:~$ find . -name 'telephone numbers' -type d ./corperateFiles/xch/telephone numbers`

```
topson@james:~$ ls -lhA './corperateFiles/xch/telephone numbers'
total 4.0K
-rw-r--r-- 1 topson topson 189 Oct 5 15:26 readME.txt

topson@james:~$ cat './corperateFiles/xch/telephone numbers/readME.txt'
202-555-0150
202-555-0125
617-555-0115
+1-617-555-0115
+1-617-555-0186
+1-617-555-0138
use the Find command to find a file with a modified date of 2016-09-12 from the /workflows directory
```

`topson@james:~$ find workflows/ -type f -newermt 2016-09-11 ! -newermt 2016-09-13`

```
workflows/xft/eBQRhHvx
```

`grep -oi '\S*flag\S*' workflows/xft/eBQRhHvx`

finally FLAG 1

Flag{feel_the_pain}

`topson@james:~$ find . -type f -name readME_hint.txt 2> /dev/null`

```
./corperateFiles/RecordsFinances/readME_hint.txt
```

```
Instructions: Move the MoveMe.txt file to the march folder directory and then execute the SH program to reveal the second flag.

you need to research three things:
how to execute bash files
how to work with files that begin with a - (dash) whether that is to do with copying or moving files
how to work with files with spaces
```

`topson@james:~/corperateFiles/RecordsFinances$ mv -- -MoveMe.txt "-march folder"`

`topson@james:~/corperateFiles/RecordsFinances$ cd -- '-march folder'`

`topson@james:~/corperateFiles/RecordsFinances/-march folder$ ls`

```
-MoveMe.txt -runME.sh
```

`topson@james:~/corperateFiles/RecordsFinances/-march folder$ ./-runME.sh`

```
-MoveMe.txt exists.
```

FLAG 2

Flag{as_I_suffer_you_shall_suffer}

`sarah@james:~$ find / -type f -name "\*.mnf" 2> /dev/null`

```
 /home/sarah/system AB/db/ww.mnf
```

`$ scp sarah@10.10.245.225:'~/system\ AB/db/ww.mnf' .`

`john -w=ww.mnf hashC.txt --format=Raw-SHA256`

`sarah@james:~$ find / -type f -name encoded.txt 2> /dev/null /home/sarah/`

```
system AB/managed/encoded.txt
```

`sarah@james:~/system AB/managed$ base64 -d '/home/sarah/system AB/managed/encoded.txt' | grep --color special`

```
special: the answer is in a file called ent.txt,
```

Geez do you feel the pain of learning through plain repetition?

Yeah? It means it's working!

`sarah@james:~/system AB/managed$ cat /home/sarah/logs/zhc/ent.txt`

```
bfddc35c8f9c989545119988f79ccc77
```

`sarah@james:~$ find /home/sarah -type f -name layer4.txt 2>/dev/null /home/sarah/system AB/keys/vnmA/layer4.txt`

`sarah@james:~$ gpg '/home/sarah/system AB/keys/vnmA/layer4.txt'`

```
gpg: WARNING: no command supplied. Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
gpg: /home/sarah/system AB/keys/vnmA/layer4.txt: unknown suffix
Enter new filename [layer4.txt]: noraj.txt
```

`sarah@james:~$ cat noraj.txt`

```
1. Find a file called layer3.txt, its password is james.
```

`sarah@james:~$ find /home/sarah -type f -name layer3.txt 2>/dev/null`

```
/home/sarah/oldLogs/2014-02-15/layer3.txt
```

`sarah@james:~$ gpg /home/sarah/oldLogs/2014-02-15/layer3.txt`

```
gpg: WARNING: no command supplied. Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
gpg: /home/sarah/oldLogs/2014-02-15/layer3.txt: unknown suffix
Enter new filename [layer3.txt]:
```

`sarah@james:~$ cat layer3.txt`

```
1. Find a file called layer2.txt, its password is tony.
```

`sarah@james:~$ find /home/sarah -type f -name layer2.txt 2>/dev/null`

```
/home/sarah/oldLogs/settings/layer2.txt
```

`sarah@james:~$ gpg /home/sarah/oldLogs/settings/layer2.txt`

```
gpg: WARNING: no command supplied. Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
gpg: /home/sarah/oldLogs/settings/layer2.txt: unknown suffix
Enter new filename [layer2.txt]:
```

`sarah@james:~$ cat layer2.txt`

```
MS4gRmluZCBhIGZpbGUgY2FsbGVkIGxheWVyMS50eHQsIGl0cyBwYXNzd29yZCBpcyBoYWNrZWQu
```

`sarah@james:~$ base64 -d layer2.txt`

```

1. Find a file called layer1.txt, its password is hacked.
```

`sarah@james:~$ find /home/sarah -type f -name layer1.txt 2>/dev/null`

```
/home/sarah/logs/zmn/layer1.txt
```

``sarah@james:~$ gpg /home/sarah/logs/zmn/layer1.txt```

```
gpg: WARNING: no command supplied. Trying to guess what you mean ...
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
gpg: /home/sarah/logs/zmn/layer1.txt: unknown suffix
Enter new filename [layer1.txt]:
```

`sarah@james:~$ cat layer1.txt`

Flag{muscle_memory_all_the_way}

yeah because redundancy is good for you

`sarah@james:~$ find /home/sarah -type f -name personal.txt.gpg 2>/dev/null`

```
/home/sarah/oldLogs/units/personal.txt.gpg
```

`sarah@james:~$ find /home/sarah -type f -name data.txt 2>/dev/null`

```
/home/sarah/logs/zmn/old stuff/-mvLp/data.txt
```

`sarah@james:~$ cat '/home/sarah/logs/zmn/old stuff/-mvLp/data.txt' > thing.txt`

`$ john /home/sarah/oldLogs/units/personal.txt.gpg -w thing.txt --format gpg`

```
...
valamanezivonia
```

`sarah@james:~$ gpg /home/sarah/oldLogs/units/personal.txt.gpg`

`sarah@james:~$ cat /home/sarah/oldLogs/units/personal.txt`

```
getting stronger in linux
```

Oh yeah I can totally feel the gains

`sarah@james:~$ find /home/sarah -type f -name employees.sql 2>/dev/null`

```
/home/sarah/serverLx/employees.sql
```

`sarah@james:~$ cd /home/sarah/serverLx/`

`sarah@james:~$ mysql -p`

```
mysql> source /home/sarah/serverLx/employees.sql

mysql> SELECT \* FROM employees WHERE first_name = 'Lobel' and last_name LIKE '%Flag%';

Flag{no_pain_no_gain}
```

No no really..I do feel smarter every second I do this

FINAL CHALLENGE

`sarah@james:/home/shared/chatlogs$ cat LpnQ`

```
(2020-08-13) Sarah: Hey Lucy, what happened to the database server? It is completely down now!

(2020-08-13) Lucy: Yes, I believe we have had a problem. I will need to investigate but for now there will be downtime for who knows how long.

(2020-08-13) Sarah: That is a shame, I needed to refer to a customer’s record due to them being unhappy with our service yesterday.

(2020-08-13) Lucy: if you ask Sameer, he may be able to help you find the back-up database copy we made a few hours ago?

(2020-08-13) Sarah: Of course, he is one of the sql developers around here in charge of the database creation, I will ask him in a few minutes. Thank you.

(2020-08-13) Lucy: No problem. By the way, our new security engineer may have accidently stored the SSH password of one of our employees. I have no idea how to change it and he will not be back till tomorrow.

(2020-08-13) Sarah: That is a shame. I am sure we will all be fine till he returns. Do you know which employee it is?

(2020-08-13) Lucy: I think it may have affected James but I not entirely sure.

(2020-08-13) Sarah: That is terrible, but I am sure nothing will come of it, he will be back tomorrow.

(2020-08-13) Lucy: True. It is just a concern of mine because James is the only one with root access. But as you said, we should be ok. Talk to you later. Bye.
```

Files including sameer

`sarah@james:~$ grep -iRl Sameer /home 2>/dev/null`

```
/home/shared/chatlogs/Pqmr
/home/shared/chatlogs/LpnQ
/home/shared/chatlogs/KfnP
```

`sarah@james:~$ cat /home/shared/chatlogs/Pqmr`

```
(2020-08-13) Sarah: Hey Sameer, do you by any chance no where I can find the sql back-up copy on this system? The database server is down, and I really need to help a customer out.

(2020-08-13) Sameer: Sure. let me check.

(2020-08-13) Sarah: Thanks.

(2020-08-13) Sameer: check the home/shared/sql/ directory. It should be in there with the date of today.

(2020-08-13) Sarah: Thank you Sameer.

(2020-08-13) Sameer: No problem. It probably is encrypted. Just use the password: danepon.

(2020-08-13) Sarah: OK, thank you.

(2020-08-13) Sameer: No problem

(2020-08-13) Sameer: By the way, if you have any issues just talk to Michael as I will be off for the remainder of the day. See you tomorrow. Bye.

(2020-08-13) Sarah: Bye.
```

`sarah@james:~$ cat /home/shared/chatlogs/KfnP`

```
(2020-08-13) Sarah: Michael, I have been having trouble accessing the sql database back-up copy made today. Sameer gave me the password, but it just will not work?

(2020-08-13) Michael: Ah, yes. I remember, the security engineer was testing out a new automated software for creating sql database backups. He must have configured it to encrypt the backups with a different password.

(2020-08-13) Sarah: So how can I get a hold of it?

(2020-08-13) Michael: Good question. From what I remember the test program utilised a configuration file around 50mb. It is located inside the home/shared/sql/conf directory. This configuration file contained the directory location of a wordlist it used to randomly select a password from for encrypting the sql back-up copies with.

(2020-08-13) Sarah: I do not really understand the last part?

(2020-08-13) Michael: once you find the configuration file and consequently the wordlist directory, visit it. One of those wordlists must contain the password it used for the testing. All I remember is that the password began with ebq. You will need Sameer’s account. His SSH password is: thegreatestpasswordever000.

(2020-08-13) Sarah: Thank you, I will try to find it.
```

Lmao I am getting tired

`sameer@james:~$ find /home/shared/sql/ -type f -size 50M`

```
/home/shared/sql/conf/JKpN
```

``sameer@james:~$ head /home/shared/sql/conf/JKpN```

```
Software: sql auto-back-up
Version: 2.3
Wordlist directory: aG9tZS9zYW1lZXIvSGlzdG9yeSBMQi9sYWJtaW5kL2xhdGVzdEJ1aWxkL2NvbmZpZ0JEQgo=
sql-encrypt: true
time: 2h\*
user: none
```

`sameer@james:~$ printf %s aG9tZS9zYW1lZXIvSGlzdG9yeSBMQi9sYWJtaW5kL2xhdGVzdEJ1aWxkL2NvbmZpZ0JEQgo= | base64 -d`

```
home/sameer/History LB/labmind/latestBuild/configBDB
```

`sameer@james:~$ grep -iRlE '^ebq' '/home/sameer/History LB/labmind/latestBuild/configBDB'`

```
/home/sameer/History LB/labmind/latestBuild/configBDB/pLmjwi
/home/sameer/History LB/labmind/latestBuild/configBDB/LmqAQl
/home/sameer/History LB/labmind/latestBuild/configBDB/Ulpsmt
```

`sameer@james:~$ grep -iRhE '^ebq' '/home/sameer/History LB/labmind/latestBuild/configBDB'`

```
ebqiojsdfioj
ebqiojsiodj
ebqiojdifoj
ebqiopsjdfopj
ebqnice
ebqops
ebqiuiud
ebqjoisjdfij
ebqkjjdd
ebqijsji
ebqopkopk
ebqattle
```

`$ scp sameer@10.10.61.194:/home/shared/sql/2020-08-13.zip.gpg .`

`gpg2john 2020-08-13.zip.gpg 2020-08-13.zip.gpg.hash`

```
File 2020-08-13.zip.gpg
Bad parameter: give(len=106935040, buf=0x5571785b0420, buf_size=90000), len can not be bigger than buf_size.
```

Holly molly...its too big for gpg2john...let's search for a custom script

```
$ ./crackgpg.sh 2020-08-13.zip.gpg wordlist.txt
FAILED - ebqiojsdfioj
FAILED - ebqiojsiodj
FAILED - ebqiojdifoj
FAILED - ebqiopsjdfopj
FAILED - ebqnice
FAILED - ebqops
FAILED - ebqiuiud
FAILED - ebqjoisjdfij
FAILED - ebqkjjdd
FAILED - ebqijsji
FAILED - ebqopkopk

SUCESS - ebqattle
```

`7z x 2020-08-13.zip`

`$ grep -ri james 2020-08-13`

```
2020-08-13/sakila/sakila-mv-data.sql:(84,'JAMES','PITT','2006-02-15 04:34:33'),
2020-08-13/sakila/sakila-mv-data.sql:(71,1,'KATHY','JAMES','KATHY.JAMES@sakilacustomer.org',75,1,'2006-02-14 22:04:36','2006-02-15 04:57:20'),
2020-08-13/sakila/sakila-mv-data.sql:(299,2,'JAMES','GANNON','JAMES.GANNON@sakilacustomer.org',304,1,'2006-02-14 22:04:37','2006-02-15 04:57:20'),
2020-08-13/load_employees.dump:(499996,'1953-03-07','James','vuimaxcullings','M','1990-09-27'),
```

creds = `james:vuimaxcullings`

Ah! privilege escalation

## Priviledge escalation

```
james@james:~$ sudo -l
[sudo] password for james:
Matching Defaults entries for james on james:
env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User james may run the following commands on james:
(ALL : ALL) ALL
```

haha James is a fricking Boss!

```
james@james:/home/sarah/serverLx$ sudo su root
[sudo] password for james:
root@james:/home/sarah/serverLx# cd /root
root@james:~# ls
root.txt
root@james:~# cat root.txt
Flag{do_you_even_bash_bro}

NOW YOU ARE LINUX STRONGER!!!

```

wow...just...wow...

G'night folks!
