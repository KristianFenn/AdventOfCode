def Main(s):
	floor = 0
	index = 0
	for char in source:
		if (char == '('):
			floor += 1
		elif (char == ')'):
			floor -= 1
		index += 1
		if (floor < 0):
			return index

source = open('input.txt').read()
print(Main(source))
