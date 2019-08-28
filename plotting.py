import math
import matplotlib.pyplot as plt

##################################@
def f(n):
	total = 0
	x = []
	y = []
	for i in range(1, n+1):
		x.append(i)
		total += 1/(i*i)
		y.append(total)
	return x, total, y


x, total, y = f(100) 

################################@

def f(n):
	a = []
	b = []
	total = 0
	for i in range(1, n+1):
		a.append(i)
		total += 1/(i*i*i)
		b.append(total)
	return a, total, b

a, total, b = f(100) 
################################@

def f(n):
	c = []
	d = []
	total = 0
	for i in range(1, n+1):
		c.append(i)
		total += ((-1)**i)/i 
		d.append(total)
	return c, total, d 

c, total, d = f(100)

################################@
def f(n):
	e = []
	g = []
	total = 0
	for i in range(0,n):
		e.append(i)
		total += 1/math.factorial(i)
		g.append(total)
	return e, total, g 

e, total,g = f(100)

################################@
def f(n):
	h = []
	j = []
	total = 0
	for i in range(1,n):
		h.append(i)
		total += 1/i
		j.append(total)
	return h, total, j

h, total,j = f(100)

################################@

plt.title('Matplotlib Legend Example')

plt.plot(a,b,label='la courbe de 1/i^2')

plt.plot(x,y,label='la courbe de 1/i^3')

plt.plot(e,g,label='la courbe de 1/i!')

plt.plot(h,j,label='la courbe de 1/i')

plt.plot(c,d,label='la courbe de ((-1)**i)/i')

plt.show()
print((math.pi**2)/6)




