# Git Happens

<img src="git.png" width=200 height=200 alt="git">

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack nginx 1.14.0 (Ubuntu)
| http-git:
|   10.10.106.206:80/.git/
|     Git repository found!
|_    Repository description: Unnamed repository; edit this file 'description' to name the...
|_http-server-header: nginx/1.14.0 (Ubuntu)
| http-methods:
|_  Supported Methods: GET HEAD
|_http-title: Super Awesome Site!
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### ffuf

```

.git/HEAD               [Status: 200, Size: 23, Words: 2, Lines: 2]
css                     [Status: 301, Size: 194, Words: 7, Lines: 8]
index.html              [Status: 200, Size: 6890, Words: 541, Lines: 61]
```

http-git? .git/HEAD? Its a git repository!

we can visit /.git/ directory for more information

we can dump the repo using `git tools` (dumper)

`./gitdumper.sh 10.10.106.206/.git/ /home/User/Desktop/Git happens/Git/.git`

Now we check logs

`git log`

```
commit d0b3578a628889f38c0affb1b75457146a4678e5 (HEAD -> master, tag: v1.0)
Author: Adam Bertrand <hydragyrum@gmail.com>
commit d0b3578a628889f38c0affb1b75457146a4678e5 (HEAD -> master, tag: v1.0)
commit d0b3578a628889f38c0affb1b75457146a4678e5 (HEAD -> master, tag: v1.0)
Author: Adam Bertrand <hydragyrum@gmail.com>
Date: Thu Jul 23 22:22:16 2020 +0000

Update .gitlab-ci.yml

commit 77aab78e2624ec9400f9ed3f43a6f0c942eeb82d
Author: Hydragyrum <hydragyrum@gmail.com>
Date: Fri Jul 24 00:21:25 2020 +0200

add gitlab-ci config to build docker file.

commit 2eb93ac3534155069a8ef59cb25b9c1971d5d199
Author: Hydragyrum <hydragyrum@gmail.com>
Date: Fri Jul 24 00:08:38 2020 +0200

setup dockerfile and setup defaults.

commit d6df4000639981d032f628af2b4d03b8eff31213
Author: Hydragyrum <hydragyrum@gmail.com>
Date: Thu Jul 23 23:42:30 2020 +0200

Make sure the css is standard-ish!

commit d954a99b96ff11c37a558a5d93ce52d0f3702a7d
Author: Hydragyrum <hydragyrum@gmail.com>
Date: Thu Jul 23 23:41:12 2020 +0200

:...skipping...
commit d0b3578a628889f38c0affb1b75457146a4678e5 (HEAD -> master, tag: v1.0)
Author: Adam Bertrand <hydragyrum@gmail.com>
Date: Thu Jul 23 22:22:16 2020 +0000

Update .gitlab-ci.yml

commit 77aab78e2624ec9400f9ed3f43a6f0c942eeb82d
Author: Hydragyrum <hydragyrum@gmail.com>
Date: Fri Jul 24 00:21:25 2020 +0200

add gitlab-ci config to build docker file.

commit 2eb93ac3534155069a8ef59cb25b9c1971d5d199
Author: Hydragyrum <hydragyrum@gmail.com>
Date: Fri Jul 24 00:08:38 2020 +0200

setup dockerfile and setup defaults.

commit d6df4000639981d032f628af2b4d03b8eff31213
Author: Hydragyrum <hydragyrum@gmail.com>
Date: Thu Jul 23 23:42:30 2020 +0200

Make sure the css is standard-ish!

commit d954a99b96ff11c37a558a5d93ce52d0f3702a7d
Author: Hydragyrum <hydragyrum@gmail.com>
Date: Thu Jul 23 23:41:12 2020 +0200

re-obfuscating the code to be really secure!

commit bc8054d9d95854d278359a432b6d97c27e24061d
Author: Hydragyrum <hydragyrum@gmail.com>
Date: Thu Jul 23 23:37:32 2020 +0200

Security says obfuscation isn't enough.

They want me to use something called 'SHA-512'

commit e56eaa8e29b589976f33d76bc58a0c4dfb9315b1
Author: Hydragyrum <hydragyrum@gmail.com>
Date: Thu Jul 23 23:25:52 2020 +0200

Obfuscated the source code.

Hopefully security will be happy!

commit 395e087334d613d5e423cdf8f7be27196a360459
Author: Hydragyrum <hydragyrum@gmail.com>
Date: Thu Jul 23 23:17:43 2020 +0200
```

Now from commits hashes we can see modified files with git show

`git show d954a99b96ff11c37a558a5d93ce52d0f3702a7d`

```
...
username === 'admin' &&

-          passwordHash === '4004c23a71fd6ba9b03ec9cb7eed08471197d84319a865c5442a9d6a7c7cbea070f3cb6aa5106ef80f679a88dbbaf89ff64cb351a151a5f29819a3c094ecebbb'
-        ) {
  ...
```

we get a hashed pasword for admin I thought about cracking it first but checking the initial commit already shows creds in plain text

```
- <script>
-      function login() {
  -        let form = document.getElementById("login-form");
  -        console.log(form.elements);
  -        let username = form.elements["username"].value;
  -        let password = form.elements["password"].value;
  -        if (
    -          username === "admin" &&
    -          password === "Git_happens_flag!"
    -        ) {
    -          document.cookie = "login=1";
    -          window.location.href = "/dashboard.html";
    -        } else {
      -          document.getElementById("error").innerHTML =
      -            "INVALID USERNAME OR PASSWORD!";
      -        }
      -      }
      - </script>
```

login creds are:

`admin : Git_happens_flag!`

the login page doesnt even work...the password you find is already the flag

so obviously don't trust mine

I deleted my Git folder content before uploading here..git repo in git repo is not a simple thing to handle
