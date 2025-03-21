---
title: "My Favorite Tools"
date: 2022-09-17T18:33:31+01:00
draft: false
---

Just a list of cool cybersec tools! The ones I use the most ( or not ) and the one I discovered during my journey. Ordered by categories (kinda)

## Reconnaissance & Enumeration

| Scanning                                                  | Footprint                                                      | Discovery                                                  |
| --------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------- |
| [Nmap](https://nmap.org/) (good old)                      | [Recon-ng](https://github.com/lanmaster53/recon-ng)            | [Gobuster](https://github.com/OJ/gobuster)                 |
| [Rustscan](https://github.com/RustScan/RustScan)          | [BlackWidow](https://github.com/1N3/BlackWidow)                | [ffuf](https://github.com/ffuf/ffuf)                       |
| [NmapAutomator](https://github.com/21y4d/nmapAutomator)   | [CmSeek](https://github.com/Tuhinshubhra/CMSeeK)               | [Sublist3r](https://github.com/aboul3la/Sublist3r)         |
| [angryIP](https://github.com/angryip/ipscan) (angry scan) | [Eyewitness](https://github.com/FortyNorthSecurity/EyeWitness) | [VhostScan](https://github.com/codingo/VHostScan/)         |
| [Massscan](https://www.kali.org/tools/masscan/)           | [Recon](https://github.com/dirsoooo/Recon) (All in one)        | [SubFinder](https://github.com/projectdiscovery/subfinder) |
|                                                           | [Shodan](https://www.shodan.io/dashboard) (the iot scanner)    |                                                            |
|                                                           | [WpScan](https://wpscan.com/) (WordPress favorite)             |                                                            |
|                                                           | [DnsDumpster](https://dnsdumpster.com/) (dig on steroids!)     |                                                            |
|                                                           | [Ahmia](https://ahmia.fi/)  (dark web search)                  |                                                            |
|                                                           | [WHOIS](https://who.is/) (nothing beat basics)                 |                                                            |
|                                                           | [viewDns](https://viewdns.info/) (whois++)                     |                                                            |
|                                                           | [webcheck](https://web-check.xyz/) (vibe check)                |                                                            |

## Vulnerability scanners ( For either professionals, lazy people, or both)

| Free (for you and me)                                         | Paid (If you got money)                                                       |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [Nikto](https://github.com/sullo/nikto) (technically correct) | [Acunetix](https://www.acunetix.com/)                                         |
| [RapidScan](https://github.com/skavngr/rapidscan) (Try it!)   | [Nessus](https://www.tenable.com/products/nessus) (technically it's not free) |
| [OpenVas](https://www.openvas.org/)                           | [Nexpose](https://www.rapid7.com/products/nexpose/) (free trial)              |
| [Vega](https://subgraph.com/vega/)                            |                                                                               |

## Exploitation

| Frameworks and payload generators                              | Common exploits                                              |
| -------------------------------------------------------------- | ------------------------------------------------------------ |
| [Metasploit](https://www.metasploit.com/) (The unmatched)      | [Exploitdb](https://www.metasploit.com/) (searchsploit)      |
| [Getsploit](https://github.com/vulnersCom/getsploit) (vulners) | [SqlMap](https://sqlmap.org/)                                |
| [PentestMonkey](https://pentestmonkey.net/) (instant shell)    | [NosqlMap](https://github.com/codingo/NoSQLMap)              |
| [RevShells](https://www.revshells.com/) (shells of quality)    | [AttackerKB](https://attackerkb.com/) (information is power) |
| [P.A.T.T](https://github.com/swisskyrepo/PayloadsAllTheThings) | [commix](https://www.kali.org/tools/commix/)                 |
|                                                                | [Slowloris](https://github.com/gkbrk/slowloris) (Don't)      |

### Web (specials)

| Proxies                                                                         | Frameworks and other scanners                                          |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [BurpSuite](https://portswigger.net/burp/communitydownload) (community edition) | [Arachni](https://github.com/Arachni/arachni)                          |
| [OWASP ZAP](https://www.zaproxy.org/) (It's from OWASP)                         | [Golismero](https://github.com/golismero/golismero)                    |
| [DnsTwist](https://github.com/elceef/dnstwist)                                  | [Leviathan](https://github.com/utkusen/leviathan) ( sadly DEPRECATED ) |
| [Caido.io](https://caido.io/)                                                   |                                                                        |

## Cloud (specials)

- [ScoutSuite](https://github.com/nccgroup/ScoutSuite)
- [CloudMapper](https://github.com/duo-labs/cloudmapper)

### Windows (specials)

| Specific services                                      | Active Directory                                             | Post-exploit                                                  |
| ------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------- |
| [Enum4Linux](https://www.kali.org/tools/enum4linux/)   | [Kerbrute](https://github.com/ropnop/kerbrute)               | [Mimikatz](https://www.kali.org/tools/mimikatz/) (the looter) |
| [EvilWinRM](https://github.com/Hackplayers/evil-winrm) | [Impacket tools](https://github.com/SecureAuthCorp/impacket) |                                                               |
|                                                        | [CrackMapExec](https://github.com/byt3bl33d3r/CrackMapExec)  |                                                               |
|                                                        | [Bloodhound](https://www.kali.org/tools/bloodhound/)         |                                                               |

## Android (specials)

| Analysis                                                                                    | Attacks                                                                       |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF)                           | [SARA](https://github.com/termuxhackers-id/SARA) (careful with this one)      |
| [ApkTool](https://ibotpeaches.github.io/Apktool/)  (uses jadx)                              | [backdoor-apk](https://github.com/dana-at-cp/backdoor-apk)                    |
| [Adb](https://developer.android.com/studio/command-line/adb)                                | [TheFatRat](https://github.com/Screetsec/TheFatRat) (obese rodent)            |
| [Anbox](https://docs.anbox.io/userguide/install.html) (or any emulator for dynamic testing) | [MsfVenom](https://www.offensive-security.com/metasploit-unleashed/msfvenom/) |
| [Zimperium tools](https://www.zimperium.com/) (yeah...kinda)                                |                                                                               |
| [Apkleaks](https://github.com/dwisiswant0/apkleaks)                                         |                                                                               |
| [MARA](https://github.com/xtiankisutsa/MARA_Framework)                                      |                                                                               |
| [Drozer](https://github.com/FSecureLABS/drozer)                                             |                                                                               |
| [Inspeckage](https://github.com/ac-pm/Inspeckage)                                           |                                                                               |
| [Quark](https://github.com/quark-engine/quark-engine)                                       |                                                                               |
| [DeGuard](http://apk-deguard.com/)                                                          |                                                                               |

## Cryptography

| Crackers                                                                               | Hashes                                                    | Decoders                                       |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------- |
| [John](https://www.kali.org/tools/john/) (the ripper)                                  | [HashCat](https://hashcat.net/hashcat/) (a cat)           | [Dcode](https://www.dcode.fr/)                 |
| [Hydra](https://www.kali.org/tools/hydra/) (the legacy)                                | [CrackStation](https://crackstation.net/)                 | [Cyberchef](https://gchq.github.io/CyberChef/) |
| [SSHTrix](https://nullsecurity.net/tools/cracker.html) (for ssh)                       | [HashCrack](https://hashcrack.com/)                       | [jwt](https://jwt.io/)                         |
| [Ciphey](https://github.com/Ciphey/Ciphey) and [Ares](https://github.com/bee-san/Ares) | [Hashes.com](https://hashes.com/en/decrypt/hash)          | [Boxentriq](https://www.boxentriq.com/)        |
|                                                                                        | [Hash analyzer](https://www.tunnelsup.com/hash-analyzer/) |                                                |
|                                                                                        | [md5hashing](https://md5hashing.net/)                     |                                                |

## wordlist generators

- [Mentalist](https://github.com/sc0tfree/mentalist) (It got a GUI)
- [Cupp](https://github.com/Mebus/cupp) (old reliable)
- [Cewl](https://www.kali.org/tools/cewl/) (if you like spiders)

## Reverse Engineering / Binary exploitation

| Disassembler Frameworks                                      | Debuggers and Decompilers                                                                                                                                                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [IDA Pro](https://hex-rays.com/ida-pro/) (industry standard) | [GDB](https://www.sourceware.org/gdb/) (check [PwnDbg](https://github.com/pwndbg/pwndbg), [PEDA](https://github.com/longld/peda), [gef](https://github.com/hugsy/gef) and [OllyDbg](http://www.ollydbg.de/)) |
| [Ghidra](https://ghidra-sre.org/) (pride of the NSA)         | [Cutter](https://cutter.re/)                                                                                                                                                                                 |
| [Radare2](https://github.com/radareorg/radare2)              | [PwnTools](https://pypi.org/project/pwntools/) (technically...)                                                                                                                                              |
| [DogBolt](https://dogbolt.org/) (also check godbolt.org)     |                                                                                                                                                                                                              |

## Steganography

| Embedded data and Text                              | Image Manipulation                                                                   | Audio                                                |
| --------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| [steghide](http://steghide.sourceforge.net/)        | [StegSolve](https://en.kali.tools/all/?tool=1762)                                    | [Sonic visualizer](https://www.sonicvisualiser.org/) |
| [stegseek](https://github.com/RickdeJager/stegseek) | [StegoSuite](https://installlion.com/kali/kali/main/s/stegosuite/install/index.html) | [Audacity](https://www.audacityteam.org/)            |
| [ExifTool](https://exiftool.org/) (might work)      | [Gimp](https://www.gimp.org/)  (PhotoShop or whatever)                               | [Morse decoder](https://morsecode.world/)            |
| [PlainSight](https://github.com/rw/plainsight)      | [Zbar-tools](http://zbar.sourceforge.net/)                                           |                                                      |
|                                                     | [FotoForensics](https://fotoforensics.com/)                                          |                                                      |
|                                                     | [ZSteg](https://github.com/zed-0xff/zsteg)                                           |                                                      |
|                                                     | [AperiSolve](https://aperisolve.com)                                                 |                                                      |

## Wifi

- [Wifite 2](https://github.com/derv82/wifite2)
- [kismet](https://www.kismetwireless.net/)
- [Aircrack suite](https://www.aircrack-ng.org/) (the OG)

## Privilege escalation

- [Linenum](https://github.com/rebootuser/LinEnum)
- [GTFOBins](https://gtfobins.github.io/) (the ultimate)
- [PEASS tools](https://github.com/carlospolop/PEASS-ng)
- [JAWS](https://github.com/411Hall/JAWS)

## Post-exploitation

| Command and control (C2)                                                            | Persistance (Rootkits +++) pivot and more       |
| ----------------------------------------------------------------------------------- | ----------------------------------------------- |
| [Cobalt strike](https://cobalt-strike.github.io/community_kit/) (industry standard) | [Reptile](https://github.com/f0rb1dd3n/Reptile) |
| [PwnCat](https://github.com/calebstewart/pwncat) (another cat)                      | [chisel](https://github.com/jpillora/chisel)    |
| [Empire](https://www.powershellempire.com/) ([deprecated] check StarKiller)         |                                                 |
| [Metasploit](https://www.metasploit.com/) (yes, again!)                             |                                                 |
| [Covenant](https://github.com/cobbr/Covenant/)                                      |                                                 |

## Social Engineering

- [SET](https://www.trustedsec.com/tools/the-social-engineer-toolkit-set/) (number one)
- [ThisPersonDoesNotExist](https://thispersondoesnotexist.com/) (don't misuse this one)
- [NameFake](https://namefake.com/) (do not misuse it!)

## OSINT

- [OSINT Framework](https://osintframework.com/) (its a framework)
- [OSINT techniques](https://www.osinttechniques.com/osint-tools.html)
- [wigle](https://wigle.net/) (google maps for networks)
- [Maltego](https://www.maltego.com/) (Feel like a Professional)
- [WayBack machine](https://archive.org/web/) (time travel powered by internet)
- [IntelX](https://intelx.io/tools?tab=facebook)
- [SpiderFoot](https://www.spiderfoot.net/)
- [Sherlock](https://github.com/sherlock-project/sherlock) (elementary)
- [BBot](https://github.com/blacklanternsecurity/bbot)
- [fbi](https://github.com/xHak9x/fbi) (might be dead)

## Anonymity and Evasion

- [AnonSurf](https://linuxhint.com/anonsurf/)
- [Obfuscator.io](https://obfuscator.io/)
- [UACME](https://github.com/hfiref0x/UACME)
- [kali-whoami](https://github.com/owerdogan/whoami-project)
- [De4js](https://lelinhtinh.github.io/de4js/)
- [UnProtect it](https://www.unprotect.it/)

## Forensics

- [Volatility](https://www.volatilityfoundation.org/)
- [BinWalk](https://github.com/ReFirmLabs/binwalk)
- [Foremost](https://www.kali.org/tools/foremost/)
- [Autopsy](https://www.sleuthkit.org/autopsy/)

## Malware Analysis

- [VirusTotal](https://www.virustotal.com/gui/) (too famous)
- [Pithus](https://beta.pithus.org/) (for android)
- [VxUnderground](https://vx-underground.org/) (what is the password?)

## Utilities (Browser extensions and such )

- [FoxyProxy](https://addons.mozilla.org/fr/firefox/addon/foxyproxy-standard/) (you know this one)
- [OneCompiler](https://onecompiler.com/) (underrated online compiler)
- [Hack-tools](https://addons.mozilla.org/fr/firefox/addon/hacktools/) (this one is cool)
- [coding tools](https://coding.tools/)
- [ua-switcher](https://addons.mozilla.org/fr/firefox/addon/user-agent-string-switcher/) (custom ua)
- [code beautify](https://codebeautify.org/) (does a lot more than that)
- [search by image](https://addons.mozilla.org/fr/firefox/addon/search_by_image/)
- [busybox](https://busybox.net/) (unix binaries for everyone)
- [LolBas](https://lolbas-project.github.io/#)
- [NirSoft](http://www.nirsoft.net/) (don't ruin it's reputation)
- [FreeFormatter](https://www.freeformatter.com/)
- [whatPortis](https://github.com/ncrocfer/whatportis)
- [GitTools](https://github.com/internetwache/GitTools)
- [extendsclass](https://extendsclass.com/)

## Threat detection, network monitoring and remediation

- [Splunk](https://www.splunk.com/) (If you understand it)
- [MITRE ATT&CK](https://attack.mitre.org/)                   |
- [Wireshark](https://www.wireshark.org/download.html) (the shark)
- [GreyNoise](https://viz.greynoise.io/)
- [sysinternals](https://docs.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite)
- [AttackerKB](https://attackerkb.com/contributors/nair0lf32) |

# My favorites ( kek )

My most used tools, mostly defines my typical process

- Utilities
  - Google (your best friend! I google a lot)
  - [ngrok](https://ngrok.com/) (Because IRL network setup is painful)
- Enumeration:
  - [Rustscan](https://github.com/RustScan/RustScan) + [Nmap](https://nmap.org/) (Fast combo when configured correctly)
  - [Gobuster](https://github.com/OJ/gobuster) or [Ffuf](https://github.com/ffuf/ffuf) (both are fast! one fuzz faster! guess which one)
- Access (exploitation):
  - [Meta-f*cking-sploit](<https://www.metasploit.com/>) (expect it again)
  - [SqlMap](https://sqlmap.org/) (will sql injection be obsolete in the future?)
- Post-Exploitation:
  - [GTFObins](https://gtfobins.github.io/) (useful hindsights)

For Other challenges:

- Crypto: dcode, CrackStation, RapidTables converter...
- Forensics: volatility

For when I am lazy:

All-in-one and frameworks/Auto-Exploiters:

- [Pentest-tools](https://app.pentest-tools.com/) with their [playground](https://pentest-ground.com/)
- [RapidScan](https://github.com/skavngr/rapidscan)
- [VulnX](https://github.com/anouarbensaad/VulnX)
- [HackingTool](https://github.com/Z4nzu/hackingtool) (this thing is a big bundle)
- [AutoSploit](https://github.com/NullArray/AutoSploit)
- [XAttacker](https://github.com/Moham3dRiahi/XAttacker)
- [FSociety](https://github.com/Manisso/fsociety) (to feel like Mr Robot)
- [Monkey](https://github.com/guardicore/monkey) (I swear it's their real name)
- Vulnnr (DEAD)
- [Sn1per](https://github.com/1N3/Sn1per)
- [Jok3r](https://github.com/koutto/jok3r)

# More tools (Moarrrr!)

Here is a list of places to find more tools:

- [Github](https://github.com) ( a lot in here! ) also check [this repository](https://github.com/Hack-with-Github/Awesome-Hacking), [this one](https://github.com/apsdehal/awesome-ctf) and [this guy](https://github.com/mgeeky)
- [Kitploit](https://www.kitploit.com/)
- [BlackArch tools](https://blackarch.org/tools.html) (Or any Pentest Linux distro tools)
- [kali tools](https://en.kali.tools/all/?category)
- [random medium article](https://shamsher-khan-404.medium.com/100-most-vulnerable-apps-systems-platforms-to-practice-penetration-testing-2021-e76ca7235e74)
- [Linux security](https://linuxsecurity.expert/security-tools/)
- [RawSec tools](https://inventory.raw.pm/tools.html)
- Also Google

There are also some shady places (mostly onion links) with mad awesome tools, but we are not going there. Also if for any reason you want to do Pentesting from a windows machine (for whatever reason) you could look into [PentestBox](https://pentestbox.org/) instead of downloading tools separately. But this is a bit old (2016) and tools are not updated regularly. [WSL](https://docs.microsoft.com/en-us/windows/wsl/) looks like a better option.

*Do not feed the script kiddy in you. Tools are cool but knowledge is better!* ( But tools are cool though )
