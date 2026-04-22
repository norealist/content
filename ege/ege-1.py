from itertools import permutations

tab = '27 146 45 236 367 245 15'.split()
pic = 'AD DC EC EB BA AG BF FG GD'.split()

print(*range(1, len(tab)+1))

for var in permutations(set(''.join(pic))):
    if all(str(var.index(x)+1) in tab[var.index(y)] for x,y in pic):
        print(*var)