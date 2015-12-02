def Calc(l, w, h):
    areas = (l * w), (w * h), (h * l)
    return sum([x * 2 for x in areas]) + min(areas)

def Main(inputFile):
    total = 0
    with open(inputFile) as data:
        for line in iter(data.readline, ''):
            split = [int(x) for x in line.split('x')]
            total += Calc(split[0], split[1], split[2])
    return total

print(Main('input.txt'))