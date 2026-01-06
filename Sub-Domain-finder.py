import requests
import socket
import datetime
from urllib.parse import urlparse

def show_logos():
    print("*" * 80)
    print("* *")
    print("* PRESENTED BY: TUSHAR PATIL                                                   *")
    print("* *")
    
    tool_logo = """
     ██████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗  ██╗
    ██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗ ██║
    ╚█████╗ ██║   ██║██████╔╝██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗██║
     ╚════██╗██║   ██║██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚████║
    ██████╔╝╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚███║
    ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚══╝
    
     ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
     ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
     █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
     ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
     ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
     ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    """
    print(tool_logo)
    print("*" * 80)
    print(f"\n[!] Session Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def get_full_details(subdomain, url):
   
    details = {}
    try:
        # 1. IP Address and Geolocation
        ip = socket.gethostbyname(subdomain)
        geo_res = requests.get(f"http://ip-api.com/json/{ip}", timeout=3).json()
        
        # 2. HTTP Headers (Server info)
        response = requests.get(url, timeout=3)
        headers = response.headers
        
        print(f"\n[+] FOUND: {url}")
        print(f"    |-- IP Address: {ip}")
        print(f"    |-- Status    : {response.status_code}")
        print(f"    |-- Server    : {headers.get('Server', 'Hidden')}")
        print(f"    |-- Technology: {headers.get('X-Powered-By', 'Not Disclosed')}")
        print(f"    |-- Location  : {geo_res.get('city')}, {geo_res.get('country')}")
        print(f"    |-- ISP       : {geo_res.get('isp')}")
        print("-" * 50)
        return True
    except:
        return False

def find_subdomains():
    show_logos()
    target = input("\nEnter Target Domain (e.g. google.com): ").strip()
    
    # Powerful Wordlist
    wordlist = [
        'www', 'mail', 'ftp', 'admin', 'blog', 'dev', 'staging', 'api', 'test', 
        'vpn', 'ssh', 'cpanel', 'webmail', 'autodiscover', 'ns1', 'ns2', 'db', 
        'secure', 'shop', 'git', 'beta', 'demo', 'cloud', 'apps', 'support',
        'internal', 'status', 'proxy', 'portal', 'assets', 'static'
    ]

    print(f"\n[~] Hunting for subdomains on: {target}...")
    print("=" * 80)

    found_count = 0
    for sub in wordlist:
        subdomain = f"{sub}.{target}"
        url = f"http://{subdomain}"
        
        if get_full_details(subdomain, url):
            found_count += 1

    print("=" * 80)
    print(f"[+] Total Active Subdomains with Full Details: {found_count}")
    print("=" * 80)

if __name__ == "__main__":
    find_subdomains()