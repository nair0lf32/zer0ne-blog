---
title: "Forest"
date: 2022-09-20T14:03:31+01:00
draft: false
categories:
  - HackTheBox
---

Look at this beautiful piece of art

{{< post-img src="forest.jpg" alt="forest" style="width:400px" >}}

yup. It's a stegano challenge

there is obviously no exif data...and looks like no file is embedded
time to play with with the image colors

I used `stegsolve` and in many color maps I could see a vertical text

I was wondering if it was the flag...it wasnt in the HTB format though

It was not...maybe its a passphrase:

`IsJuS1Af0r3sTbR0`


```bash
└──╼ $steghide --extract -sf forest.jpg
Entrez la passphrase:
�criture des donn�es extraites dans "nothinghere.txt".
```

Indeed!

read the extracted file for flag! (this one is on me)

