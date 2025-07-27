---
title: "Illumination"
date: 2022-09-20T14:03:31+01:00
draft: false
categories:
  - HackTheBox
---

New forensics challenge

its a discord bot and there is a base64 encoded username in the json file
we decode that to:

`Red Herring, read the JS carefully`

there is also a `.git` repo so we can explore those:

```bash
└──╼ $git log
commit edc5aabf933f6bb161ceca6cf7d0d2160ce333ec (HEAD -> master)
Author: SherlockSec <dan@lights.htb>
Date:   Fri May 31 14:16:43 2019 +0100

    Added some whitespace for readability!

commit 47241a47f62ada864ec74bd6dedc4d33f4374699
Author: SherlockSec <dan@lights.htb>
Date:   Fri May 31 12:00:54 2019 +0100

    Thanks to contributors, I removed the unique token as it was a security risk. Thanks for reporting responsibly!

commit ddc606f8fa05c363ea4de20f31834e97dd527381
Author: SherlockSec <dan@lights.htb>
Date:   Fri May 31 09:14:04 2019 +0100

    Added some more comments for the lovely contributors! Thanks for helping out!

commit 335d6cfe3cdc25b89cae81c50ffb957b86bf5a4a
Author: SherlockSec <dan@lights.htb>
Date:   Thu May 30 22:16:02 2019 +0100

    Moving to Git, first time using it. First Commit!
```

Checking the first commit is always the best

that mostly where the mistake are made

Before they remove them

```bash
└──╼ $git show 335d6cfe3cdc25b89cae81c50ffb957b86bf5a4a
commit 335d6cfe3cdc25b89cae81c50ffb957b86bf5a4a
Author: SherlockSec <dan@lights.htb>
Date:   Thu May 30 22:16:02 2019 +0100

    Moving to Git, first time using it. First Commit!

...

```

And you decode the token again at the bottom to get the flag!
