﻿def Main(s):
	floor = 0
	for char in s:
		if (char == '('):
			floor += 1
		elif (char == ')'):
			floor -= 1
	return floor

source = open('input.txt').read()
print(Main(source))
