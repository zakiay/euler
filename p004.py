def isPal(n):
	strNumber = str(n)

	if len(n) % 2 == 0: # length is even, must compare first with last, and so on	
		for i in range(0, len(strNumber) / 2):
			if strNumber[i] != strNumber[len(strNumber) - i - 1]:
				return False
	else: # length is odd, can ignore middle number
		for i in range(0, (len(strNumber) - 1) / 2): # -1 is to ignore the middle character 
			if strNumber[i] != strNumber[len(strNumber) - i - 1]:
				return False
	return True

temp = 0 
for i in range(100, 1000):
	for j in range(i, 1000):	
		if isPal(str(i*j)):
			if temp < (i*j):
				temp = i*j

print "\nPalindrom: \t", temp
