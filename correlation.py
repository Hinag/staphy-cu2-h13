#!/usr/bin/python

import main
import matplotlib.pyplot as plt

dim = 64
gitter2 = main.grid(dim, dim)
x_axis = main.np.arange(0,dim,1)
steps = 100
updatesteps = 100
plt.plot(x_axis, gitter2.correlation_plot(3, steps, updatesteps), 'r', x_axis, gitter2.correlation_plot(5, steps, updatesteps), 'b', x_axis, gitter2.correlation_plot(8, steps, updatesteps), 'g', x_axis, gitter2.correlation_plot(11, steps, updatesteps), 'y')
plt.xlim(1,32)
plt.show()
