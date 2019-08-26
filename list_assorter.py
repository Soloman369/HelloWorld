
l = [3,4,5,67,1,4,6,1,7]
k = [0,0,0,0,0,0,0,0,0] # can you please sort l in increasing order ?

N = len(l)

for i in l:
  a = 0
  while a < N:
    k[a] = min(l)
    l.remove(min(l))
    a = a + 1




print(k)