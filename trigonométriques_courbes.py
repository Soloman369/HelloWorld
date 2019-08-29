import math
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
z = []

for i in np.linspace(-10, 10, 100):
    x.append(i)
    y.append(math.cos(i))
    z.append(math.sin(i))

plt.cla()
plt.title('Courbes trigonométriques 😅')
plt.plot(x, y, label='Cos')
plt.plot(x, z, label='Sin')
plt.gca().legend(loc = 'upper left')
plt.show()
