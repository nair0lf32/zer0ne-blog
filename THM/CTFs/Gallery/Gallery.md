# Gallery

<img src="gallery.png" width=200 alt="gallery">

Ok this one was easy so speedrun!

## Enumeration: 

the quick parts:

The CMS (on port 8080) got 2 known vulns:

- RCE 
- SQLi

Both are available on exploitdb

with RCE u can get php files content and with sqli upload a shell as image for admin

its the most basic sqli auth bypass so just do it

you can then access the mariadb database and get the admin hash!


For mike (a bit harder part)...his password is here


```
www-data@gallery:/$ cat /var/backups/mike_home_backup/.bash_history
cat /var/backups/mike_home_backup/.bash_history
cd ~
ls
ping 1.1.1.1
cat /home/mike/user.txt
cd /var/www/
ls
cd html
ls -al
cat index.html
sudo -lb3stpassw0rdbr0xx
clear
sudo -l
exit
```
## Privilege escalation

```
mike@gallery:~$ sudo -l
sudo -l
Matching Defaults entries for mike on gallery:
env_reset, mail_badpass,
secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User mike may run the following commands on gallery:
(root) NOPASSWD: /bin/bash /opt/rootkit.sh
```
lol That is all you need!

Good luck!
