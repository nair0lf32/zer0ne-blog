# Ignition

add `ignition.htb` to your `/etc/hosts`

## Eumeration

### nmap
```
PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack nginx 1.14.2
|_http-server-header: nginx/1.14.2
|_http-title: Did not follow redirect to http://ignition.htb/
| http-methods: 
|_  Supported Methods: GET HEAD POST

```
### gobuster
```
/0                    (Status: 200) [Size: 25803]
/admin                (Status: 200) [Size: 7092] 
...

```

Go to admin dir and login as `admin:qwerty123` 

if you are patient trial-and-error

if you are optimal `hydra` or burp `intruder` (idc if its overkill XD)

get flag!