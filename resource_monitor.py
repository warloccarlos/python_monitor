import requests
import socket
import json
import multiprocessing
import time
from datetime import date
from requests import exceptions
import config_uat as cfgu

class monitor:

	s = socket.socket()
	
	identity_url = cfgu.access_token['identity_url']

	user = cfgu.access_token['user']
	password = cfgu.access_token['password']

	payload = cfgu.access_token['payload']

	headers = cfgu.access_token['headers']

	apiurls = cfgu.api_url.values()
	apiname = cfgu.api_url.keys() 

	def sendSMS(self, name):
		name = "message="+ name +"is having issue"
		url = cfgu.sms['url']
		payload = cfgu.sms['payload1'] + name + cfgu.sms['payload2']
		headers = cfgu.sms['headers']
		response = requests.request("POST", url, data=payload, headers=headers)
		print(response.text)
		return

	def access_tok(self, identity_url, payload, headers):
		response = requests.request("POST", identity_url, data=payload, headers=headers)
		print("Access Token received")
		val_json = response.json()
		return val_json

	def service_chk(self, name):
		inp = 1
		sms_count = 0
		while inp:
			for (ip, p) in zip(cfgu.services_ip, cfgu.services_ports):
				res = self.s.connect_ex((ip, p))
				if(res == 0 or res == 106):
					print(cfgu.services[p], " is up n running")
					sms_count = 0
				else:
					print(cfgu.services[p], " issue ", res)
					if(sms_count < 1):
						self.sendSMS()
						sms_count = sms_count + 1
			time.sleep(cfgu.delay['wait'])

	def acp_apis(self, bearer, url, name):
		try:
			inp = 1
			sms_count = 0
			bearer_tok = bearer
			url_headers = {'Authorization': "Bearer " + bearer_tok, 'Content-Type': "application/json"}
			while inp:
				response = requests.get(url)
				rcode = response.status_code
				if(rcode == 200):
					sms_count = 0
					print(name, "API Up and running", rcode)
				else:
					if(rcode == 401):
						resp_json = access_tok(identity_url, payload, headers)
						bearer_tok = resp_json['access_token']
					else:
						print(name, rcode)
						if(sms_count < 1):
							self.sendSMS(name)
							sms_count = sms_count + 1
				time.sleep(30)
		except KeyboardInterrupt:
			SystemExit(0)

	def f_calls(self):
		resp_json = self.access_tok(self.identity_url, self.payload, self.headers)
		bearer = resp_json['access_token']
		for (url, name) in zip(self.apiurls, self.apiname):
			p = Process(target=self.acp_apis, args=(bearer, url, name))
			p.start()
			
m = monitor()
m.f_calls()
