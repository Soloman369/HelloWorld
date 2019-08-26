import random

l = []
for i in range(20):
    l.append(random.randint(0,15))
k = sorted(l)
print(k)

s = []
for i in l:
    if i not in s:
        s.append(i)

print(s)         
