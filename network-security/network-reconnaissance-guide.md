# 🌐 Network Reconnaissance Guide
## Information Gathering for Ethical Hackers & Security Professionals

---

## 📋 Table of Contents
- [Overview](#overview)
- [Passive Reconnaissance](#passive-reconnaissance)
- [Active Reconnaissance](#active-reconnaissance)
- [Tools & Techniques](#tools--techniques)
- [Best Practices](#best-practices)

---

## 🎯 Overview

**Network Reconnaissance** is the first phase of a penetration test where attackers (and defenders) gather information about target systems without direct engagement. Understanding this phase is crucial for both offensive and defensive cybersecurity.

### Why is Reconnaissance Important?
- ✅ Identifies network topology and structure
- ✅ Discovers active hosts and open ports
- ✅ Maps services and potential vulnerabilities
- ✅ Reduces time on-target for pen testing
- ✅ Helps defenders understand attacker perspective

---

## 🔍 Passive Reconnaissance

### Definition
Gathering information WITHOUT directly interacting with target systems. Leaves minimal traces.

### Techniques

#### 1. **DNS Enumeration**
- Query public DNS records
- Identify subdomains
- Reveal mail servers

```bash
# DNS lookup
nslookup target.com
dig target.com
digitalocean.com any
```

#### 2. **WHOIS Lookup**
- Domain registration information
- Owner details
- Hosting provider

```bash
whois target.com
```

#### 3. **IP Geolocation**
- Identify server locations
- Understand infrastructure distribution
- Plan attack/defense strategy

#### 4. **Google Dorking**
- Use search operators for information gathering
- Find exposed files, backups, admin panels

```
site:target.com filetype:pdf
site:target.com inurl:admin
cache:target.com
```

---

## 🎪 Active Reconnaissance

### Definition
Direct interaction with target systems. Must have written permission before testing!

### Techniques

#### 1. **ICMP Ping Sweep**
- Identify active hosts on network
- Quick availability check

```bash
ping -c 4 target.com          # Single ping
fping -g 192.168.1.0/24       # Network sweep
```

#### 2. **Port Scanning with Nmap**
- Discover open ports and services
- Identify service versions
- Most critical reconnaissance technique

```bash
# Basic scan
nmap target.com

# Aggressive scan with version detection
nmap -sV -A target.com

# Stealth scan (avoid detection)
nmap -sS target.com

# UDP scan
nmap -sU target.com
```

#### 3. **Service Enumeration**
- Identify service versions
- Search for known vulnerabilities
- Plan exploitation strategy

```bash
nmap -sV -p 22,80,443 target.com
```

#### 4. **Traceroute Analysis**
- Map network path to target
- Identify intermediate systems
- Spot filtering/firewall devices

```bash
traceroute target.com
mtr target.com  # Better alternative
```

---

## 🛠️ Tools & Techniques

| Tool | Purpose | Type |
|------|---------|------|
| **Nmap** | Port scanning & OS detection | Active |
| **Wireshark** | Network traffic analysis | Passive/Active |
| **Shodan** | IoT & infrastructure search | Passive |
| **theHarvester** | Email & subdomain enumeration | Passive |
| **Recon-ng** | Framework for reconnaissance | Passive |
| **Metasploit** | Scanning & exploitation | Active |
| **Burp Suite** | Web reconnaissance | Active |
| **DNS tools** | nslookup, dig, host | Passive |

---

## ⚡ Quick Reference: Nmap Commands

```bash
# Ping scan (host discovery)
nmap -sn 192.168.1.0/24

# Connect scan (full three-way handshake)
nmap -sT target.com

# SYN scan (half-open, stealthy)
nmap -sS target.com

# UDP scan
nmap -sU target.com

# Version detection
nmap -sV target.com

# OS detection
nmap -O target.com

# Aggressive scan
nmap -A -T4 target.com

# Scan specific ports
nmap -p 22,80,443,3306 target.com

# Scan all ports
nmap -p- target.com

# Output to file
nmap -oN results.txt target.com
```

---

## ✅ Best Practices

### 1. **Always Get Written Permission**
- Obtain scope documentation
- Define authorized targets
- Establish rules of engagement
- Never test without permission

### 2. **Document Everything**
- Record all findings
- Screenshot important results
- Note timestamps
- Keep detailed logs

### 3. **Minimize Detection**
- Use stealth techniques when appropriate
- Spread scans over time
- Use VPNs/proxies for anonymity
- Understand IDS/IPS limitations

### 4. **Respect Firewall Rules**
- Don't attempt to bypass firewalls
- Respect network segmentation
- Stay within scope boundaries

### 5. **Combine Multiple Techniques**
- Use both passive and active methods
- Cross-reference findings
- Build comprehensive network map

---

## 🚨 Common Mistakes

❌ Testing without written permission
❌ Scanning outside defined scope
❌ Using aggressive techniques on production systems
❌ Not documenting reconnaissance results
❌ Forgetting to disable scanning tools after testing

---

## 📚 Resources

- NMAP Official Guide: https://nmap.org/
- CEH Study Guide: Network Reconnaissance
- OWASP Testing Guide
- Metasploit Framework Documentation

---

**Last Updated:** 2025  
**Author:** Rohith D | CEH in Progress  
**Purpose:** Educational & Authorized Security Testing Only
