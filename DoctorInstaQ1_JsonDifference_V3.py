#V2 update
#Added programming for cases in which Keys are missing from one or other dict
# or value type does not match


def main():	
	jsonData_Source ='{"name":"Kaleigh","username":"Kaleigh60","email":"Kaleigh6047@gmail.com","address":{"street":"MyahCourse","suite":"Apt.657","city":"Boyerberg","zipcode":"66413-8920","geo":{"lat":"-44.6203","lng":"16.7454"}},"website":"megane.biz","friends":[{"name":"Little-Reinger","catchPhrase":"Enhancedregionalemulation"},{"name":"Big-Reinger","catchPhrase":"emulation"}],"Numbers":[1,2,3,4]}'
	jsonData_Destination = '{"name":"Kaligh","username":"Kaleigh60","email":"Kaleigh6047@gmail.com","address":{"street":"GoldCourse","suite":"Apt.657","city":"Boyerberg","zipcode":"66413-8920","geo":{"lat":"-44.6203","lng":"16.7454"}},"website":"megane.biz","friends":[{"name":"Reinger","catchPhrase":"Enhancedregionalemulation"},{"name":"Bigger-Reinger","catchPhrase":"emulation"}],"Numbers":[4,2,1,5]}'

	# jsonData_Source= '{"name":"Kaleigh","username":"Kaleigh60","email":"Kaleigh6047@gmail.com","address":{"street":"MyahCourse","suite":"Apt.657","city":"Boyerberg","zipcode":"66413-8920","geo":{"lat":"-44.6203","lng":"16.7454"}}}'
	# jsonData_Destination = '{"name":"Kaleigh","address":{"street":"MyahCourse","suite":"Apt.657","city":"Boyerberg","zipcode":"66413-8920","geo":{"lat":"-44.6203","lng":"16.7454"}},"username":"Kaleigh60","email":"Kaleigh6047@gmail.com"}'
	
	jsonData_Source='{"NotInDest":"OnlyInSource","firstItem":[1,2,3,4,5,6],"boolean":true,"boolean2":false,"boolean3":true,"color":"#82b92c","null":null,"number":123,"array2":[1,2,3,4,5,6],"array3":[1,2,3,4,2,3],"dict1":{"1":1,"2":2,"3":4},"object1":{"a":"b","c":"d","e":"f"},"object2":{"a":"b","c":"d","e":"f"},"object3":{"object1":{"a":"b","c":"d","e":"f"},"object2":{"a":"b","c":"d","e":"f"}},"object4":{"object1":{"a":"b","c":"d","e":"fzz"}},"string":"Hello World","string2":"Hello World","string3":"Hello World"}'
	jsonData_Destination='{"NotInSrc":"OnlyInDest","firstItem":[1,2,3,4,5,6],"boolean":true,"boolean2":false,"boolean3":true,"color":"#82b92c","null":null,"number":123,"array2":[1,2,3,4,6],"array3":[1,2,3,4],"dict1":{"1":1,"2":2,"3":4},"object1":{"a":"b","c":"d","e":"f"},"object2":{"a":"b","c":"d","e":"f"},"object3":{"object1":{"a":"b","c":"d","e":"f"},"object2":{"a":"b","c":"d","e":"f"}},"object4":{"object1":{"a":"b","c":"d","e":"f"},"object2":{"a":"b","c":"d","e":"f"}},"string":"Hello World","string2":"Hello World","string3":"Hello World"}'
	jsonDifference(jsonData_Source,jsonData_Destination)



def comparisonFunction(keyName,val1,val2,difference):
	keyNameBackup = keyName
	if isinstance(val1,list) is True:
		if isinstance(val2,list) is False:
			differnece[keyName] = [val1,val2]
		else:
			if len(val1) > len(val2):
				l = len(val2)
				l2 = len(val1)
				v= val1
			else:
				l = len(val1)
				l2=len(val2)
				v = val2
			for position in range(0,l):
				value1 = val1[position]
				value2 = val2[position]
				if isinstance(value1,list) is True:
					keyName += '[{}]'.format(position)
					if isinstance(value2,list) is False:
						difference[keyName] = [value1,value2]
					else:
						comparisonFunction(keyName,value1,value2,difference)
					keyName=keyNameBackup
				elif isinstance(value1,dict) is True:
					keyName += '[{}]'.format(position)
					if isinstance(value2,dict) is False:
						difference[keyName] = [value1,value2]
					comparisonFunction(keyName,value1,value2,difference)
					keyName=keyNameBackup
				else:
					keyName += '[{}]'.format(position)
					pair = [value1,value2]
					if pair[0] != pair[1]:
						difference[keyName] = pair
					keyName = keyNameBackup
			if len(val1) != len(val2):
				for pos in (position+1,l2):
					difference[keyName] = [val1,val2,'!!Error!! List length mismatch in source and destination json']
				
	elif isinstance(val1,dict) is True:
		if isinstance(val2,dict) is False:
			difference[keyName] = [val1,val2]
		else:
			keys_x = val1.keys()
			keys_y = val2.keys()
			if len(keys_x) >= len(keys_y):
				for subkey in keys_x:
					value1 = val1[subkey]
					try:
						value2 = val2[subkey]
						if isinstance(value1,list) is True:
							if isinstance(value2,list) is False:
								difference[keyName] = [value1,value2]
							else:
								keyName += '.{}'.format(subkey)
								comparisonFunction(keyName,value1,value2,difference)
								keyName = keyNameBackup
						elif isinstance(value1,dict) is True:
							if isinstance(value2,dict) is False:
								difference[keyName] = [value1,value2]
							else:
								keyName += '.{}'.format(subkey)
								comparisonFunction(keyName,value1,value2,difference)
								keyName = keyNameBackup
						else:
							keyName += '.{}'.format(subkey)
							pair=[value1,value2]
							if pair[0] != pair[1]:
								difference[keyName] = pair
							keyName=keyNameBackup
					except:
						difference[keyName+'.{}'.format(subkey)] = [value1,'!! ERROR !! Key missing in Destination Json']
			else:
				for subkey in keys_y:
					value2 = val2[subkey]
					try:
						value1 = val1[subkey]
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
					except:
						difference[keyName+'.{}'.format(subkey)] = ['!! ERROR !! Key missing in Source Json',value2]
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
	if len(key_x)>=len(key_y):
	
		for k in key_x:
			try:
				val1 = x[k]
			except:
				val2 = y[k]
				differnce[k] = ['!! ERROR !! Key missing in source Json',val2]
				continue
			try:
				val2 = y[k]
			except:
				difference[k] = [val1,'!! ERROR !! Key missing in Destination Json']
				continue
			comparisonFunction(k,val1,val2,difference)
		for k in key_y:
			if k not in key_x:
				difference[k] = ['!! ERROR !! Key missing in source Json',y[k]]
	else:
		for k in key_y:
			val2= y[k]
			try:
				val1=x[k]
				comparisonFunction(k,val1,val2,difference)
			except:
				difference[k] = ['!! ERROR !! Key missing in source Json',val2]
				
	print('{',end='')
	for x in difference.keys():
		print()
		print('{}: {},'.format(x,difference[x]))
	print('}')
	#assuming both json contain same keys atleast for now
	

main()
