from math import pow, log2, log10

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
  x = 1
  r = 0
  while x < n:
    print(f'invariant start: {x < 2*n}')
    x = 2 * x
    r = r + 1
    print(f'invariant end: {x < 2*n}')
  return r

# n >= 0
# for i in range(5):

# n >= 1
for i in range(1, 6):
  ToPotens(i)