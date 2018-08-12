encodingDic = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F", 16:"G"}
binaryList = [128, 64, 32, 16, 8, 4, 2, 1]
encodingList = [8, 4, 2, 1]
def rgb(r, g, b):
	r = hexa(r)
	g = hexa(g)
	b = hexa(b)
	return(str(r) + str(g) + str(b))    

def hexa(num):
	# Find binary of int
	binary = ""
	for x in range(8):
		if (num - binaryList[x] >= 0):
			num -= binaryList[x]
			binary += "1"
		else:
			binary += "0"
	firstBin, secondBin = binary[:int(len(binary)/2)], binary[int(len(binary)/2):]
	hexa1 = 0
	hexa2 = 0
	for x in range(len(firstBin)):
		if (firstBin[x] == "1"):
			hexa1 += encodingList[x]
	for x in range(len(secondBin)):
		if (secondBin[x] == "1"):
				hexa2 += encodingList[x]			

	return1 = hexa1 if hexa1<10 else encodingDic[int(hexa1)]
	return2 = hexa2 if hexa2<10 else encodingDic[int(hexa2)]
	if (not isInt(str(return1)+ str(return2))):
		return(str(return1) + str(return2))
	else:
		if (isInt(str(return1) + str(return2)) < 10):
			return("0" + str(hexa1 + hexa2))
		else:
			return(str(return1) + str(return2))
		

def isInt(string):
	try:
		num = int(string)
	except:
		return False
	return(num)
