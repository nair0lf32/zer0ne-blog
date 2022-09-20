---
title: "Digital Cube"
date: 2022-09-20T14:03:31+01:00
draft: false
categories:
  - HackTheBox
---
Stego challenge that start with a text file

oh look! binary? we can get an image from that!

I used an online tool to draw the binary-image

the size of the image is 50x50 (the hints say it too)

and you get a QR code!

you can use `zbarimg` from Zbar tools (what I did)

or any online qr decoder like [this one](https://zxing.org/w/decode.jspx)

The flag is revealed when you decode the QR image!

