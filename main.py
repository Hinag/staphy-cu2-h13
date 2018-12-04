#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Daniel Scheiermann   3227680
Felix Springer       10002537
Hinnerk              10002310
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.animation as animation
import random

class grid:
    """class for spin-lattice"""

    def __init__(self, xdim, ydim):
        """creates lattice with random spins"""
        self.xdim = xdim
        self.ydim = ydim
        self.lattice = np.random.randint(low=0, high=2, size=(xdim, ydim))
        self.lattice = 2 * self.lattice - 1 # lattice with random 1 and -1
        self.h = 0 # magnetic field
        self.tau = 1 # temperature
        self.speed = 1 # speed of time progression
        self.time = 0 # time step
        return

    def print_settings(self):
        """gives information about lattice to stdout"""
        print("Gittergröße: ",self.xdim, "x",self.ydim)
        print(self.lattice)
        return

    def update(self):
        """uses the metropolis algorithm on the lattice (1 time step)"""
        self.time += 1

        x_rand = random.randint(0, self.xdim - 1)
        y_rand = random.randint(0, self.ydim - 1)

        current = self.lattice[x_rand][y_rand] # random lattice site
        new = -current
        up = self.lattice[x_rand][(y_rand + 1) % self.xdim]
        down = self.lattice[x_rand][y_rand - 1]
        left = self.lattice[x_rand - 1][y_rand]
        right = self.lattice[(x_rand + 1) % self.ydim][y_rand]

        energy_old = (-current) * (up + down + left + right + self.h)
        energy_new = (-new) * (up + down + left + right + self.h)

        energy_delta = energy_new - energy_old # energy difference to flip spin
        if(energy_delta < 0):
            self.lattice[x_rand][y_rand] = new # flip if deltaE<0
        else:
            probability = np.exp(-energy_delta / self.tau)
            if(random.random() < probability):
                self.lattice[x_rand][y_rand] = new # flip with probability exp(deltaE / tau)
        return

    def make_plot(self):
        """creates animation of current state of lattice"""
        self.fig = plt.figure()

        ax = self.fig.add_subplot(111)
        self.fig.subplots_adjust(bottom=0.2)
        im = plt.matshow(self.lattice, fignum=0, animated=True)
        ax_tau = plt.axes([0.2, 0.13, 0.6, 0.03])
        sli_tau = Slider(ax_tau, 'Temp', 0.01, 30.0, valinit=1.)
        ax_h = plt.axes([0.2, 0.08, 0.6, 0.03])
        sli_h = Slider(ax_h, 'h', -5., 5., valinit=0.)
        ax_speed = plt.axes([0.2, 0.03, 0.6, 0.03])
        sli_speed = Slider(ax_speed, 'SpeedUp', 1, 100, valinit=1, valstep=1)

        def update_fig(*args):
            """updates plot"""
            self.tau = sli_tau.val
            self.h = sli_h.val
            self.speed = sli_speed.val

            for i in range(int(self.speed)):
                self.update()

            im.set_array(self.lattice)
            return im,


        ani = animation.FuncAnimation(self.fig, update_fig, interval=5, blit=True)
        plt.show()
        return

    def correlation_add(self, row, distance):
        """returns the sum of the correlation function (still needs '/ time'"""
        cor = 0
        for i in range(self.ydim):
            cor += self.lattice[row][i] * self.lattice[row][i - distance]
        cor = cor / (self.ydim)
        return cor

    def correlation_plot(self, tau, steps, updatesteps):
        self.tau = tau
        cor_of_dist = np.zeros(self.ydim)
        for i in range(steps):
            for j in range(updatesteps):
                self.update()
            for j in range(self.ydim):
                cor_of_dist[j] += self.correlation_add(row=32, distance=j)

        cor_of_dist = cor_of_dist / self.time
        return cor_of_dist
