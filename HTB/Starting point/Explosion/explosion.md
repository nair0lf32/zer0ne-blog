# Explosion

## Enumeration

### nmap
```
PORT     STATE    SERVICE       REASON      VERSION
135/tcp  open     msrpc         syn-ack     Microsoft Windows RPC
139/tcp  open     netbios-ssn   syn-ack     Microsoft Windows netbios-ssn
445/tcp  open     microsoft-ds? syn-ack
2811/tcp filtered gsiftp        no-response
3389/tcp open     ms-wbt-server syn-ack     Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: EXPLOSION
|   NetBIOS_Domain_Name: EXPLOSION
|   NetBIOS_Computer_Name: EXPLOSION
|   DNS_Domain_Name: Explosion
|   DNS_Computer_Name: Explosion
|   Product_Version: 10.0.17763
|_  System_Time: 2021-12-16T16:04:59+00:00
|_ssl-date: 2021-12-16T16:05:12+00:00; +13m10s from scanner time.
| ssl-cert: Subject: commonName=Explosion
| Issuer: commonName=Explosion
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-09-20T16:22:34
| Not valid after:  2022-03-22T16:22:34
| MD5:   3d0d 95be 9ffd 7e5d dc0b b710 607a c1bf
| SHA-1: 4e49 35a6 106c 0136 56f6 9bd7 2673 f6bd 8d9d 0cb9
| -----BEGIN CERTIFICATE-----
| MIIC1jCCAb6gAwIBAgIQGkjkAVhQx7lNZOeRvb95LjANBgkqhkiG9w0BAQsFADAU
| MRIwEAYDVQQDEwlFeHBsb3Npb24wHhcNMjEwOTIwMTYyMjM0WhcNMjIwMzIyMTYy
| MjM0WjAUMRIwEAYDVQQDEwlFeHBsb3Npb24wggEiMA0GCSqGSIb3DQEBAQUAA4IB
| DwAwggEKAoIBAQDXNahamG7ZRXZYu0LsKsRg0IdfmfiEojv+/dmf5kAoVSGifF2g
| JZO7chAzptL/xZNsMQF94nawOK5wZunCtqp02NijdViV7kay6Zg3Grxks3cAS2ZQ
| 0UI2t819AZYmduguBpf0ABIbECslodc2cu5i6EP8Ry0FPzRFKdikSvSjg0wSbDnk
| FCTJLEtb0KYkGpAy331yfdF/fvk9CMDn94iBrNpXEoWy5PqPnLWyr4Ee3lDjPhPH
| Fp+8jV6hwlgJy4iN8VTvk8jvL0iaNd120WbpibnO0GUq281Czx02DwPnS/j5RZf7
| 0IRI9Dn516NyNB0U0q7xZRMWu9fs5ZyHzOYVAgMBAAGjJDAiMBMGA1UdJQQMMAoG
| CCsGAQUFBwMBMAsGA1UdDwQEAwIEMDANBgkqhkiG9w0BAQsFAAOCAQEAAz/8Jd3e
| obmfgOlNPvoSYMN27a62k4tzggHKCCBj9LfxylaXtC3KolUmIZ5CxSkiGU7ABU3j
| KKFMWc7GnWu2qLb3D8Z3S2aOYMlS+o9Ecd7NcmbUqJD1KBFexSRvG8H/BAa3S2HF
| C06Vi1Mp3h76WeFL+BnNANBdz9UGfNub0q0tuuRLh2Oa+sWE9/BjMWIV6yeIDbvK
| 9I1VLUCq72uW+0T+YYM9YyvHz5GrfMcXX1QwZP1DW9uH0zKx5EvZORIHfrwI0/g7
| T2XI84Q97JzXyY6bBRI2snk7vFwNf+w38GcEzcEld0lYQDYL85SdfuhZAHh4ysNB
| GNBEucHfr0ILdA==
|_-----END CERTIFICATE-----
9485/tcp filtered unknown       no-response
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2021-12-16T16:05:02
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 30771/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 42507/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 45788/udp): CLEAN (Timeout)
|   Check 4 (port 20803/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
|_clock-skew: mean: 13m09s, deviation: 0s, median: 13m09s
```

there is no password...just RDP as `Administrator` and grab the flag on desktop


