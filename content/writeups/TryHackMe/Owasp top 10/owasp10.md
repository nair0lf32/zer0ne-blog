 # OWASP top 10

<img src="owasp.png" width=200 height=200 alt="owasp">

If you started to learn web exploitation recently you might have heard about them

If you are already a computer wizard...well you definitelly heard about them

Here comes the TOP 10:

## 1 - (command) Injection

>Command Injection occurs when server-side code (like PHP) in a web application makes a system call on the hosting machine.  It is a web vulnerability that allows an attacker to take advantage of that made system call to execute operating system commands on the server

- blind command injection (you don't see the output directly)

- active command injection

well...for the practical part it's pretty easy as there is almost no command filter

Just use your `linux` basics knoweledge to answer the questions

## 2 - Broken Authentication

>If an attacker is able to find flaws in an authentication mechanism, they would then successfully gain access to other users accounts. This would allow the attacker to access sensitive data (depending on the purpose of the application)

- Bruteforce credentials / weak credentials

- Weak session cookies

Here also the task is trivial...not very realistic but hey...Just do as they say

## 3 - Sensitive data exposure

>When a webapp accidentally divulges sensitive data, we refer to it as "Sensitive Data Exposure"

- Names, dates-of-birth, financial information

- Usernames, Passwords 

- Man-in-the-middle (MITM) attacks...

Start the new machine to access the webapp and ALWAYS check the source code of the page

(you could also discover the directory with gobuster or ffuf)

the rest of the task is already explained

## 4 - XML External Entity (XXE)

>An XML External Entity (XXE) attack is a vulnerability that abuses features of XML parsers/data. It often allows an attacker to interact with any backend or external systems that the application itself can access and can allow the attacker to read the file on that system. They can also cause Denial of Service (DoS) attack or could use XXE to perform Server-Side Request Forgery (SSRF) inducing the web application to make requests to other applications. XXE may even enable port scanning and lead to remote code execution.

Another cool one! you need to understand `XML` a bit for this one

- In-band XXE

- Out-of-band XXE

Once again you are guided for the exploitation so...yeah!

Note that this vulnerability doesnt directly grant you machine access but with the sensitive files you can read like `/etc/passwd` and user's `ssh keys` (not very probable)
you can get further access

## 5 - Broken access control

>To put simply, broken access control allows attackers to bypass authorization which can allow them to view sensitive data or perform tasks as if they were a privileged user.

It's like...privilege escalation but for web apps users (lol kind of)

- Insecure Direct Object Reference (IDOR) (I like this one alot)

## 6 - Security Misconfiguration

>Security Misconfigurations are distinct from the other Top 10 vulnerabilities, because they occur when security could have been configured properly but was not

Another one on the dev team! here is the bingo for this one: 

- Poorly configured permissions on cloud services, like S3 buckets
- Having unnecessary features enabled, like services, pages, accounts or privileges
- Default accounts with unchanged passwords 
- Error messages that are overly detailed and allow an attacker to find out more about the system
- Not using HTTP security headers, or revealing too much detail in the Server: HTTP header

Wich ones did your website got? 


## 7 - Cross-site scripting (XSS)

>Cross-site scripting, also known as XSS is a security vulnerability typically found in web applications. It's a type of injection which can allow an attacker to execute malicious scripts and have it execute on a victim's machine

- Stored xss (most dangerous)

- Reflected Xss

- Dom-based Xss

This one is a real star in the industry. 

Mostly because it's very common and sometimes not taken seriously ("it's not server-side duh" shut up and check your code betty!)

`Javascript` is all you need sometimes...like for instance the next task 

## 8 - Insecure Deserialisation 

>"Insecure Deserialization is a vulnerability which occurs when untrusted data is used to abuse the logic of an application" (Acunetix., 2017)

>This definition is still quite broad to say the least. Simply, insecure deserialization is replacing data processed by an application with malicious code; allowing anything from DoS (Denial of Service) to RCE (Remote Code Execution) that the attacker can use to gain a foothold in a pentesting scenario.

Well...this one is not simple 

And you need to have good understanding of `object-oriented programming (OOP)`

The task is guided so just follow to get RCE!

## 9 -  Known Vulnerabilities

>Occasionally, you may find that the company/entity that you're pen-testing is using a program that already has a well documented vulnerability.

If it's known it should be patched! (else exploit-db got your back)

This one is ultra-easy to exploit (ask 'em script kiddies)

But nowadays most of the serious companies tend to patch their zero-day vulnerabilities very quickly (like...very very quickly)

## 10 - Insufficient Logging and Monitoring 

>When web applications are set up, every action performed by the user should be logged. Logging is important because in the event of an incident, the attackers actions can be traced. Once their actions are traced, their risk and impact can be determined. Without logging, there would be no way to tell what actions an attacker performed if they gain access to particular web applications

You got the point! this one is on the defensive side*

But what should be logged you ask? at least...

- HTTP status codes
- Time Stamps
- Usernames
- API endpoints/page locations
- IP addresses

But note that logging should be sanitized too

Recent events show that it can also be exploited for access

`log4j` patched it's biggest CVE already 

But not everyone updated it already (as it seems it's hard to even know if you are using it for logging XD) 

This was not really a ctf writeup but a quick recap 

Those are the most common web vulnerabilities according to OWASP (good guys)

I suggest you visit their website, as they update it very often :

[OWASP Top 10 website](https://owasp.org/www-project-top-ten/)


Good luck and have fun!