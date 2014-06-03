
#	1	2	3	5	8	13	21	34
#	x	y	z
#		x	y	z
#			x	y	z
#				x	y	z
#					x	y	z
#						x	y	z

# z = y + x
# x = y 
# y = z
##############

x = 1
y = 2
z = 0

s = 0

while y <= 4000000:
	z = y + x
	x = y
	y = z

	if y % 2 == 0:
		s += y

print "\n\tSum: %d\n" % s

