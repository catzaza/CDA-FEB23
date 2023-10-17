import json
import sys
import requests
import re
import getpass
import urllib3

### Settings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
### Configuration Definitions
def finishPostData(post_data, bad_post_data, t):
	post_data[t]['id'] = ""
	post_data[t]['links'] = ""
	post_data[t]['metadata'] = ""
	del post_data[t]['id']
	del post_data[t]['links']
	del post_data[t]['metadata']
	if len(post_data[t]['name']) > 30:
		bad_post_data.append(post_data[t])
		del post_data[t]
	return(post_data)
def enableLogging(post_data, t, loggOpt):
	if int(loggOpt) == 1:
		post_data[t]['logBegin'] = True
	elif int(loggOpt) == 2:
		post_data[t]['logEnd'] = True
	elif int(loggOpt) == 3:
		post_data[t]['logBegin'] = True
		post_data[t]['logEnd'] = True
	post_data[t]['sendEventsToFMC'] = True
	return(post_data)
def enableIPS(post_data, t, ips_uuid, ips_name):
	if post_data[t]['action'] == "ALLOW":
		post_data[t]['ipsPolicy'] = {'id': ips_uuid, 'name': ips_name, 'type': "intrusionpolicy"}
	return(post_data)
def postRules(policy_json_resp, get_json_resp, post_data, bad_post_data, server, headers, domain, change, ips_uuid, ips_name, loggOpt):
	for i in range(0,len(get_json_resp['items'])):
		post_data.append(get_json_resp['items'][i])
	for t in range(0,len(post_data)):
		if int(change) == 1:
			enableLogging(post_data, t, loggOpt)
		elif int(change) == 2:
			enableIPS(post_data, t, ips_uuid, ips_name)
		finishPostData(post_data, bad_post_data, t)
		with open('post_data.log', 'w') as f:
			print(post_data, file=f)
		api_path = "/api/fmc_config/v1/domain/"+domain+"/policy/accesspolicies/"+policy_json_resp['id']+"/accessrules?bulk=true"
		url = server + api_path
	r = requests.post(url, data=json.dumps(post_data), headers=headers, verify=False)
	post_request_data = json.loads(r.text)
	post_request_data_status_code = r.status_code
### Policy Definitions
def getIPS(headers, server, domain):
	ips_api_path = "/api/fmc_config/v1/domain/"+domain+"/policy/intrusionpolicies"
	ips_url = server+ips_api_path
	ips = requests.get(ips_url, headers=headers, verify=False)
	ips_data = json.loads(ips.text)
	ips_policies = {}
	cnt = 0
	for i in range(0, len(ips_data['items'])):
		cnt = cnt+1
		ips_policies[cnt] = ips_data['items'][i]['name']
	print("IPS Polices: ")
	print(ips_policies)
	choice = input("Which IPS policy are we using: ")
	for i in range(0, len(ips_data['items'])):
		if ips_policies[int(choice)] == ips_data['items'][i]['name']:
			ips_uuid = ips_data['items'][i]['id']
			ips_name = ips_data['items'][i]['name']
	return(ips_uuid, ips_name)
def getACPs(headers, server, domain):
	acp_api_path = "/api/fmc_config/v1/domain/"+domain+"/policy/accesspolicies"
	acp_url = server+acp_api_path
	acp = requests.get(acp_url, headers=headers, verify=False)
	acp_data = json.loads(acp.text)
	polices = {}
	cnt = 0
	for i in range(0, len(acp_data['items'])):
		if re.search('._copy$', acp_data['items'][i]['name']) is not None:
			del_acp = requests.delete(acp_url+"/"+acp_data['items'][i]['id'], headers=headers, verify=False)
		else:
			cnt = cnt+1
			polices[cnt] = acp_data['items'][i]['name']
	print("Polices: ")
	print(polices)
	choice = input("Which policy are we editing: ")
	for i in range(0, len(acp_data['items'])):
		if polices[int(choice)] == acp_data['items'][i]['name']:
			uuid = acp_data['items'][i]['id']
	return(uuid)
### Utility Definitions
def copyACP(headers, server, uuid, domain):
	try:
		getdefaultAction_api_path = "/api/fmc_config/v1/domain/"+domain+"/policy/accesspolicies/"+uuid
		getdefaultAction_url = server + getdefaultAction_api_path
		getd = requests.get(getdefaultAction_url, headers=headers, verify=False)
		getdefaultAction_data = json.loads(getd.text)
		defaultAction_api_path = "/api/fmc_config/v1/domain/"+domain+"/policy/accesspolicies/"+uuid+"/defaultactions/"+getdefaultAction_data['defaultAction']['id']
		defaultAction_url = server + defaultAction_api_path
		d = requests.get(defaultAction_url, headers=headers, verify=False)
		defaultAction_data = json.loads(d.text)
		api_path = "/api/fmc_config/v1/domain/"+domain+"/policy/accesspolicies/"+uuid
		url = server + api_path
		r = requests.get(url, headers=headers, verify=False)
		policy_data = json.loads(r.text)
		policy_data['name'] = policy_data['name']+"_copy"
		policy_data['defaultAction'] = defaultAction_data
		del policy_data['id']
		del policy_data['rules']
		del policy_data['links']
		del policy_data['metadata']
		api_path = "/api/fmc_config/v1/domain/"+domain+"/policy/accesspolicies"
		url = server + api_path
		r = requests.post(url, data=json.dumps(policy_data), headers=headers, verify=False)
		status_code = r.status_code
		resp = r.text
		if (status_code == 201):
			print("Policy copied successfully")
			policy_json_resp = json.loads(resp)
		else:
			r.raise_for_status()
			print("Status code:-->")
			print(status_code)
			print("Error occurred in POST:--> "+resp)
	except requests.exceptions.HTTPError as err:
		print ("Error in connection --> "+str(err))
	finally:
		if r: r.close()
	return(policy_json_resp)
def main():
	ip_port = input('Server Address <:port>: ')
	server = "https://"+ip_port
	username = input('Username: ')
	password = getpass.getpass('Password:')
	ips_uuid = ""
	ips_name = ""
	loggOpt = 0
	# server = "https://10.201.163.38:446"
	# username = "admin"
	# password = "Admin123"
	r = None
	headers = {'Content-Type': 'application/json'}
	api_auth_path = "/api/fmc_platform/v1/auth/generatetoken"
	auth_url = server + api_auth_path
	try:
		print('Authenticating User ...')
		r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username,password), verify=False)
		auth_headers = r.headers
		auth_token = auth_headers.get('X-auth-access-token', default=None)
		if auth_token == None:
			print("auth_token not found. Exiting...")
			sys.exit()
	except Exception as err:
		print ("Error in generating auth token --> "+str(err))
		sys.exit()
	print('User Authenticated Successfully.')
	headers['X-auth-access-token']=auth_token
	auth_domain = json.loads(auth_headers.get('domains', default=None))
	cnt = 0
	domains = {}
	if len(auth_domain) > 1:
		for i in range(0, len(auth_domain)):
			cnt = cnt+1
			domains[cnt] = auth_domain[i]['name']
		print('Domains: ')
		print(domains)
		choice = input("Which domain are we using: ")
		for i in range(0, len(auth_domain)):
			if domains[int(choice)] == auth_domain[i]['name']:
				domain = auth_domain[i]['uuid']
		print("We are using this domain ID: "+domain)
		print()
		print()
	elif len(auth_domain) == 0:
		print("Erroring grabbing domains. Exiting...")
		sys.exit()
	uuid = getACPs(headers, server, domain)
	post_data = []
	bad_post_data = []
	policy_json_resp = copyACP(headers, server, uuid, domain)
	print("Configurations:")
	print("1: Enabling Logging, 2: Enable IPS")
	change = input('Which Configuration Change do we want: ')
	if int(change) == 1:
		print("1: Log at Begin, 2: Log at End, 3: Log at Both")
		loggOpt = input("How are we enabling Logging: ")
		print("Enabling Logging on all rules")
	elif int(change) == 2:
		print("Enabling IPS on all rules")
		ips_uuid, ips_name = getIPS(headers, server, domain)
		print(ips_uuid)
		print(ips_name)
	else:
		print("invalid Entry. Exiting...")
		sys.exit()
	print()
	print()
	try:
		api_path = "/api/fmc_config/v1/domain/"+domain+"/policy/accesspolicies/"+uuid+"/accessrules?limit=1000&expanded=true"
		url = server + api_path
		if (url[-1] == '/'):
			url = url[:-1]
		r = requests.get(url, headers=headers, verify=False)
		status_code = r.status_code
		resp = r.text
		if (status_code == 200):
			print("GET successful. Response data --> ")
			get_json_resp = json.loads(resp)
			#with open('json_resp.log', 'w') as f:
			#	print(get_json_resp, file=f)
			postRules(policy_json_resp, get_json_resp, post_data, bad_post_data, server, headers, domain, change, ips_uuid, ips_name, loggOpt)
			status_code = r.status_code
			resp = r.text
			if (status_code == 201):
				print("Post was successful")
			elif (status_code == 200):
				#print("GET was successful")
				print()
			else:
				r.raise_for_status()
				print("Status code:-->"+str(status_code))
				print("Error occurred in POST:--> "+resp)
			countl = 0
			while get_json_resp['paging'].get('next') != None:
				countl+=1
				post_data = []
				bad_post_data = []
				try:
					link = get_json_resp['paging']['next'][0]
					np = requests.get(link, headers=headers, verify=False)
					np_resp = np.text
					status_code = r.status_code
					get_json_resp = json.loads(np_resp)
					postRules(policy_json_resp, get_json_resp, post_data, bad_post_data, server, headers, domain, change, ips_uuid, ips_name, loggOpt)
					status_code = r.status_code
					resp = r.text
					if (status_code == 201):
						print("Post was successful")
					elif (status_code == 200):
						#print("GET was successful")
						print()
					else:
						r.raise_for_status()
						print("Status code:-->"+str(status_code))
						print("Error occurred in POST:--> "+resp)
				except requests.exceptions.HTTPError as err:
					print ("Error in connection --> "+str(err))
				finally:
					if r: r.close()
				with open('post_data.log', 'w') as f:
					print(post_data, file=f)
				with open('bad_post_data.log', 'w') as f:
					print(bad_post_data, file=f)
		else:
			r.raise_for_status()
			print("Error occurred in GET --> "+resp)
	except requests.exceptions.HTTPError as err:
		print ("Error in connection --> "+str(err))
	finally:
		if r : r.close()
	print()
	print()
	print("Finished!")
main()
