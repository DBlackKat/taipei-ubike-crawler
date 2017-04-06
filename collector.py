import urllib, json
import requests
import time
if __name__ == "__main__":
	url = "http://data.ntpc.gov.tw/api/v1/rest/datastore/382000000A-000352-001"
	try:
		lastDay = u'2017'
		while(True):
			data = json.loads(requests.get("http://data.taipei/youbike").content)
			if data['retVal']['0001']['mday'] != lastDay:
				lastDay = data['retVal']['0001']['mday']
				with open(lastDay+'.json', 'w') as json_file:
					json.dump(data,json_file)
				print 'data renew!' + lastDay
			time.sleep(30)
	except:
		pass
	#data = json.loads(response.read())
	#print data
