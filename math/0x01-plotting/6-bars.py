#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

names = ['Farrah', 'Fred', 'Felicia']
apples = fruit[0]
bananas = fruit[1]
oranges = fruit[2]

plt.title("Number of Fruit per Person")
plt.ylabel("Quantity of Fruit")
plt.yticks(range(0, 81, 10))
plt.ylim(0, 80)
plt.bar(names, fruit[0][:], color='red', label='apples', width=0.5)
plt.bar(names, fruit[1][:], color='yellow', label='bananas',
        width=0.5, bottom=apples)
plt.bar(names, fruit[2][:], color='#ff8000', label='oranges',
        width=0.5, bottom=apples + bananas)
plt.bar(names, fruit[3][:], color='#ffe5b4', label='peaches',
        width=0.5, bottom=apples + bananas + oranges)
plt.legend()
plt.show()
