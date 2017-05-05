import numpy as np
import matplotlib.pyplot as plt

from fracdiff import fracdiff

t = np.linspace(0, 10, 1000)
f = np.sin(t)

fig, ax = plt.subplots(figsize=(7, 4))

for alpha in np.arange(0, 2.0, 0.2):
	y = fracdiff(f, alpha, t)
	plt.plot(t, y, label=r'$\alpha = {}$'.format(str(alpha)))


plt.axis([0, 10, -1.5, 2])
plt.xlabel('time (s)')
plt.ylabel(r'$\mathcal{D}_{t}^{\alpha}\sin(t)$')
plt.grid()
plt.legend()
plt.show()
