---
title: "Scripting"
date: 2022-10-09T22:03:31+01:00
draft: false
---

When it comes to hacking, people usually imagine a dangerous criminal lurking in his basement (black hoodie is a bonus), furiously smacking a keyboard, typing incomprehensible code directly in a terminal with green on black font. Well...if media didn't make a fool of you...It's not even close to reality. Ok maybe a little bit. A hacker is usually talented at coding. Not necessarily a criminal, but it is a person talented with computers. He knows so much about how they work he can spot malfunctions and well...abuse those malfunctions if he is the said criminal or fix them if he is a good guy. For the coding part, well...I said "usually". Some so-called hackers can get into a system without typing a single line of code.

So the usual question is "Do I need to learn coding before being a hacker?"

Basically I'd say it depends of your definition of a hacker. it's not a requirement, but if you want to be efficient, you need to learn it.

"But coding is a vast domain that can take years to master and there are dozens of programming languages. How would I learn all that?"

Then you better get started!

I am actually not here to talk about how much coding you need to do some "hacking" or play a CTF. Instead I want to talk about how I do it! (yeah it's mostly about me here). I made a [post](posts/Hacking-methodology.md) about my hacking methodology, where I explain how I basically google my way out of everything. well there is one kind of problems you cannot always solve by using google alone. You need a functional brain for those. Programming problems require logic and good syntax knowledge (this one can be Googled). So for some tasks you need to write some scripts.

What are the Scripting languages I use? It's the whole point of this article

## [Python](https://www.python.org/)

Obviously I start with python! If there is one thing this language is known for is HOW FAST IT IS...(*dodges rotten tomatoes)...TO DEVELOP WITH. Python with its dozen of libraries makes the development process way easier and faster. People already solved that problem for you, why reimplement the wheel? just `import this` ...and face the problems of someone else. In hacking you have to be fast and quickly implement a Poc for your exploits so python fits perfectly. Here are my favorite libraries:

- [requests](https://pypi.org/project/requests/). You expected this one! obviously it's for http requests, and it makes that way too simple. This one is very often used in coding challenges to scrape data from a given website, so you usually add [beautifulsoup](https://pypi.org/project/beautifulsoup4/) (or [scrapy](https://pypi.org/project/Scrapy/)).

- [cryptography](https://pypi.org/project/cryptography/) does what it says. It's a cryptography Swiss-knife. Just like [pycryptodome](https://pypi.org/project/pycryptodome/), you can make those work with other modules like [hashlib](https://docs.python.org/3/library/hashlib.html), [base64](https://docs.python.org/3/library/base64.html)...

- [PwnTools](https://pypi.org/project/pwntools/) describe itself as a CTF framework for exploit development. Do I need to add anything else? I just love how it makes remote socket connections easier than the [socket](https://docs.python.org/3/library/socket.html?highlight=socket#module-socket) module itself. But I had to use the latter for an IRC challenge so it still rocks.

- [Impacket](https://pypi.org/project/impacket/) is another famous name in CTFs, for anything network-related. It allows easy connection using many protocols. I used it mostly against windows, for SMB connections. Also check [RawSocketPy](https://pypi.org/project/rawsocketpy/) for connections relying mostly on MAC addresses (WIFI/ETHERNET).

- [Scapy](https://pypi.org/project/scapy/) Is for network packets analysis. Its power is a bit underrated IMO. For packet injection you might as well look at [Pylibnet](https://pylibnet.sourceforge.net/). No need to install this one it comes with your python 3 installation.

There are many other libraries and even implementations of full-fledged hacking frameworks or tools in python, but those are the ones mostly used to quickly come up with a working solution. The tool used is not the most important thing. It's how you solve the problem (fast? efficient? re-usable?) that matters.

## [bash](https://www.gnu.org/software/bash/)

I do not write a lot of `bash` scripts yet but I think it is a language you definitely need to automate your Linux tasks. I mostly use quick one liners to perform quick actions, like filtering a wordlist with `awk` and `sed`, find things with `find` and `grep`... But we all know bash is more powerful than that and I definitely recommend you getting familiar with it.

## Others

well...It was a short list right? You are dead wrong! I just wanted it that way because there is a lot of scripting languages you could use. [perl](https://www.perl.org/) and [ruby](https://www.ruby-lang.org/en/) could fit too, but the two above are the ones I use so far. [C](https://en.wikipedia.org/wiki/C_(programming_language)) is not a scripting language but I think it's another one you should know for CTFs! If you are interested in tools development and obviously you want those tools to be fast, there are new players in the arena: [Golang](https://go.dev/) and [Rust](https://www.rust-lang.org/). You can also use Golang for scripts and PoCs.
Anyway, those languages are mere tools that will automate your solutions to any problem. The most important thing will always be your ability to come up with the said solutions.
