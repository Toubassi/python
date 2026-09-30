def larger(a, b):
    if a > b:
        return a
    return a

print(larger(1, 4)) #expected 4, returns 1
print(larger(9, 2)) #expecte 9, returns 9

def larger_fixed(c, d):
    if c > d:
        return c
    else:
        return d

print(larger_fixed(9, 11)) #expected 11, returns 11
print(larger_fixed(19, 1)) #expected 19, returns 19