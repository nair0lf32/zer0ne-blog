---
title: "Hackerman"
date: 2022-09-18T18:33:31+01:00
draft: false
categories:
  - Cyberseclabs
---

{{< image src="/csl/hackerman.jpg" alt="hackerman" position="center" style="width: 400px;" >}}

```
└──╼ $exif hackerman.jpg
Données corrompues
Les données fournies ne respectent pas les spécifications.
ExifLoader: Les données fournies ne semblent pas contenir de données EXIF.


└──╼ $steghide --info hackerman.jpg
"hackerman.jpg":
  format: jpeg
  capacit�: 7,0 KB
Essayer d'obtenir des informations � propos des donn�es incorpor�es ? (o/n) o
Entrez la passphrase:
steghide: impossible d'extraire des donn�es avec cette passphrase!
```
passphrase? so cracking involved...

friendship with `stegcracker` is over now `stegseek` is my best friend

```
└──╼ $stegseek  hackerman.jpg /usr/share/wordlists/rockyou.txt
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Progress: 99.98% (133.4 MB)
[!] error: Could not find a valid passphrase.
```

Actually no cracking was needed I am a bit stupid, because the passphrase was in plain sight all this time: `HACKERMAN`

```

└──╼ $steghide --extract -sf hackerman.jpg
Entrez la passphrase:
�criture des donn�es extraites dans "secret.txt".
```
The `secret.txt` file introduce us to `Jake Bellagot`

We finally got a name...you know what to do...

we got a twitter account

`@JBellagot` talks about `NoobCon2020` and that picture with a QR code

{{< image src="/csl/EWda8qmXgAMdaR7.jpeg" alt="JBQR" position="center" >}}

Reading the qr code take us to `https://jakeyboybellagot.github.io/ubiquitous-waffle/`

When trying to contact him using the button you notice the link is encoded in base64

`Q1NMezk0YTA0OTBhZDZjMjcxNWFmMTI0OTA1NWE5YTVkYzI3fQ==` which decodes to

`CSL{the_flag_goes_here}`

Done.

I really wanted to contact this guy, but he could blackhat me later
