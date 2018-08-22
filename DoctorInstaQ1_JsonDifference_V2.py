#V2 update
#cleaned up the code

def main():	
	jsonData_Source ='{"name":"Kaleigh","username":"Kaleigh60","email":"Kaleigh6047@gmail.com","address":{"street":"MyahCourse","suite":"Apt.657","city":"Boyerberg","zipcode":"66413-8920","geo":{"lat":"-44.6203","lng":"16.7454"}},"website":"megane.biz","friends":[{"name":"Little-Reinger","catchPhrase":"Enhancedregionalemulation"},{"name":"Big-Reinger","catchPhrase":"emulation"}],"Numbers":[1,2,3,4]}'
	jsonData_Destination = '{"name":"Kaligh","username":"Kaleigh60","email":"Kaleigh6047@gmail.com","address":{"street":"GoldCourse","suite":"Apt.657","city":"Boyerberg","zipcode":"66413-8920","geo":{"lat":"-44.6203","lng":"16.7454"}},"website":"megane.biz","friends":[{"name":"Reinger","catchPhrase":"Enhancedregionalemulation"},{"name":"Big-Reinger","catchPhrase":"emulation"}],"Numbers":[4,2,1,5]}'

	# jsonData_Source= '{"name":"Kaleigh","username":"Kaleigh60","email":"Kaleigh6047@gmail.com","address":{"street":"MyahCourse","suite":"Apt.657","city":"Boyerberg","zipcode":"66413-8920","geo":{"lat":"-44.6203","lng":"16.7454"}}}'
	# jsonData_Destination = '{"name":"Kaleigh","address":{"street":"MyahCourse","suite":"Apt.657","city":"Boyerberg","zipcode":"66413-8920","geo":{"lat":"-44.6203","lng":"16.7454"}},"username":"Kaleigh60","email":"Kaleigh6047@gmail.com"}'

	jsonDifference(jsonData_Source,jsonData_Destination)



def comparisonFunction(keyName,val1,val2,difference):
	keyNameBackup = keyName
	if isinstance(val1,list) is True:
		for position in range(0,len(val1)):
			value1 = val1[position]
			value2 = val2[position]
			if isinstance(value1,list) is True or isinstance(value1,dict) is True:
				keyName += '[{}]'.format(position)
				comparisonFunction(keyName,value1,value2,difference)
				keyName=keyNameBackup
			else:
				keyName += '[{}]'.format(position)
				pair = [value1,value2]
				if pair[0] != pair[1]:
					difference[keyName] = pair
				keyName = keyNameBackup
				
	elif isinstance(val1,dict) is True:
		keys = val1.keys()
		#keys will be same for both val1, val2
		for subkey in keys:
			value1 = val1[subkey]
			value2 = val2[subkey]
			if isinstance(value1,list) is True or isinstance(value1,dict) is True:
				keyName += '.{}'.format(subkey)
				comparisonFunction(keyName,value1,value2,difference)
				keyName = keyNameBackup
			else:
				keyName += '.{}'.format(subkey)
				pair=[value1,value2]
				if pair[0] != pair[1]:
					difference[keyName] = pair
				keyName=keyNameBackup
	else:
		pair=[val1,val2]
		if pair[0] != pair[1]:
			difference[keyName] = pair

def jsonDifference(json1,json2):
	import json
	x=json.loads(json1)
	y=json.loads(json2)
	
	difference = dict()
	key_x = x.keys()
	key_y = y.keys()
	
	for k in key_x:
		val1 = x[k]
		val2 = y[k]
		comparisonFunction(k,val1,val2,difference)
	
	print('{',end='')
	for x in difference.keys():
		print()
		print('{}: {},'.format(x,difference[x]))
	print('}')
	#assuming both json contain same keys atleast for now
	

main()
