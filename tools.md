# Tools

Just a list of cool cybersec tools! The ones I use the most ( or not )

and the one I discovered during my journey

Ordered by categories (kinda)

## Reconnaissance & Enumeration 

| Scanning                                                  |  Footprint                                                        | Discovery
| --------                                                  |  ---------                                                        | ---------
| [Nmap](https://nmap.org/) (good old)                      | [Recon-ng](https://github.com/lanmaster53/recon-ng)               | [Gobuster](https://github.com/OJ/gobuster) 
| [Rustscan](https://github.com/RustScan/RustScan)          | [Blackwidow](https://github.com/1N3/BlackWidow)                   | [Ffuf](https://github.com/ffuf/ffuf)
| [NmapAutomator](https://github.com/21y4d/nmapAutomator)   | [Cmseek](https://github.com/Tuhinshubhra/CMSeeK)                  | [Sublist3r](https://github.com/aboul3la/Sublist3r)
| [onesixtyone](https://github.com/trailofbits/onesixtyone) | [Eyewitness](https://github.com/FortyNorthSecurity/EyeWitness)    | [VhostScan](https://github.com/codingo/VHostScan/)
|                                                           | [Recon](https://github.com/dirsoooo/Recon) (All in one)           | 
|                                                           | [shodan](https://www.shodan.io/dashboard) (the iot scanner)       |
|                                                           | [Shodan eye](https://github.com/BullsEye0/shodan-eye) (sodan-cli) |
|                                                           | [VulnX](https://github.com/anouarbensaad/VulnX)                   |
|                                                           | [wpscan](https://wpscan.com/) (Wordpress favorite)
|                                                           | [Dnsdumpster](https://dnsdumpster.com/) (dig on steroids!)        |
|                                                           | [ahmia](https://ahmia.fi/)  (dark web search)                     |
|                                                           | [WHOIS](https://who.is/) (nothing beat basics)                    |
|                                                           | [viewdns](https://viewdns.info/) (whois++)                        |


### Vulnerabilty scanners ( For either professionals, lazy people, or both)

| Free (for you and me)                                                 | Paid (If you got money)
| ---------------------                                                 | ----------------------
| [Nikto](https://github.com/sullo/nikto) (technically correct)         | [Acunetix](https://www.acunetix.com/)
| [Rapidscan](https://github.com/skavngr/rapidscan) (Try it!)           | [Nessus](https://www.tenable.com/products/nessus) (technically it's not free)
| [OpenVas](https://www.openvas.org/)                                   | 
| [Vega](https://subgraph.com/vega/)                                    |
| Vulnnr (DEAD?)                                                        |



### Windows (specials)

| Specific services                                       | Active Directory                                                  | Post-exploit
| -----                                                   | ----------------                                                  | -------------
| [Enum4linux](https://www.kali.org/tools/enum4linux/)    | [Kerbrute](https://github.com/ropnop/kerbrute)                    | [Mimikatz](https://www.kali.org/tools/mimikatz/) (the looter)
| [Evilwinrm](https://github.com/Hackplayers/evil-winrm)  | [Impacket tools](https://github.com/SecureAuthCorp/impacket)      |



## exploitation

| Frameworks and payload generators                             | Common exploits                                               | Targetted
| ----------                                                    | ---------------                                               | ------
| [Metasploit](https://www.metasploit.com/) (The unmatched)     | [Exploitdb](https://www.metasploit.com/) (searchsploit)       | [Camover](https://github.com/EntySec/CamOver)
| [Hatsploit](https://github.com/EntySec/HatSploit) (Hatvenom)  | [Sqlmap](https://sqlmap.org/)                                 | [Slowloris](https://github.com/gkbrk/slowloris) (Don't)
|                                                               | [Nosqlmap](https://github.com/codingo/NoSQLMap)               | [GmailHack](https://github.com/adrijano/Gmail-Hack) (Idk either)
|                                                               | [AttackerKB](https://attackerkb.com/) (information is power)  |
| [Pentestmonkey](https://pentestmonkey.net/) (instant shell)   |                                                               | 
| [Revshells](https://www.revshells.com/) (shells of quality)   |                                                               |


### Web (specials)

| Proxies                                                                             | Frameworks and other scanners
| -------                                                                             | -----------
| [burpsuite](https://portswigger.net/burp/communitydownload) (community edition)     | [Arachni](https://github.com/Arachni/arachni)
| [Owasp ZAP](https://www.zaproxy.org/) (It's from OWASP)                             | [Golismero](https://github.com/golismero/golismero)
|                                                                                     | [Leviathan](https://github.com/utkusen/leviathan) ( sadly DEPRECATED )


## Cryptography

| Crackers                                                          | Hashes                                                      | Decoders
| --------                                                          | --------------                                              | ---------
| [John](https://www.kali.org/tools/john/) (the ripper)             | [Hashcat](https://hashcat.net/hashcat/) (a cat)             | [Dcode](https://www.dcode.fr/)
| [Hydra](https://www.kali.org/tools/hydra/) (the legacy)           | [crackstation](https://crackstation.net/)                   | [Cyberchef](https://gchq.github.io/CyberChef/)                             
| [sshtrix](https://nullsecurity.net/tools/cracker.html) (for ssh)  | [Hashcrack](https://hashcrack.com/)                         | 
| [Hatch](https://github.com/nsgodshall/Hatch) (will test more)     | [Hashes.com](https://hashes.com/en/decrypt/hash)            |
|                                                                   | [Hash analyzer](https://www.tunnelsup.com/hash-analyzer/)   |


## Reverse Engeneering

| Disassembler Frameworks                                            | Debuggers and Decompilers
| -------------                                                      | ---------
| [IDA Pro](https://hex-rays.com/ida-pro/) (industry standard)       | [GDB](https://www.sourceware.org/gdb/) (check PwnGdb and olly gdb)
| [Ghidra](https://ghidra-sre.org/) (pride of the NSA)               | [Cutter](https://cutter.re/)
| [Radare2](https://github.com/radareorg/radare2)                    |



## Steganography

| Embedded data                                            | Image Manipulation                                                                       | Audio
| -------------                                            | -------------------                                                                      | ------
| [steghide](http://steghide.sourceforge.net/)             | [Stegsolve](https://en.kali.tools/all/?tool=1762)                                        | [Sonic vizualizer](https://www.sonicvisualiser.org/)
| [stegseek](https://github.com/RickdeJager/stegseek)      | [Stegosuite](https://installlion.com/kali/kali/main/s/stegosuite/install/index.html)     | [Audacity](https://www.audacityteam.org/)
|                                                          | [Gimp](https://www.gimp.org/)                                                            | [Morse decoder](https://morsecode.world/)
|                                                          | [Zbar-tools](http://zbar.sourceforge.net/)                                               |


## Malware Analysis

| Online
| -------
| [virustotal](https://www.virustotal.com/gui/) (too famous)
| [Pithus](https://beta.pithus.org/) (for android)



### Android (specials)

| Analysis                                                                                    | Attacks
| --------                                                                                    | ---------
| [Mobsf](https://github.com/MobSF/Mobile-Security-Framework-MobSF)                           | [SARA](https://github.com/termuxhackers-id/SARA) (careful with this one)
| [Apktool](https://ibotpeaches.github.io/Apktool/)  (uses jadx)                              | [backdoor-apk](https://github.com/dana-at-cp/backdoor-apk)
| [Adb](https://developer.android.com/studio/command-line/adb)                                | [TheFatRat](https://github.com/Screetsec/TheFatRat) (obese rodent)   
| [anbox](https://docs.anbox.io/userguide/install.html) (or any emulator for dynamic testing) |  [Msfvenom](https://www.offensive-security.com/metasploit-unleashed/msfvenom/)       
| [Zimperium tools](https://www.zimperium.com/) (yeah...kinda)                                | 
| [Apkleaks](https://github.com/dwisiswant0/apkleaks)                                         | 
| [MARA](https://github.com/xtiankisutsa/MARA_Framework)                                      |
| [Drozer](https://github.com/FSecureLABS/drozer)                                             |
| [Inspeckage](https://github.com/ac-pm/Inspeckage)                                           |
| [Quark](https://github.com/quark-engine/quark-engine)                                       |
| [Deguard](http://apk-deguard.com/)

## Wifi

| Audit tools
| -----------
| [wifite 2](https://github.com/derv82/wifite2)


## privilege escalation

| Scripts                                                 | References
| -------                                                 | ----------
| [Linenum](https://github.com/rebootuser/LinEnum)        | [GTFObins](https://gtfobins.github.io/) (the ultimate)
| [PEASS tools](https://github.com/carlospolop/PEASS-ng)  |
| [JAWS](https://github.com/411Hall/JAWS)                 |


## post-exploitation

| Command and control (C2)                                                               | Persistance (Roorkits +++) pivot and more                     
| ---------                                                                              | ------------
| [Cobalt strike](https://cobalt-strike.github.io/community_kit/) (industry standard)    | [Reptile](https://github.com/f0rb1dd3n/Reptile)
| [pwncat](https://github.com/calebstewart/pwncat) (another cat)                         |
| [Empire](https://www.powershellempire.com/) ([deprecated] check Starkiller)            |
| [Metasploit](https://www.metasploit.com/) (yes, again!)                                |
| [Covenant](https://github.com/cobbr/Covenant/)                                                                           |


## Forensics

| Frameworks/suites 
| ----------
| [Volatility](https://www.volatilityfoundation.org/)


## Social Engeneering

| Frameworks and tools
| ----------
| [SET](https://www.trustedsec.com/tools/the-social-engineer-toolkit-set/) (number one)
| [thispersondoesnotexist](https://thispersondoesnotexist.com/) (don't misuse this one)
| [namefake](https://namefake.com/) (do not misuse it!)



## OSINT

| Frameworks/suites
| ----------
| [Osint Framework](https://osintframework.com/) (its a framework)
| [Osint techniques](https://www.osinttechniques.com/osint-tools.html)
| [wigle](https://wigle.net/) (google maps for networks)
| [Maltego](https://www.maltego.com/) (Feel like a Professional)
| [wayback machine](https://archive.org/web/) (wayback)
| [intelX](https://intelx.io/tools?tab=facebook)


## Anonimity

| Cloaking                                                             | (De)Obfuscation                                   | Evasion
| ----------                                                           | ----------------                                  | ---------- 
| [Anonsurf](https://linuxhint.com/anonsurf/)                          | [Obfuscator.io](https://obfuscator.io/)           |
|                                                                      | [de4js](https://lelinhtinh.github.io/de4js/)           |

## Utilities
| Browser extensions                                                                                    | Others
| ------------------                                                                                    | -------
| [Foxyproxy](https://addons.mozilla.org/fr/firefox/addon/foxyproxy-standard/) (you know this one)      | [Onecompiler](https://onecompiler.com/) (underrated online compiler)
| [Hack-tools](https://addons.mozilla.org/fr/firefox/addon/hacktools/) (this one is cool)               | [coding tools](https://coding.tools/)
| [ua-switcher](https://addons.mozilla.org/fr/firefox/addon/user-agent-string-switcher/) (custom ua)    | [code beautify](https://codebeautify.org/) (does alot more than that)
| [search by image](https://addons.mozilla.org/fr/firefox/addon/search_by_image/)                       | [busybox](https://busybox.net/) (unix binaries for everyone)
|                                                                                                       | [lolbas](https://lolbas-project.github.io/#)




# My favorites ( kek )

My most used tools, mostly defines my typical process 
- Utilities:
  - Google (your best friend)
- Enumeration:
  - Rustscan
  - Nmap
- Access (exploitation):
  - Meta(fcking)sploit
  - Sqlmap
- Post-Exploitation:
  - Gtfobins

For Other challenges:
- Crypto: dcode, crackstation, rapidtables converter...
- Forensics: volatility

# More tools (Moarrrr!)

Here is a list of places to find more tools:

- [Github](https://github.com) ( alot in here! )

- [Kitploit](https://www.kitploit.com/)

- [Blackarch tools](https://blackarch.org/tools.html) (Or any pentest linux distro tools)

- [kali tools](https://en.kali.tools/all/?category) 

- Also Google. 

There are also some shady places (mostly onion links) with mad awesome tools, but we are not going there ( know what youre doing)

** Do not feed the script kiddy in you. Tools are cool but knoweledge is better! ( But tools are cool though )

