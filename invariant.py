def gange_syv(n):
  x = n
  r = 0
  while x > 0:
    print(f'invariant start: {7*x+r == 7*n}')
    x = x - 1
    r = r + 7
    print(f'invariant end: {7*x+r == 7*n}')
  return r

def ToPotens(n):
  x = n
  r = 1
  while x > 0:
    print(f'invariant start: {x >= 0}')
    r = 2*r
    x = x -1
    print(f'invariant end: {x >= 0}')
    return r

for i in range(5):
  ToPotens(i)