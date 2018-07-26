#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from time import time

def mandelbrot_loop(x_min, x_max, dx, y_min, y_max, dy, n_max, tolerance):
    X = np.arange(x_min, x_max, dx)
    Y = np.arange(y_min, y_max, dy)
    C = X + Y[:, np.newaxis]*1j
    Z = np.zeros_like(C, dtype = np.complex)
    N = np.zeros_like(C, dtype = np.int32)
    for x in range(X.size):
        for y in range(Y.size):
            for n in range(n_max):
                if np.abs(Z[y, x]) > tolerance:
                    N[y, x] = n
                    break
                Z[y, x] = Z[y, x]**2 + C[y, x]
    return X, Y, Z, N


if __name__ == '__main__':
    delta = 0.005
    x_min, x_max, dx = -1.6, .6, delta
    y_min, y_max, dy = -1.2, 1.2, delta
    n_max = 50
    tolerance = 5
    X, Y, Z, N = mandelbrot_loop(x_min, x_max, dx, y_min, y_max, dy, \
            n_max, tolerance)
    with np.errstate(invalid="ignore"):
        M = np.nan_to_num(N + 1 - np.log(np.log(np.abs(Z)))/np.log(2) \
                + np.log(tolerance))
    plt.imshow(M, interpolation="nearest", extent=[x_min, x_max, y_min, y_max])
    plt.colorbar()
    plt.savefig("img_mandelbrot.png")
    plt.show()
