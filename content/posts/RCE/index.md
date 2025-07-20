---
title: "RCE"
date: 2024-04-13T03:03:31+01:00
draft: false
---

Hello hackers! It's been a while and today I wanna talk about a thing we all love: RCE.
For the sake of the normies that might stumble upon this article (google indexing works in mysterious ways),
RCE stands for Remote Code Execution. It's a vulnerability that allows an attacker to execute arbitrary code on a target machine. It's the holy grail of hacking, the ultimate goal of every Pentester and the worst nightmare of every sysadmin, it's often worth a lot of money in bug bounty programs and it's what those Hollywood hackers achieve when they say "I'm in". But what aspect of it make someone write an article at 3am? well... let's find out.

If you have been playing CTFs on sandBoxed platforms like "tryhackme" or "hackthebox" you might have encountered a few RCE challenges and when you submitted that flag your heart was filled with joy and pride, but someday you decided to move on to new platforms like "root me" or found a critical RCE IRL you try to get that RCE like you used to do...it's a vulnerability you exploited on Tryhackme before, so it should work right? well... not really. And then you realize RCE is not that simple IRL. That's what I wanna talk about today, the intricacies of RCE in real life.

I was much frustrated by this upon my learning journey so I need to do some ranting. When people told you that you needed solid networking knowledge to be a hacker they were not kidding. I won't teach networking to you all here, or how to get RCE (that would be disrespectful) so if you stumble on some words please use GOOGLE.

In SandBoxed platforms like tryhackme or Hackthebox (for elitists) they provide you a VPN connection to the target machine. They basically put you in the same network as the target machine. This is why you can easily exploit RCE vulnerabilities in these platforms. You can just run your exploit and it will work because you are in the same LAN as the target machine. The tun0 interface provides you a comfortable private IP address that you can use to communicate with the target machine.

But in real life, you are probably not in the same network as the target machine. You are over WAN, on the internet, that big cluster of LANs. You can't just communicate with any machine on internet because well, there are basic security measures or else anyone would be a hacker (lol). I will proceed now by talking about my Own setup and how I exploited RCE vulnerabilities over internet.

I have a [virtualBox](https://www.virtualbox.org/) VM running either Kali/Parrot OS/Athena on a Windows host (yeah I know, I am an heretic).
I either use bridged or NAT network mode with port forward (bridged preferred). Therefore my VM communicate
with its host machine over LAN. That is the easy part. Now the problem comes when you want to tell your target to reach you on your local machine. You can't just give them your private IP address because it's not routable over internet. On internet we communicate using public IP addresses and domain names.

But why can't you just use your public IP address? well, because you are probably behind a NAT. NAT stands for Network Address Translation. It's a technique that allows multiple devices to share a single public IP address. This is what your router does. It assigns a private IP address to each device on your network and then translates the private IP address to the public IP address when the device communicates with the internet. This is why you can't just use your public IP address to communicate with your local machine. Your router doesn't know which device to send the packets to.

Depending on your ISP, you might have a static public IP address or a dynamic public IP address. If you have a static public IP address, good for you, But if you have a dynamic public IP address, your public IP address changes every time you restart your router, which adds another layer of complexity. You might also be behind a CGNAT (Carrier Grade NAT) which is a type of NAT that is used by ISPs to share a single public IP address among multiple customers. This makes it even harder to communicate with your local machine.

So you need to make your local machine accessible over internet, and make it act like a server.
Multiple options are available to do this, you can use a VPS but that cost money...it's basically a server that you rent on the internet.

You can also either use a VPN like [OpenVpn](https://openvpn.net/) (free) or [Wireguard](https://www.wireguard.com/) that support port forwarding. This way, the target machine can communicate with your local machine over the VPN. This is a good option if you want to keep your local machine hidden from the internet.

Third option is similar to a VPN but is called a reverse ssh tunnel
like [ngrok](https://ngrok.com/) or [tunnelin](https://app.tunnelin.com/). They basically route the traffic from the target machine to your local machine through their servers, and
usually provide you a subdomain that you can use to communicate with your local machine. The downfall is that most are temporary solutions that refresh the subdomain every time you restart the tunnel (your address changes).

Now back to my personal experience. I faced this issue first on RootMe, then while playing the Hackerlab CTF. I wrote a writeup [here]({{< ref "/writeups/hackerlab/hackerlab-2022/" >}} "Hackerlab 2022") about it. More recently I got access to a machine using Metasploit. Here are the properties that are important to know:

- The target machine IP `RHOSTS` if using Metasploit: usually a public IP address (or a domain name)
- Your own IP `LHOST`: That's the tricky part. if like me you used a TCP tunnel you might get a domain name. You put that there! If you care about persistence you can use a dynamic DNS service like [no-ip](https://www.noip.com/) to get a domain name that will always point to your public IP address.
- The port `LPORT` that you used to listen for incoming connections: you have to use the port provided by the tunneling service.
- If you used Metasploit you need to set `ReverseListenerBindAddress` to your local IP address. By default it binds to your loopback interface so you might never need to change it. But if you are using a tunneling service you need to set `ReverseListenerBindPort` to your destination port.

You are all set! But what if you are not using Metasploit? well, you just need multiple terminals. One for your tunnel (ngrok much), one to listen for incoming connections (netcat, socat, ncat, etc)...You just use the same properties as above for your payload and your listener. I let you figure out what would logically go where. Also test multiple times...experiment and learn.

It's important to precise that those settings are mostly relevant if you use a reverse shell payload. If you use a bind shell payload, you  just need to make sure that the target machine can reach your local machine on the port you specified.

This is the end of my rant. I hope you learned something. This might be a terrible summary of what I learned but RCE is a complex topic and you need a bit of creativity and ingenuity to achieve it. Understanding how your network setup works is the ultimate key to success. After smashing my keyboard for hours I can gladly say to you people that "I'm in".
