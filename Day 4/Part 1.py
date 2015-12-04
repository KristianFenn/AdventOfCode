import hashlib

def Main(input):
    cur = 1
    while(True):
        m = hashlib.md5()
        s = input + str(cur)
        m.update(s.encode('ascii'))
        result = m.hexdigest()
        if (result[0:5] == '00000'):
            break;
        cur += 1
    return cur

print(Main('iwrupvqb'))