import urllib, json
import requests
import time

if __name__ == "__main__":
	lastDay = u'2017'
	while(True):
		try:
			while(True):
				data = json.loads(requests.get("http://data.taipei/youbike").content)
				if data['retVal']['0001']['mday'] != lastDay:
					lastDay = data['retVal']['0001']['mday']
					with open('data/'+lastDay+'.json', 'w') as json_file:
						json.dump(data,json_file)
					print 'data renew!' + lastDay
				time.sleep(30)
		except:
			pass
	#data = json.loads(response.read())
	#print data
