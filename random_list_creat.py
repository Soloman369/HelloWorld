import random

def generate_list(n_elements, max_possible_value):
  l = []
  for i in range(n_elements):
    s = random.randint(0, max_possible_value)
    l.append(s)
  return l

l = sorted(generate_list(3, 50))
k = sorted(generate_list(2, 100))

p = l + k
N = len(p)

Q = []
for i in range(N):
  Q.append(min(p))
  p.remove(min(p))
print("Q = ",Q)
print('-----')
print(len(Q))