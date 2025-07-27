---
title: "Reversing elf"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src="elf.png" alt="elf" width=200>

## crackme1

just chmod and run the binary

## crackme2

the password is in the "strings" (you know what to do)

## crackme3

strings with base64 in them

## crackme4

I chose radare2 (IDA is good too)

we start with the basics

```
└──╼ $r2 -d ./crackme4
Process with PID 10508 started...
= attach 10508 10508
bin.baddr 0x00400000
Using 0x400000
asm.bits 64

[0x7fc191002090]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for vtables
[TOFIX: aaft can't run in debugger mode.ions (aaft)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.

[0x7fc191002090]> afl
0x00400540    1 41           entry0
0x00400510    1 6            sym.imp.__libc_start_main
0x00400570    4 41           sym.deregister_tm_clones
0x004005a0    4 57           sym.register_tm_clones
0x004005e0    3 28           sym.__do_global_dtors_aux
0x00400600    4 45   -> 42   entry.init0
0x004007d0    1 2            sym.__libc_csu_fini
0x0040062d    4 77           sym.get_pwd
0x004007d4    1 9            sym._fini
0x0040067a    6 156          sym.compare_pwd
0x00400760    4 101          sym.__libc_csu_init
0x00400716    4 74           main
0x004004b0    3 26           sym._init
0x00400530    1 6            loc.imp.__gmon_start__
0x004004e0    1 6            sym.imp.puts
0x004004f0    1 6            sym.imp.__stack_chk_fail
0x00400500    1 6            sym.imp.printf
0x00400520    1 6            sym.imp.strcmp

```
The main function calls `sym.compare_pwd` to check the password so I check that one too

```
[0x00400716]> s 0x0040067a
[0x0040067a]> pdf
; CALL XREF from main @ 0x400754
┌ 156: sym.compare_pwd (int64_t arg1);
│           ; var int64_t var_28h @ rbp-0x28
│           ; var int64_t var_20h @ rbp-0x20
│           ; var int64_t var_18h @ rbp-0x18
│           ; var int64_t var_10h @ rbp-0x10
│           ; var int64_t var_eh @ rbp-0xe
│           ; var int64_t var_8h @ rbp-0x8
│           ; arg int64_t arg1 @ rdi
│           0x0040067a      55             push rbp
│           0x0040067b      4889e5         mov rbp, rsp
│           0x0040067e      4883ec30       sub rsp, 0x30
│           0x00400682      48897dd8       mov qword [var_28h], rdi    ; arg1
│           0x00400686      64488b042528.  mov rax, qword fs:[0x28]
│           0x0040068f      488945f8       mov qword [var_8h], rax
│           0x00400693      31c0           xor eax, eax
│           0x00400695      48b8495d7b49.  movabs rax, 0x7b175614497b5d49
│           0x0040069f      488945e0       mov qword [var_20h], rax
│           0x004006a3      48b857414751.  movabs rax, 0x547b175651474157
│           0x004006ad      488945e8       mov qword [var_18h], rax
│           0x004006b1      66c745f05340   mov word [var_10h], 0x4053  ; 'S@'
│           0x004006b7      c645f200       mov byte [var_eh], 0
│           0x004006bb      488d45e0       lea rax, [var_20h]
│           0x004006bf      4889c7         mov rdi, rax
│           0x004006c2      e866ffffff     call sym.get_pwd
│           0x004006c7      488b55d8       mov rdx, qword [var_28h]
│           0x004006cb      488d45e0       lea rax, [var_20h]
│           0x004006cf      4889d6         mov rsi, rdx
│           0x004006d2      4889c7         mov rdi, rax
│           0x004006d5      e846feffff     call sym.imp.strcmp         ; int strcmp(const char *s1, const char *s2)
│           0x004006da      85c0           test eax, eax
│       ┌─< 0x004006dc      750c           jne 0x4006ea
│       │   0x004006de      bfe8074000     mov edi, str.password_OK    ; 0x4007e8 ; "password OK"
│       │   0x004006e3      e8f8fdffff     call sym.imp.puts           ; int puts(const char *s)
│      ┌──< 0x004006e8      eb16           jmp 0x400700
│      │└─> 0x004006ea      488b45d8       mov rax, qword [var_28h]
│      │    0x004006ee      4889c6         mov rsi, rax
│      │    0x004006f1      bff4074000     mov edi, str.password___s__not_OK_n ; 0x4007f4 ; "password \"%s\" not OK\n"
│      │    0x004006f6      b800000000     mov eax, 0
│      │    0x004006fb      e800feffff     call sym.imp.printf         ; int printf(const char *format)
│      │    ; CODE XREF from sym.compare_pwd @ 0x4006e8
│      └──> 0x00400700      488b45f8       mov rax, qword [var_8h]
│           0x00400704      644833042528.  xor rax, qword fs:[0x28]
│       ┌─< 0x0040070d      7405           je 0x400714
│       │   0x0040070f      e8dcfdffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
│       └─> 0x00400714      c9             leave
└           0x00400715      c3             ret

```

the call to `strcmp` is at address `0x004006d5` 

We need to get the value stored in the `rdi` register

I tried to debug with a breakpoint just before the call but I could not make it work

Alternatively I used `ltrace`

it captures calls made to libraries like `strcmp` (similar to strace for system calls)

```
└──╼ $ltrace ./crackme4 test
__libc_start_main(0x400716, 2, 0x7ffcbb73c618, 0x400760 <unfinished ...>
strcmp("n0_3asY_pa5sw0rd", "test")                                                                                                              = -7
printf("password "%s" not OK\n", "test"password "test" not OK
)                                                                                                          = 23
+++ exited (status 0) +++
```
There is also the good ol' `gdb` method (even better IMO)

## crackme5


This is very similar to `crackme4` challenge

instead of using an argument it takes input and still uses `strcmp`

```
│           0x00400801      bf54094000     mov edi, str.Enter_your_input: ; 0x400954 ; "Enter your input:"
│           0x00400806      e865fdffff     call sym.imp.puts           ; int puts(const char *s)
│           0x0040080b      488d45b0       lea rax, [var_50h]
│           0x0040080f      4889c6         mov rsi, rax
│           0x00400812      bf66094000     mov edi, 0x400966
│           0x00400817      b800000000     mov eax, 0
│           0x0040081c      e89ffdffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x00400821      488d55d0       lea rdx, [var_30h]
│           0x00400825      488d45b0       lea rax, [var_50h]
│           0x00400829      4889d6         mov rsi, rdx
│           0x0040082c      4889c7         mov rdi, rax
│           0x0040082f      e8a2feffff     call sym.strcmp_
│           0x00400834      8945ac         mov dword [var_54h], eax
│           0x00400837      837dac00       cmp dword [var_54h], 0
│       ┌─< 0x0040083b      750c           jne 0x400849
│       │   0x0040083d      bf69094000     mov edi, str.Good_game      ; 0x400969 ; "Good game"
│       │   0x00400842      e829fdffff     call sym.imp.puts           ; int puts(const char *s)
│      ┌──< 0x00400847      eb0a           jmp 0x400853
│      │└─> 0x00400849      bf73094000     mov edi, str.Always_dig_deeper ; 0x400973 ; "Always dig deeper"
│      │    0x0040084e      e81dfdffff     call sym.imp.puts           ; int puts(const char *s)

```

same process, but note how the variables declared in the main function also give you the answer

I just used `ltrace` again with a random input

```
└──╼ $ltrace ./crackme5
__libc_start_main(0x400773, 1, 0x7ffdf90329d8, 0x4008d0 <unfinished ...>
puts("Enter your input:"Enter your input:
)                                                                                                                         = 18
__isoc99_scanf(0x400966, 0x7ffdf9032890, 0, 0x7f07de835f33 tester
)                                                                                       = 1
strlen("tester")                                                                                                                                  = 6
strlen("tester")                                                                                                                                  = 6
strlen("tester")                                                                                                                                  = 6
strlen("tester")                                                                                                                                  = 6
strlen("tester")                                                                                                                                  = 6
strlen("tester")                                                                                                                                  = 6
strlen("tester")                                                                                                                                  = 6
strncmp("tester", "answer_would_be_here", 28)                                                                                             = 37
puts("Always dig deeper"Always dig deeper
)                                                                                                                         = 18
+++ exited (status 0) +++

```

## crackme6

Back to password as argument

main calls `sym.compare_pwd` wich calls `sym.my_secure_test`

```
[0x7f6fdbd79090]> pdf @sym.my_secure_test
; CALL XREF from sym.compare_pwd @ 0x4006e4
┌ 340: sym.my_secure_test (int64_t arg1);
│           ; var int64_t var_8h @ rbp-0x8
│           ; arg int64_t arg1 @ rdi
│           0x0040057d      55             push rbp
│           0x0040057e      4889e5         mov rbp, rsp
│           0x00400581      48897df8       mov qword [var_8h], rdi     ; arg1
│           0x00400585      488b45f8       mov rax, qword [var_8h]
│           0x00400589      0fb600         movzx eax, byte [rax]
│           0x0040058c      84c0           test al, al
│       ┌─< 0x0040058e      740b           je 0x40059b
│       │   0x00400590      488b45f8       mov rax, qword [var_8h]
│       │   0x00400594      0fb600         movzx eax, byte [rax]
│       │   0x00400597      3c31           cmp al, 0x31                ; 49
│      ┌──< 0x00400599      740a           je 0x4005a5
│      │└─> 0x0040059b      b8ffffffff     mov eax, 0xffffffff         ; -1
│      │┌─< 0x004005a0      e92a010000     jmp 0x4006cf
│      └──> 0x004005a5      488b45f8       mov rax, qword [var_8h]
│       │   0x004005a9      4883c001       add rax, 1
│       │   0x004005ad      0fb600         movzx eax, byte [rax]
│       │   0x004005b0      84c0           test al, al
│      ┌──< 0x004005b2      740f           je 0x4005c3
│      ││   0x004005b4      488b45f8       mov rax, qword [var_8h]
│      ││   0x004005b8      4883c001       add rax, 1
│      ││   0x004005bc      0fb600         movzx eax, byte [rax]
│      ││   0x004005bf      3c33           cmp al, 0x33                ; 51
│     ┌───< 0x004005c1      740a           je 0x4005cd
│     │└──> 0x004005c3      b8ffffffff     mov eax, 0xffffffff         ; -1
│     │┌──< 0x004005c8      e902010000     jmp 0x4006cf
│     └───> 0x004005cd      488b45f8       mov rax, qword [var_8h]
│      ││   0x004005d1      4883c002       add rax, 2
│      ││   0x004005d5      0fb600         movzx eax, byte [rax]
│      ││   0x004005d8      84c0           test al, al
│     ┌───< 0x004005da      740f           je 0x4005eb
│     │││   0x004005dc      488b45f8       mov rax, qword [var_8h]
│     │││   0x004005e0      4883c002       add rax, 2
│     │││   0x004005e4      0fb600         movzx eax, byte [rax]
│     │││   0x004005e7      3c33           cmp al, 0x33                ; 51
│    ┌────< 0x004005e9      740a           je 0x4005f5
│    │└───> 0x004005eb      b8ffffffff     mov eax, 0xffffffff         ; -1
│    │┌───< 0x004005f0      e9da000000     jmp 0x4006cf
│    └────> 0x004005f5      488b45f8       mov rax, qword [var_8h]
│     │││   0x004005f9      4883c003       add rax, 3
│     │││   0x004005fd      0fb600         movzx eax, byte [rax]
│     │││   0x00400600      84c0           test al, al
│    ┌────< 0x00400602      740f           je 0x400613
│    ││││   0x00400604      488b45f8       mov rax, qword [var_8h]
│    ││││   0x00400608      4883c003       add rax, 3
│    ││││   0x0040060c      0fb600         movzx eax, byte [rax]
│    ││││   0x0040060f      3c37           cmp al, 0x37                ; 55
│   ┌─────< 0x00400611      740a           je 0x40061d
│   │└────> 0x00400613      b8ffffffff     mov eax, 0xffffffff         ; -1
│   │┌────< 0x00400618      e9b2000000     jmp 0x4006cf
│   └─────> 0x0040061d      488b45f8       mov rax, qword [var_8h]
│    ││││   0x00400621      4883c004       add rax, 4
│    ││││   0x00400625      0fb600         movzx eax, byte [rax]
│    ││││   0x00400628      84c0           test al, al
│   ┌─────< 0x0040062a      740f           je 0x40063b
│   │││││   0x0040062c      488b45f8       mov rax, qword [var_8h]
│   │││││   0x00400630      4883c004       add rax, 4
│   │││││   0x00400634      0fb600         movzx eax, byte [rax]
│   │││││   0x00400637      3c5f           cmp al, 0x5f                ; 95
│  ┌──────< 0x00400639      740a           je 0x400645
│  │└─────> 0x0040063b      b8ffffffff     mov eax, 0xffffffff         ; -1
│  │┌─────< 0x00400640      e98a000000     jmp 0x4006cf
│  └──────> 0x00400645      488b45f8       mov rax, qword [var_8h]
│   │││││   0x00400649      4883c005       add rax, 5
│   │││││   0x0040064d      0fb600         movzx eax, byte [rax]
│   │││││   0x00400650      84c0           test al, al
│  ┌──────< 0x00400652      740f           je 0x400663
│  ││││││   0x00400654      488b45f8       mov rax, qword [var_8h]
│  ││││││   0x00400658      4883c005       add rax, 5
│  ││││││   0x0040065c      0fb600         movzx eax, byte [rax]
│  ││││││   0x0040065f      3c70           cmp al, 0x70                ; 112
│ ┌───────< 0x00400661      7407           je 0x40066a
│ │└──────> 0x00400663      b8ffffffff     mov eax, 0xffffffff         ; -1
│ │┌──────< 0x00400668      eb65           jmp 0x4006cf
│ └───────> 0x0040066a      488b45f8       mov rax, qword [var_8h]
│  ││││││   0x0040066e      4883c006       add rax, 6
│  ││││││   0x00400672      0fb600         movzx eax, byte [rax]
│  ││││││   0x00400675      84c0           test al, al
│ ┌───────< 0x00400677      740f           je 0x400688
│ │││││││   0x00400679      488b45f8       mov rax, qword [var_8h]
│ │││││││   0x0040067d      4883c006       add rax, 6
│ │││││││   0x00400681      0fb600         movzx eax, byte [rax]
│ │││││││   0x00400684      3c77           cmp al, 0x77                ; 119
│ ────────< 0x00400686      7407           je 0x40068f
│ └───────> 0x00400688      b8ffffffff     mov eax, 0xffffffff         ; -1
│ ┌───────< 0x0040068d      eb40           jmp 0x4006cf
│ ────────> 0x0040068f      488b45f8       mov rax, qword [var_8h]
│ │││││││   0x00400693      4883c007       add rax, 7
│ │││││││   0x00400697      0fb600         movzx eax, byte [rax]
│ │││││││   0x0040069a      84c0           test al, al
│ ────────< 0x0040069c      740f           je 0x4006ad
│ │││││││   0x0040069e      488b45f8       mov rax, qword [var_8h]
│ │││││││   0x004006a2      4883c007       add rax, 7
│ │││││││   0x004006a6      0fb600         movzx eax, byte [rax]
│ │││││││   0x004006a9      3c64           cmp al, 0x64                ; 100
│ ────────< 0x004006ab      7407           je 0x4006b4
│ ────────> 0x004006ad      b8ffffffff     mov eax, 0xffffffff         ; -1
│ ────────< 0x004006b2      eb1b           jmp 0x4006cf
│ ────────> 0x004006b4      488b45f8       mov rax, qword [var_8h]
│ │││││││   0x004006b8      4883c008       add rax, 8
│ │││││││   0x004006bc      0fb600         movzx eax, byte [rax]
│ │││││││   0x004006bf      84c0           test al, al
│ ────────< 0x004006c1      7407           je 0x4006ca
│ │││││││   0x004006c3      b8ffffffff     mov eax, 0xffffffff         ; -1
│ ────────< 0x004006c8      eb05           jmp 0x4006cf
│ ────────> 0x004006ca      b800000000     mov eax, 0
│ │││││││   ; XREFS: CODE 0x004005a0  CODE 0x004005c8  CODE 0x004005f0  CODE 0x00400618  CODE 0x00400640  CODE 0x00400668  
│ │││││││   ; XREFS: CODE 0x0040068d  CODE 0x004006b2  CODE 0x004006c8  
│ └└└└└└└─> 0x004006cf      5d             pop rbp
└           0x004006d0      c3             ret

```
well that's alot...I used the visual (vvv) to analyze it better

basically it compares (`cmp al, <value>`) every character of our argument in `rax` register with a hex value

from top to bottom you get : 0x31,0x33,0x33,0x37,0x5f,0x70,0x77,0x64

Decode it from hex/to ascii (I used cyberchef)

And that guy said it was an easy password lol

## crackme7

analysing the `main` function

We can see it does another comparison:

```
│ ││││ │    0x08048665      3d697a0000     cmp eax, 0x7a69
```

Then gives you the flag

```
│ ││││ ││   0x0804866f      68bc880408     push str.Wow_such_h4x0r_    ; 0x80488bc ; "Wow such h4x0r!"
│ ││││ ││   0x08048674      e8f7fcffff     call sym.imp.puts           ; int puts(const char *s)
│ ││││ ││   0x08048679      83c410         add esp, 0x10
│ ││││ ││   0x0804867c      e825000000     call sym.giveFlag
```
interresting part is the comparison of `eax` register with the hex value

I decode it and try it as input for the menu!

It works but remember the menu takes numbers so decode from hex to decimal (base 16 to base 10)

nice flag lol (I didnt even use IDA)

## crackme8

Final one! must be the hardest!!!

interresting part of `main` function

```
│    0x080484db      50             push eax
│      │    0x080484dc      e89ffeffff     call sym.imp.atoi           ; int atoi(const char *str)
│      │    0x080484e1      83c410         add esp, 0x10
│      │    0x080484e4      3d0df0feca     cmp eax, 0xcafef00d
│      │┌─< 0x080484e9      7417           je 0x8048502
│      ││   0x080484eb      83ec0c         sub esp, 0xc
│      ││   0x080484ee      6874860408     push str.Access_denied.     ; 0x8048674 ; "Access denied."
│      ││   0x080484f3      e858feffff     call sym.imp.puts           ; int puts(const char *s)
│      ││   0x080484f8      83c410         add esp, 0x10
│      ││   0x080484fb      b801000000     mov eax, 1
│     ┌───< 0x08048500      eb1a           jmp 0x804851c
│     ││└─> 0x08048502      83ec0c         sub esp, 0xc
│     ││    0x08048505      6883860408     push str.Access_granted.    ; 0x8048683 ; "Access granted."
│     ││    0x0804850a      e841feffff     call sym.imp.puts           ; int puts(const char *s)
│     ││    0x0804850f      83c410         add esp, 0x10
│     ││    0x08048512      e80d000000     call sym.giveFlag

```

`atoi` converts a string to an integer

and you know what this does already: `cmp eax, 0xcafef00d`

So I converted the hex to decimal again and tried it but got denied

the result was a bit long for an integer anyway...

I got stuck here a bit and went for help...I got this suggestion:

"trying to convert the hex to binary, you may notice the decimal number is actually negative"

that's how I learnt about signed 2's complement

I used [rapidtables](https://www.rapidtables.com/convert/number/hex-to-decimal.html) to decode the hex and used the negative value

It worked!

Alternatively you could use a breakpoint at the comparison, change eax to the hex value and continue to get the flag

This one feels like a more "hacky" workaround...so cool!

Anyway! fun room! RE is hard but I am slowly getting better at it! 

I could do this room faster with `ghidra` but I chose pain and spent hours!

I think even IDA would be faster than r2. 












