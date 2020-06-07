def getRemainder(num, divisor): 
    return (num - divisor * (num // divisor)) 

a = [67, 20, 17, None, 33, None, 16, 2, None, None, 15]
s = len(a)
x = 18

# Double hasing
#let hash(x) be the slot index computed using hash function.  
#If slot hash(x) % S is full, then we try (hash(x) + 1*hash2(x)) % S
#If (hash(x) + 1*hash2(x)) % S is also full, then we try (hash(x) + 2*hash2(x)) % S
#If (hash(x) + 2*hash2(x)) % S is also full, then we try (hash(x) + 3*hash2(x)) % S
def hash(x):
  return (x + 2) % 7

def hash2(x):
  return (x % 6) + 1

i = 0
while a[getRemainder((hash(x) + i*hash2(x)), s)] is not None:
  i = i + 1
print('double hashing index is: ', getRemainder((hash(x) + i*hash2(x)), s))

# Linear Probing: S = table size
#If slot hash(x) % S is full, then we try (hash(x) + 1) % S
#If (hash(x) + 1) % S is also full, then we try (hash(x) + 2) % S
#If (hash(x) + 2) % S is also full, then we try (hash(x) + 3) % S
def hash1(x):
  return (7*x + 4) % 11

i = 0
while a[getRemainder(hash1(x)+i, s)] is not None:
  i = i + 1
print('Linear Probing index is: ', getRemainder(hash1(x)+i, s))

#Quadratic Probing
#let hash(x) be the slot index computed using hash function.  
#If slot hash(x) % S is full, then we try (hash(x) + 1*1) % S
#If (hash(x) + 1*1) % S is also full, then we try (hash(x) + 2*2) % S
#If (hash(x) + 2*2) % S is also full, then we try (hash(x) + 3*3) % S
def hash3(x):
  return (x + 2) % 7

i = 0
while a[getRemainder((hash3(x) + i*i), s)] is not None:
  i = i + 1
print('Quadratic Probing index is: ', getRemainder((hash3(x) + i*i), s))