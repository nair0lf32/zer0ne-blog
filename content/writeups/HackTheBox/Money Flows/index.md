---
title: "Money Flowz"
date: 2022-09-20T14:03:31+01:00
draft: false
categories:
  - HackTheBox
---

Another OSINT challenge

We have to know how `Frank Vitalik` make his money

Yeah...why would people make money? we have to know
we obviously google his name and get stuff

He got a reddit account

```text
Frank Vitalik
u/frankvitalik
Cryptocurrency enthusiast @htb My Twitter account @frankvitalik was restricted


Incredible SCAM giveaway! you can get free coins!

Follow the link to get free fake coins!!

https://steemit.com/htb/@freecoinz/freecoinz

```

Ok he does crypto SCAMS

(Case solved! lol)

On the website there is a ropsten etherum address. We follow that
So basically on this website you can see all his transactions

`https://ropsten.etherscan.io/address/0x1b3247cd0a59ac8b37a922804d150556db837699`

Now the task say "where he gets the money from"
there are two outbound transactions
so lets check the sender's addresses
In the oldest transaction deploy "see more" and you see an address in comment
see it as 'utf-8' and there is your flag!

