#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import time
import tkinter
from numpy import sin, cos
from numpy import array as a

angle1 = np.pi/4
angle2 = 3*np.pi/4

canvHeight = 700
canvWidth  = 700
canvbd = 10

def get_points(n):
    z = a([[0], [1]])
    for k in range(n):
        m = f1(z)
        n = f2(z)
        z = np.concatenate((m,n), axis=1)

    x = z.real
    y = z.imag
    return x, y

def g_get_points(n):
    z = a([[0], [1]])
    for k in range(n):
        m = g1(z)
        n = g2(z)
        z = np.concatenate((m,n), axis=1)

    x = z.real
    y = z.imag
    return x, y

def f_get_points(n):
    z = a([[0, 1], [0, 0]])
    for k in range(n):
        z1 = f1real(z)
        z2 = f2real(z)
        z = np.concatenate((z1,z2), axis=1)

    x = np.zeros([2, 2**n])
    y = np.zeros([2, 2**n])
    for k in range(2**n):
        x[:, k] = z[0, k:k+2]
        y[:, k] = z[1, k:k+2]
    return x, y 

def draw_points(x, y):
    plt.plot(x, y, 'k')
    plt.show()

def draw_points_looped(x, y):
    t = time.time()
    for n in range(x.shape[1]):
        plt.plot(x[:,n], y[:,n], 'k')
    
    tt = time.time()
    plt.show()

def draw_points_tkinter(x, y):
    master = tkinter.Tk()
    master.configure(bg="black", bd=10)
    xmin, xmax = np.amin(x), np.amax(x)
    ymin, ymax = np.amin(y), np.amax(y)
    c = tkinter.Canvas(master, width = canvWidth, height = canvHeight, bd=0, bg="white")
    c.xview_moveto(0)
    c.yview_moveto(0)
    yrescmax = 0
    for n in range(x.shape[1]):
        x0 = 0*canvbd + 1+ (x[0,n] - xmin)/(xmax - xmin)*(canvWidth  -3 + 0*canvbd)
        y0 = 0*canvbd + 1+ (y[0,n] - ymin)/(ymax - ymin)*(canvHeight -3 + 0*canvbd)
        x1 = 0*canvbd + 1+ (x[1,n] - xmin)/(xmax - xmin)*(canvWidth  -3 + 0*canvbd)
        y1 = 0*canvbd + 1+ (y[1,n] - ymin)/(ymax - ymin)*(canvHeight -3 + 0*canvbd)
        if(y1 > yrescmax): yrescmax = y1
        c.create_line(x0,y0, x1,y1, fill="black")
    c.pack()

def f1(z):
    return (1+1j)*z/2

def f2(z):
    return 1 - (1-1j)*z/2

ang1 = np.pi/4
ang2 =-np.pi/3
def g1(z):
    return np.sqrt(2)*np.exp(1j*ang1)*z/2

def g2(z):
    return 1 - np.sqrt(2)*np.exp(1j*ang2)*z/2

def f1real(s):
    X = np.array([[cos(angle1), -sin(angle1)], [sin(angle1), cos(angle1)]])
    X /= np.sqrt(2)
    return np.dot(X,s)

def f2real(s):
    X = np.array([[cos(angle2), -sin(angle2)], [sin(angle2), cos(angle2)]])
    X /= np.sqrt(2)
    return np.dot(X,s) + np.array([[1], [0]])

if __name__ == '__main__':
    t = time.time()
    x, y = get_points(18)
    tt = time.time()
    draw_points_tkinter(x, y)
    ttt = time.time()
    tkinter.mainloop()
