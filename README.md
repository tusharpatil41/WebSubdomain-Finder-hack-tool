# 🔍 SUBDOMAIN FINDER (Tushar Patil Edition) 🛡️

**SUBDOMAIN FINDER** is a professional **Python-based security reconnaissance tool**
designed for the **subdomain discovery and infrastructure mapping phase**
of a penetration test.
It automates the identification of hidden subdomains and gathers
deep technical intelligence about each discovered asset.

---

## 🚀 Features

- 🔎 **Subdomain Enumeration**  
  Rapidly checks for active subdomains using an optimized brute-force wordlist.

- 🌍 **IP Geolocation Tracking**  
  Identifies the physical location of each subdomain’s server, including
  **Country, City, and Timezone**.

- 🧾 **HTTP Header Retrieval**  
  Extracts critical server information such as **web server software**
  (Apache, Nginx, Cloudflare, etc.) and technology stacks.

- 🏢 **ISP & Organization Mapping**  
  Detects the **Internet Service Provider (ISP)** and the organization hosting
  the subdomain (e.g., Cloudflare, AWS, Google).

- ✅ **Live Status Verification**  
  Checks real-time HTTP status codes (200, 301, 403, etc.) to identify active targets.

---

## 🛠️ Installation & Usage

### 1️⃣ Requirements
- Python 3.x
- `requests` library
- pip install requests

  
### 2️⃣ Setup (Termux or PC)

```bash
# Clone the repository
git clone https://github.com/tusharpatil41/WebSubdomain-Finder-hack-tool.git

# Navigate to the directory
cd WebSubdomain-Finder-hack-tool
cd subdomain_finder

# Run the tool
python Sub-Domain-Finder.py


📊 Technical Specifications
Language: Python 3
Dependencies: requests, socket, urllib, datetime
Data Source: IP-API (real-time geolocation & network intelligence)
Portability: Windows / Linux , Android (Termux)


👤 Author
Tushar Patil
Offensive Security Researcher & Ethical Hacking Tool Developer


⚠️ Disclaimer
This tool is developed strictly for educational and ethical security testing purposes.
Do NOT use this tool on any system or domain without explicit prior authorization.

The author is not responsible for any misuse or legal consequences arising from the use of this tool.

