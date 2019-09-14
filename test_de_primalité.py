import math
import matplotlib.pyplot as plt
import numpy as np


def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

prime_numbers = []

q = int(input("Quelle est la valeur MAX que vous voulez?"))


for i in range(2 ,q):
    if is_prime(i):
        prime_numbers.append(i)





plt.title('Comportement des nombres premiers 😅')
plt.plot(prime_numbers)
plt.ylabel('nombres normaux')
plt.xlabel('nombres de nombres premiers')
plt.show()
