import math

import matplotlib.pyplot as plt


x = []
y = []
def f(n):
	total = 0
	#x = []
	#y = []
	for i in range(1, n+1):
		x.append(i)
		total += 1/(i*i)
		y.append(total)
	return x, total, y


res = f(1000) 
print(res)



plt.plot(x,y)
plt.show()