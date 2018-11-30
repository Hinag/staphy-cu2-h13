# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:15:33 2018

@author: Hinnerk
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.widgets import Slider, Button, RadioButtons
import random
import matplotlib.animation as animation

class grid:
    """ kommt später"""

    def __init__(self, xdim, ydim):
        self.xdim = xdim
        self.ydim = ydim
        self.lattice = np.ones((xdim,ydim))

    def print_settings(self):
        print("Gittergröße: ",self.xdim, "x",self.ydim)
        print(self.lattice)

    def random(self):
        array = np.zeros((8,8))
        for x in range(8):
            for y in range(8):
                array[x,y] = random.randint(-0,1)
        return(array)

    def make_plot(self):
        self.fig = plt.figure()
        #ax = self.fig.add_subplot(111)
        #self.fig.subplots_adjust(left=0.25, bottom=0.25)
        #temp_slider_ax = self.fig.add_axes([0.25, 0.15, 0.65, 0.03], axisbg="red")
        #temp_slider = Slider(temp_slider_ax, 'Temp.', 0.1, 10.0, valinit=0)
        #[data] = ax.arrow(0,0,1,1, linewidth=2, color='red')
        im = plt.matshow(self.random(), fignum=0, animated=True)

        def updatefig(*args):
            im.set_array(self.random())
            return im,

        ani = animation.FuncAnimation(self.fig, updatefig, interval=50, blit=True)
        plt.show()

gitter = grid(8,8)
gitter.print_settings()
gitter.make_plot()
