from PIL import Image
from tkinter import filedialog
from cmath import *
from math import sqrt
from numpy import linspace

width = 1000
height = 1000

minx = float(input("Please enter the minimum x value:"))
maxx = float(input("Please enter the maximum x value:"))
miny = float(input("Please enter the minimum y value:"))
maxy = float(input("Please enter the maximum y value:"))

gradient = Image.open("mandelbrot.png")
gradlist = list(gradient.getdata())

def testMandelbrot(x, y):
    z = 0 + 0j
    c = x + (y*1j)
    iter = 0
    while iter <= 69 and sqrt(z.real**2 + z.imag**2) < 4:
        z = (z*z) + c
        iter += 1
    if iter == 70:
        return (0, 0, 0, 255)
    else:
        return gradlist[int((iter - 1) * 140 / 70)]

img = Image.new('RGBA', (width, height), color=(255, 255, 255, 255))
image = [testMandelbrot(x, y) for y in linspace(miny, maxy, height) for x in linspace(minx, maxx, width)]
img.putdata(image)
img.save(filedialog.asksaveasfilename() + ".png", "PNG")
