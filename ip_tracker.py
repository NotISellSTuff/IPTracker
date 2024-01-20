import requests
import colorama
from colorama import Fore, Back, Style

print(Fore.BLUE + """
  _____ _____    _______             _             
 |_   _|  __ \  |__   __|           | |            
   | | | |__) |    | |_ __ __ _  ___| | _____ _ __ 
   | | |  ___/     | | '__/ _` |/ __| |/ / _ \ '__|
  _| |_| |         | | | | (_| | (__|   <  __/ |   
 |_____|_|         |_|_|  \__,_|\___|_|\_\___|_|   

      Made By ISellStuff                                                   
      
      """)

def get_ip_info(ip):
            try:
                response = requests.get(f"https://ipinfo.io/{ip}")
                response.raise_for_status()
                ip_info = response.json()
                print()
                print(f"Hostname: {ip_info['hostname']}")
                print(f"City: {ip_info['city']}")
                print(f"State: {ip_info['region']}")
                print(f"Country: {ip_info['country']}")
                print(f"Location: {ip_info['loc']}")
                print(f"ISP: {ip_info['org']}")
            except requests.exceptions.HTTPError as e:
                print("[!] Unable to retrieve information. Error: ", e)
ip = input("Enter an IP address: ")
get_ip_info(ip)
print()

input(Fore.BLUE + "Press Enter To Close....")