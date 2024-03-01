#program to compute the cubes of numbers
#name : Susan Maina
#date :28/02/2024

a = int(input("enter first number:"))
b = int (input("enter second number:"))

def squares(a,b):
    for i in range(a,b + 1):
        print(b**3)

squares(a,b)