import os
import time
import json
import requests

from colorama import Fore, Back, Style, init
from prettytable import PrettyTable


def initialize_sites():
    for site in sites:
        site["total_requests"] = 0
        site["successful_requests"] = 0

def check_sites():
    for site in sites:
        try:
            response = requests.get(site["url"], timeout=2)
            site["status"] = "UP" if response.status_code == 200 else "DOWN"
        except requests.exceptions.ConnectionError:
            site["status"] = "DOWN"

        site["total_requests"] += 1
        if site["status"] == "UP":
            site["successful_requests"] += 1

        if site["status"] == "DOWN":
            send_discord_webhook(site["name"], site["url"])

def print_table(sites):
    x = PrettyTable()
    x.field_names = ["Site Name", "Status", "Rate", "Uptime"]
    for site in sites:
        formatted_site = format_site(site)
        x.add_row(formatted_site)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(x)

def send_discord_webhook(site_name, site_url):
    try:
        data = {
            "content": f":warning: {site_name} ({site_url}) is DOWN! :warning:"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers)
    
    except:
        pass

def format_site(site):
    rate = f"{site['successful_requests']}/{site['total_requests']}"
    uptime = (site["successful_requests"] / site["total_requests"]) * 100 
    if site["status"] == "UP":
        status = Fore.GREEN + site["status"] + Style.RESET_ALL
    else:
        status = Fore.RED + site["status"] + Style.RESET_ALL
    return [site["name"], status, Fore.YELLOW + rate + Style.RESET_ALL, f"{uptime:.2f}%"]

sites = [
    {"name": "Site A", "url": "https://sitea.com"},
    {"name": "Site B", "url": "http://siteb.com"}
]

WEBHOOK_URL = "" #DC Webhook URL

init(autoreset=True)
initialize_sites()
while True:
    check_sites()
    print_table(sites)
    time.sleep(3)
