# Amol Arora, 116491705

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(threshold=50):
    # I start by creating a 500x500 grid for the real and imaginary parts of complex numbers c
    # spanning the region [-2, 1] on the real axis and [-1.5, 1.5] on the imaginary axis
    x, y = np.mgrid[-2:1:500j, -1.5:1.5:500j]
    c = x + 1j * y # Combine x and y to form a grid of complex numbers

    # Now, I Initialize z to be zero for all points in the grid, with the same shape as c
    z = np.zeros_like(c, dtype=complex)

    # Creating a boolean mask to track which points are within the Mandelbrot set
    # Initially, assume all points are in the set (True)
    mask = np.full(c.shape, True, dtype=bool)

    for i in range(threshold):
        # Updating z based on the Mandelbrot iteration z = z^2 + c
        # Only updating points that haven't diverged (where mask is True)
        z[mask] = z[mask]**2 + c[mask]
        mask = mask & (np.abs(z) < 100)
    
    # Plotting the Mandelbrot set using the mask
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('results/mandelbrot.png')
    plt.show()

mandelbrot()
