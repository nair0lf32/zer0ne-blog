---
title: "Cicada 3301"
date: 2024-03-03T16:48:00+01:00
draft: false
categories:
  - TryHackMe
---

![cicada](/thm/cicada-3301/cicada.jpeg)

![welcome](/thm/cicada-3301/welcome.jpg)

## Ananlyse the audio

[here is the audio](/thm/cicada-3301/audio.wav)

With visual-analyser add a spectrogram layer and get this qr code

![qr](/thm/cicada-3301/qr.png)

It gives you a link to a pastebin. Answer to question 1

## Decode the passphrase

from the pastebin you get a passhprase and a key, both in base64

Then use  the key to decode the new passphrase. I let you guess this one it's funnier...

Or just use the hints

## Gather Metadata

use `steghide` with the passphrase to get the `invitation.txt` which contains a link to an imgur image

![qr](/thm/cicada-3301/undefined.jpg)

Looks like the first image right? Not the same! use `outguess` to extract the next challenge

Note: Make  sure to download the image correctly from imgur and not just "save as" image

```bash
└─(01:53:12 on master ✭)──> outguess -r  undefined.jpg  out.txt                                                                                                         1 ↵ ──(lun.,mars04)─┘
Reading undefined.jpg....
Extracting usable bits:   29035 bits
Steg retrieve: seed: 38, len: 1351
```

## Book cypher

In the text we just extracted there is a hash. Use [this](https://md5hashing.net/hash/) to get it cracked

yes it's another pastebin link...

From that you get a book...and now the rest of the challenge makes sense...You use the pattern provided in the extracted text
to read something from the book...

use some good old pen and paper to get ANOTHER link (not pastebin this time)

## The final song

The satisfaction of solving this room is perfectly described by this song. This room is very cool

Remember, cicadas don't cry
