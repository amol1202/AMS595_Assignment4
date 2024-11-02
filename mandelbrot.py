import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(threshold=50):
    x, y = np.mgrid[-2:1:500j, -1.5:1.5:500j]
    c = x + 1j * y
    z = np.zeros_like(c, dtype=complex)
    mask = np.full(c.shape, True, dtype=bool)

    for i in range(threshold):
        z[mask] = z[mask]**2 + c[mask]
        mask = mask & (np.abs(z) < 100)
    
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('results/mandelbrot.png')
    plt.show()

mandelbrot()
