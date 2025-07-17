---
title: "Hacking methodology"
date: 2022-10-01T20:10:31+01:00
draft: false
---

It's not about the general methodology (you can easily get this one on google) but it's about mine (quick reminder: I own this place!). In simpler words I will just talk about how I do my things, aka how I tackle CTFs challenges (and problems in general). I will also talk about my favorite categories of challenges so "buckle up buckaroos!"

## My Methodology

Took me time to define my own hacking methodology and it might still change (improvements plz). I was very confused as a beginner on my first CTF. Hacking communities are know to be very welcoming nowadays but for the sake of effort no one will just serve you flags, answers or even hints sometimes. Don't get me wrong that's a very good thing because that's exactly what it's about so you know what to expect. They will instead point you toward general concepts or learning material. Got it already? First thing you need in the cyber is `curiosity`. Seriously, wanna "hack" anything you do not understand yourself? You better learn to `Google` real quick

I won't tell you the generic things like "you need to know this and that..." to get into cybersecurity or play CTFs but there is a general methodology to know.

What? you want me to give it to you? You better love to google things real real quick!

Personally I follow three big steps and one general rule.

## Step 1: Reconnaissance

If you googled already you expected me to start here! You also already know it's about knowing what you are dealing with. You mostly need either `experience` (practice a lot), `big brain time` (analysis and deduction) or both.

"Oh this is an easy crypto challenge? oh I know this one it's ROT13!" That's experience.

But before you get there the second type of person would be like:

"Hmm! a cryptography challenge. I notice every letter is a shift of an alphabet letter" That guy would probably grab a pen and paper and furiously manually decode it. That's analysis for you.

But let's be honest such scenario is not very common. Now there is me:

"what the f*ck is that?"

*Copy pastes the encoded ROT13 on Google, reads some results, add cryptography to the search query and learn about ROT13

"Oh okay" *Decodes it with the online tool I just found and added to my collection

Basically, that's what I do! mostly Google! I have no shame!

Be it a challenge, a lab, a machine...If I don't know it I Google it! Obviously it doesn't always work (Google-fu is an art)

Now you already noticed I said this first step was about "Reconnaissance"...The mainstream thing to know is how to get `information` about your target. But as not every kind of information is on Google you still need your brain + automated tools. Brain first because you have to know what tool to use. I talk about my tools in [another post](posts/My-Favorite-Tools.md)
Also I won't teach enumeration or reconnaissance here (it's a huge subject). But how do I do it when Google isn't enough?

Every machine starts with a `nmap` scan (or `rustscan` if you are not that patient). But once the scan is over and you see the open ports and available services that's where your "analysis" should kick in! The next steps is the funniest one

## Step 2: Exploitation

Here again I basically Google everything! It's the part where you take advantage of the information you got (step 1) to solve the problem. But there are many types of problems and solving methods are too specific to be debated here so I will just talk about my favorite ones

- Machines/Systems: So far I know about Linux and Windows. Those usually need the most enumeration. These types of challenges are usually to showcase a common vulnerability (`exploitdb` and `github` got your back) or you get access through a server (web,ssh,rdp...). Once again Google will save you
- Cryptography: Oh I love those! they go from "`cyberchef`,`boxentriq` or `dcode` will do" to "you have to reverse engineer the whole Cypher or encoding method to decode this one" (you might need some `scripting` skills for the reverse engineering part...just...just learn `python`)
- OSINT: This one would go into reconnaissance but it takes more critical thinking than you think so add it to a LOT of Google searches
- Steganography: You need hints to even think about this one! sometimes the context helps...sometimes the author is just like "f*ck you! here is a picture" (with obviously no exif data). If they were nice you have to `stegseek` the `steghide` passphrase, else you have to deduce it from "context". And if it's not a picture, well you know what to do!
- Pwn/Binary exploitation: input mad long characters sequences, Learn `C`, Learn some `Assembly`, cry a little, then just run any `decompiler`, `debugger` or `disassembler` you know and hope for the best
- Android: Install `android studio` first, Learn to decompile `apk` and get familiar with `proxies`
- Web: Memorize `The OWASP top 10` vulnerabilities and how to exploit them, Fire up `BurpSuite` or your favorite proxy on every input field you ever see

Now to those who expected step 3 to be about `privilege escalation`, SIKE! I put privilege escalation here in step 2 because it's my methodology steps and not my hacking steps!

I consider privesc a form of exploitation (just local). You mostly have to learn about this one, because the common vectors are already known. Or use noisy scripts like `linpeas` or `winpeas` to win some time.

## Step 3: Writeups

After you did everything (succeed or failed miserably) writeups are an important step (well, for me at least).

If you solved the problem, it's time to write about how you did it! It will help you retain information better. I often re-read my old writeups to solve similar challenges. Also you can help others by doing so, and you should read other's writeups to learn alternative ways of solving the problem. They probably did it differently and you might wanna be aware of that.

If you were just stuck for too long (This is very relative) and wanna move on you can read a writeup (YES you CAN). I personally think learning is the most important thing in all this, so whenever I admit the challenge was too hard for me I look for writeups. But it should usually be a last resort. Most platforms have forums and ChatRooms where you can get hints before going for a whole "tutorial". Also never EVER accept writeups that give flags or answers away. That's sh*tty learning material. Even after reading the writeup, close it and re-do the challenge yourself. You retain more by doing than just reading, so that's the whole point

Now what if no writeup is available?

well...either no one bothered writing one because it was too trivial (less probable) or the difficulty was so insane authors wanted to keep it challenging for people of such level and also strongly disallowed public writeups (more probable)

Either way you just have to `try harder` or leave the challenge unsolved. You cannot solve everything and an unsolved challenge just mean you are not there yet so do something else and try again later...

## Rule: Keep it simple

I said I had a rule for any problem I face...well I like to `keep it simple`. I am not the "very smart" kind of person (more like a "meh") so I easily get confused by complex situations. I also have a hard time focusing on them, so I am a big fan of `Divide-and-conquer algorithm` (Google it). I apply it on "everything"! Whenever the problem seems big `break it down`. Smaller problems still big? break them down again and solve separate trivial tasks! Assemble the smaller solutions and voilà, big problem solved!

This is mostly used in computer science but I think this can be applied to many CTFs or real life problems as well...you just need to know how to "break it down"
