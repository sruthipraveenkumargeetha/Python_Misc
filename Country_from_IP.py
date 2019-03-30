#finding IP location from IP
#pip install requests

import requests

def what_country(ip):

	API="https://api.ip2country.info/ip?{}"
	response=requests.get(API.format(ip))
	data=response.json()
	return data["countryName"]

ips="212.45.128.255","122.45.127.255","165.45.211.255"

print what_country(ips[0])
print what_country(ips[1])
print what_country(ips[2])
