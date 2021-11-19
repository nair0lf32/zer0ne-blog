# Dancing

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
|   date: 2021-10-27T18:08:09
|_  start_date: N/A
|_clock-skew: 4h12m16s
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled but not required
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 28068/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 58368/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 13121/udp): CLEAN (Timeout)
|   Check 4 (port 41395/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

```

hmmm...dancing...samba...samba..dancing

### smbclient

Samba without password (unrealistic jokes 101)

```
$smbclient -L 10.129.143.2
Enter WORKGROUP\nair0lf32's password:

Sharename Type Comment

---

ADMIN$ Disk Remote Admin
C$ Disk Default share
IPC$ IPC Remote IPC
WorkShares Disk
SMB1 disabled -- no workgroup available
```

At this point we know its about samba shares right?

Anonymous smb access

```
smbclient \\\\10.129.143.2\\WorkShares
Enter WORKGROUP\nair0lf32's password:
Try "help" to get a list of possible commands.
smb: \>
```

`get flag.txt` litterally!

worknotes.txt is not useful...it's just a to-do for the developer
