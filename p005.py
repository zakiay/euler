counter = 20
found = False

def go(num):
	for i in range(10, 22, 1):
		if num % i != 0:
			return False
	found = True
	return True

while not found:
	if(go(counter)):
		print counter
		break
	else:
		counter += 20