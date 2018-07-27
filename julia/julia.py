#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from time import time

def julia_loop(x_min, x_max, dx, y_min, y_max, dy, c, m, n_max, tolerance):
    X = np.arange(x_min, x_max, dx)
    Y = np.arange(y_min, y_max, dy)
    C = c
    Z = X + Y[:, np.newaxis]*1j
    N = np.zeros_like(Z, dtype = np.int32)
    for x in range(X.size):
        for y in range(Y.size):
            for n in range(n_max):
                if np.abs(Z[y, x]) > tolerance:
                    N[y, x] = n
                    break
                Z[y, x] = Z[y, x]**m + C
    return X, Y, Z, N


if __name__ == '__main__':
    delta = 0.005
    x_min, x_max, dx = -1.5, 1.5, delta
    y_min, y_max, dy = -1.5, 1.5, delta
    n_max = 50
    c = -.4 + .6*1j
    m = 2
    tolerance = 5
    X, Y, Z, N = julia_loop(x_min, x_max, dx, y_min, y_max, dy, c, m, \
            n_max, tolerance)

    # This part adds a fractional part to the iteration count, making the
    # figure smoother looking. The fractional part is based on how much 
    # larger than the tolerance the absolute of z became when it crossed it.
    # This is an estimate of how quickly the iterated map diverges.
    # Read about this in following link:
    # https://linas.org/art-gallery/escape/smooth.html
    # For an implementation that uses more features of numpy to calculate
    # the map see https://matplotlib.org/examples/showcase/mandelbrot.html
    with np.errstate(invalid="ignore"):
        M = np.nan_to_num(N + 1 - np.log(np.log(np.abs(Z)))/np.log(2) \
                + np.log(tolerance))
    plt.imshow(M, interpolation="nearest", extent=[x_min, x_max, y_min, y_max])
    plt.colorbar()
    plt.savefig("img_julia.png")
    plt.show()
