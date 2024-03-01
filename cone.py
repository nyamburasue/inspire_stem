#program to solve sa and volume of a cone
#name : Susan Maina
#date :28/02/2024

import math

r =float(input("enter the radius of the cone:"))
h=float(input("enter the radius of the cone:"))
l=float(input("enter the lenght of the cone:"))

def sa_cone(sa_cone):
    sa_cone = ((3.14 * (r**2)) + (3.14 * r*l))
    print("the surface area of the cone is {0}".format(sa_cone))

sa_cone({0})

def cone_vol(cone_vol):
    cone_vol = ((1/3) * 3.14 * (r**2) * h)
    print("the volume of the cone is {0}".format(cone_vol))

cone_vol({0})
