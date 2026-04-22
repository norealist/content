def toN(num: int, n: int):
    s = ''
    while num != 0:
        s = str(num%n) + s 
        num //= n
    return s

from string import ascii_uppercase

z = []
for x in range(0,2031):
    a = 6**2030 + 6**100 - x
    z.append(toN(a, 6).count('0'))

print((z))