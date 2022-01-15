# Hackerman

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

When there is a passphrase there is cracking involved

stegcracker is one of the best...uhm I mean stegseek

```
└──╼ $stegseek  hackerman.jpg /usr/share/wordlists/rockyou.txt
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Progress: 99.98% (133.4 MB)
[!] error: Could not find a valid passphrase.
```

oh wow

```
└──╼ $stegseek --seed  hackerman.jpg hackerman.txt
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found (possible) seed: "10961b21"
        Plain size: 45.0 Byte(s) (compressed)
        Encryption Algorithm: rijndael-128
        Encryption Mode:      cbc

```

well..I am STUCK! TODO: complete this challenge!
