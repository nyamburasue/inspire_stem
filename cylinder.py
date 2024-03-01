#program to solve volume and sa of a cylinder
#name : Susan Maina
#date :28/02/2024
import math
r=float(input("enter radius of the cylinder:"))
h = float(input("enter the height of the cylinder:"))
d = 2*r

def sa_cylinder():
    sa_cylinder = ((2 * 3.142 * r**2) +(3.142 * d * h))
    print("the surface area of the cylinder is {0}".format(sa_cylinder))

sa_cylinder({0})

def vol_cylinder():
    volume = (3.142 * r**2 * h)
    print("the volume of the cylinder is{0}cm ".format(vol_cylinder))