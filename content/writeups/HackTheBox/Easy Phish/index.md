---
title: "Easy Phish"
date: 2022-09-20T14:03:31+01:00
draft: false
categories:
  - HackTheBox
---

googling secure-startup.com gave nothing

time to look at dns records (TXT v=SPF,DKIM,DMARC)

```bash
└──╼ $dig TXT secure-startup.com _dmarc.secure-startup.com

; <<>> DiG 9.16.22-Debian <<>> TXT secure-startup.com _dmarc.secure-startup.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 64720
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

...

```

Join the two flags parts and submit!
