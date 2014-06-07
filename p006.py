lim = 100

def sums():
	s = 0
	for i in range(1, lim+1):
		s += + i*i

	return s

def sqrt():
	s = 0
	for i in range(1, lim+1):
		s += i

	return s*s

print sqrt(), " - ", sums(), " = ", sqrt() - sums()
