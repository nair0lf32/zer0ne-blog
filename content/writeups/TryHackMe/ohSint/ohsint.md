---
title: "Ohsint"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

Oh boy I love OSINT...makes you feel like a detective and stuff

we got a picture only to start

![image](WindowsXP.jpg)

I already think about exif data and steganography

```
exif WindowsXP.jpg
Données corrompues
Les données fournies ne respectent pas les spécifications.
ExifLoader: Les données fournies ne semblent pas contenir de données EXIF.
```

there is no exif data...no wait there is little data in image properties

```
copyright: lang="x-default" OWoodflint
lat: 54,17.687778N
lon: 2,15.022104W
```

`Googling OWoodflint` get us stuff...hehe we are on right tracks

`Twitter` and `github` accounts gave us those

```
Hi all, I am from London, I like taking photos and open source projects.

Follow me on twitter: @OWoodflint

This project is a new social network for taking photos in your home town.

Project starting soon! Email me if you want to help out: OWoodflint@gmail.com
```

with the wifi bssid we get we visit `wigle.net` (map of networks)

The person also got a `wordpress` blog

```
Oliver Woodflint Blog
Im in New York right now, so I will update this site right away with new photos!
```

the password part was the least obvious

Always inspect source code

From the wp blog code:

```
<p style="color:#ffffff;" class="has-text-color">pennYDr0pper.!</p>
</div><!-- .entry-content -->
```

So all informations gathered:

```
name: Oliver WOODFLINT
username: OWoodflint
profile_picture: cat
city: London, charles II street (B327)
wifi Bssid: B4:5D:50:AA:86:41
wifi SSID: UnileverWifi
email:OWoodflint@gmail.com
password: pennYDr0pper.!
```

Elementary, my dear Watson!
