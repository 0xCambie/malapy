#!/bin/python3

import requests
from bs4 import BeautifulSoup
import argparse


base_url = "https://malapi.io/winapi/"

def find_information(apicall):
    r = requests.get(base_url+f"{apicall}").text
    soup = BeautifulSoup(r, features="lxml")
    title = soup.title.text
    function_name = soup.find_all("div", {"class": "content"})[0].get_text("", strip=True)
    description = soup.find_all("div", {"class": "content"})[1].get_text("", strip=True)
    library = soup.find_all("div", {"class": "content"})[2].get_text("", strip=True)
    associated_attacks = soup.find_all("span", {"class": "attack-container"})
    attacks = ""
    for attack in associated_attacks:
        attacks = attacks + (attack.get_text("", strip=True)) + " "    
    documentation_link = soup.find_all('a')[-1]['href']


    print(f"Function Call:\n\t{function_name}")
    print(f"General Description:\n\t{description}")
    print(f"Associated Library:\n\t{library}")
    print(f"Associated Attacks:\n\t{attacks}")
    print(f"Official Documentation:\n\t{documentation_link}")

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Finds information about Windos API calls.')
    parser.add_argument('-f', '--find', metavar='<WinAPI name>', help='Input the name of the Windows API Call.')
    args = parser.parse_args()

    if args.find:
        winapi_call = args.find
        find_information(winapi_call)
    else:
        print("Get help with --help or -h flags\n\tExample Usage: ./malAPY.py -f GetProcAddress")
