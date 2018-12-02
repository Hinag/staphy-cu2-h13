#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Daniel Scheiermann   3227680
Felix Springer       10002537
Hinnerk
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.animation as animation
import random

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
        self.speed = 1
        return

    def print_settings(self):
        """gibt Informationen über das Gitter and stdout"""
        print("Gittergröße: ",self.xdim, "x",self.ydim)
        print(self.lattice)

    def update(self):
        """wendet den Metropolis Algorithmus auf das Gitter an"""
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

        ax = self.fig.add_subplot(111)
        self.fig.subplots_adjust(bottom=0.2)
        im = plt.matshow(self.lattice, fignum=0, animated=True)
        ax_tau = plt.axes([0.2, 0.13, 0.6, 0.03])
        sli_tau = Slider(ax_tau, 'Temp', 0.01, 50.0, valinit=1.)
        ax_h = plt.axes([0.2, 0.08, 0.6, 0.03])
        sli_h = Slider(ax_h, 'h', -5., 5., valinit=0.)
        ax_speed = plt.axes([0.2, 0.03, 0.6, 0.03])
        sli_speed = Slider(ax_speed, 'SpeedUp', 1, 100, valinit=1, valstep=1)

        def update_fig(*args):
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

dim = 64
gitter = grid(dim, dim)
gitter.print_settings()
gitter.make_plot()
