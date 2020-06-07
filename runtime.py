import big_o

def algoritme1(n):
  for i in range(1, n):
    j = i
    while j > 0:
      j = j - 1

def algoritme2(n):
  i = 1
  while i < n:
    i = i * 2

def algoritme3(n):
  i = 1
  while i < n:
    i = i * n

def algoritme4(n):
  i = 1
  while i < n:
    s = 0
    while s < n:
      s = s + i
    i = i * 2

best_for_1, others_for_1 = big_o.big_o(algoritme1, big_o.datagen.n_, n_repeats=1000, min_n=1, max_n=1000)
best_for_2, others_for_2 = big_o.big_o(algoritme2, big_o.datagen.n_, n_repeats=1000, min_n=1, max_n=1000)
best_for_3, others_for_3 = big_o.big_o(algoritme3, big_o.datagen.n_, n_repeats=1000, min_n=1, max_n=1000)
best_for_4, others_for_4 = big_o.big_o(algoritme4, big_o.datagen.n_, n_repeats=1000, min_n=1, max_n=1000)

def print_others(others):
  for class_, residuals in others.items():
    print('{!s:<60s}    (res: {:.2G})'.format(class_, residuals))

print(best_for_1)
print(best_for_2)
print(best_for_3)
print(best_for_4)