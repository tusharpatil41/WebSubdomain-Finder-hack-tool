🔍 SUBDOMAIN FINDER (Tushar Patil Edition) 🛡️
SUBDOMAIN FINDER is a professional Python-based security tool designed for the reconnaissance and infrastructure mapping phase of a penetration test. It automates the discovery of hidden subdomains and gathers deep technical intelligence about each discovered asset.


🚀 Features

Subdomain Enumeration: Rapidly checks for active subdomains using an optimized brute-force wordlist.

IP Geolocation Tracking: Identifies the physical location of each subdomain's server, including Country, City, and Timezone.

HTTP Header Retrieval: Extracts critical server information like Server software (Nginx, Apache, etc.) and technology stacks.

ISP & Organization Mapping: Detects the Internet Service Provider (ISP) and the organization hosting the subdomain (e.g., Cloudflare, AWS, Google).

Live Status Verification: Checks for real-time HTTP status codes (e.g., 200 OK, 403 Forbidden) to identify active targets.


🛠️ Installation & Usage
1. Requirements
Python 3.x

requests library

# Install dependencies
pip install requests


2. Setup (Termux or PC)

# Clone the repository
git clone https://github.com/tusharpatil41/WebSubdomain-Finder-hack-tool.git

# Enter the directory
cd WebSubdomain-Finder-hack-tool

# Run the tool
python Sub-Domain-Finder.py


📊 Technical Specifications
Language: Python 3

Dependencies: requests, socket, urllib, datetime

Data Source: Integrated with IP-API for real-time geolocation and network intelligence.

Portability: Fully compatible with PC (Windows/Linux) and Mobile (Termux).


👤 Author
Tushar Patil - Offensive Security Researcher & Tool Developer


⚠️ Disclaimer
This tool is for educational purposes only. Do not use it on targets without prior authorization. The author is not responsible for any misuse or legal consequences of this tool.
