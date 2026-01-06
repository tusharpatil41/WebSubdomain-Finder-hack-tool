import socket
import requests
from urllib.parse import urlparse
import datetime

def show_logo():
    # WEB RECON Main Logo with Tushar Patil's Name
    logo = """
    ***************************************************************************
    * *
    * TUSHAR PATIL Presents:                                                 *
    * *
    * ██╗    ██╗███████╗██████╗      ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗ *
    * ██║    ██║██╔════╝██╔══██╗     ██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║ *
    * ██║ █╗ ██║█████╗  ██████╔╝     ██████╔╝█████╗  ██║     ██║  ██║██╔██╗ ██║ *
    * ██║███╗██║██╔══╝  ██╔══██╗     ██╔══██╗██╔══╝  ██║     ██║  ██║██║╚██╗██║ *
    * ╚███╔███╔╝███████╗██████╔╝     ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║ *
    * ╚══╝╚══╝ ╚══════╝╚═════╝      ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ *
    * *
    * [+] Web Reconnaissance Framework v1.1                                  *
    * Purpose: Reconnaissance & IP Geolocation Tracking                      *
    ***************************************************************************
    """
    print(logo)
    print(f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def ip_tracker(ip):
    """
    Feature: Track the physical location of the target server IP.
    """
    try:
        print("\n[+] Tracking IP Location Details...")
        # Using IP-API to fetch geolocation data
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        
        if response['status'] == 'success':
            print(f"    - Country     : {response['country']} ({response['countryCode']})")
            print(f"    - Region/State : {response['regionName']}")
            print(f"    - City        : {response['city']}")
            print(f"    - Zip Code    : {response['zip']}")
            print(f"    - ISP         : {response['isp']}")
            print(f"    - Organization: {response['org']}")
        else:
            print("[!] Could not retrieve location for this IP.")
    except Exception as e:
        print(f"[!] Tracker Error: {e}")

def web_recon():
    show_logo()
    
    url = input("\nEnter Target URL (e.g., https://google.com): ").strip()
    
    if not url.startswith("http"):
        print("\n[!] Error: URL must start with http:// or https://")
        return

    domain = urlparse(url).netloc
    print(f"\n[~] Scanning Target: {domain}")

    # 1. Resolve IP Address
    ip_addr = ""
    try:
        ip_addr = socket.gethostbyname(domain)
        print(f"[+] IP Address: {ip_addr}")
        
        # Start IP Tracker once IP is found
        ip_tracker(ip_addr)
        
    except:
        print("[!] Could not resolve IP Address.")

    # 2. Fetch Server & HTTP Header Info
    try:
        print("\n[+] Fetching Server Headers...")
        response = requests.get(url, timeout=5)
        headers = response.headers
        
        server = headers.get('Server', 'Not Disclosed')
        print(f"[+] Web Server: {server}")
        
        print("\n--- Important HTTP Headers ---")
        keys_to_check = ['Content-Type', 'Content-Encoding', 'X-Powered-By', 'Strict-Transport-Security']
        for key in keys_to_check:
            if key in headers:
                print(f"{key}: {headers[key]}")
            else:
                print(f"{key}: Not Found")
                
    except Exception as e:
        print(f"[!] HTTP Connection Failed: {e}")

    print("\n" + "="*50)
    print("Scan Complete! Developed by Tushar Patil")
    print("="*50)

if __name__ == "__main__":
    web_recon()