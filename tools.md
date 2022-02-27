# Tools

Just a list of cool tools! The ones I use the most ( or not )

and the one I discovered during my journey

Ordered by categories (kinda)

## Reconnaissance & Enumeration 

| Scanning                                                  |  Footprint                                                     | Discovery
| --------                                                  |  ---------                                                     | ---------
| [Nmap](https://nmap.org/) (good old)                      | [Recon-ng](https://github.com/lanmaster53/recon-ng)            | [Gobuster](https://github.com/OJ/gobuster) 
| [Rustscan](https://github.com/RustScan/RustScan)          | [Blackwidow](https://github.com/1N3/BlackWidow)                | [Ffuf](https://github.com/ffuf/ffuf)
| [NmapAutomator](https://github.com/21y4d/nmapAutomator)   | [Cmseek](https://github.com/Tuhinshubhra/CMSeeK)               | [Sublist3r](https://github.com/aboul3la/Sublist3r)
| [onesixtyone](https://github.com/trailofbits/onesixtyone) | [Eyewitness](https://github.com/FortyNorthSecurity/EyeWitness) | [VhostScan](https://github.com/codingo/VHostScan/)
|                                                           | [Recon](https://github.com/dirsoooo/Recon) (All in one)        |
|                                                           | [Shodan eye](https://github.com/BullsEye0/shodan-eye)          |
|                                                           | [VulnX](https://github.com/anouarbensaad/VulnX)                |




### Vulnerabilty scanners ( For either professionals, lazy people, or both)

| Free (for you and me)                                                 | Paid (If you got money)
| ---------------------                                                 | ----------------------
| [Nikto](https://github.com/sullo/nikto) (technically correct)         | [Acunetix](https://www.acunetix.com/)
| [Rapidscan](https://github.com/skavngr/rapidscan) (Try it!)           | [Nessus](https://www.tenable.com/products/nessus) (technically it's not free)
| [OpenVas](https://www.openvas.org/)                                   | 
| [Vega](https://subgraph.com/vega/)                                    |
| Vulnnr (DEAD?)                                                           |



### Windows (specials)

| Samba                                                 | Active Directory                                                | Post-exploit
| -----                                                 | ----------------                                                | -------------
| [Enum4linux](https://www.kali.org/tools/enum4linux/)  | [Kerbrute](https://github.com/ropnop/kerbrute)                  | [Mimikatz](https://www.kali.org/tools/mimikatz/) (the looter)
|                                                       | [Impacket tools](https://github.com/SecureAuthCorp/impacket)    |



## exploitation

| Frameworks                                                  | Common exploits
| ----------                                                  | ---------------
| [Metasploit](https://www.metasploit.com/) (the unmatched)   | [Exploitdb](https://www.metasploit.com/) (searchsploit)


### Web (specials)

| Proxies                                                                               | Frameworks
| -------                                                                               | -----------
| [burpsuite](https://portswigger.net/burp/communitydownload) (community edition)       | [Arachni](https://github.com/Arachni/arachni)
| [Owasp ZAP](https://www.zaproxy.org/) (It's from OWASP)                               | [Golismero](https://github.com/golismero/golismero)
|                                                                                       | [Leviathan](https://github.com/utkusen/leviathan) ( sadly DEPRECATED )



## Cryptography

| Crackers                                                  | Hashes                                                      | Decoders
| --------                                                  | --------------                                              | ---------
| [John](https://www.kali.org/tools/john/) (the ripper)     | [Hashcat](https://hashcat.net/hashcat/) (a cat)             | [Dcode](https://www.dcode.fr/)
| [Hydra](https://www.kali.org/tools/hydra/) (the legacy)   | [crackstation](https://crackstation.net/)                   | [Cyberchef](https://gchq.github.io/CyberChef/)                             
|                                                           | [Hashcrack](https://hashcrack.com/)                         | 
|                                                           | [Hashes.com](https://hashes.com/en/decrypt/hash)            |
|                                                           | [Hash analyzer](https://www.tunnelsup.com/hash-analyzer/)   |


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




### Android (specials)

| Analysis                                                                        | Attacks
| --------                                                                        | ---------
| [Mobsf](https://github.com/MobSF/Mobile-Security-Framework-MobSF)               | [§ARA](https://github.com/termuxhackers-id/SARA) (careful with this one)
| [Apktool](https://ibotpeaches.github.io/Apktool/)  (uses jadx)                  | [backdoor-apk](https://github.com/dana-at-cp/backdoor-apk)
| [Adb](https://developer.android.com/studio/command-line/adb)                    | [TheFatRat](https://github.com/Screetsec/TheFatRat) (obese rodent)             
| [Zimperium tools](https://www.zimperium.com/) (yeah...kinda)                    | [Msfvenom](https://www.offensive-security.com/metasploit-unleashed/msfvenom/)
| [Apkleaks](https://github.com/dwisiswant0/apkleaks)                             |
| [MARA](https://github.com/xtiankisutsa/MARA_Framework)                          |
| [Drozer](https://github.com/FSecureLABS/drozer)                                 |
| [Inspeckage](https://github.com/ac-pm/Inspeckage)                               |
| [Quark](https://github.com/quark-engine/quark-engine)                           |



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

| Command and control (C2)                                                               | Persistance (Roorkits +++)
| ---------                                                                              | ------------
| [Cobalt strike](https://cobalt-strike.github.io/community_kit/) (industry standard)    | [Reptile](https://github.com/f0rb1dd3n/Reptile)
| [pwncat](https://github.com/calebstewart/pwncat) (another cat)                         |
| [Empire](https://www.powershellempire.com/) ([deprecated] check Starkiller)            |
| [Metasploit](https://www.metasploit.com/) (yes, again!)                                |
| [Covenant](https://github.com/cobbr/Covenant/)                                                                           |



## Social Engeneering

| Frameworks
| ----------
| [SET](https://www.trustedsec.com/tools/the-social-engineer-toolkit-set/)



## OSINT

| Utilities
| ----------
| [Osint Framework](https://osintframework.com/) (its a framework)
| [Maltego](https://www.maltego.com/) (Feel like a Professional)



## Anonimity

| Cloaking                  | (De)Obfuscation                                   | Evasion
| ----------                | ----------------                                  | ---------- 
|                           | [Obfuscator.io](https://obfuscator.io/)           |




# My favorites ( kek )

- nmap
- Meta(fcking)sploit
- ...


# More tools (Moarrrr!)

Do not feed the script kiddy in you. Tools are cool but knoweledge is better!

Now that I said this, here is a list of places to find more tools:

- TODO

- TODO

