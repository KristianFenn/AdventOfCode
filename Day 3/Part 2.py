def Move(dir, x, y):
    if dir == '>':
        x += 1
    elif dir == '<':
        x -= 1
    elif dir == '^':
        y += 1
    elif dir == 'v':
        y -= 1
    return (x, y)

def Main(directions):
    santaDir = directions[0::2]
    roboDir = directions[1::2]
    x, y = 0, 0
    delivered = list([(x, y), (x, y)])
    for dir in santaDir:
        x, y = Move(dir, x, y)
        delivered.append((x, y))
    x, y = 0, 0
    for dir in roboDir:
        x, y = Move(dir, x, y)
        delivered.append((x, y))
    return len(set(delivered))

source = open('input.txt').read()
print(Main(source))

