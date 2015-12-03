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
    x = 0
    y = 0
    delivered = list([(x, y)])
    for dir in directions:
        x, y = Move(dir, x, y)
        delivered.append((x, y))
    return len(set(delivered))

source = open('input.txt').read()
print(Main(source))

