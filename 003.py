# prime numbers
# 13195 = 5, 7, 13, 29...
# 600851475143 = ...

n = 600851475143

def isPrime(m):
	if m % 2 == 0:
		return False
	for j in range(3, m, 2):
		if m % j == 0:
			return False
	return True

i = 1
while i < n:
	if n % i == 0:
		if isPrime(i):
			print i
		
	i += 2

