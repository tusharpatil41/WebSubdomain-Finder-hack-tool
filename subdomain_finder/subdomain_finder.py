import requests
import socket
import datetime
from urllib.parse import urlparse

def show_logos():
    print("*" * 85)
    print("* *")
    print("* PRESENTED BY: TUSHAR PATIL                                                    *")
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
    print("*" * 85)
    print(f"\n[!] Session Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[!] Target Setting: Subdomain Enumeration + IP Geo + Header Analysis")

def get_detailed_info(subdomain):
    
    url = f"http://{subdomain}"
    try:
        # 1. HTTP Status and Headers
        response = requests.get(url, timeout=4)
        headers = response.headers
        
        # 2. IP Resolution
        ip = socket.gethostbyname(subdomain)
        
        # 3. IP Geolocation Analysis
        geo_data = requests.get(f"http://ip-api.com/json/{ip}", timeout=4).json()
        
        # Display Results in a Professional Format
        print(f"\n[+] TARGET FOUND: {subdomain}")
        print(f"    |-- URL Status     : {response.status_code} OK")
        print(f"    |-- IP Address     : {ip}")
        print(f"    |-- Server Software: {headers.get('Server', 'Not Disclosed')}")
        print(f"    |-- Technology     : {headers.get('X-Powered-By', 'Hidden')}")
        print(f"    |-- Geolocation    : {geo_data.get('city')}, {geo_data.get('country')} ({geo_data.get('countryCode')})")
        print(f"    |-- ISP/Org        : {geo_data.get('isp')} / {geo_data.get('org')}")
        print(f"    |-- Timezone       : {geo_data.get('timezone')}")
        print("-" * 60)
        return True
    except (requests.ConnectionError, socket.gaierror):
        return False
    except Exception as e:
        return False

def run_subdomain_finder():
    show_logos()
    target_domain = input("\nEnter Target Domain (e.g., example.com): ").strip()
    
    # Powerful Brute-force Wordlist
    common_subs = [
        'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk', 
        'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 'dev', 'direct', 
        'admin', 'test', 'api', 'staging', 'vpn', 'secure', 'cloud', 'portal'
    ]

    print(f"\n[~] Enumerating subdomains for: {target_domain}...")
    print("=" * 85)

    success_count = 0
    for sub in common_subs:
        current_sub = f"{sub}.{target_domain}"
        if get_detailed_info(current_sub):
            success_count += 1

    print("=" * 85)
    print(f"[!] Scan Completed. Total Subdomains Analyzed: {success_count}")
    print("=" * 85)

if __name__ == "__main__":
    run_subdomain_finder()