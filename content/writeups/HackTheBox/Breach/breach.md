---
title: "Breach"
date: 2022-09-20T14:03:31+01:00
draft: false
categories:
  - HackTheBox
---

Osint challenge!

Starting with the job anouncement docx file we google `supersecurestartup.com`


The website is empty...ignore that yet

twitter got better informations..so we read all those tweets and replies

and we end up with 4 interresting people

```
Josh Terranwald (@JTerranwald) : Web Developer, Father, Full of front of stack passion

Johanna Boyce (@boyce_johanna) : HR Manager at Super Secure Startup

Alia Mccarty (@mccarty_alia) : Internal Communications Designer at Evil Corp LLC, secret nerd, loves role playing - it's all about communication!

Bianka Phelps (@BiankaPhelps) : HR professional at Super Secure Startup

```

Alia is the most suspicious one...

`What Clas-ERR HTB{s are you?`

and she likes dnd...alot?

`Crest is the key` 

actually...nah don't bother that nerd is a rabbit hole

when you grep those 4 employees names in the data breach txt file only two appears:

- johanna : password doesnt work
- bianka : password doesnt work NEITHER? 

at this point I was confused alot but the forums helped

looking at how bianca made the password: 'Love!July2018'

she could have changed the months or year...the timeline on twitter is around:

- March 2019 : `Love!March2019` 

It worked! the key is just the flag in base64!
