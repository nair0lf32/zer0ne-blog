---
title: "Sakura room"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

{{< post-img src="sakura.png" alt="sakura" style="width: 200px;" >}}

A cool Osint room, and we love osint
time to join the dojo as a detective

## Tip-OFF

we are looking for a vilain...a cyberCRIMINAL!

we are provided with an [image](https://raw.githubusercontent.com/OsintDojo/public/3f178408909bc1aae7ea2f51126984a8813b0901/sakurapwnedletter.svg) hosted on github

I could not first download it...its even an svg

But analysing the source code get us this

```text
   inkscape:version="0.92.5 (2060ec1f9f, 2020-04-08)"
   sodipodi:docname="pwnedletter.svg"
   inkscape:export-filename="/home/SakuraSnowAngelAiko/Desktop/pwnedletter.png"
   inkscape:export-xdpi="96"
   inkscape:export-ydpi="96">>
```
I deduced that the username could be `SakuraSnowAngelAiko`

## Reconnaissance

we do like any osint professional...we google that username
we the name `Aiko Abe` from many sources like images and linkedin
from the github account we get a `PGP` repo with a `publickey`
we import that

```bash
└──╼ $gpg --import publickey
gpg: clef ECDD0FD294110450 : clef publique « SakuraSnowAngel83@protonmail.com » importée
gpg:       Quantité totale traitée : 1
gpg:                     importées : 1
```

And as expected we are provided with origin info, the mail :

`SakuraSnowAngel83@protonmail.com`

protonmail is a pretty solid and secure mail service though

## Unveil

On github there is a `ETH` repository with a `miningscript` check the history for the person's `ethereum address`

```bash
stratum://0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef.Aiko:pswd@eu1.ethermine.org:4444
```
we visit `ethermine.org` and there we can search by wallet address
go to `payouts` tab and check for `January 23, 2021 UTC` transaction
exploring he transactions you can see in details one about `tether usd` too

## Taunt

Now we go to twitter (that beloved place)
the bold attacker sent a message that we are provided a screenshot of

{{< post-img src="screenshot.png" alt="screenshot" style="width: 300px;" >}}

Google exactly `AikoAbe3` twitter to not be fooled by others fake accounts
Once you get the handle with the sakura stuff...
In one tweet that criminal says

```text
Not too concerned about someone else finding them on the Dark Web.

Anyone who wants them will have to do a real DEEP search to find where I PASTEd them.
```

All the hints were pointing us toward the dark web anyway (another charming place)
Ever heard about `deeppaste` son? google it for onion links! you like onions?
Too bad the website was down...and I am not feeling like waiting right now so I just use the hint
your patience is gona be tested anyway, as typing all the long link by hand is no joke
Now when it comes to wifi and osint I go to `wiggle.net`
used that website before and its pretty cool
An advanced search there will give you the `BSSID`

## Homebound

Back to twitter, we analyse the tweet pictures
The filthy criminal scum retweeted about `bethesda` cherryblossoms
google that for a close airport code (in washington)
Always from twitter pics we see `sakura lounge JAL` seems like its in `haneda` airport
Google for the codes,
Then Go to Google maps and look for a lake in the area
This part was not easy for me...mostly focus to try and recognize the general shape
then its trial and error, to help you its a lake close to fukushima, in the middle of the  japan map
From wifi data the attacker might be heading to `hirosaki, japan`, their home
Not we got'em! Right to jail!
