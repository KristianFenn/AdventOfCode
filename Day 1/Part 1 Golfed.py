def m(s):
	return s.count('(') - s.count(')')

i = open('input.txt').read()
print(m(i))
