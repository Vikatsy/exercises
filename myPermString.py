def myPermString(MyStr):
	if len(MyStr) == 0:
		yield[]
	elif len(MyStr)	 == 1:
		yield MyStr
	else:
			for i in range (len(MyStr)):
				s = MyStr[i]
				s_rest = MyStr[:i] + MyStr[i+1:]
				for k in myPermString(s_rest):
					yield [s] + k

data = list('gabsd')
for x in myPermString(data):
	print x					