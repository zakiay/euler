lim = 100

def sums():
	m = 0
	n = 0
	for i in range(1, lim+1):
		m += + i*i
		n += i

	return n*n - m

print sums()