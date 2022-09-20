# Crack the hash

<img src="cth.jpeg" width=200 height=200 alt="cth">

Anoher challenges room

Just hashes to crack

`md5: 48bb6e862e54f2a795ffc4e541caed4d` : easy

`sha1: CBFDAC6008F9CAB4083784CBD1874F76618D2A97` : password123

`sha256: 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032` : letmein

here comes trouble

```
hashcat -a 0 -m 3200 '$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom' /usr/share/wordlists/rockyou.txt
```

oh lawd this gon' take yeeears

As we know the answer is 4-characters long, we can filter rockyou to create a smaller list.

`awk 'length == 4' rockyou.txt >four.txt`

```
hashcat -a 0 -m 3200 '$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom' '/home/myusername/Crack the hash/four.txt'
```

`bcrypt: $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom` : bleh

`md4: 279412f945939ba78ce0758d3fd83daa` : Eternity22

`sha256: F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85` : paule

`NTLM: 1DFECA0C002AE40B8619ECF94819CC1B` : n63umy8lkf4i

if they say this one is hard it is HARD: (`salt = aReallyHardSalt`)

we filter rockyou again and hashcat this thing

```
$hashcat -m 1800 -a 0 '$6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.' '/home/da_username/Desktop/Crack the hash/six.txt'
```

`SHA-512, many rounds : $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.` : waka99

this one is special HMAC-SHA1 that takes a "key" as salt (`salt = tryhackme`)

```
hashcat -m 160 -a 0 'e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme' '/home/itsyaboynairolf/Crack the hash/rockyou.txt'
```

`HMAC-SHA1: e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme` : 481616481616

Hashes cracked!
