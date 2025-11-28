# 🎓 CEH Exam Quick Reference Cheatsheet
## Certified Ethical Hacker - 5 Domains Overview

---

## 📚 CEH v11 Exam Domains

### Domain 1: Reconnaissance & Footprinting
**Objective:** Information gathering techniques

- **Passive Information Gathering**
  - WHOIS, DNS lookup, Google dorking
  - Job postings, press releases, social media
  - Website analysis and technology stack identification

- **Active Information Gathering**
  - Port scanning (Nmap)
  - Network enumeration
  - OS fingerprinting
  - Service enumeration

**Key Tools:** Nmap, theHarvester, Shodan, DNSRecon, Recon-ng

---

### Domain 2: Scanning & Enumeration
**Objective:** Identify live systems and services

- **Network Scanning Types**
  - Ping scan (ICMP) - Host discovery
  - SYN scan (-sS) - Stealth/half-open
  - Connect scan (-sT) - Full three-way handshake
  - UDP scan (-sU) - UDP services

- **Enumeration Techniques**
  - NetBIOS enumeration
  - DNS zone transfer
  - SNMP enumeration
  - LDAP enumeration

**Common Ports:**
- 21 = FTP | 22 = SSH | 23 = Telnet
- 25 = SMTP | 53 = DNS | 80 = HTTP
- 110 = POP3 | 143 = IMAP | 443 = HTTPS
- 3306 = MySQL | 5432 = PostgreSQL | 3389 = RDP

**Key Tools:** Nmap, Wireshark, NetStat, Zenmap

---

### Domain 3: Gaining Access (Exploitation)
**Objective:** Exploit vulnerabilities to gain access

- **Attack Types**
  - Brute force attacks
  - Dictionary attacks
  - Password spraying
  - SQL injection
  - Cross-site scripting (XSS)

- **Privilege Escalation**
  - Horizontal escalation (same privilege level, different user)
  - Vertical escalation (lower to higher privilege)

**Key Tools:** Metasploit, Burp Suite, SQLmap, John the Ripper

---

### Domain 4: Maintaining Access
**Objective:** Establish persistent access

- **Techniques**
  - Backdoors and rootkits
  - Trojan horses
  - Remote access tools (RAT)
  - Web shells
  - Privilege escalation techniques

- **Covering Tracks**
  - Log deletion/manipulation
  - Artifact cleanup
  - Anti-forensics techniques

**Key Tools:** Metasploit, Empire, Cobalt Strike, Netcat

---

### Domain 5: Covering Tracks
**Objective:** Hide evidence of attack

- **Log Management**
  - Clear application logs
  - Disable auditing
  - Clear system logs
  - Modify timestamps

- **Artifact Removal**
  - Delete temp files
  - Clear browser history
  - Remove registry entries

**Key Tools:** CCleaner, Eraser, Anti-forensics tools

---

## 🌐 Cryptography Essentials

| Algorithm | Type | Key Size | Security |
|-----------|------|----------|----------|
| **MD5** | Hash | 128-bit | ❌ Broken |
| **SHA-1** | Hash | 160-bit | ⚠️ Deprecated |
| **SHA-256** | Hash | 256-bit | ✅ Industry Standard |
| **SHA-512** | Hash | 512-bit | ✅ Very Secure |
| **AES** | Symmetric | 128/192/256 | ✅ NIST Approved |
| **RSA** | Asymmetric | 2048+bit | ✅ Secure |
| **Diffie-Hellman** | Key Exchange | 2048+bit | ✅ Secure |

---

## 🛡️ Security Models & Frameworks

- **CIA Triad**
  - Confidentiality: Only authorized access
  - Integrity: Data not altered
  - Availability: Service accessible when needed

- **AAA Framework**
  - Authentication: Verify identity
  - Authorization: Grant permissions
  - Accounting: Track activities

- **CVSS (Common Vulnerability Scoring System)**
  - 0.0 = None | 1.0-3.9 = Low
  - 4.0-6.9 = Medium | 7.0-8.9 = High
  - 9.0-10.0 = Critical

---

## 🚀 Quick Command Reference

```bash
# Port scanning
nmap -sV -p- target.com          # All ports with version
nmap -O target.com               # OS detection
nmap -A -T4 target.com           # Aggressive scan

# Password cracking
john --wordlist=rockyou.txt hashes.txt
HashCat -a 0 -m 1800 hash.txt wordlist.txt

# Web exploitation
sqlmap -u "http://target.com?id=1" --dbs
burpsuite                        # Web proxy/scanner

# Network tools
wireshark                        # Packet analysis
tcpdump -i eth0 'port 80'       # Capture traffic

# Privilege escalation
sudo -l                          # Check sudo permissions
whoami                           # Current user
```

---

## ⚡ Memory Aids

**Nmap Scan Types:**
- **-sS**: SYN (stealthy)
- **-sT**: TCP connect
- **-sU**: UDP
- **-sA**: ACK
- **-sP**: Ping sweep

**TCP Handshake:**
1. SYN (client → server)
2. SYN-ACK (server → client)
3. ACK (client → server)

**CVSS Score Calculation:**
Base Score × Temporal Score × Environmental Score

---

## ✅ Study Tips

✓ Understand the "why" behind each technique
✓ Practice in lab environments (HackTheBox, TryHackMe)
✓ Know the legal implications of each action
✓ Master tool usage through hands-on practice
✓ Review real-world penetration test reports
✓ Study case studies of major breaches

---

**Last Updated:** 2025  
**Purpose:** CEH Exam Preparation & Reference  
**Author:** Rohith D | CEH in Progress
