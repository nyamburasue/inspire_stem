#program to compute data for employees
#name : Susan Maina
#date :26/02/2024

employee_name = input("enter employee`s name :")
age = input ("enter age of employee : ")
salary = int (input("enter salary : "))
bonus =int(input("enter bonus :"))

print("name :", employee_name)
print("age :" , age)
print("salary:", salary)
print("bonus, ",bonus)

if salary <= 50000 :
    salary = salary * 0.3 + salary 
    print (salary)
elif salary <= 60000 : 
    salary = salary * 0.15 + salary 
    print (salary)
else :
    salary = salary * 0.05 + salary 
    print (salary)




