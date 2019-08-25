l = [6,4,3,7,8,4,57,12,60]

k = []


N = len(l) 
for i in range(N):
  if i%2 == 0:
    k.append(l[i])

print(k)



assert k == l[::2]
#'k should be [6,3,8,57,60]' 
# this is to test if your function works