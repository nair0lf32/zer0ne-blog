---
title: "Buffer Overflow prep"
date: 2022-09-20T16:00:31+01:00
draft: true
categories:
  - TryHackMe
---

{{< post-img src="bofprep.png" alt="bofprep" style="width: 200px;" >}}

# Overflow 1

xfreerdp /u:admin /p:password /cert:ignore /v:10.10.16.170 /workarea

immunity debugger: oscp.exe

nc 10.10.16.170 1337

```bash
└──╼ $/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 600

Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9
```

```bash
Log data
Address    Message
           Immunity Debugger 1.85.0.0 : R'lyeh
           Need support? visit http://forum.immunityinc.com/
           "C:\Users\admin\Desktop\vulnerable-apps\oscp\oscp.exe"

           Console file 'C:\Users\admin\Desktop\vulnerable-apps\oscp\oscp.exe'
           [18:15:09] New process with ID 000003D8 created
004012D0   Main thread with ID 000009F8 created
00400000   Modules C:\Users\admin\Desktop\vulnerable-apps\oscp\oscp.exe
62500000   Modules C:\Users\admin\Desktop\vulnerable-apps\oscp\essfunc.dll
75BA0000   Modules C:\Windows\system32\KERNELBASE.dll
75C80000   Modules C:\Windows\system32\msvcrt.dll
76E40000   Modules C:\Windows\system32\kernel32.dll
76F20000   Modules C:\Windows\system32\RPCRT4.dll
777A0000   Modules C:\Windows\SYSTEM32\ntdll.dll
77900000   Modules C:\Windows\system32\NSI.dll
77930000   Modules C:\Windows\system32\WS2_32.dll
004012D0   [18:15:09] Program entry point
           Analysing oscp
             16 heuristical procedures
             236 calls to known functions
             8 loops, 1 switches
0BADF00D   [+] Command used:
0BADF00D   !mona config -set workingfolder c:\mona\%p
0BADF00D   Writing value to configuration file
0BADF00D   Old value of parameter workingfolder =
0BADF00D   [+] Creating config file, setting parameter workingfolder
0BADF00D   New value of parameter workingfolder =  c:\mona\%p
0BADF00D
0BADF00D   [+] This mona.py action took 0:00:00
75330000   Modules C:\Windows\system32\mswsock.dll
76FD0000   Modules C:\Windows\system32\user32.dll
77350000   Modules C:\Windows\system32\GDI32.dll
77210000   Modules C:\Windows\system32\LPK.dll
75E90000   Modules C:\Windows\system32\USP10.dll
77910000   Modules C:\Windows\system32\IMM32.DLL
76D70000   Modules C:\Windows\system32\MSCTF.dll
00401973   New thread with ID 000000EC created
           [18:23:57] Thread 000000EC terminated, exit code 0
0BADF00D   [+] Command used:
0BADF00D   !mona findmsp -distance 600
0BADF00D   [+] Looking for cyclic pattern in memory
74E80000   Modules C:\Windows\System32\wshtcpip.dll
0BADF00D       Cyclic pattern (normal) found at 0x003c3952 (length 600 bytes)
0BADF00D   [+] Examining registers
0BADF00D   [+] Examining SEH chain
0BADF00D   [+] Examining stack (+- 600 bytes) - looking for cyclic pattern
0BADF00D       Walking stack from 0x0022f7b8 to 0x0022fc6c (0x000004b4 bytes)
0BADF00D   [+] Examining stack (+- 600 bytes) - looking for pointers to cyclic pattern
0BADF00D       Walking stack from 0x0022f7b8 to 0x0022fc6c (0x000004b4 bytes)
0BADF00D   [+] Preparing output file 'findmsp.txt'
0BADF00D       - Creating working folder c:\mona\oscp
0BADF00D       - Folder created
0BADF00D       - (Re)setting logfile c:\mona\oscp\findmsp.txt
0BADF00D   [+] Generating module info table, hang on...
0BADF00D       - Processing modules
0BADF00D       - Done. Let's rock 'n roll.
0BADF00D
0BADF00D   [+] This mona.py action took 0:00:06.146000
0BADF00D   [+] Command used:
0BADF00D   !mona findmsp -distance 600
0BADF00D   [+] Looking for cyclic pattern in memory
0BADF00D       Cyclic pattern (normal) found at 0x003c3952 (length 600 bytes)
0BADF00D   [+] Examining registers
0BADF00D   [+] Examining SEH chain
0BADF00D   [+] Examining stack (+- 600 bytes) - looking for cyclic pattern
0BADF00D       Walking stack from 0x0022f7b8 to 0x0022fc6c (0x000004b4 bytes)
0BADF00D   [+] Examining stack (+- 600 bytes) - looking for pointers to cyclic pattern
0BADF00D       Walking stack from 0x0022f7b8 to 0x0022fc6c (0x000004b4 bytes)
0BADF00D   [+] Preparing output file 'findmsp.txt'
0BADF00D       - (Re)setting logfile c:\mona\oscp\findmsp.txt
0BADF00D   [+] Generating module info table, hang on...
0BADF00D       - Processing modules
0BADF00D       - Done. Let's rock 'n roll.
0BADF00D
0BADF00D   [+] This mona.py action took 0:00:13.152000
```



[TODO: FINISH THIS !!!]
