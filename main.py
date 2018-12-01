#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:15:33 2018

@author: Hinnerk, Felix, Daniel
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.animation as animation
import random
#import time

class grid:
    """Klasse für Spin-Gitter"""

    def __init__(self, xdim, ydim):
        """erstellt Gitter mit zufälligen Einträgen"""
        self.xdim = xdim
        self.ydim = ydim
        self.lattice = np.random.randint(low=0, high=2, size=(xdim, ydim))
        self.lattice = 2 * self.lattice - 1
        self.h = 0
        self.tau = 1

    def print_settings(self):
        print("Gittergröße: ",self.xdim, "x",self.ydim)
        print(self.lattice)

#   def random(self): # langsam und keinen zweck fuer aufgabe?
#       array = np.zeros((8,8))
#       for x in range(8):
#           for y in range(8):
#               array[x,y] = random.randint(-0,1)
#       return(array)

    def update(self):
        """wendet den Metropolis Algorithmus auf das Gitter an und gibt es zurück"""
        x_rand = random.randint(0, self.xdim - 1)
        y_rand = random.randint(0, self.ydim - 1)

        current = self.lattice[x_rand][y_rand]
        new = -current
        up = self.lattice[x_rand][(y_rand + 1) % self.xdim]
        down = self.lattice[x_rand][y_rand - 1]
        left = self.lattice[x_rand - 1][y_rand]
        right = self.lattice[(x_rand + 1) % self.ydim][y_rand]

        energy_old = (-current) * (up + down + left + right + self.h)
        energy_new = (-new) * (up + down + left + right + self.h)

        energy_delta = energy_new - energy_old
        if(energy_delta < 0):
            self.lattice[x_rand][y_rand] = new
        else:
            probability = np.exp(-energy_delta / self.tau)
            if(random.random() < probability):
                self.lattice[x_rand][y_rand] = new

        return

    def make_plot(self):
        self.fig = plt.figure()
        #ax = self.fig.add_subplot(111)
        #self.fig.subplots_adjust(left=0.25, bottom=0.25)
        #temp_slider_ax = self.fig.add_axes([0.25, 0.15, 0.65, 0.03], axisbg="red")
        #temp_slider = Slider(temp_slider_ax, 'Temp.', 0.1, 10.0, valinit=0)
        #[data] = ax.arrow(0,0,1,1, linewidth=2, color='red')
        im = plt.matshow(self.lattice, fignum=0, animated=True)

        def update_fig(*args):
            self.update()
            im.set_array(self.lattice)
            return im,


        ani = animation.FuncAnimation(self.fig, update_fig, interval=0, blit=True)
        plt.show()

dim =34
gitter = grid(dim, dim)
gitter.print_settings()
gitter.make_plot()
