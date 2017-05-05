import numpy as np
import matplotlib.pyplot as plt

from fracdiff import fracdiff
import siggen

t = np.linspace(0, 10, 1000)
f = siggen.u(t - 1)

fig, ax = plt.subplots(figsize=(7, 4))

for alpha in np.arange(0, 1.2, 0.2):
	y = fracdiff(f, alpha, t)
	plt.plot(t, y, label=r'$\alpha = {}$'.format(str(alpha)))


plt.axis([0, 10, 0, 2])
plt.xlabel('time (s)')
plt.ylabel(r'$\mathcal{D}_{t}^{\alpha}u(t)$')
plt.grid()
plt.legend()
plt.show()
