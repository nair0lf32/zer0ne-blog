# Preignition

## Enumeration

### nmap
```
PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack nginx 1.14.2
|_http-server-header: nginx/1.14.2
|_http-title: Welcome to nginx!
| http-methods: 
|_  Supported Methods: GET HEAD

```

### gobuster

```
└──╼ $gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://10.129.240.135/
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.240.135/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/12/16 17:10:33 Starting gobuster in directory enumeration mode
===============================================================
/admin.php            (Status: 200) [Size: 999]
                                               
===============================================================
2021/12/16 17:11:45 Finished
===============================================================
```

Go there and login as `admin:admin` for flag
