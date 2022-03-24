# WebAppSec 101

<img src="was.png" alt="was" width=200>

First, Why I liked this room?

>This room is a small vulnerable web application. In the OWASP Juice shop, we looked at how some basic vulnerabilities worked. In this room, we'll walk though the methodology and approach of testing a web application. As an ethical hacker, you need to test the web application from the perspective of an attacker. We'll be using this mindset to establish a strategy to look for weaknesses in the web application. 

It is guided so We wont talk much

## Enumeration

### rustscan + nmap

```
PORT    STATE SERVICE REASON  VERSION
22/tcp  open  ssh     syn-ack OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 ab:58:43:31:39:5d:3a:f5:21:e4:7c:b9:e2:7b:7c:df (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC/RPuU6en8LmHkp1goxuWoXOobuO5rKcZ27iN2yfQtobt78rXgOP92+pPqIxpUro4haHSyj+cZO+KO7UE8Bm1uOSgjDG3grfwx7I131qTa/n2gZjMsH9LG1VF4q8MDgZQCJz5sbu87xrNSGgIcFPXuH43uUEBMpYkPypW43cRuoowloEwm1IRZNE2TzQVVfWRkTXXg0fQKKeplekaZZmXdKM/bo9+xYniWQ02XGvaY1/sZHo9g42QP04y2iOOtXUjBKQIYqBD04L8GIY/LafbT9/xdKnld4zvXfJy3O3VQ+jCk7X1ZBSQw8GoUN1NwLucvy/mvGyzZ6ViKsV084I3p
|   256 54:81:c0:a6:a6:c2:71:2a:07:22:45:98:e9:11:16:10 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFMXVQplwlZXDt5r1CXLlXeU+7RGeSeLHYs7/os/l/d24s6Vqz41w756VpJfvHIeZLil4Ka9EjT5nJ+u3MZLeI0=
|   256 6c:69:52:9a:76:91:98:a6:f1:d4:e9:7e:9e:71:2e:82 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIkT1IxbagEaJXC5rIvPEECtlIQS+P1/Av8r7k8Th4HD

80/tcp  open  http    syn-ack Apache httpd 2.4.7 ((Ubuntu))
|_http-title: WackoPicko.com
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.7 (Ubuntu)

111/tcp open  rpcbind syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          34337/tcp   status
|   100024  1          37222/udp6  status
|   100024  1          50341/tcp6  status
|_  100024  1          58249/udp   status

```
PHP version in http headers. I used `httpie`

Its `curl` on steroids (you can use whatever you want)

```
└──╼ $http 10.10.249.216       
HTTP/1.1 200 OK
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Connection: Keep-Alive
Content-Encoding: gzip
Content-Length: 1249
Content-Type: text/html
Date: Thu, 24 Mar 2022 16:53:51 GMT
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Keep-Alive: timeout=5, max=100
Pragma: no-cache
Server: Apache/2.4.7 (Ubuntu)
Set-Cookie: PHPSESSID=s4mck41b91f7l6rqmlrffta1d6; path=/
Vary: Accept-Encoding
X-Powered-By: PHP/5.5.9-1ubuntu4.24

```

## Methodology

>The first way is by going through every page and testing all the functionality. This would involve going through every page on the application, and depending on the functionality, testing for all the bugs/vulnerabilities that apply to the page. In this case, if we start off at the home page, we would try see what functionality we can exploit on the home page, and then move on to every page. 

>The second way is by breaking down the testing into different stages(including but not limited to):
>- Authorization
>- Authentication
>- Injection
>- Client Side Controls
>- Application Logic

### Authentication

- Brute Forcing/Weak Credentials

- Session Management 

Login with the classics of unrealistically stupid credentials and check the cookies

Then register on "wackopicko.com" to get user access

When you try to see your pictures you see this in the url

`http://10.10.249.216/users/view.php?userid=13`

The `userid` parameter is what you wanna mess with

You can do it manually like a savage or use automation (I am a savage lol)

You will get other's usernames on their picture page

There is also the bruteforce method (hydra mostly, I had issues filtering burp intruder and ZAP fuzzer )

But the first way is easier


### Cross-site scripting (XSS)

Xss is a star in the web pentesting vulnerability industry

>XSS is a vulnerability that involves injecting malicious javascript in trusted websites. Once an attacker has injected malicious javascript, sometimes a browser will not know whether to trust it, and it will run the script. Using this exploit an attacker can:

- steal session information through cookies
- arbitrarily redirect users to their own pages(for phishing)

>There are a few different types of XSS attacks:

- Persistent/Non-Reflected - Here the XSS payload has been stored in the database, and once the server/framework passes the data from the database into the webpage, the script/payload is executed

- Non Persistent/Reflected - Here the XSS payload is usually crafted using a malicious link. It is not stored. 

### Injection

When you have an 'injection' vulnerability, RCE or access is not far away

It's a great way in! So obviously those are hard to spot IRL

- SQL Injection

- Command Injection 

### Miscellaneous & Logic Flaws 

a.k.a the rest!

- Parameter Manipulation (we did that)

- Directory Traversal (Another famous one!)

- Forceful Browsing (The basics)


That room was cool as an introduction to "common web vulnerabilities"

It was rated medium but it was not that difficult actually

To wrap it up let's simply say that now you know what to look for when testing a web app

But in a real context this might not be that simple
