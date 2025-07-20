---
title: "Plastic Preservation"
date: 2022-09-18T18:33:31+01:00
draft: false
categories:
  - Cyberseclabs
---
Here is the [challenge](/csl/plastic_preservation/password_encrypter.py) script

This one, "dey hard"! I was stuck on this for days so I just went for the solution writeup

Found it [here](https://plasticuproject.com/posts/plastic-preservation-write-up/)

I then proceed to "fully" understand what the [decrypter.py](/csl/plastic_preservation/decrypter.py) script does

I did not beat that challenge tbh...but I have to keep learning :(

Basically the encrypted script was obfuscated so first [put some clarity in it](/csl/plastic_preservation/deobuscated.py)

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

Now I realise this was not even that hard (smh)
