
def getRemainder(num, divisor): 
    return (num - divisor * (num // divisor))

def double_hashing(hash, hash2, A, x):
  """
    let hash(x) be the slot index computed using hash function.  
    If slot hash(x) % S is full, then we try (hash(x) + 1*hash2(x)) % S
    If (hash(x) + 1*hash2(x)) % S is also full, then we try (hash(x) + 2*hash2(x)) % S
    If (hash(x) + 2*hash2(x)) % S is also full, then we try (hash(x) + 3*hash2(x)) % S
  """
  i = 0
  s = len(A)
  while A[getRemainder((hash(x) + i*hash2(x)), s)] is not None:
    i = i + 1
  index = getRemainder((hash(x) + i*hash2(x)), s)
  print(f'Double Hashing index is: {index}')
  A[index] = x
  print(f'insertion of {x}: {A}')

def linear_probing(hash, A, x):
  """
    If slot hash(x) % S is full, then we try (hash(x) + 1) % S
    If (hash(x) + 1) % S is also full, then we try (hash(x) + 2) % S
    If (hash(x) + 2) % S is also full, then we try (hash(x) + 3) % S
  """
  i = 0
  s = len(A)
  while A[getRemainder(hash(x)+i, s)] is not None:
    i = i + 1
  index = getRemainder(hash(x)+i, s)
  print(f'Linear Probing index is: {index}')
  A[index] = x
  print(f'insertion of {x}: {A}')

def quadratic_probing(hash, A, x, c1 = 0, c2 = 0):
  """
    let hash(x) be the slot index computed using hash function.  
    If slot hash(x) % S is full, then we try (hash(x) + 1*1) % S
    If (hash(x) + 1*1) % S is also full, then we try (hash(x) + 2*2) % S
    If (hash(x) + 2*2) % S is also full, then we try (hash(x) + 3*3) % S
  """
  i = 0
  s = len(A)
  index = None
  if c1 & c2 > 0:
    while A[getRemainder((hash(x) + c1*i + c2*(i**2)), s)] is not None:
      i = i + 1
    index = getRemainder((hash(x) + c1*i + c2*(i**2)), s)
  else:
    while A[getRemainder((hash(x) + i*i), s)] is not None:
      i = i + 1
    index = getRemainder((hash(x) + i*i), s)

  print(f'Quadratic Probing index is: {index}')
  A[index] = x
  print(f'insertion of {x}: {A}')


if __name__ == '__main__':
  a = [3, None, None, 59, None, 23, 38, 53, None, 72, 87]

  def hash(x):
    return (3*x + 2) % 11

  def hash2(x):
    return 1 + (x % 12)

  #quadratic_probing(hash=hash, A=a, x=22, c1=3, c2=1)

  #quadratic_probing(hash=hash, A=a, x=16, c1=3, c2=1)

  #quadratic_probing(hash=hash, A=a, x=17, c1=3, c2=1)

  #double_hashing(hash=hash, hash2=hash2, A=a, x=3)

  #double_hashing(hash=hash, hash2=hash2, A=a, x=5)

  #double_hashing(hash=hash, hash2=hash2, A=a, x=15)

  linear_probing(hash=hash, A=a, x=60)

  linear_probing(hash=hash, A=a, x=45)
  
  # function not given bot value - change in code to get value of function

  #double_hashing(3 , 6, a, 11)
  
  #linear_probing(6, a, 11) 