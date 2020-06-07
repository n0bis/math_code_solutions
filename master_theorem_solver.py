import math

def calc(a, b, k, i):
  if (a == b and k == i and k > 0 and i > 0):
    raise Exception("Cannot be resolved - might be case 2 or case 3")
  p = math.log(a) / math.log(b)
  result = 'T(n) = \u0398('
  if floatEquals(p, k):
    result += formatPolyLog(k, i + 1)
  elif p < k:
    result += formatPolyLog(k, i)
  elif p > k:
    if floatEquals(round(p), p):
      result += formatPolyLog(round(p), 0)
    else:
      result += formatPolyLog(f'(log_{b}({a}))', 0)
      result += f') ≈ \u0398({formatPolyLog(round(p, 3), 0)}'
  result += ")"
  if a > math.pow(b, k):
    print('case 1')
  if a == math.pow(b, k):
    print('case 2')
  if a < math.pow(b, k):
    print('case 3')
  print(result)

def formatPolyLog(k, i):
  # Process n^k
  result = ''
  if isinstance(k, str):
    result = f'n^{k}'
  if k == 0:
    result = '1'
  elif k == 0.5:
    result = 'sqrt(n)'
  elif k == 1:
    result = 'n'
  else:
    result = f'n^{k}'

  if i != 0:
    if result != '':
      result += ' '
    result += 'log'
    if i != 1:
      result += f'^{i}'
    result += ' n'
  return result
  

def floatEquals(x, y):
  return abs(x - y) < 1e-9

if __name__ == '__main__':
    # T(n)=2T(n/4)+1: a = 2, b = 4, k = 0
    # T(n)=2T(n/4)+√n: a = 2, b = 4, k = 0.5
    # T(n)=2T(n/4)+n: a = 2, b = 4, k = 1
    # T(n)=2T(n/4)+n^2: a = 2, b = 4, k = 2
    # T(n)=4·T(n/4)+n log n: a = 4, b = 4, k = 1, i = 1
    # T(n) = 16 · T(n/2) + n^4 + n^2: a = 16, b = 2, k = 4, i = 0
    a = 1
    b = 4
    k = 0
    i = 0
    # T(n) = a T(n / b) + Θ(n^k(log n)^i)
    calc(a, b, k, i)
