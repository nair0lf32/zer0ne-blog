---
title: "Plastic Preservation"
date: 2022-09-18T18:33:31+01:00
draft: false
categories:
  - Cyberseclabs
---

```

└──╼ $cat encrypted.txt | base64 -d
c40d1f1b7bdd6012

```
This one, "dey hard"! I was stuck on this for days so I just went for a writeup

Found a nice one [here](https://plasticuproject.com/posts/plastic-preservation-write-up/)

I then proceed to "fully understand" what the `decrypter.py` script does

I did not beat that challenge tbh...but I got to keep learning :(

Basically the encrypted script was obfuscated so first put some clarity in it

The decrypter function should look like this:

```
def decrypt(passwd, debugs):
    solve = []
    b = 14695981039346656037
    c = 1099511628211
    passwd = int(base64.b64decode(str.encode(passwd)).decode(), 16)
    passwd ^= 1152921504606846975
    debugs.append(passwd)
    debugs = debugs[::-1]
    debugs.append(b)
    for i in range(len(debugs) - 1):
        solve.append(chr(int((debugs[i] ^ debugs[i+1]) / c)))
    print( 'PASSWORD: ' + ''.join(solve[::-1]))
    quit()
```
