from collections import deque
import re
from ast import literal_eval
d = deque()
a= input()
a = (re.findall("[^,]+",a[1:-1]))
for n,i in enumerate(a):
	try:
		# number
		if(int(i)): d.append(int(i))
	except ValueError:
		# boolean
		if(i =="true" or i==True): d.append(True)
		elif(i =="false" or i==False): d.append(False)
		# array
		elif(i[0]=="[" and a[n+1][-1]=="]"):
			d.append(literal_eval(i+","+a[n+1]))
		elif(i[-1]=="]"):
			continue
		else:
			d.append( (re.findall("[^'|\"]+",i))[0])
print(list(d))
