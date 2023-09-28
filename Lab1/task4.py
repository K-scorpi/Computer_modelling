import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4, 4, 0.0001)
b = 3

f1 = 2 * x ** 2 + b
f2 = -np.sqrt(1 - (x ** 2)) + np.sqrt(abs(x))  # вычисления
f3 = np.sqrt(1 - (x ** 2)) + np.sqrt(abs(x))

plt.subplot(1, 2, 1)
plt.plot(x, f1, 'b', label='f1')
plt.title('f1 = 2 * x^2 + b', fontsize=12)
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.legend()

plt.subplot(1, 2, 2)
line1, line2 = plt.plot(x, f2, 'r', x, f3, 'r', label='f2')
plt.title('x^2 = (f2 - sqrt|x|)^2 = 1', fontsize=12)
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)

plt.legend([line1, line2], ['f2'])
plt.show()
